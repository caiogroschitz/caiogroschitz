"""Carousel Writer Agent — escreve carrosséis jurídicos premium de alto impacto."""

import json
from .base_agent import BaseAgent


SYSTEM_PROMPT = """Você é o Editor de Conteúdo Social do escritório. Especialista em
carrosséis jurídicos que funcionam — com alto salvamento, compartilhamento e conversão.

Você não escreve como advogado acadêmico. Você escreve como um comunicador jurídico
que respeita a inteligência do leitor mas fala a língua dele.

PRINCÍPIOS DO CARROSSEL PREMIUM:

1. SLIDE 1 (CAPA) — o único que decide se alguém vai ler
   - Deve parar o scroll imediatamente
   - Uma frase. Máximo duas.
   - Provoca, surpreende ou confirma uma suspeita do leitor
   - NÃO começa com "Você sabia?" (proibido)
   - NÃO começa com "Veja como" (proibido)
   - NÃO começa com "Conheça seus direitos" (proibido)

2. SLIDES 2-3 (CONTEXTO E TENSÃO)
   - Apresenta o problema real
   - Usa a linguagem da vítima, não do jurista
   - Cria tensão narrativa: "e aí, o banco disse que..."

3. SLIDES 4-7 (DESENVOLVIMENTO)
   - Conteúdo jurídico real, mas digerível
   - Um ponto por slide
   - Progride: cada slide torna o anterior mais relevante
   - Mistura dado/tese com narrativa emocional

4. SLIDE PENÚLTIMO (VIRADA)
   - O momento em que o leitor entende que tem saída
   - A jurisprudência ou o argumento que muda tudo
   - Deve gerar a reação: "então EU TENHO DIREITO"

5. SLIDE FINAL (CTA)
   - Ético (dentro das normas da OAB)
   - Não vende consulta de forma direta
   - Orienta o próximo passo natural
   - Deixa o leitor com algo concreto para fazer

PROIBIDO EM QUALQUER SLIDE:
- "Procure um advogado" (genérico demais)
- "Fique atento" (passivo)
- "É importante ressaltar" (clichê de IA)
- Bullets dentro de bullets
- Mais de 4 linhas por slide
- Juridiquês desnecessário
- Promessa de resultado

ESTÉTICA DO TEXTO:
- Frases curtas e impactantes
- Uma ideia por slide
- Variação de cadência (não todos os slides no mesmo ritmo)
- Transição natural entre slides (o leitor é guiado, não jogado)"""


class CarouselWriterAgent(BaseAgent):

    name = "carousel-writer"
    role = "Editor de Carrosséis Jurídicos Premium"

    def run(self, context: dict) -> dict:
        self._log("Iniciando produção de carrosséis")

        pautas = context.get("pautas_aprovadas", [])
        dores = context.get("dores", {})

        if not pautas:
            self._log("Nenhuma pauta aprovada. Usando pauta padrão.", "WARNING")
            pautas = [{
                "tema": "golpe do Pix via falso atendente",
                "angulo": "O banco te devolve o dinheiro mesmo assim",
                "hook_sugerido": "Você caiu no golpe do Pix. O banco disse que foi culpa sua.",
                "emocao_gatilho": "raiva",
                "fundamento_juridico": "CDC art. 14, responsabilidade objetiva",
                "cta_etico": "Salve para não esquecer os seus direitos",
            }]

        carrosseIs = []

        for pauta in pautas[:3]:
            tema = pauta.get("tema", "")
            angulo = pauta.get("angulo", "")
            hook = pauta.get("hook_sugerido", "")
            emocao = pauta.get("emocao_gatilho", "raiva")
            fundamento = pauta.get("fundamento_juridico", "")
            cta = pauta.get("cta_etico", "")
            dor_tema = dores.get("mapa_dores", {}).get(tema, {})

            user_message = f"""Escreva um carrossel jurídico premium sobre:

TEMA: {tema}
ÂNGULO EDITORIAL: {angulo}
HOOK SUGERIDO: {hook}
EMOÇÃO GATILHO: {emocao}
FUNDAMENTO JURÍDICO: {fundamento}
CTA APROVADO: {cta}

DOR DO CONSUMIDOR (contexto):
{json.dumps(dor_tema, ensure_ascii=False, indent=2) if dor_tema else "Mapeie com base no tema"}

ESCREVA O CARROSSEL COMPLETO (8-10 slides):

Para cada slide, use este formato:
---
**SLIDE [N]**
[Texto do slide — máximo 4 linhas, preferencialmente 2-3]
---

REQUISITOS:
- Slide 1: hook que para o scroll (sem "Você sabia?", "Veja como", "Conheça")
- Slides 2-3: apresenta a situação real com linguagem da vítima
- Slides 4-6: conteúdo jurídico real e prático (o que a lei diz)
- Slide 7 ou 8: a virada (o direito que o leitor não sabia que tinha)
- Último slide: CTA ético e uma ação concreta
- Todos os slides: linguagem humana, sem aparência de IA

Após o carrossel, forneça:
- **Título do carrossel:** (para uso interno)
- **Por que este carrossel vai funcionar:** (análise em 3-5 frases)
- **Palavras-chave para legenda:** (5-8 hashtags relevantes)
- **Legenda sugerida:** (3-5 frases + CTA)"""

            self._log(f"Gerando carrossel: {tema}")
            resultado = self._call_claude(SYSTEM_PROMPT, user_message, max_tokens=4096)

            carrosseIs.append({
                "tema": tema,
                "angulo": angulo,
                "conteudo": resultado,
            })

            output_name = tema.lower().replace(" ", "_")[:40]
            self._save_output(f"carrossel_{output_name}", resultado, "md")

        output_path = self._save_output("carrosseIs_todos", carrosseIs, "json")

        self._log(f"{len(carrosseIs)} carrosséis gerados")

        return {
            "agent": self.name,
            "status": "success",
            "output_path": str(output_path),
            "data": {"carrosseIs": carrosseIs},
            "summary": f"{len(carrosseIs)} carrosséis premium gerados",
        }
