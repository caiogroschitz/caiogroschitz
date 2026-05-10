"""Jurisprudência Agent — pesquisa e classifica decisões jurídicas relevantes."""

import json
from datetime import datetime
from pathlib import Path

from .base_agent import BaseAgent


SYSTEM_PROMPT = """Você é o Curador de Jurisprudência do escritório. Formação em direito
com especialização em direito do consumidor bancário. Pensa como um advogado que
precisa encontrar a decisão certa para ganhar uma causa.

Sua missão é encontrar, resumir e classificar jurisprudência REAL sobre golpes digitais
e responsabilidade bancária — com foco em teses que fundamentam ações de consumidores.

TRIBUNAIS POR PRIORIDADE:
1. STJ (jurisprudência nacional, efeito multiplicador)
2. TJSP (maior volume, estado mais rico, precedente)
3. TJRJ (alta litigiosidade bancária)
4. TJMG (pesos em responsabilidade do consumidor)
5. TJRS (histórico consumerista progressivo)

TEMAS DE BUSCA PRIORITÁRIOS:
- Responsabilidade objetiva do banco por fraude eletrônica
- Golpe do Pix: falha no dever de segurança
- Empréstimo consignado não autorizado: dano moral in re ipsa
- SIM swap e invasão de conta: banco responsável
- Engenharia social: culpa exclusiva do consumidor ou não?
- Cancelamento de transação Pix: prazo e obrigação do banco
- Indenização por fraude em conta digital
- CDC art. 14 e instituições financeiras: aplicabilidade
- LGPD e vazamento de dados bancários

REGRA CRÍTICA: NUNCA invente jurisprudência. Se não souber um processo real,
diga explicitamente que é uma tese jurídica sem citação de processo específico.
Marque claramente como "TESE SEM PROCESSO CITADO" quando aplicável.

FORMATO: Markdown jurídico estruturado, linguagem técnica mas acessível."""


class JurisprudenciaAgent(BaseAgent):

    name = "jurisprudencia"
    role = "Curador de Jurisprudência"

    def run(self, context: dict) -> dict:
        self._log("Iniciando pesquisa de jurisprudência")

        tendencias = context.get("tendencias", [])
        temas_prioritarios = [t.get("tema", "") for t in tendencias[:5]] if tendencias else [
            "golpe do Pix",
            "empréstimo consignado não autorizado",
            "invasão de conta bancária digital",
            "responsabilidade banco fraude eletrônica",
        ]

        user_message = f"""Pesquise jurisprudência relevante sobre os seguintes temas:

TEMAS PRIORITÁRIOS (baseados nas tendências identificadas hoje):
{json.dumps(temas_prioritarios, ensure_ascii=False, indent=2)}

Para cada tema, forneça:

1. TESE JURÍDICA DOMINANTE
   - Qual é o entendimento majoritário nos tribunais?
   - Quais são os fundamentos legais (CDC, CC, lei específica)?

2. DECISÕES FAVORÁVEIS AO CONSUMIDOR
   - Cite decisões reais quando souber (tribunal, número aproximado se disponível)
   - Identifique o relator quando relevante
   - Marque "TESE SEM PROCESSO ESPECÍFICO" quando não tiver citação real

3. DECISÕES DESFAVORÁVEIS (análise de risco)
   - Quando o consumidor perde? (culpa exclusiva, negligência grave)
   - Tese da culpa exclusiva de terceiro: quando funciona para o banco?

4. DIVERGÊNCIA JURISPRUDENCIAL
   - Há divisão entre tribunais?
   - STJ já pacificou?

5. TENDÊNCIA RECENTE (2023-2025)
   - Está ficando mais favorável ou desfavorável ao consumidor?
   - Há súmula ou tese fixada?

6. VALOR MÉDIO DE INDENIZAÇÃO (quando aplicável)
   - Dano moral: faixa em cada tribunal
   - Dano material: critério de cálculo

7. APLICAÇÃO PRÁTICA
   - O que preciso provar?
   - Quais documentos são essenciais?
   - Prazo prescricional aplicável

Formato obrigatório para cada decisão citada:
**[TRIBUNAL] — [Tipo da decisão] — [Ano aproximado]**
*Tese: [resumo da tese em uma frase]*
*Fundamento: [base legal]*
*Favorabilidade: FAVORÁVEL/DESFAVORÁVEL/NEUTRA ao consumidor*
*Nota de verificação: REAL (citar processo) | TESE SEM PROCESSO ESPECÍFICO*

Ao final, gere um RANKING DE TESES por solidez jurídica (1 = mais sólida)."""

        self._log("Chamando Claude para pesquisa de jurisprudência")
        resultado_md = self._call_claude(SYSTEM_PROMPT, user_message, max_tokens=8192)

        output_path = self._save_output("jurisprudencia", resultado_md, "md")

        juris_dir = Path("jurisprudencia")
        juris_dir.mkdir(exist_ok=True)
        index_path = juris_dir / "index.json"

        index = {}
        if index_path.exists():
            try:
                index = json.loads(index_path.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                index = {}

        data_hoje = datetime.now().strftime("%Y-%m-%d")
        index[data_hoje] = {
            "temas": temas_prioritarios,
            "arquivo": str(output_path),
            "timestamp": datetime.now().isoformat(),
        }
        index_path.write_text(json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8")

        self._log(f"Jurisprudência salva em {output_path}")

        return {
            "agent": self.name,
            "status": "success",
            "output_path": str(output_path),
            "data": {"conteudo_md": resultado_md, "temas_pesquisados": temas_prioritarios},
            "summary": f"Jurisprudência pesquisada para {len(temas_prioritarios)} temas",
        }
