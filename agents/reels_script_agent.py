"""Reels Script Agent — cria roteiros de vídeo curto de alto impacto jurídico."""

import json
from .base_agent import BaseAgent


SYSTEM_PROMPT = """Você é o Roteirista de Conteúdo em Vídeo do escritório.
Especialista em vídeos curtos que geram autoridade, empatia e consultas.

Você pensa em tempo, não em palavras. Cada segundo conta.

ESTRUTURA OBRIGATÓRIA (adaptada por duração):

PARA REELS DE 30 SEGUNDOS:
- 0-3s: Hook visual + frase de abertura (para o scroll)
- 3-12s: O problema (situação da vítima)
- 12-22s: A solução jurídica (o que a lei diz)
- 22-30s: CTA + conclusão

PARA REELS DE 60 SEGUNDOS:
- 0-3s: Hook (frase-bomba)
- 3-8s: Quebra de padrão (surpreende o que o leitor esperava)
- 8-25s: Contexto e dor (apresenta o problema real)
- 25-45s: Conteúdo jurídico + storytelling
- 45-55s: A virada (o direito que eles não sabem)
- 55-60s: CTA

PARA REELS DE 90 SEGUNDOS:
- 0-3s: Hook
- 3-10s: Contexto emocional
- 10-30s: Desenvolvimento do problema (com exemplos reais)
- 30-60s: A lei e a jurisprudência (simplificadas)
- 60-80s: O que fazer (passos práticos)
- 80-90s: CTA + convite

PRINCÍPIOS DO ROTEIRO:

1. HOOK nos primeiros 3 segundos — decisivo
   - Começa com a dor, não com apresentação
   - Nunca: "Olá, tudo bem? Hoje vou falar sobre..."
   - Sim: "Você acabou de ser vítima do golpe do Pix."
   - Sim: "O banco negou o seu reembolso. Isso é ilegal."

2. LINGUAGEM CONVERSACIONAL
   - Fala diretamente com o espectador ("você", "sua conta")
   - Tom de quem entende e quer ajudar, não de quem quer impressionar
   - Frases curtas. Pausa dramática. Continuação.

3. STORYTELLING REAL
   - Use uma situação concreta (sem identificar cliente real)
   - "Uma cliente chegou aqui semana passada..."
   - "Isso aconteceu com uma aposentada de 67 anos..."

4. CREDIBILIDADE SEM JURIDIQUÊS
   - Cita a lei de forma que o leigo entende
   - "O Código de Defesa do Consumidor diz que o banco é RESPONSÁVEL"
   - Não: "Nos termos do art. 14 do CDC c/c art. 927 do CC..."

5. CTA ÉTICO
   - "Me segue para mais informações sobre seus direitos"
   - "Salva esse vídeo se você ou alguém que você conhece passou por isso"
   - "Comenta DIREITO se quiser saber mais sobre o seu caso"
   - NÃO: "Entre em contato para uma consulta" (captação direta proibida)"""


class ReelsScriptAgent(BaseAgent):

    name = "reels-script"
    role = "Roteirista de Vídeo Jurídico"

    def run(self, context: dict) -> dict:
        self._log("Iniciando produção de roteiros")

        pautas = context.get("pautas_aprovadas", [])
        dores = context.get("dores", {})

        if not pautas:
            pautas = [{
                "tema": "empréstimo consignado não autorizado",
                "angulo": "Como descobrir e cancelar um empréstimo que não fez",
                "hook_sugerido": "Descubriram um empréstimo em seu nome que você não autorizou.",
                "emocao_gatilho": "raiva",
            }]

        roteiros = []

        for pauta in pautas[:2]:
            tema = pauta.get("tema", "")
            angulo = pauta.get("angulo", "")
            hook = pauta.get("hook_sugerido", "")
            emocao = pauta.get("emocao_gatilho", "")
            dor_tema = dores.get("mapa_dores", {}).get(tema, {})
            vocabulario = dor_tema.get("vocabulario_chave", [])

            user_message = f"""Crie um roteiro de Reels jurídico de 60 segundos sobre:

TEMA: {tema}
ÂNGULO: {angulo}
HOOK SUGERIDO: {hook}
EMOÇÃO GATILHO: {emocao}
VOCABULÁRIO DA VÍTIMA: {json.dumps(vocabulario, ensure_ascii=False)}

FORMATO DO ROTEIRO:

**TÍTULO DO VÍDEO:** (interno, não aparece no vídeo)
**DURAÇÃO ALVO:** 60 segundos
**TOM:** [urgente/empático/revelador/informativo]

---
**ROTEIRO COMPLETO**

[0-3s | HOOK]
*[direção de cena: enquadramento, postura]*
FALA: "..."

[3-8s | QUEBRA DE PADRÃO]
*[direção de cena]*
FALA: "..."

[8-25s | CONTEXTO E DOR]
*[direção de cena]*
FALA: "..."

[25-45s | LEI E JURISPRUDÊNCIA]
*[direção de cena]*
FALA: "..."

[45-55s | A VIRADA — direito que eles não sabiam]
*[direção de cena]*
FALA: "..."

[55-60s | CTA]
*[direção de cena]*
FALA: "..."
---

**LEGENDA SUGERIDA:** (para o post)
**PRIMEIRA FRASE DA LEGENDA:** (crítica para o algoritmo)
**HASHTAGS:** (8-10 relevantes)
**ELEMENTOS VISUAIS SUGERIDOS:** (o que mostrar na tela)

**ANÁLISE DE PERFORMANCE:**
- Por que o hook vai funcionar: ...
- Momento de maior retenção esperado: ...
- Gatilho de compartilhamento: ...

Escreva o roteiro como se fosse para um advogado falar em frente à câmera.
Tom natural, direto, humano. Sem teleprompter aparente."""

            self._log(f"Gerando roteiro: {tema}")
            resultado = self._call_claude(SYSTEM_PROMPT, user_message, max_tokens=4096)

            roteiros.append({"tema": tema, "angulo": angulo, "roteiro": resultado})

            output_name = tema.lower().replace(" ", "_")[:40]
            self._save_output(f"reels_{output_name}", resultado, "md")

        output_path = self._save_output("roteiros_todos", roteiros, "json")

        return {
            "agent": self.name,
            "status": "success",
            "output_path": str(output_path),
            "data": {"roteiros": roteiros},
            "summary": f"{len(roteiros)} roteiros de Reels gerados",
        }
