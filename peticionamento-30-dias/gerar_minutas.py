"""Gera as minutas de impulso (.docx no timbrado do escritório) a partir do lote.csv.

Uso:
    python gerar_minutas.py lote.csv MODELO.docx --pasta "SAIDA" [--data 2026-09-25] [--so 5001248-92.2025.8.08.0016]

- Uma minuta por processo: "{nº do processo} - petição de impulso.docx".
- Se a minuta já existir na pasta, ela NÃO é refeita (rodar de novo nunca duplica nem reescreve).
- Também grava "Controle - Peticionamento 30 dias.xlsx" na mesma pasta.
- Nada é inventado: sem o nome do autor (coluna `autor`), sai o marcador [NOME DA PARTE AUTORA].
"""
import argparse
import copy
import csv
import datetime
import os
import re
import unicodedata

import docx
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill

MESES = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto",
         "setembro", "outubro", "novembro", "dezembro"]

# OAB do Mario por tribunal (fonte: skills picpay-levantamento-valores e picpay-cumprimento-liminar).
# Chave: (segmento J, tribunal TR) do número CNJ.
OAB_MARIO = {
    ("8", "26"): ("SP", "OAB/SP 246.508"),
    ("8", "08"): ("ES", "OAB/ES 39.165-S"),
    ("8", "13"): ("MG", "OAB/MG 230.285-S"),
    ("8", "07"): ("DF", "OAB/DF 75.486-S"),
    ("8", "19"): ("RJ", "OAB/RJ 242.778-S"),
    ("8", "16"): ("PR", "OAB/PR 122.193-S"),
    ("8", "05"): ("BA", "OAB/BA 77.639-S"),
    ("8", "09"): ("GO", "OAB/GO 68.355-S"),
    ("8", "17"): ("PE", "OAB/PE 63.181-S"),
    ("4", "06"): ("MG", "OAB/MG 230.285-S"),  # TRF6 = Justiça Federal em Minas Gerais
}
UF_NOME = {"ES": "ESPÍRITO SANTO", "MG": "MINAS GERAIS", "DF": "DISTRITO FEDERAL", "SP": "SÃO PAULO",
           "RJ": "RIO DE JANEIRO", "PR": "PARANÁ", "BA": "BAHIA", "GO": "GOIÁS", "PE": "PERNAMBUCO"}

REUS = [
    (r"picpay\s*bank", "PICPAY BANK – BANCO MÚLTIPLO S.A."),
    (r"picpay\s*instituic", "PICPAY INSTITUIÇÃO DE PAGAMENTO S.A."),
    (r"picpay\s*servic", "PICPAY SERVIÇOS S.A."),
    (r"picpay\s*invest", "PICPAY INVEST DISTRIBUIDORA DE TÍTULOS E VALORES MOBILIÁRIOS LTDA."),
]

MARCA_AUTOR = "[NOME DA PARTE AUTORA]"
MARCA_REU = "[PARTE RÉ – CONFERIR NO ASTREA]"

# Categorias da coluna "Providência sugerida" que geram minuta.
SEM_MINUTA = {
    "Acordo – concluir tratativa": "Sem minuta: aguarda definição do cliente sobre o acordo (aceite ou recusa).",
    "Cumprimento – comprovar pagamento": "Sem minuta: aguarda o comprovante de pagamento para requerer a extinção (art. 924, II, do CPC).",
    "Aguardar – suspenso/IRDR": "Sem minuta: feito sobrestado; conferir no Astrea se a suspensão segue vigente.",
}


def sem_acento(s):
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn").lower()


def data_extenso(d):
    return f"{d.day} de {MESES[d.month - 1]} de {d.year}"


def tribunal(processo):
    m = re.match(r"\d{7}-\d{2}\.\d{4}\.(\d)\.(\d{2})\.\d{4}$", processo)
    return (m.group(1), m.group(2)) if m else (None, None)


def nome_reu(cliente):
    c = sem_acento(cliente)
    for padrao, nome in REUS:
        if re.search(padrao, c):
            return nome, ""
    return MARCA_REU, f"Cliente cadastrado na planilha como “{cliente}”, que não é entidade PicPay: conferir a parte ré no Astrea."


# ---------------------------------------------------------------- endereçamento

ACENTOS = {"brasilia": "Brasília", "vitoria": "Vitória", "civel": "Cível", "especia": "Especial",
           "santa barbara": "Santa Bárbara"}


