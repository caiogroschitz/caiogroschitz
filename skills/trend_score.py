"""Skill: Calcula score multidimensional de tendências jurídicas."""

from datetime import datetime
from typing import Optional


WEIGHTS = {
    "volume": 0.25,
    "urgencia": 0.25,
    "recorrencia": 0.15,
    "novidade": 0.15,
    "potencial_comercial": 0.10,
    "potencial_juridico": 0.10,
}

VOLUME_SCORES = {
    "muito_alto": 100,
    "alto": 80,
    "medio": 60,
    "baixo": 40,
    "muito_baixo": 20,
}

URGENCIA_SCORES = {
    "ALTA": 100,
    "MEDIA": 65,
    "BAIXA": 35,
}

NOVIDADE_SCORES = {
    "EMERGENTE": 100,
    "CRESCENTE": 75,
    "CONSOLIDADO": 50,
    "SATURADO": 20,
}


def calculate(
    tema: str,
    volume: str = "medio",
    urgencia: str = "MEDIA",
    recorrencia: float = 0.5,
    novidade: str = "CRESCENTE",
    potencial_comercial: float = 0.5,
    potencial_juridico: float = 0.5,
    penalidades: Optional[dict] = None,
) -> dict:
    """
    Calcula o score de tendência multidimensional.

    Args:
        tema: Nome do tema
        volume: "muito_alto" | "alto" | "medio" | "baixo" | "muito_baixo"
        urgencia: "ALTA" | "MEDIA" | "BAIXA"
        recorrencia: 0.0 a 1.0
        novidade: "EMERGENTE" | "CRESCENTE" | "CONSOLIDADO" | "SATURADO"
        potencial_comercial: 0.0 a 1.0 (likelihood de gerar consultas)
        potencial_juridico: 0.0 a 1.0 (solidez da tese jurídica)
        penalidades: dict com penalidades aplicáveis

    Returns:
        dict com score detalhado
    """
    raw_scores = {
        "volume": VOLUME_SCORES.get(volume, 60),
        "urgencia": URGENCIA_SCORES.get(urgencia, 65),
        "recorrencia": round(recorrencia * 100),
        "novidade": NOVIDADE_SCORES.get(novidade, 75),
        "potencial_comercial": round(potencial_comercial * 100),
        "potencial_juridico": round(potencial_juridico * 100),
    }

    weighted_score = sum(
        raw_scores[dim] * weight
        for dim, weight in WEIGHTS.items()
    )

    penalidade_total = 0
    penalidades_aplicadas = []
    if penalidades:
        for pen_name, pen_value in penalidades.items():
            penalidade_total += abs(pen_value)
            penalidades_aplicadas.append({"nome": pen_name, "valor": -abs(pen_value)})

    final_score = max(0, min(100, round(weighted_score - penalidade_total)))

    return {
        "tema": tema,
        "score_final": final_score,
        "score_ponderado": round(weighted_score),
        "classificacao": _classify(final_score),
        "scores_componentes": raw_scores,
        "pesos": WEIGHTS,
        "penalidades": penalidades_aplicadas,
        "penalidade_total": penalidade_total,
        "publicar": final_score >= 65,
        "prioridade": _priority(final_score),
        "calculado_em": datetime.now().isoformat(),
    }


def batch_calculate(trends: list[dict]) -> list[dict]:
    """Calcula score para lista de tendências e ordena."""
    results = []
    for trend in trends:
        score_data = calculate(
            tema=trend.get("tema", ""),
            volume=trend.get("volume", "medio"),
            urgencia=trend.get("urgencia", "MEDIA"),
            recorrencia=trend.get("recorrencia", 0.5),
            novidade=trend.get("novidade", "CRESCENTE"),
            potencial_comercial=trend.get("potencial_comercial", 0.5),
            potencial_juridico=trend.get("potencial_juridico", 0.5),
        )
        merged = {**trend, **score_data}
        results.append(merged)

    return sorted(results, key=lambda x: x["score_final"], reverse=True)


def _classify(score: int) -> str:
    if score >= 85:
        return "TENDÊNCIA CRÍTICA — publicar imediatamente"
    elif score >= 70:
        return "TENDÊNCIA FORTE — prioridade esta semana"
    elif score >= 55:
        return "TENDÊNCIA RELEVANTE — agenda nos próximos 14 dias"
    elif score >= 40:
        return "TENDÊNCIA FRACA — monitorar"
    return "IRRELEVANTE — descartar"


def _priority(score: int) -> str:
    if score >= 85:
        return "P1"
    elif score >= 70:
        return "P2"
    elif score >= 55:
        return "P3"
    return "P4"
