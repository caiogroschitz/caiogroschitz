"""Scoring Engine — motor de ranking de pautas editoriais jurídicas."""

import json
from datetime import datetime
from pathlib import Path
from typing import Optional


DIMENSOES = {
    "urgencia": {
        "peso": 0.20,
        "descricao": "Quão urgente é o tema? Está acontecendo agora?",
        "escala": {"muito_alta": 100, "alta": 80, "media": 60, "baixa": 40, "muito_baixa": 20},
    },
    "conversao": {
        "peso": 0.20,
        "descricao": "Probabilidade de gerar consulta ou ação do leitor",
        "escala": {"muito_alta": 100, "alta": 80, "media": 60, "baixa": 40, "muito_baixa": 20},
    },
    "impacto_emocional": {
        "peso": 0.15,
        "descricao": "Força da dor emocional associada ao tema",
        "escala": {"muito_alto": 100, "alto": 80, "medio": 60, "baixo": 40, "muito_baixo": 20},
    },
    "viabilidade_juridica": {
        "peso": 0.15,
        "descricao": "Solidez da tese jurídica disponível",
        "escala": {"muito_alta": 100, "alta": 80, "media": 60, "baixa": 40, "muito_baixa": 20},
    },
    "potencial_compartilhamento": {
        "peso": 0.10,
        "descricao": "Chance de ser compartilhado por quem não foi vítima",
        "escala": {"muito_alto": 100, "alto": 80, "medio": 60, "baixo": 40, "muito_baixo": 20},
    },
    "potencial_comentarios": {
        "peso": 0.08,
        "descricao": "Tendência a gerar comentários e discussão",
        "escala": {"muito_alto": 100, "alto": 80, "medio": 60, "baixo": 40, "muito_baixo": 20},
    },
    "potencial_salvamento": {
        "peso": 0.07,
        "descricao": "Chance de ser salvo para consulta futura",
        "escala": {"muito_alto": 100, "alto": 80, "medio": 60, "baixo": 40, "muito_baixo": 20},
    },
    "risco_juridico": {
        "peso": 0.05,
        "descricao": "Risco ético e jurídico (penalidade — score alto = risco alto = penalidade)",
        "escala": {"muito_alto": 100, "alto": 75, "medio": 50, "baixo": 25, "muito_baixo": 0},
        "penalidade": True,
    },
}

PENALIDADES_CONTEXTUAIS = {
    "tema_repetido_7d": -25,
    "tema_repetido_30d": -15,
    "headline_similar": -10,
    "saturacao_social": -8,
    "risco_etico_alto": -40,
    "jurisprudencia_fragil": -20,
    "publico_muito_nicho": -5,
}

BONUS_CONTEXTUAIS = {
    "novidade_emergente": +15,
    "decisao_recente_stj": +20,
    "alta_reclamacao_reclame_aqui": +12,
    "viralidade_atual": +18,
    "periodo_safra_fraude": +10,
}