def _acentua(s):
    for k, v in ACENTOS.items():
        s = re.sub(rf"(?i)\b{k}\b", v, s)
    return s


def _limpa_cidade(foro, uf):
    c = foro or ""
    c = re.sub(r"(?i)comarca\s+d[aeo]s?\s+capital", "", c)
    c = re.sub(r"(?i)^.*comarca\s+de\s+", "", c)
    c = re.sub(r"(?i)\s*-\s*(vara única|juizado especial)\s*$", "", c)
    c = re.sub(rf"(?i)\s*-\s*({uf}|{UF_NOME.get(uf, '')})\s*$", "", c)
    c = c.strip(" -")
    if sem_acento(c) in {sem_acento(UF_NOME.get(uf, "")), sem_acento(uf)}:
        return ""
    return c


def enderecamento(item, uf, justica):
    """Monta o endereçamento a partir das colunas Vara/Foro da planilha (sempre marcado para conferência).

    Se a coluna `enderecamento_astrea` estiver preenchida, ela prevalece.
    """
    if item.get("enderecamento_astrea"):
        return item["enderecamento_astrea"].strip(), ""
    vara = _acentua(" ".join((item["vara"] or "").split()))
    foro = _acentua(" ".join((item["foro"] or "").split()))
    obs = "Endereçamento montado pela planilha (vara/foro): conferir no Astrea ou nos autos."
    if justica == "4":
        juizo = re.sub(r"(?i)^juízo\s+(substituto\s+)?d[ao]\s+", "", vara)
        cidade = _limpa_cidade(foro, uf).upper() or "[CIDADE]"
        return (f"EXCELENTÍSSIMO SENHOR DOUTOR JUIZ FEDERAL DA {juizo.upper()} DA SUBSEÇÃO JUDICIÁRIA DE "
                f"{cidade} - {uf}."), obs

    # Cidade: "Comarca de X" em qualquer dos campos; senão, o Foro; senão, o trecho do campo Vara que não é órgão.
    cidade = ""
    for campo in (vara, foro):
        m = re.search(r"(?i)comarca\s+de\s+([^-]+?)\s*(-|$)", campo)
        if m:
            cidade = m.group(1).strip()
            break
    if not cidade:
        cidade = _limpa_cidade(foro, uf)
    partes = [p.strip() for p in vara.split(" - ") if p.strip()]
    orgaos = [p for p in partes if re.search(r"(?i)vara|juizado|unidade|juízo", p)]
    if not cidade:
        outros = [p for p in partes if p not in orgaos and not re.search(r"(?i)comarca|\bJD\b", p)]
        cidade = _limpa_cidade(outros[0], uf) if outros else ""
    # Órgão: junta os trechos que são órgão ou juizado distrital ("3º JD"), sem a menção à comarca.
    trechos = [p for p in partes if p in orgaos or re.search(r"\bJD\b", p)]
    orgao = " - ".join(trechos)
    orgao = re.sub(r"(?i)\s*(d[aeo]\s+)?comarca(\s+d[aeo])?(\s+[^-]+)?$", "", orgao).strip(" -")
    orgao = re.sub(r"(?i)^juízo\s+d[aeo]\s+", "", orgao)
    orgao = re.sub(r"(?i)\s+d[aeo]s?$", "", orgao).strip(" -")
    if not orgao:
        orgao = "[VARA/JUIZADO]"
    elif not re.search(r"\d|única", orgao, re.I):
        orgao = f"[Nª] {orgao}"  # sem número: conferir qual vara/juizado
    orgao = orgao.upper()
    artigo = "DO" if re.match(r"(\[Nª\]\s*)?(\d+º\s*)?(JUIZADO|JUÍZO)", orgao) else "DA"
    local = ("DA CIRCUNSCRIÇÃO JUDICIÁRIA DE" if uf == "DF" else "DA COMARCA DE")
    texto = (f"EXCELENTÍSSIMO SENHOR DOUTOR JUIZ DE DIREITO {artigo} MM. {orgao} {local} "
             f"{cidade.upper() or '[COMARCA]'} - {uf}.")
    return texto, obs


# ---------------------------------------------------------------- texto por categoria

