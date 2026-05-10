"""Skill: Detecta temas com alto potencial de conversão jurídica."""

import json
from typing import Any


CONVERSION_SIGNALS = {
    "urgencia_emocional": [
        "perdi meu dinheiro", "não reconheço", "não autorizei",
        "fui enganado", "golpe", "fraude", "invasão", "roubaram",
    ],
    "acao_judicial_clara": [
        "responsabilidade", "indenização", "devolução", "ressarcimento",
        "banco deve", "direito a", "proibido", "ilegal",
    ],
    "prova_documental_facil": [
        "comprovante", "extrato", "print", "captura de tela",
        "boletim", "registro", "e-mail", "sms",
    ],
    "publico_vulneravel": [
        "aposentado", "idoso", "pensionista", "inss",
        "benefício", "servidor", "microempreendedor",
    ],
    "alta_recorrencia": [
        "golpe do pix", "consignado", "conta digital",
        "cartão clonado", "whatsapp clonado", "sim swap",
    ],
}

TEMA_SCORES = {
    "golpe do pix": 95,
    "empréstimo consignado não autorizado": 92,
    "invasão de conta bancária": 88,
    "fraude cartão de crédito": 85,
    "whatsapp clonado golpe": 87,
    "sim swap": 82,
    "fake store compra não recebida": 78,
    "golpe falso suporte bancário": 90,
    "cobrança indevida banco": 75,
    "tarifa abusiva": 70,
}


def score_topic(topic_text: str, metadata: dict = None) -> dict:
    """
    Calcula o score de conversão de um tema.

    Args:
        topic_text: Texto do tema/tendência
        metadata: Dados adicionais (volume, urgência, etc)

    Returns:
        dict com score detalhado e recomendação
    """
    text_lower = topic_text.lower()
    scores = {
        "urgencia_emocional": 0,
        "acao_judicial_clara": 0,
        "prova_documental_facil": 0,
        "publico_vulneravel": 0,
        "alta_recorrencia": 0,
    }

    for category, signals in CONVERSION_SIGNALS.items():
        hits = sum(1 for signal in signals if signal in text_lower)
        scores[category] = min(hits * 15, 25)

    base_score = 0
    for tema_known, score_known in TEMA_SCORES.items():
        if tema_known in text_lower or any(w in text_lower for w in tema_known.split()):
            base_score = max(base_score, score_known)

    if metadata:
        if metadata.get("urgencia") == "ALTA":
            base_score += 10
        if metadata.get("novidade") == "EMERGENTE":
            base_score += 8
        volume = metadata.get("volume_estimado", "médio")
        if volume == "alto":
            base_score += 12
        elif volume == "médio":
            base_score += 6

    signal_score = sum(scores.values())
    total = min(round((base_score * 0.6) + (signal_score * 0.4)), 100)

    return {
        "tema": topic_text,
        "score_total": total,
        "scores_componentes": scores,
        "score_base_tema": base_score,
        "classificacao": _classify(total),
        "recomendacao": _recommend(total),
        "publicar": total >= 65,
    }


def _classify(score: int) -> str:
    if score >= 85:
        return "CONVERSÃO MUITO ALTA"
    elif score >= 70:
        return "CONVERSÃO ALTA"
    elif score >= 55:
        return "CONVERSÃO MEDIA"
    elif score >= 40:
        return "CONVERSÃO BAIXA"
    return "NÃO RECOMENDADO"


def _recommend(score: int) -> str:
    if score >= 85:
        return "Publicar imediatamente. Prioridade máxima. Carrossel + Reels + SEO."
    elif score >= 70:
        return "Alta prioridade. Publicar esta semana. Carrossel + SEO."
    elif score >= 55:
        return "Prioridade média. Agenda nos próximos 14 dias. Blog SEO."
    elif score >= 40:
        return "Baixa prioridade. Manter na fila. Apenas LinkedIn técnico."
    return "Não publicar. Score insuficiente para conversão."


def batch_score(topics: list[dict]) -> list[dict]:
    """Score de múltiplos temas, ordenados por relevância."""
    results = []
    for topic in topics:
        text = topic.get("tema", "") or topic.get("topic", "")
        meta = {k: v for k, v in topic.items() if k != "tema"}
        result = score_topic(text, meta)
        result.update({k: v for k, v in topic.items() if k not in result})
        results.append(result)
    return sorted(results, key=lambda x: x["score_total"], reverse=True)
