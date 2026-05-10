"""Trend Hunter Agent — detecta tendências emergentes de golpes digitais no Brasil."""

import json
from datetime import datetime, timedelta
from pathlib import Path

from .base_agent import BaseAgent


SYSTEM_PROMPT = """Você é o Pesquisador de Tendências do escritório. Sua função é identificar
quais golpes digitais, fraudes bancárias e temas de direito do consumidor bancário
estão em crescimento no Brasil agora.

Você pensa como um jornalista investigativo com formação jurídica: conecta sinais fracos,
identifica padrões antes de viralizarem e alerta a equipe com antecedência.

Sua análise deve ser baseada em dados reais e lógica dedutiva — nunca inventada.
Quando não tiver dados confirmados, diga claramente que é uma projeção com base
em padrões históricos.

TEMAS CENTRAIS DE MONITORAMENTO:
- Golpe do Pix em todas as variantes (falso atendente, portabilidade, QR Code)
- Fraude no consignado (INSS, servidores públicos, aposentados)
- Empréstimos não solicitados (fintechs, Nubank, PicPay, Mercado Pago)
- Account takeover (invasão de conta via SIM swap, phishing, engenharia social)
- Fake stores e marketplace (ML, Shopee, Amazon)
- Golpe da portabilidade de número (WhatsApp clonado)
- Fraude em seguros digitais
- Golpe do falso suporte técnico bancário
- Fraude em investimentos digitais (pirâmides, falsos robôs)
- Golpe da falsa central de segurança bancária

FORMATO DE SAÍDA:
Retorne um JSON estruturado com tendências ordenadas por score decrescente.
Cada tendência deve ter: tema, descricao, score, urgencia, volume_estimado,
novidade, fundamento_juridico, potencial_conteudo."""


class TrendHunterAgent(BaseAgent):

    name = "trend-hunter"
    role = "Pesquisador de Tendências Jurídicas"

    def run(self, context: dict) -> dict:
        self._log("Iniciando varredura de tendências")

        prompt_base = self._load_prompt("trend_hunter_prompt")
        contexto_juridico = self._load_context("digital_scams")

        data_hoje = datetime.now().strftime("%d/%m/%Y")
        data_limite = (datetime.now() - timedelta(days=30)).strftime("%d/%m/%Y")

        user_message = f"""Analise as tendências emergentes de golpes digitais e fraudes bancárias
no Brasil para o período de {data_limite} a {data_hoje}.

Contexto jurídico atual:
{contexto_juridico}

Contexto adicional do sistema:
{json.dumps(context, ensure_ascii=False, indent=2)}

Com base no seu conhecimento sobre:
1. Padrões sazonais de fraude bancária no Brasil
2. Evolução recente do golpe do Pix e suas variantes
3. Crescimento de reclamações no Reclame Aqui e Consumidor.gov
4. Decisões recentes do BACEN e STJ sobre responsabilidade bancária
5. Tendências internacionais de fraude digital adaptadas ao Brasil

Identifique as TOP 10 tendências mais relevantes agora.

Para cada tendência, calcule um score de 0 a 100 considerando:
- Volume de reclamações estimado (0-25 pts)
- Urgência (novidade, crescimento recente) (0-25 pts)
- Potencial jurídico (há tese sólida?) (0-25 pts)
- Potencial de conteúdo (gera engajamento?) (0-25 pts)

Retorne SOMENTE o JSON no formato especificado, sem explicações adicionais.

Formato:
{{
  "data_analise": "DD/MM/YYYY",
  "total_tendencias": 10,
  "tendencias": [
    {{
      "id": 1,
      "tema": "nome curto do tema",
      "descricao": "descrição detalhada em 2-3 frases",
      "score_total": 85,
      "scores": {{
        "volume": 22,
        "urgencia": 23,
        "potencial_juridico": 20,
        "potencial_conteudo": 20
      }},
      "urgencia": "ALTA|MEDIA|BAIXA",
      "novidade": "EMERGENTE|CRESCENTE|CONSOLIDADO",
      "publico_afetado": ["aposentados", "jovens", "empreendedores"],
      "fundamento_juridico": "CDC art. 14, Lei 12.865/13...",
      "tese_juridica": "responsabilidade objetiva da instituição financeira por...",
      "potencial_conteudo": ["carrossel", "reels", "artigo_seo"],
      "palavras_chave": ["golpe pix 2025", "fraude bancária indenização"],
      "emocao_primaria": "medo|raiva|urgencia|esperança",
      "ponto_de_dor": "descrição da dor real do consumidor",
      "hook_sugerido": "frase de abertura poderosa para este tema"
    }}
  ]
}}"""

        self._log("Chamando Claude para análise de tendências")
        raw_response = self._call_claude(SYSTEM_PROMPT, user_message, max_tokens=8192)

        try:
            start = raw_response.find("{")
            end = raw_response.rfind("}") + 1
            json_str = raw_response[start:end]
            result = json.loads(json_str)
        except (json.JSONDecodeError, ValueError):
            self._log("Erro ao parsear JSON, retornando raw", "WARNING")
            result = {"raw": raw_response, "erro": "json_parse_error"}

        output_path = self._save_output("tendencias", result, "json")
        self._log(f"Tendências salvas em {output_path}")

        trends_dir = Path("trends")
        trends_dir.mkdir(exist_ok=True)
        cache_path = trends_dir / f"{datetime.now().strftime('%Y-%m-%d')}_trends.json"
        cache_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")

        return {
            "agent": self.name,
            "status": "success",
            "output_path": str(output_path),
            "data": result,
            "summary": f"Identificadas {result.get('total_tendencias', 0)} tendências",
        }