def textos(item, data_hist):
    prov = item["providencia"]
    desde = f"desde {data_hist}" if data_hist else "há mais de trinta dias"
    fundamento_duracao = ("em observância ao princípio da razoável duração do processo (art. 5º, LXXVIII, da "
                          "Constituição Federal) e ao dever de o juiz velar por ela (arts. 4º e 139, II, do Código de "
                          "Processo Civil)")
    if prov == "Conclusão para sentença":
        pedido = "a CONCLUSÃO DOS AUTOS PARA PROLAÇÃO DE SENTENÇA"
        corpo = [
            f"O feito encontra-se apto a julgamento, sem que tenha sobrevindo pronunciamento judicial {desde}, "
            "embora não haja diligência pendente a cargo das partes.",
            "Os arts. 226 e 227 do Código de Processo Civil fixam prazo para a prolação de sentença, admitida sua "
            f"prorrogação apenas por motivo justificado. Assim, {fundamento_duracao}, a ré requer a imediata "
            "conclusão dos autos e a prolação de sentença.",
        ]
    elif prov in ("Impulso oficial – requerer prosseguimento", "Análise + impulso oficial"):
        pedido = "o REGULAR PROSSEGUIMENTO DO FEITO"
        corpo = [
            f"Os autos encontram-se paralisados {desde}, sem despacho que lhes dê andamento, embora não haja "
            "providência pendente a cargo da ré.",
            f"Desse modo, {fundamento_duracao}, a ré requer o prosseguimento do feito, com a conclusão dos autos "
            "para despacho ou, nada mais havendo a ser produzido, para sentença.",
        ]
    elif prov == "Designação de audiência":
        pedido = "a DESIGNAÇÃO DE AUDIÊNCIA OU O JULGAMENTO ANTECIPADO DO MÉRITO"
        corpo = [
            f"Apresentada a defesa, o feito aguarda a designação de audiência {desde}, sem que tenha havido "
            "novo pronunciamento judicial.",
            f"Assim, {fundamento_duracao}, a ré requer a designação de audiência de conciliação, instrução e "
            "julgamento ou, sendo desnecessária a produção de outras provas, o julgamento antecipado do mérito, "
            "nos termos do art. 355, I, do Código de Processo Civil.",
        ]
    elif prov == "Recursal – impulso do julgamento":
        pedido = "INFORMAÇÕES SOBRE O PROCESSAMENTO DO RECURSO"
        corpo = [
            f"Interposto recurso nos autos, não houve notícia de sua distribuição ou inclusão em pauta de "
            f"julgamento {desde}.",
            f"Assim, {fundamento_duracao}, a ré requer sejam prestadas informações sobre a distribuição do "
            "recurso e sua inclusão em pauta, com a remessa dos autos à instância recursal, caso ainda não "
            "efetivada. Subsidiariamente, se o recurso já tiver sido julgado, requer a certificação do trânsito "
            "em julgado e a baixa dos autos, na forma do art. 1.006 do Código de Processo Civil.",
        ]
    elif prov == "Habilitação/cadastro nos autos":
        pedido = "a JUNTADA DO INSTRUMENTO DE MANDATO E O CADASTRAMENTO DE SEUS PATRONOS"
        corpo = [
            "Para a regular representação processual, a ré junta o instrumento de mandato e os atos "
            "constitutivos anexos.",
            "Requer, por isso, o cadastramento de seus patronos no sistema processual, para que passem a receber "
            "as intimações, e a abertura de vista dos autos.",
        ]
    else:
        return None
    return pedido, corpo


# ---------------------------------------------------------------- montagem do .docx

def _p(texto_runs, alinhamento="both", primeira_linha=None, esquerda=None):
    """Parágrafo no padrão das peças do escritório: Prompt 12, entrelinha 1,5, 10pt antes/depois."""
    p = OxmlElement("w:p")
    ppr = OxmlElement("w:pPr")
    sp = OxmlElement("w:spacing")
    for k, v in (("w:after", "200"), ("w:before", "200"), ("w:line", "360"), ("w:lineRule", "auto")):
        sp.set(qn(k), v)
    ppr.append(sp)
    if primeira_linha is not None or esquerda is not None:
        ind = OxmlElement("w:ind")
        ind.set(qn("w:left"), str(esquerda or 0))
        ind.set(qn("w:firstLine"), str(primeira_linha or 0))
        ppr.append(ind)
    jc = OxmlElement("w:jc")
    jc.set(qn("w:val"), alinhamento)
    ppr.append(jc)
    p.append(ppr)
    for texto, negrito in texto_runs:
        r = OxmlElement("w:r")
        rpr = OxmlElement("w:rPr")
        f = OxmlElement("w:rFonts")
        for k in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
            f.set(qn(k), "Prompt")
        rpr.append(f)
        if negrito:
            rpr.append(OxmlElement("w:b"))
            rpr.append(OxmlElement("w:bCs"))
        for tag in ("w:sz", "w:szCs"):
            s = OxmlElement(tag)
            s.set(qn("w:val"), "24")
            rpr.append(s)
        r.append(rpr)
        t = OxmlElement("w:t")
        t.set(qn("xml:space"), "preserve")
        t.text = texto
        r.append(t)
        p.append(r)
    return p


