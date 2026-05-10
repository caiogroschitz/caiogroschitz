"""SEO Blog Agent — produz artigos jurídicos otimizados para busca orgânica."""

import json
from .base_agent import BaseAgent


SYSTEM_PROMPT = """Você é o Especialista em SEO Jurídico do escritório.
Domina a produção de artigos que ranqueiam no Google e são lidos até o fim.

Você pensa em dois leitores ao mesmo tempo:
1. O algoritmo do Google (quer estrutura, keywords, profundidade)
2. A vítima real (quer respostas claras, sem juridiquês, sem enrolação)

ESTRUTURA PADRÃO DO ARTIGO SEO JURÍDICO:

H1: Keyword principal com promessa clara (não genérica)
Meta description: 155 chars, inclui keyword + benefício
Intro: 150-200 palavras, confirma que o leitor está no lugar certo

H2: [Contextualiza o problema — o que está acontecendo]
H2: [A responsabilidade do banco — o que a lei diz]
H2: [O que fazer imediatamente após o golpe — passos práticos]
H2: [Documentação necessária — o que juntar]
H2: [Como funciona na prática — processo simplificado]
H2: [Perguntas frequentes] → FAQ Schema

Conclusão: recapitula + CTA ético

PRINCÍPIOS SEO JURÍDICO:

1. KEYWORD RESEARCH SIMULADO
   - Keyword principal: intenção transacional/informacional
   - Keywords secundárias: variações long-tail
   - Semantic SEO: termos relacionados naturalmente

2. ESTRUTURA TÉCNICA
   - H1 único com keyword principal
   - H2 e H3 com keywords secundárias naturalmente
   - FAQ com 5-7 perguntas reais que as pessoas pesquisam
   - Internal linking sugerido (mencionar outros temas relacionados)

3. CONTEÚDO QUE CONVERTE
   - Responde a pergunta do título nos primeiros 100 palavras
   - Usa dados reais quando disponíveis
   - Cita a lei de forma simples (não técnica)
   - Inclui exemplo prático
   - Termina com ação clara

4. PROIBIDO:
   - Keyword stuffing (forçar keyword em excesso)
   - Conteúdo de relleno (encher de parágrafo vazio)
   - Prometer resultado
   - Inventar jurisprudência
   - Juridiquês que o leigo não entende"""


class SeoBlogAgent(BaseAgent):

    name = "seo-blog"
    role = "Especialista em SEO Jurídico"

    def run(self, context: dict) -> dict:
        self._log("Iniciando produção de artigo SEO")

        pautas = context.get("pautas_aprovadas", [])
        jurisprudencia_md = context.get("data", {}).get("jurisprudencia", {}).get("data", {}).get("conteudo_md", "")

        pauta = pautas[0] if pautas else {
            "tema": "golpe do Pix por falso atendente bancário",
            "angulo": "banco é obrigado a devolver o dinheiro",
            "palavras_chave_seo": [
                "golpe do pix falso atendente",
                "banco devolver dinheiro golpe pix",
                "fui vítima de golpe do pix o que fazer",
            ],
            "fundamento_juridico": "CDC art. 14, responsabilidade objetiva do fornecedor",
        }

        tema = pauta.get("tema", "")
        angulo = pauta.get("angulo", "")
        keywords = pauta.get("palavras_chave_seo", [tema])
        fundamento = pauta.get("fundamento_juridico", "")
        kw_principal = keywords[0] if keywords else tema
        kw_secundarias = keywords[1:] if len(keywords) > 1 else []

        user_message = f"""Escreva um artigo SEO jurídico completo sobre:

TEMA: {tema}
ÂNGULO EDITORIAL: {angulo}
KEYWORD PRINCIPAL: {kw_principal}
KEYWORDS SECUNDÁRIAS: {json.dumps(kw_secundarias, ensure_ascii=False)}
FUNDAMENTO JURÍDICO: {fundamento}

CONTEXTO JURISPRUDENCIAL:
{jurisprudencia_md[:1500] if jurisprudencia_md else "Pesquise com base no seu conhecimento atual"}

ESPECIFICAÇÕES DO ARTIGO:
- Mínimo 1.800 palavras, máximo 2.800 palavras
- Linguagem: B2C (consumidor leigo, não jurista)
- Tom: informativo, empático, autoridade sem arrogância
- CTA ético ao longo e no final

ESTRUTURA OBRIGATÓRIA:

# [H1 com keyword principal — deve ser atraente e preciso]

**Meta description:** [155 chars exatos — inclui keyword + benefício]
**Keyword principal:** {kw_principal}
**Keywords secundárias:** {', '.join(kw_secundarias)}

---
[INTRODUÇÃO — 150-200 palavras]
Confirma que o leitor está no lugar certo. Apresenta o problema brevemente.
Antecipa o que o artigo vai responder. NÃO enrola.

## [H2: O problema e como acontece — contextualiza]
[300-400 palavras]

## [H2: O que a lei diz — responsabilidade do banco]
[300-400 palavras — cita o fundamento jurídico de forma simples]

## [H2: O que fazer imediatamente — passos práticos]
[300-400 palavras — lista numerada, acionável]

## [H2: Documentação — o que reunir]
[200-300 palavras]

## [H2: Como o processo funciona na prática]
[200-300 palavras]

## Perguntas Frequentes sobre [tema]

**[Pergunta 1 real que as pessoas pesquisam no Google]**
[Resposta direta em 2-4 frases]

**[Pergunta 2]**
[Resposta]

**[Pergunta 3]**
[Resposta]

**[Pergunta 4]**
[Resposta]

**[Pergunta 5]**
[Resposta]

---
[CONCLUSÃO — 100-150 palavras]
Recapitula brevemente. Orienta o próximo passo. CTA ético.

---
*[Nota de rodapé: As informações deste artigo têm caráter educativo e não constituem
assessoria jurídica individual. Cada caso possui particularidades que devem ser
avaliadas por um advogado.]*"""

        self._log(f"Gerando artigo SEO: {tema}")
        resultado = self._call_claude(SYSTEM_PROMPT, user_message, max_tokens=6000)

        output_name = kw_principal.lower().replace(" ", "_")[:50]
        output_path = self._save_output(f"artigo_seo_{output_name}", resultado, "md")

        return {
            "agent": self.name,
            "status": "success",
            "output_path": str(output_path),
            "data": {"artigo_md": resultado, "keyword_principal": kw_principal},
            "summary": f"Artigo SEO gerado: {kw_principal}",
        }
