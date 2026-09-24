#!/usr/bin/env python3
"""
crop_doc.py - Recorta trechos de documentos PDF (autos, contratos, extratos,
prints) em imagens PNG individuais, prontas para colar numa peticao.

Renderiza a pagina do PDF, recorta a faixa indicada (ou a pagina inteira),
remove a margem branca, aplica borda branca e, opcionalmente, escreve uma
legenda no topo (ex.: "Doc. 04 - dispositivo autorizado em 09/05/2026").

Depende de: pdftoppm (poppler) e convert (ImageMagick).
Verifique com: which pdftoppm convert

INDIVIDUAL:
  python crop_doc.py --pdf autos.pdf --page 18 --out 10-extrato.png
  python crop_doc.py --pdf ccb.pdf --page 1 --rect 1653x1620+0+150 --out 08-ccb.png --label "Doc. 08 - CCB"

EM LOTE (recomendado, faz tudo de uma vez):
  python crop_doc.py --batch jobs.json
  jobs.json = lista de {"pdf","page","out","rect"?,"label"?}

COORDENADAS: A4 a 200 DPI ~ 1654x2339 px. Faixa vertical = "LARGURAxALTURA+0+TOPO".
Renderize a pagina inteira primeiro (sem --rect), olhe, ajuste TOPO/ALTURA. O -trim limpa sobras.
"""
import argparse, json, os, subprocess, sys, tempfile, shutil

def _need(t):
    if shutil.which(t) is None:
        sys.exit(f"ERRO: '{t}' nao encontrado. Instale poppler-utils e imagemagick.")

def render_page(pdf, page, dpi, tmp):
    base = os.path.join(tmp, "pg")
    subprocess.run(["pdftoppm","-png","-r",str(dpi),"-f",str(page),"-l",str(page),pdf,base], check=True)
    for f in os.listdir(tmp):
        if f.startswith("pg") and f.endswith(".png"):
            return os.path.join(tmp, f)
    sys.exit(f"ERRO: falha ao renderizar pagina {page} de {pdf}")

def do_one(job, dpi_d, fuzz_d, border_d, outdir):
    pdf=job["pdf"]; page=int(job.get("page",1)); out=job["out"]
    if outdir and not os.path.isabs(out): out=os.path.join(outdir,out)
    rect=job.get("rect"); label=job.get("label")
    dpi=int(job.get("dpi",dpi_d)); fuzz=job.get("fuzz",fuzz_d); border=int(job.get("border",border_d))
    if not os.path.exists(pdf):
        print(f"  PULADO (PDF nao encontrado): {pdf}"); return False
    with tempfile.TemporaryDirectory() as tmp:
        png=render_page(pdf,page,dpi,tmp)
        cmd=["convert",png]
        if rect: cmd+=["-crop",rect,"+repage"]
        cmd+=["-fuzz",f"{fuzz}%","-trim","+repage","-bordercolor","white","-border",str(border)]
        if label:
            cmd+=["-background","#f0f0f0","-fill","#111","-gravity","Northwest",
                  "-pointsize","30","-splice","0x70","-annotate","+25+18",label]
        os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
        cmd+=[out]
        subprocess.run(cmd, check=True)
    print(f"  OK: {out}"); return True

def main():
    ap=argparse.ArgumentParser(description="Recorta trechos de PDF em PNG para colar em peticao.")
    ap.add_argument("--pdf"); ap.add_argument("--page",type=int,default=1); ap.add_argument("--out")
    ap.add_argument("--rect"); ap.add_argument("--label"); ap.add_argument("--batch")
    ap.add_argument("--outdir",default=""); ap.add_argument("--dpi",type=int,default=200)
    ap.add_argument("--fuzz",type=int,default=6); ap.add_argument("--border",type=int,default=25)
    a=ap.parse_args(); _need("pdftoppm"); _need("convert")
    if a.batch:
        jobs=json.load(open(a.batch,encoding="utf-8")); ok=0
        for j in jobs:
            if do_one(j,a.dpi,a.fuzz,a.border,a.outdir): ok+=1
        print(f"\nConcluido: {ok}/{len(jobs)} recortes gerados.")
    else:
        if not (a.pdf and a.out): sys.exit("Informe --pdf e --out, ou use --batch jobs.json")
        do_one({"pdf":a.pdf,"page":a.page,"out":a.out,"rect":a.rect,"label":a.label}, a.dpi,a.fuzz,a.border,a.outdir)

if __name__=="__main__":
    main()