def montar(modelo, destino, item, reu, autor, ender, pedido, corpo, oab_mario, fecho):
    d = docx.Document(modelo)
    body = d.element.body
    tabela = body.find(qn("w:tbl"))
    # Remove tudo que vem antes da tabela de assinaturas (endereçamento, campos [ESPECIFICAR], linhas de teste).
    for el in list(body):
        if el is tabela:
            break
        body.remove(el)
    INDENT = 2126  # recuo de primeira linha usado nas peças do escritório (~3,75 cm)
    novos = [
        _p([(ender, True)]),
        _p([]), _p([]),
        _p([(f"Autos nº {item['processo']}", True)]),
        _p([(reu, True), (", já devidamente qualificada e representada nos autos da ação em epígrafe, que lhe é "
                          "movida por ", False), (autor, True),
            (", vem, respeitosamente, à presença de Vossa Excelência, por seus advogados infra-assinados, requerer ",
             False), (pedido, True), (", nos termos a seguir dispostos.", False)], esquerda=0, primeira_linha=0),
    ]
    novos += [_p([(c, False)], primeira_linha=INDENT) for c in corpo]
    novos += [
        _p([("Por fim, requer que as publicações ocorridas nestes autos sejam feitas exclusivamente em nome de ",
             False), ("MARIO THADEU LEME DE BARROS FILHO", True), (f" ({oab_mario}), sob pena de nulidade.", False)],
           primeira_linha=INDENT),
        _p([]),
        _p([("Termos em que pede deferimento.", False)], alinhamento="center"),
        _p([(f"São Paulo, {fecho}.", False)], alinhamento="center"),
    ]
    for el in novos:
        tabela.addprevious(el)
    # Atualiza a OAB do Mario na tabela de assinaturas conforme o estado.
    for cel in d.tables[0]._cells:
        for par in cel.paragraphs:
            if re.fullmatch(r"OAB/SP\s*246\.508", par.text.strip()):
                par.runs[0].text = oab_mario
                for r in par.runs[1:]:
                    r.text = ""
    d.save(destino)


# ---------------------------------------------------------------- controle

CORES = {
    "Minuta pronta para revisão": "C6EFCE",
    "Minuta com marcador — completar antes de protocolar": "FFEB9C",
    "Sem minuta — pendência": "F4CCCC",
    "Minuta já existia — não refeita": "DDEBF7",
}


def gravar_controle(caminho, linhas):
    wb = Workbook()
    ws = wb.active
    ws.title = "Controle"
    cab = ["Linha planilha", "Nº do processo", "Prioridade", "Dias parado", "Providência", "Parte ré", "Parte autora",
           "Fonte do autor", "OAB Mario", "Status", "Observações", "Arquivo"]
    ws.append(cab)
    for c in ws[1]:
        c.font = Font(bold=True)
    for l in linhas:
        ws.append([l.get(k, "") for k in ("linha", "processo", "prioridade", "dias", "providencia", "reu", "autor",
                                           "fonte_autor", "oab", "status", "obs", "arquivo")])
        cor = CORES.get(l["status"])
        if cor:
            for c in ws[ws.max_row]:
                c.fill = PatternFill("solid", fgColor=cor)
    larguras = [8, 28, 10, 8, 32, 34, 30, 12, 18, 40, 70, 45]
    for i, w in enumerate(larguras):
        ws.column_dimensions[chr(65 + i)].width = w
    for row in ws.iter_rows(min_row=2):
        for c in row:
            c.alignment = Alignment(wrap_text=True, vertical="top")
    ws.freeze_panes = "A2"
    wb.save(caminho)


