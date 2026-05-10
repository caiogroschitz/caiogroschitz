"""Content Strategist Agent — prioriza pautas e define estratégia editorial."""

import json
from datetime import datetime

from .base_agent import BaseAgent


SYSTEM_PROMPT = """Você é o Estrategista de Marketing Jurídico do escritório.
Pensa como um diretor de conteúdo de um perfil jurídico premium com 500 mil seguidores
— e como um advogado que entende de negócio.

Você não produz conteúdo. Você decide O QUE produzir, PARA QUEM, EM QUE FORMATO
e COM QUE OBJETIVO. Cada pauta que você aprova tem um objetivo comercial ético:
educar o consumidor, gerar consultas, construir autoridade.

PRINCÍPIOS DE PRIORIZAÇÃO:
1. Urgência — o tema está acontecendo agora?
2. Volume — muitas pessoas estão passando por isso?
3. Dor — a dor emocional é forte e real?
4. Prova — tem jurisprudência sólida?
5. Ação — leva o leitor a um próximo passo?
6. Formato — o tema se adapta bem a Reels/carrossel/artigo?
7. Saturação — já foi muito coberto?

CRITÉRIOS DE ELIMINAÇÃO (elimine a pauta se):
- Tema muito técnico para o público leigo
- Jurisprudência frágil ou inexistente
- Alto risco ético (promessa implícita de resultado)
- Já foi coberto nos últimos 15 dias
- Baixo potencial de ação do leitor

FORMATO DE SAÍDA: JSON ranqueado + briefing editorial para cada pauta aprovada."""


class ContentStrategistAgent(BaseAgent):

    name = "content-strategist"
    role = "Estrategista de Marketing Jurídico"

    def run(self, context: dict) -> dict:
        self._log("Iniciando estratégia editorial")

        tendencias = context.get("tendencias", {})
        dores = context.get("dores", {})
        jurisprudencia = context.get("jurisprudencia_resumo", "")
        memoria = context.get("memoria", {})

        temas_usados = memoria.get("temas_recentes", []) if memoria else []
        headlines_usadas = memoria.get("headlines_recentes", []) if memoria else []

        user_message = f"""Com base nos dados coletados hoje, defina a estratégia editorial.

TENDÊNCIAS IDENTIFICADAS:
{json.dumps(tendencias, ensure_ascii=False, indent=2)}

DORES DO CONSUMIDOR:
{json.dumps(dores, ensure_ascii=False, indent=2)}

CONTEXTO JURISPRUDENCIAL:
{jurisprudencia[:2000] if jurisprudencia else "Não disponível"}

TEMAS JÁ USADOS (evitar repetição):
{json.dumps(temas_usados, ensure_ascii=False)}

HEADLINES JÁ USADAS:
{json.dumps(headlines_usadas[:20], ensure_ascii=False)}

TAREFA:
1. Selecione as TOP 10 pautas com maior potencial
2. Para cada pauta, defina o briefing completo
3. Calcule o score final (0-100) para cada uma
4. Recomende o formato ideal

Retorne um JSON estruturado:

{{
  "data": "DD/MM/YYYY",
  "total_pautas": 10,
  "pautas": [
    {{
      "rank": 1,
      "tema": "nome do tema",
      "angulo": "ângulo editorial específico (não o tema genérico)",
      "score": 87,
      "scores_detalhados": {{
        "urgencia": 20,
        "conversao": 18,
        "impacto_emocional": 15,
        "viabilidade_juridica": 14,
        "potencial_compartilhamento": 9,
        "potencial_comentarios": 6,
        "potencial_salvamento": 5
      }},
      "formato_ideal": "carrossel|reels|seo_blog|linkedin|todos",
      "formato_secundario": "carrossel",
      "publico_alvo": "aposentados|jovens|empreendedores|geral",
      "tom": "urgente|educativo|emocional|tecnico",
      "headline_sugerida": "headline principal do conteúdo",
      "headline_alternativas": ["alt 1", "alt 2", "alt 3"],
      "hook_sugerido": "frase de abertura para carrossel ou reels",
      "cta_etico": "chamada para ação dentro das normas da OAB",
      "fundamento_juridico": "base legal resumida",
      "nivel_risco_juridico": "BAIXO|MEDIO|ALTO",
      "justificativa_rank": "por que este tema agora?",
      "palavras_chave_seo": ["kw1", "kw2", "kw3"],
      "emocao_gatilho": "medo|raiva|urgencia|esperanca|empatia",
      "objecao_principal": "a maior objeção do leitor",
      "quebra_objecao": "como o conteúdo quebra essa objeção"
    }}
  ],
  "calendario_sugerido": {{
    "segunda": "rank 1",
    "terca": "rank 2",
    "quarta": "rank 3",
    "quinta": "rank 4",
    "sexta": "rank 5",
    "sabado": "rank 6",
    "domingo": "descanso_ou_rank_7"
  }},
  "observacoes_estrategicas": "insights gerais sobre a semana"
}}"""

        self._log("Chamando Claude para estratégia de conteúdo")
        raw_response = self._call_claude(SYSTEM_PROMPT, user_message, max_tokens=8192)

        try:
            start = raw_response.find("{")
            end = raw_response.rfind("}") + 1
            result = json.loads(raw_response[start:end])
        except (json.JSONDecodeError, ValueError):
            result = {"raw": raw_response, "erro": "json_parse_error"}

        output_path = self._save_output("estrategia_editorial", result, "json")
        self._log(f"Estratégia salva em {output_path}")

        return {
            "agent": self.name,
            "status": "success",
            "output_path": str(output_path),
            "data": result,
            "summary": f"Top {result.get('total_pautas', 0)} pautas priorizadas",
        }
