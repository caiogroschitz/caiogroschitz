#!/usr/bin/env python3
"""
gerar_docx.py — Converte uma peça processual em Markdown para .docx no padrão
forense brasileiro (Times New Roman 12, espaçamento 1,5, justificado, recuo de
primeira linha, títulos hierárquicos, ementas recuadas), com tipografia correta
de cabeçalho.

Uso:
    python gerar_docx.py entrada.md "saida.docx"

CONVENÇÕES DE MARKDOWN (cabeçalho da peça):
  # NOME DA PEÇA        -> centralizado, negrito, CAIXA-ALTA (nome/título da peça)
  LINHA TODA EM CAIXA   -> endereçamento e fecho: alinhado à esquerda, negrito,
                           sem recuo (ex.: EXCELENTÍSSIMO ... / nomes de advogados)
  **Linha curta**       -> linha-cabeçalho em negrito, à esquerda, sem recuo
                           (ex.: **Processo nº 1000438-51.2016.5.02.0718**)
  ## Título             -> seção (negrito, CAIXA-ALTA, à esquerda)
  ### Subtítulo         -> subtítulo de tese (negrito)
  > linha               -> ementa/transcrição (recuada, fonte menor, simples)
  1. / a) / -           -> item de lista (pedidos, documentos)
  **negrito** / *itálico* dentro de qualquer parágrafo

Dependência: python-docx (pip install python-docx --break-system-packages)
"""
import sys, re, argparse

try:
    from docx import Document
    from docx.shared import Pt, Cm
    from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
except ImportError:
    sys.stderr.write("Falta python-docx. Rode: pip install python-docx --break-system-packages\n")
    sys.exit(1)

FONTE = "Times New Roman"
TAM_CORPO = 12
TAM_EMENTA = 10
TAM_TITULO = 12
TAM_NOME_PECA = 13


def add_inline(par, texto):
    for p in re.split(r"(\*\*.+?\*\*|\*.+?\*)", texto):
        if not p:
            continue
        if p.startswith("**") and p.endswith("**"):
            r = par.add_run(p[2:-2]); r.bold = True
        elif p.startswith("*") and p.endswith("*"):
            r = par.add_run(p[1:-1]); r.italic = True
        else:
            par.add_run(p)


def style_corpo(par):
    f = par.paragraph_format
    f.line_spacing_rule = WD_LINE_SPACING.ONE_POINT_FIVE
    f.space_after = Pt(8)
    f.first_line_indent = Cm(2.0)
    par.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY


def is_caps_line(line):
    """Linha de cabeçalho em caixa-alta: tem letras e nenhuma minúscula."""
    if any(c.islower() and c not in "ªº" for c in line):
        return False
    return sum(1 for c in line if c.isalpha()) >= 6


def is_full_bold_short(line):
    return line.startswith("**") and line.endswith("**") and line.count("**") == 2 and len(line) <= 110


def build(md_text):
    doc = Document()
    normal = doc.styles["Normal"]
    normal.font.name = FONTE
    normal.font.size = Pt(TAM_CORPO)
    for sec in doc.sections:
        sec.left_margin = Cm(3.0); sec.right_margin = Cm(2.0)
        sec.top_margin = Cm(2.5); sec.bottom_margin = Cm(2.0)

    lines = md_text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        st = line.strip()
        if not st:
            i += 1; continue

        # Nome da peça: # ...  -> centralizado, negrito, caixa-alta
        if st.startswith("# ") and not st.startswith("## "):
            txt = st[2:].strip()
            doc.add_paragraph()
            p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            f = p.paragraph_format; f.space_before = Pt(6); f.space_after = Pt(12)
            f.line_spacing_rule = WD_LINE_SPACING.ONE_POINT_FIVE
            r = p.add_run(txt.upper()); r.bold = True; r.font.size = Pt(TAM_NOME_PECA)
            i += 1; continue

        # Seção ##
        if st.startswith("## "):
            txt = st[3:].strip()
            doc.add_paragraph()
            p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.space_before = Pt(6); p.paragraph_format.space_after = Pt(8)
            p.paragraph_format.line_spacing_rule = WD_LINE_SPACING.ONE_POINT_FIVE
            r = p.add_run(txt.upper()); r.bold = True; r.font.size = Pt(TAM_TITULO)
            i += 1; continue

        # Subtítulo ###
        if st.startswith("### "):
            txt = st[4:].strip()
            p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.space_after = Pt(6)
            p.paragraph_format.line_spacing_rule = WD_LINE_SPACING.ONE_POINT_FIVE
            r = p.add_run(txt); r.bold = True; r.font.size = Pt(TAM_TITULO)
            i += 1; continue

        # Ementa / transcrição recuada >
        if st.startswith(">"):
            txt = st.lstrip(">").strip()
            p = doc.add_paragraph()
            f = p.paragraph_format
            f.left_indent = Cm(4.0); f.right_indent = Cm(0.5)
            f.line_spacing_rule = WD_LINE_SPACING.SINGLE; f.space_after = Pt(6)
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            add_inline(p, txt)
            for rr in p.runs:
                rr.font.size = Pt(TAM_EMENTA)
            i += 1; continue

        # Lista numerada / alínea / hífen
        m = re.match(r"^(\d+\.|[a-z]\))\s+(.*)$", st)
        if m or st.startswith("- "):
            conteudo = st[2:] if st.startswith("- ") else st
            p = doc.add_paragraph()
            f = p.paragraph_format
            f.left_indent = Cm(2.0); f.first_line_indent = Cm(-0.6)
            f.line_spacing_rule = WD_LINE_SPACING.ONE_POINT_FIVE; f.space_after = Pt(4)
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            add_inline(p, ("• " + conteudo) if st.startswith("- ") else conteudo)
            i += 1; continue

        # Linha-cabeçalho em negrito (ex.: número do processo): esquerda, sem recuo
        if is_full_bold_short(st):
            p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.space_after = Pt(8)
            p.paragraph_format.line_spacing_rule = WD_LINE_SPACING.ONE_POINT_FIVE
            add_inline(p, st)
            i += 1; continue

        # Endereçamento / fecho (linha inteira em caixa-alta): esquerda, negrito, sem recuo
        if is_caps_line(st):
            p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.space_after = Pt(8)
            p.paragraph_format.line_spacing_rule = WD_LINE_SPACING.ONE_POINT_FIVE
            add_inline(p, st)
            for rr in p.runs:
                rr.bold = True
            i += 1; continue

        # Parágrafo de prosa (junta linhas até linha em branco ou novo marcador)
        buff = [st]; j = i + 1
        while j < len(lines) and lines[j].strip() and not re.match(r"^(#|>|\d+\.\s|[a-z]\)\s|-\s)", lines[j].strip()) and not is_caps_line(lines[j].strip()) and not is_full_bold_short(lines[j].strip()):
            buff.append(lines[j].strip()); j += 1
        p = doc.add_paragraph(); style_corpo(p)
        add_inline(p, " ".join(buff))
        i = j

    return doc


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("entrada")
    ap.add_argument("saida")
    ap.add_argument("--titulo", default=None, help="(opcional) título centralizado no topo; em peça real prefira '# NOME DA PEÇA' no corpo")
    args = ap.parse_args()
    md = open(args.entrada, encoding="utf-8").read()
    doc = build(md)
    if args.titulo:
        pass  # mantido só por compatibilidade; não recomendado em peças reais
    doc.save(args.saida)
    print(f"OK -> {args.saida}")


if __name__ == "__main__":
    main()