# ---------------------------------------------------------------- principal

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("lote")
    ap.add_argument("modelo")
    ap.add_argument("--pasta", required=True, help="pasta de saída (ex.: a pasta sincronizada 'Peticionamento 30 dias')")
    ap.add_argument("--data", help="data do fecho, AAAA-MM-DD (padrão: hoje)")
    ap.add_argument("--so", nargs="*", help="gerar só estes processos (piloto)")
    a = ap.parse_args()

    fecho = data_extenso(datetime.date.fromisoformat(a.data) if a.data else datetime.date.today())
    os.makedirs(a.pasta, exist_ok=True)
    with open(a.lote, newline="", encoding="utf-8") as f:
        itens = list(csv.DictReader(f))

    controle = []
    geradas = 0
    for item in itens:
        if a.so and item["processo"] not in a.so:
            continue
        obs = []
        justica, tr = tribunal(item["processo"])
        uf, oab = OAB_MARIO.get((justica, tr), (None, None))
        reu, obs_reu = nome_reu(item["cliente"])
        if obs_reu:
            obs.append(obs_reu)
        autor = item.get("autor", "").strip().upper() or MARCA_AUTOR
        linha = {"linha": item["linha_planilha"], "processo": item["processo"], "prioridade": item["prioridade"],
                 "dias": item["dias_parado"], "providencia": item["providencia"], "reu": reu,
                 "autor": autor, "fonte_autor": "Astrea" if autor != MARCA_AUTOR else "—", "oab": oab or "—"}
        if item.get("obs_astrea"):
            obs.append(f"Astrea: {item['obs_astrea']}")
        if "ATENÇÃO" in item.get("detalhamento", ""):
            obs.append("Planilha: " + item["detalhamento"].split("ATENÇÃO", 1)[1].strip(" –-"))
        if item.get("status_projuris") and item["status_projuris"] != "ATIVOS":
            obs.append(f"Projuris: {item['status_projuris']} — confirmar se ainda cabe peticionar.")

        if item["providencia"] in SEM_MINUTA:
            controle.append({**linha, "status": "Sem minuta — pendência",
                             "obs": " ".join([SEM_MINUTA[item["providencia"]]] + obs), "arquivo": ""})
            continue
        if not oab:
            controle.append({**linha, "status": "Sem minuta — pendência",
                             "obs": " ".join(["Tribunal fora da tabela de OAB do Mario: informar a inscrição."] + obs),
                             "arquivo": ""})
            continue
        data_hist = ""
        if item.get("data_ult_historico"):
            try:
                data_hist = data_extenso(datetime.date.fromisoformat(item["data_ult_historico"]))
                obs.append("Data de paralisação tirada do último histórico do Astrea (planilha): conferir com a "
                           "última movimentação nos autos.")
            except ValueError:
                pass
        t = textos(item, data_hist)
        if t is None:
            controle.append({**linha, "status": "Sem minuta — pendência",
                             "obs": " ".join([f"Providência não mapeada: {item['providencia']}."] + obs),
                             "arquivo": ""})
            continue
        pedido, corpo = t
        ender, obs_ender = enderecamento(item, uf, justica)
        if obs_ender:
            obs.append(obs_ender)
        if item["providencia"] == "Habilitação/cadastro nos autos":
            obs.append("Anexar procuração/substabelecimento e atos constitutivos no protocolo.")
        if item["providencia"] == "Recursal – impulso do julgamento":
            obs.append("Se os autos já estiverem na Turma/Câmara, reendereçar ao relator antes de protocolar.")
        if item["providencia"] == "Análise + impulso oficial":
            obs.append("Planilha sem gatilho claro: conferir no Astrea a providência pendente do juízo.")

        nome = f"{item['processo']} - petição de impulso.docx"
        destino = os.path.join(a.pasta, nome)
        marcadores = [m for m in (MARCA_AUTOR, MARCA_REU, "[VARA/JUIZADO]", "[Nª]", "[COMARCA]", "[CIDADE]")
                      if m in (autor + reu + ender)]
        if os.path.exists(destino):
            status = "Minuta já existia — não refeita"
        else:
            montar(a.modelo, destino, item, reu, autor, ender, pedido, corpo, oab, fecho)
            geradas += 1
            status = ("Minuta com marcador — completar antes de protocolar" if marcadores
                      else "Minuta pronta para revisão")
        if marcadores:
            obs.insert(0, "Marcadores a completar: " + ", ".join(marcadores) + ".")
        controle.append({**linha, "status": status, "obs": " ".join(obs), "arquivo": nome})

    gravar_controle(os.path.join(a.pasta, "Controle - Peticionamento 30 dias.xlsx"), controle)
    from collections import Counter
    resumo = Counter(l["status"] for l in controle)
    print(f"{geradas} minutas novas em {a.pasta}")
    for k, v in resumo.items():
        print(f"  {v:3d}  {k}")


if __name__ == "__main__":
    main()
