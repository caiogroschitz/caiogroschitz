"""Busca, nas APIs públicas do CNJ, os dados de cada processo do lote.csv e grava no próprio lote.

Uso:
    python buscar_dados.py lote.csv [--so NUMERO ...]

Fontes (sem login e sem CAPTCHA):
- DataJud (api-publica.datajud.cnj.jus.br): órgão julgador, classe e movimentações.
  A chave é a pública divulgada pelo CNJ; se ela mudar, informe a nova em DATAJUD_APIKEY.
- DJEN, Comunica PJe (comunicaapi.pje.jus.br): intimações publicadas, com as partes (polo ativo e passivo),
  o órgão e o texto do ato.

Cada processo é consultado uma vez por fonte. Se falhar, a falha é anotada em `busca_status` e o lote segue.
Processos já buscados (busca_status = ok) não são consultados de novo. O lote.csv é gravado depois de cada processo.
"""
import argparse
import csv
import datetime
import json
import os
import re
import time
import urllib.error
import urllib.parse
import urllib.request

DATAJUD_APIKEY = os.environ.get(
    "DATAJUD_APIKEY", "cDZHYzlZa0JadVREZDJCendQbXY6SkJlTzNjLV9TRENyQk1RdnFKZGRQdw==")
DATAJUD_URL = "https://api-publica.datajud.cnj.jus.br/api_publica_{alias}/_search"
DJEN_URL = "https://comunicaapi.pje.jus.br/api/v1/comunicacao?numeroProcesso={num}"

# (segmento J, tribunal TR) -> alias do DataJud
ALIAS = {("8", "08"): "tjes", ("8", "13"): "tjmg", ("8", "07"): "tjdft", ("8", "26"): "tjsp",
         ("8", "19"): "tjrj", ("4", "06"): "trf6", ("4", "01"): "trf1"}

CAMPOS_NOVOS = ["autor", "orgao_oficial", "classe", "ult_mov_data", "ult_mov_nome", "ult_publicacao",
                "alerta_movimentos", "busca_status"]

# Movimentos que indicam que o impulso pode não caber mais (sentença, extinção, arquivamento, baixa).
ALERTA = re.compile(r"(?i)julgad[oa]|senten|extin|arquiv|baixa definitiva|trânsito em julgado|homologa")


def _http(url, dados=None, cabecalhos=None, timeout=25):
    req = urllib.request.Request(url, data=dados, headers=cabecalhos or {})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8"))


def datajud(numero):
    m = re.match(r"\d{7}-\d{2}\.\d{4}\.(\d)\.(\d{2})\.\d{4}$", numero)
    alias = ALIAS.get((m.group(1), m.group(2))) if m else None
    if not alias:
        return None, "tribunal sem alias no DataJud"
    corpo = json.dumps({"query": {"match": {"numeroProcesso": re.sub(r"\D", "", numero)}}}).encode()
    r = _http(DATAJUD_URL.format(alias=alias), corpo,
              {"Authorization": f"APIKey {DATAJUD_APIKEY}", "Content-Type": "application/json"})
    hits = r.get("hits", {}).get("hits", [])
    if not hits:
        return None, "não encontrado no DataJud"
    # Pode haver um registro por grau; usa o atualizado mais recentemente.
    src = max((h["_source"] for h in hits), key=lambda s: s.get("dataHoraUltimaAtualizacao", ""))
    return src, ""


def djen(numero):
    r = _http(DJEN_URL.format(num=re.sub(r"\D", "", numero)))
    return r.get("items", []) or []


def _data_iso(s):
    return (s or "")[:10]


def processar(item):
    erros = []
    try:
        src, err = datajud(item["processo"])
        if err:
            erros.append(err)
    except (urllib.error.URLError, TimeoutError, ValueError) as e:
        src = None
        erros.append(f"DataJud: {e}")
    try:
        pubs = djen(item["processo"])
    except (urllib.error.URLError, TimeoutError, ValueError) as e:
        pubs = []
        erros.append(f"DJEN: {e}")

    if src:
        item["orgao_oficial"] = (src.get("orgaoJulgador") or {}).get("nome", "")
        item["classe"] = (src.get("classe") or {}).get("nome", "")
        movs = sorted(src.get("movimentos") or [], key=lambda m: m.get("dataHora", ""))
        if movs:
            ult = movs[-1]
            comp = "; ".join(c.get("nome", "") for c in ult.get("complementosTabelados") or [] if c.get("nome"))
            item["ult_mov_data"] = _data_iso(ult.get("dataHora"))
            item["ult_mov_nome"] = ult.get("nome", "") + (f" ({comp})" if comp else "")
            alertas = [f"{_data_iso(m.get('dataHora'))} {m.get('nome')}" for m in movs if ALERTA.search(m.get("nome", ""))]
            item["alerta_movimentos"] = " | ".join(alertas[-3:])

    if pubs:
        pubs.sort(key=lambda p: p.get("data_disponibilizacao", ""))
        ult = pubs[-1]
        texto = re.sub(r"<[^>]+>|\s+", " ", ult.get("texto", ""))[:300]
        item["ult_publicacao"] = (f"{_data_iso(ult.get('data_disponibilizacao'))} "
                                  f"{ult.get('tipoComunicacao', '')}: {texto}").strip()
        if not item.get("orgao_oficial"):
            item["orgao_oficial"] = ult.get("nomeOrgao", "")
        ativos = []
        for p in pubs:
            for d in p.get("destinatarios") or []:
                if d.get("polo") == "A" and d.get("nome") and d["nome"] not in ativos:
                    ativos.append(d["nome"].strip())
        if ativos and not item.get("autor"):
            item["autor"] = " e ".join(ativos[:2]) + (" e outros" if len(ativos) > 2 else "")

    ok = bool(src or pubs)
    item["busca_status"] = "ok" if ok and not erros else ("parcial: " if ok else "falhou: ") + "; ".join(erros)
    return item


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("lote")
    ap.add_argument("--so", nargs="*")
    a = ap.parse_args()
    with open(a.lote, newline="", encoding="utf-8") as f:
        leitor = csv.DictReader(f)
        campos = list(leitor.fieldnames)
        itens = list(leitor)
    for c in CAMPOS_NOVOS:
        if c not in campos:
            campos.append(c)

    def gravar():
        with open(a.lote, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=campos)
            w.writeheader()
            w.writerows(itens)

    feitos = 0
    for item in itens:
        if a.so and item["processo"] not in a.so:
            continue
        if item.get("busca_status") == "ok":
            continue
        processar(item)
        feitos += 1
        gravar()
        print(f"{item['processo']}: {item['busca_status']} | autor={item.get('autor') or '—'} | "
              f"últ. mov.={item.get('ult_mov_data')} {item.get('ult_mov_nome', '')[:60]}")
        time.sleep(0.5)
    gravar()
    print(f"{feitos} processos consultados em {datetime.datetime.now():%H:%M}")


if __name__ == "__main__":
    main()
