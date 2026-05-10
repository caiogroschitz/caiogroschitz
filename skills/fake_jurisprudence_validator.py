"""Skill: Valida se citações jurisprudenciais são coerentes e existem."""

import re
from datetime import datetime


TRIBUNAIS_VALIDOS = {
    "STJ", "STF", "TJSP", "TJRJ", "TJMG", "TJRS", "TJPR", "TJSC",
    "TJBA", "TJGO", "TJPE", "TJDF", "TJCE", "TJAM", "TJPA",
    "TRF1", "TRF2", "TRF3", "TRF4", "TRF5",
}

NUMERO_PROCESSO_PATTERNS = [
    r"\d{7}-\d{2}\.\d{4}\.\d\.\d{2}\.\d{4}",
    r"\d{7}-\d{2}\.\d{4}\.\d\.\d{4}",
    r"REsp\s*\d{6,7}",
    r"AgRg\s*no\s*REsp\s*\d{6,7}",
    r"AREsp\s*\d{6,7}",
    r"Ap\s*\d{7}-?\d{2}",
    r"\d{4}/\d{7}-\d",
]

TESES_CONSOLIDADAS_STJ = {
    "sumula_479": {
        "texto": "As instituições financeiras respondem objetivamente pelos danos gerados por fortuito interno",
        "numero": "Súmula 479",
        "tribunal": "STJ",
        "ano": 2012,
        "aplicacao": "Fraude eletrônica, golpes digitais, invasão de conta",
        "solida": True,
    },
    "responsabilidade_pix": {
        "texto": "Banco responde objetivamente por transação Pix fraudulenta quando há falha no sistema de segurança",
        "numero": "Tese consolidada (sem súmula específica até 2024)",
        "tribunal": "STJ/TJEs",
        "ano": 2022,
        "aplicacao": "Golpe do Pix por falso atendente, engenharia social",
        "solida": True,
    },
    "consignado_fraude": {
        "texto": "Empréstimo consignado contratado por terceiro fraudador gera responsabilidade objetiva da financeira",
        "numero": "Tese consolidada (múltiplos julgados)",
        "tribunal": "STJ/TJEs",
        "ano": 2020,
        "aplicacao": "Empréstimos não autorizados, INSS fraude",
        "solida": True,
    },
}

SINAIS_FAKE_JURISPRUDENCIA = [
    "decidiu unanimemente em favor do consumidor",
    "garantiu indenização em todos os casos",
    "determinou que todos os bancos devolvam",
    "fixou valor mínimo de indenização",
    "proibiu bancos de cobrar",
    "todos os consumidores têm direito",
    r"REsp\s*9{6,}",
    r"Processo\s*9{7}",
]


def validate_citation(
    citacao: str,
    tribunal: str = "",
    tese: str = "",
    verificado_externamente: bool = False,
) -> dict:
    """
    Valida uma citação jurisprudencial.

    Args:
        citacao: Texto da citação (número + tribunal + tese)
        tribunal: Sigla do tribunal
        tese: Texto da tese jurídica
        verificado_externamente: Se foi verificado em fonte oficial

    Returns:
        dict com resultado da validação
    """
    issues = []
    warnings = []
    score_confianca = 50

    tribunal_upper = tribunal.upper() if tribunal else _extract_tribunal(citacao)
    if tribunal_upper not in TRIBUNAIS_VALIDOS:
        issues.append(f"Tribunal '{tribunal_upper}' não reconhecido")
        score_confianca -= 20

    numero = _extract_numero(citacao)
    if numero:
        score_confianca += 20
    else:
        warnings.append("Número do processo não identificado — verifique antes de publicar")
        score_confianca -= 10

    for sinal in SINAIS_FAKE_JURISPRUDENCIA:
        if re.search(sinal, citacao, re.IGNORECASE):
            issues.append(f"Sinal de jurisprudência falsa detectado: '{sinal}'")
            score_confianca -= 40

    tese_check = _check_tese_coerencia(tese or citacao)
    if not tese_check["coerente"]:
        issues.append(f"Tese incoerente com padrão jurisprudencial: {tese_check['motivo']}")
        score_confianca -= 15

    if _is_near_consolidada(tese or citacao):
        score_confianca += 15

    if verificado_externamente:
        score_confianca += 30

    score_confianca = max(0, min(100, score_confianca))

    return {
        "citacao": citacao[:200],
        "tribunal": tribunal_upper,
        "numero_processo": numero,
        "status": _status(score_confianca, issues),
        "score_confianca": score_confianca,
        "issues": issues,
        "warnings": warnings,
        "verificado_externamente": verificado_externamente,
        "publicavel": score_confianca >= 50 and not any("falsa" in i for i in issues),
        "marcacao_recomendada": _get_marking(score_confianca, verificado_externamente),
        "instrucao": _get_instruction(score_confianca, issues),
    }


