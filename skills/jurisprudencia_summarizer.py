"""Skill: Resume decisões jurídicas complexas em formato editorial utilizável."""

import re
from typing import Optional


TRIBUNAIS_SIGLAS = {
    "STJ": "Superior Tribunal de Justiça",
    "STF": "Supremo Tribunal Federal",
    "TJSP": "Tribunal de Justiça de São Paulo",
    "TJRJ": "Tribunal de Justiça do Rio de Janeiro",
    "TJMG": "Tribunal de Justiça de Minas Gerais",
    "TJRS": "Tribunal de Justiça do Rio Grande do Sul",
    "TJPR": "Tribunal de Justiça do Paraná",
    "TJSC": "Tribunal de Justiça de Santa Catarina",
    "TJBA": "Tribunal de Justiça da Bahia",
    "TJGO": "Tribunal de Justiça de Goiás",
}

FUNDAMENTOS_FREQUENTES = {
    "CDC_14": "Art. 14, CDC — Responsabilidade objetiva do fornecedor por defeito na prestação de serviço",
    "CDC_6": "Art. 6º, CDC — Direitos básicos do consumidor (facilitação da defesa, inversão do ônus)",
    "CC_927": "Art. 927, CC — Obrigação de reparar dano causado por ato ilícito",
    "CC_186": "Art. 186, CC — Ato ilícito (ação ou omissão voluntária, negligência, imprudência)",
    "BACEN_4935": "Resolução BACEN 4.935/2021 — Procedimentos para devolução em transações Pix suspeitas",
    "LGPD_46": "Art. 46, LGPD — Dever do controlador de adotar medidas de segurança",
    "SUMULASSTJ_479": "Súmula 479/STJ — As instituições financeiras respondem objetivamente pelos danos gerados por fortuito interno",
}


def summarize(
    decisao_texto: str,
    tribunal: str = "",
    numero_processo: str = "",
    verificado: bool = False,
) -> dict:
    """
    Resume uma decisão jurídica em formato editorial.

    Args:
        decisao_texto: Texto da ementa ou decisão
        tribunal: Sigla do tribunal
        numero_processo: Número do processo (se disponível)
        verificado: True se a decisão foi verificada como real

    Returns:
        dict com resumo estruturado
    """
    tese = _extract_tese(decisao_texto)
    fundamento = _extract_fundamento(decisao_texto)
    favorabilidade = _detect_favorabilidade(decisao_texto)
    risco = _assess_risk(decisao_texto, favorabilidade)
    aplicacao_pratica = _practical_application(tese, favorabilidade)
    linguagem_consumidor = _translate_to_consumer(tese)

    return {
        "tribunal": tribunal,
        "tribunal_completo": TRIBUNAIS_SIGLAS.get(tribunal, tribunal),
        "numero_processo": numero_processo or "Não informado",
        "verificado": verificado,
        "alerta_verificacao": "" if verificado else "⚠️ TESE NÃO VINCULADA A PROCESSO ESPECÍFICO — usar apenas como referência doutrinária",
        "tese": tese,
        "fundamento_legal": fundamento,
        "favorabilidade": favorabilidade,
        "risco_processual": risco,
        "aplicacao_pratica": aplicacao_pratica,
        "linguagem_consumidor": linguagem_consumidor,
        "usavel_em_conteudo": favorabilidade in ("FAVORÁVEL", "NEUTRA"),
        "formato_citacao": _format_citation(tribunal, numero_processo, tese, verificado),
    }


def build_legal_brief(decisoes: list[dict], tema: str) -> str:
    """
    Constrói um brief jurídico editorial a partir de múltiplas decisões.
    Retorna Markdown formatado pronto para uso no conteúdo.
    """
    favoraveis = [d for d in decisoes if d.get("favorabilidade") == "FAVORÁVEL"]
    desfavoraveis = [d for d in decisoes if d.get("favorabilidade") == "DESFAVORÁVEL"]
    neutras = [d for d in decisoes if d.get("favorabilidade") == "NEUTRA"]

    lines = [
        f"## Brief Jurídico: {tema}",
        "",
        f"**Panorama:** {len(favoraveis)} decisões favoráveis | {len(desfavoraveis)} desfavoráveis | {len(neutras)} neutras",
        "",
        "### Tese Dominante",
    ]

    if favoraveis:
        lines.append(favoraveis[0].get("tese", "Não identificada"))
        lines.append("")
        lines.append("### Fundamento Legal Principal")
        lines.append(favoraveis[0].get("fundamento_legal", "Não identificado"))
        lines.append("")

    if favoraveis:
        lines.append("### Decisões Favoráveis ao Consumidor")
        for d in favoraveis[:3]:
            lines.append(f"- {d.get('formato_citacao', '')}")
        lines.append("")

    if desfavoraveis:
        lines.append("### Atenção — Quando o Consumidor Perde")
        for d in desfavoraveis[:2]:
            lines.append(f"- {d.get('tese', '')} *({d.get('tribunal', '')})*")
        lines.append("")

    if favoraveis:
        lines.append("### Aplicação Prática")
        lines.append(favoraveis[0].get("aplicacao_pratica", ""))
        lines.append("")
        lines.append("### Linguagem para o Consumidor")
        lines.append(f"> {favoraveis[0].get('linguagem_consumidor', '')}")

    return "\n".join(lines)


