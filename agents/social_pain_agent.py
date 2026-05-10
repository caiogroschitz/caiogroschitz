"""Social Pain Agent — mapeia dores reais do consumidor vítima de golpes."""

import json
from datetime import datetime

from .base_agent import BaseAgent


SYSTEM_PROMPT = """Você é o Analista de Dores do Consumidor. Pensa como um psicólogo
que entende de direito — e como um copywriter que entende de trauma.

Sua missão é identificar e documentar as dores REAIS, EMOCIONAIS e PRÁTICAS das pessoas
que foram vítimas de golpes digitais e fraudes bancárias.

Você NÃO escreve conteúdo jurídico técnico. Você escreve a linguagem da vítima.
A vergonha de ter "caído". O medo de não conseguir recuperar. A raiva do banco
que não quis ajudar. A sensação de impotência diante do sistema.

Essas emoções são o combustível do conteúdo. Sem elas, o conteúdo não conecta.

FONTES QUE VOCÊ SIMULA ANALISAR:
- Reclame Aqui (reclamações abertas sobre bancos e fintechs)
- Consumidor.gov.br (registros oficiais de disputas)
- Grupos no WhatsApp e Telegram de vítimas de golpes
- Comentários em vídeos do YouTube sobre fraudes bancárias
- Reddit r/brasil e r/financaspessoais
- Fóruns de aposentados sobre fraude no INSS
- Comentários públicos em posts de advogados no Instagram

CATEGORIAS DE DOR:
1. Dor emocional (vergonha, raiva, desamparo)
2. Dor prática (perdeu dinheiro, não sabe o que fazer)
3. Dor sistêmica (banco não ajuda, PROCON não resolve, delegacia não sabe)
4. Dor temporal (meses esperando solução)
5. Dor relacional (família que cobrou, cônjuge que ficou sabendo)

REGRA: Use linguagem popular. Não escreva como advogado. Escreva como a vítima fala."""


class SocialPainAgent(BaseAgent):

    name = "social-pain"
    role = "Analista de Dores do Consumidor"

    def run(self, context: dict) -> dict:
        self._log("Iniciando mapeamento de dores sociais")

        tendencias = context.get("tendencias", [])
        temas = [t.get("tema", "") for t in tendencias[:5]] if tendencias else [
            "golpe do Pix",
            "empréstimo consignado não autorizado",
            "invasão de conta",
        ]

        user_message = f"""Mapeie as dores reais dos consumidores brasileiros vítimas dos seguintes golpes:

TEMAS:
{json.dumps(temas, ensure_ascii=False, indent=2)}

Para cada tema, entregue:

## MAPA DE DORES: [TEMA]

### 1. A DOR PRINCIPAL
*Como a vítima descreve o momento em que percebeu o golpe?*
- Frase típica que a vítima usa (na linguagem dela, não do advogado)
- O que ela sente primeiro: raiva, vergonha, desespero, negação?
- O que ela faz nas primeiras horas?

### 2. OBJEÇÕES E MEDOS (antes de buscar ajuda)
- "Fui eu que errei, não tem como reclamar"
- "O banco vai dizer que foi culpa minha"
- "Isso leva anos na Justiça"
- [Outras objeções específicas deste golpe]

### 3. LINGUAGEM DA VÍTIMA
*Frases reais que aparecem em reclamações e comentários:*
- [5-8 frases no vocabulário do consumidor leigo]

### 4. PERGUNTAS MAIS COMUNS
*O que ela quer saber antes de qualquer coisa:*
- [5-7 perguntas reais que fazem nas primeiras buscas no Google]

### 5. COMPORTAMENTO EMOCIONAL
- Estágio 1 (descoberta): como reage
- Estágio 2 (negação): o que tenta fazer sozinha
- Estágio 3 (busca): quando começa a procurar ajuda
- Estágio 4 (decisão): o que a faz tomar ação

### 6. VERGONHA E SILÊNCIO
- Por que muitas vítimas não reclamam?
- O que as faz ficar em silêncio?
- Como quebrar essa barreira no conteúdo?

### 7. GATILHOS DE AÇÃO
*O que faz uma vítima decidir tomar uma atitude?*
- [3-5 gatilhos específicos deste golpe]

### 8. VOCABULÁRIO PARA CONTEÚDO
*Palavras e expressões que ressoam com essa vítima:*
- [10-15 palavras/expressões da linguagem dela]

Ao final, gere um JSON com as principais dores indexadas por tema para uso nos outros agentes.

```json
{{
  "mapa_dores": {{
    "[tema]": {{
      "dor_principal": "...",
      "emocao_primaria": "vergonha|raiva|medo|desespero",
      "objecoes": ["...", "..."],
      "perguntas_frequentes": ["...", "..."],
      "gatilhos_acao": ["...", "..."],
      "vocabulario_chave": ["...", "..."],
      "hook_emocional": "frase de abertura que conecta com essa dor"
    }}
  }}
}}
```"""

        self._log("Chamando Claude para mapeamento de dores")
        resultado = self._call_claude(SYSTEM_PROMPT, user_message, max_tokens=8192)

        json_data = {}
        try:
            start = resultado.find("```json")
            end = resultado.find("```", start + 7)
            if start != -1 and end != -1:
                json_str = resultado[start + 7:end].strip()
                json_data = json.loads(json_str)
        except (json.JSONDecodeError, ValueError):
            pass

        output_path_md = self._save_output("dores_consumidor", resultado, "md")
        if json_data:
            self._save_output("dores_consumidor_index", json_data, "json")

        self._log(f"Mapa de dores salvo em {output_path_md}")

        return {
            "agent": self.name,
            "status": "success",
            "output_path": str(output_path_md),
            "data": {"conteudo_md": resultado, "json_index": json_data},
            "summary": f"Dores mapeadas para {len(temas)} temas",
        }