def validate_batch(citacoes: list[dict]) -> dict:
    """Valida múltiplas citações em lote."""
    results = []
    aprovadas = 0
    reprovadas = 0
    alertas = 0

    for cit in citacoes:
        result = validate_citation(
            citacao=cit.get("citacao", ""),
            tribunal=cit.get("tribunal", ""),
            tese=cit.get("tese", ""),
            verificado_externamente=cit.get("verificado", False),
        )
        results.append(result)
        if result["status"] == "APROVADA":
            aprovadas += 1
        elif result["status"] == "REPROVADA":
            reprovadas += 1
        else:
            alertas += 1

    return {
        "total": len(citacoes),
        "aprovadas": aprovadas,
        "com_alerta": alertas,
        "reprovadas": reprovadas,
        "validacoes": results,
        "pode_publicar": reprovadas == 0,
    }


def get_tese_consolidada(tema: str) -> dict:
    """Retorna tese consolidada para temas conhecidos."""
    tema_lower = tema.lower()
    for key, tese in TESES_CONSOLIDADAS_STJ.items():
        if any(word in tema_lower for word in key.split("_")):
            return tese
    if "pix" in tema_lower or "fraude" in tema_lower:
        return TESES_CONSOLIDADAS_STJ["responsabilidade_pix"]
    if "consignado" in tema_lower:
        return TESES_CONSOLIDADAS_STJ["consignado_fraude"]
    return TESES_CONSOLIDADAS_STJ["sumula_479"]


def _extract_tribunal(texto: str) -> str:
    for trib in TRIBUNAIS_VALIDOS:
        if trib in texto.upper():
            return trib
    return ""


def _extract_numero(texto: str) -> str:
    for pattern in NUMERO_PROCESSO_PATTERNS:
        match = re.search(pattern, texto, re.IGNORECASE)
        if match:
            return match.group()
    return ""


def _check_tese_coerencia(tese: str) -> dict:
    tese_lower = tese.lower()
    incoerencias = [
        ("garantiu", "Decisão judicial não garante — determina no caso concreto"),
        ("todos os casos", "Jurisprudência não se aplica universalmente"),
        ("valor mínimo de", "Tribunais não fixam valores mínimos absolutos"),
        ("proibiu todos", "Decisão judicial vincula as partes, não o mercado inteiro"),
    ]
    for sinal, motivo in incoerencias:
        if sinal in tese_lower:
            return {"coerente": False, "motivo": motivo}
    return {"coerente": True, "motivo": ""}


def _is_near_consolidada(texto: str) -> bool:
    texto_lower = texto.lower()
    for tese_data in TESES_CONSOLIDADAS_STJ.values():
        keywords = tese_data["texto"].lower().split()[:5]
        if sum(1 for kw in keywords if kw in texto_lower) >= 3:
            return True
    return False


def _status(score: int, issues: list) -> str:
    if any("falsa" in i for i in issues):
        return "REPROVADA"
    if score >= 70:
        return "APROVADA"
    if score >= 40:
        return "ALERTA"
    return "REPROVADA"


def _get_marking(score: int, verificado: bool) -> str:
    if verificado:
        return "✅ Processo verificado em fonte oficial"
    if score >= 70:
        return "📌 Tese coerente — verificar processo antes de publicar"
    return "⚠️ TESE SEM PROCESSO VERIFICADO — usar como referência doutrinária apenas"


def _get_instruction(score: int, issues: list) -> str:
    if any("falsa" in i for i in issues):
        return "BLOQUEADO — remover esta citação imediatamente. Risco de fake jurisprudence."
    if score >= 70:
        return "Verificar o número do processo no JusBrasil ou tribunal antes de publicar."
    return "Reformular como tese jurídica consolidada sem citar processo específico."