def _extract_tese(texto: str) -> str:
    sentences = [s.strip() for s in texto.replace("\n", " ").split(".") if len(s.strip()) > 50]
    keywords = ["responsabilidade", "dever", "direito", "indenização", "obrigação", "culpa"]
    for sentence in sentences[:5]:
        if any(kw in sentence.lower() for kw in keywords):
            return sentence[:300] + ("..." if len(sentence) > 300 else ".")
    return sentences[0][:300] + "..." if sentences else texto[:200]


def _extract_fundamento(texto: str) -> str:
    text_lower = texto.lower()
    found = []
    for key, desc in FUNDAMENTOS_FREQUENTES.items():
        abbr = key.replace("_", " ").lower()
        if abbr in text_lower or key.lower() in text_lower:
            found.append(desc)
    if not found:
        patterns = [
            r"art(?:igo)?\.?\s*\d+[,\s].*?(?:CDC|CC|CP|CF|Lei)",
            r"súmula\s*\d+",
            r"resolução\s*\d+",
        ]
        for pattern in patterns:
            matches = re.findall(pattern, texto, re.IGNORECASE)
            found.extend(matches[:2])
    return "; ".join(found[:3]) if found else "Fundamento não extraído automaticamente"


def _detect_favorabilidade(texto: str) -> str:
    text_lower = texto.lower()
    favoravel_signals = [
        "provimento", "procedente", "indenizar", "responsabilidade",
        "dano moral", "ressarcimento", "condenar o réu", "obrigação de indenizar",
        "deve devolver", "banco responsável",
    ]
    desfavoravel_signals = [
        "improcedente", "culpa exclusiva do consumidor", "caso fortuito externo",
        "não há responsabilidade", "não comprovado", "improcedência",
    ]
    fav_count = sum(1 for s in favoravel_signals if s in text_lower)
    defav_count = sum(1 for s in desfavoravel_signals if s in text_lower)
    if fav_count > defav_count:
        return "FAVORÁVEL"
    elif defav_count > fav_count:
        return "DESFAVORÁVEL"
    return "NEUTRA"


def _assess_risk(texto: str, favorabilidade: str) -> str:
    if favorabilidade == "FAVORÁVEL":
        return "BAIXO — decisão apoia a tese do consumidor"
    elif favorabilidade == "DESFAVORÁVEL":
        text_lower = texto.lower()
        if "culpa exclusiva" in text_lower:
            return "ALTO — culpa exclusiva do consumidor reconhecida"
        return "MÉDIO — decisão desfavorável, analisar contexto"
    return "MÉDIO — neutralidade pode indicar divergência"


def _practical_application(tese: str, favorabilidade: str) -> str:
    if favorabilidade == "FAVORÁVEL":
        return (
            f"Use como argumento central. Cite para reforçar a tese de responsabilidade objetiva. "
            f"Aplica-se especialmente quando o banco nega responsabilidade por fraude eletrônica."
        )
    return "Use como contraponto para antecipar a defesa do banco e rebatê-la."


def _translate_to_consumer(tese: str) -> str:
    tese_lower = tese.lower()
    if "responsabilidade objetiva" in tese_lower:
        return "O banco é responsável pelo golpe mesmo que você tenha sido enganado — é o que diz a lei."
    elif "dano moral" in tese_lower:
        return "Além de devolver o dinheiro, o banco pode ser obrigado a pagar uma indenização por dano moral."
    elif "inversão" in tese_lower and "ônus" in tese_lower:
        return "Na Justiça, é o banco que precisa provar que não teve culpa — não você."
    return "A decisão judicial confirma que consumidores têm proteção legal nessa situação."


def _format_citation(tribunal: str, numero: str, tese: str, verificado: bool) -> str:
    marker = "" if verificado else " [TESE SEM PROCESSO VERIFICADO]"
    if numero and numero != "Não informado":
        return f"{tribunal} — {numero[:30]}... — *\"{tese[:100]}...\"*{marker}"
    return f"{tribunal} — *\"{tese[:100]}...\"*{marker}"