class ScoringEngine:
    """Motor de scoring e ranking de pautas editoriais."""

    def __init__(self, config: dict = None):
        self.config = config or {}
        custom_pesos = self.config.get("scoring", {}).get("pesos", {})
        if custom_pesos:
            for dim, peso in custom_pesos.items():
                if dim in DIMENSOES:
                    DIMENSOES[dim]["peso"] = peso

    def score_pauta(
        self,
        tema: str,
        angulo: str = "",
        scores_input: dict = None,
        penalidades: list = None,
        bonus: list = None,
    ) -> dict:
        """
        Calcula o score completo de uma pauta.

        Args:
            tema: Nome do tema
            angulo: Ângulo editorial específico
            scores_input: Dict com valores por dimensão (0-100 ou nivel string)
            penalidades: Lista de penalidades a aplicar (chaves de PENALIDADES_CONTEXTUAIS)
            bonus: Lista de bônus a aplicar (chaves de BONUS_CONTEXTUAIS)

        Returns:
            dict com score completo e classificação
        """
        if scores_input is None:
            scores_input = {}

        scores_normalizados = {}
        for dim, config in DIMENSOES.items():
            raw = scores_input.get(dim, 60)
            if isinstance(raw, str):
                raw = config["escala"].get(raw, 60)
            scores_normalizados[dim] = int(raw)

        score_ponderado = 0.0
        for dim, config in DIMENSOES.items():
            valor = scores_normalizados[dim]
            peso = config["peso"]
            if config.get("penalidade"):
                score_ponderado -= valor * peso
            else:
                score_ponderado += valor * peso

        pen_total = 0
        pen_aplicadas = []
        if penalidades:
            for pen in penalidades:
                valor_pen = PENALIDADES_CONTEXTUAIS.get(pen, 0)
                pen_total += valor_pen
                pen_aplicadas.append({"nome": pen, "valor": valor_pen})

        bonus_total = 0
        bonus_aplicados = []
        if bonus:
            for bon in bonus:
                valor_bon = BONUS_CONTEXTUAIS.get(bon, 0)
                bonus_total += valor_bon
                bonus_aplicados.append({"nome": bon, "valor": valor_bon})

        score_final = max(0, min(100, round(score_ponderado + pen_total + bonus_total)))

        return {
            "tema": tema,
            "angulo": angulo,
            "score_final": score_final,
            "score_ponderado_base": round(score_ponderado),
            "scores_componentes": scores_normalizados,
            "penalidades_aplicadas": pen_aplicadas,
            "bonus_aplicados": bonus_aplicados,
            "penalidade_total": pen_total,
            "bonus_total": bonus_total,
            "classificacao": self._classify(score_final),
            "prioridade": self._priority(score_final),
            "publicar": score_final >= 65,
            "formato_recomendado": self._recommend_format(scores_normalizados),
            "calculado_em": datetime.now().isoformat(),
        }

    def rank_pautas(self, pautas: list[dict]) -> list[dict]:
        """Ranqueia múltiplas pautas e retorna ordenadas por score."""
        ranked = []
        for i, pauta in enumerate(pautas):
            if "score_final" not in pauta:
                score_data = self.score_pauta(
                    tema=pauta.get("tema", f"Pauta {i+1}"),
                    angulo=pauta.get("angulo", ""),
                    scores_input=pauta.get("scores_detalhados", {}),
                    penalidades=pauta.get("penalidades", []),
                    bonus=pauta.get("bonus", []),
                )
                pauta = {**pauta, **score_data}
            ranked.append(pauta)

        ranked.sort(key=lambda x: x.get("score_final", 0), reverse=True)
        for i, pauta in enumerate(ranked):
            pauta["rank"] = i + 1

        return ranked

    def generate_report(self, pautas_ranked: list[dict]) -> str:
        """Gera relatório de ranking em Markdown."""
        lines = [
            "# Ranking de Pautas Editorial",
            f"**Gerado em:** {datetime.now().strftime('%d/%m/%Y %H:%M')}",
            f"**Total de pautas avaliadas:** {len(pautas_ranked)}",
            "",
            "| Rank | Tema | Score | Classificação | Publicar | Formato |",
            "|------|------|-------|---------------|----------|---------|",
        ]

        for p in pautas_ranked:
            publicar = "✅ Sim" if p.get("publicar") else "❌ Não"
            lines.append(
                f"| {p.get('rank', '-')} "
                f"| {p.get('tema', '')[:40]} "
                f"| {p.get('score_final', 0)} "
                f"| {p.get('classificacao', '')} "
                f"| {publicar} "
                f"| {p.get('formato_recomendado', '')} |"
            )

        lines.append("")
        lines.append("## Detalhamento Top 5")
        for p in pautas_ranked[:5]:
            lines.extend([
                f"### #{p.get('rank')} — {p.get('tema')} (Score: {p.get('score_final')})",
                f"**Ângulo:** {p.get('angulo', 'N/A')}",
                f"**Classificação:** {p.get('classificacao')}",
                f"**Formato recomendado:** {p.get('formato_recomendado')}",
                "",
                "**Scores por dimensão:**",
            ])
            for dim, score in p.get("scores_componentes", {}).items():
                lines.append(f"- {dim}: {score}/100")
            if p.get("penalidades_aplicadas"):
                lines.append(f"**Penalidades:** {p['penalidades_aplicadas']}")
            if p.get("bonus_aplicados"):
                lines.append(f"**Bônus:** {p['bonus_aplicados']}")
            lines.append("")

        return "\n".join(lines)

    def save_report(self, pautas_ranked: list[dict], output_dir: str = "ranking") -> Path:
        """Salva o relatório de ranking."""
        path = Path(output_dir)
        path.mkdir(exist_ok=True)
        date_str = datetime.now().strftime("%Y-%m-%d")

        md_path = path / f"{date_str}_ranking.md"
        md_path.write_text(self.generate_report(pautas_ranked), encoding="utf-8")

        json_path = path / f"{date_str}_ranking.json"
        json_path.write_text(
            json.dumps({"data": date_str, "pautas": pautas_ranked}, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

        return md_path

    def _classify(self, score: int) -> str:
        if score >= 85:
            return "PRIORIDADE MÁXIMA"
        elif score >= 70:
            return "ALTA PRIORIDADE"
        elif score >= 55:
            return "PRIORIDADE MÉDIA"
        elif score >= 40:
            return "BAIXA PRIORIDADE"
        return "DESCARTAR"

    def _priority(self, score: int) -> str:
        if score >= 85:
            return "P1"
        elif score >= 70:
            return "P2"
        elif score >= 55:
            return "P3"
        return "P4"

    def _recommend_format(self, scores: dict) -> str:
        emocional = scores.get("impacto_emocional", 0)
        compartilhamento = scores.get("potencial_compartilhamento", 0)
        salvamento = scores.get("potencial_salvamento", 0)
        juridico = scores.get("viabilidade_juridica", 0)

        if emocional >= 80 and compartilhamento >= 70:
            return "reels"
        elif salvamento >= 80 or juridico >= 80:
            return "carrossel"
        elif juridico >= 75:
            return "seo_blog + carrossel"
        return "carrossel"
