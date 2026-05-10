"""Authority LinkedIn Agent — posts de autoridade técnica sem parecer artigo acadêmico."""

import json
from .base_agent import BaseAgent


SYSTEM_PROMPT = """Você é o Editor de LinkedIn Jurídico do escritório.
Especialista em posts que geram autoridade real sem ser chato, sem juridiquês,
sem parecer currículo e sem aparência de IA.

ANATOMIA DO POST LINKEDIN JURÍDICO QUE PERFORMA:

LINHA 1-2 (gancho)
— A linha que aparece antes do "ver mais"
— Deve parar o scroll de qualquer profissional ou consumidor
— Provoca, revela, confronta ou confima algo relevante
— NÃO começa com "Hoje quero falar sobre..."
— NÃO começa com "Você sabia que..."
— NÃO começa com "Dica:"

LINHA 3 em branco (respiração antes do "ver mais")

CORPO DO POST (depois do "ver mais")
— Desenvolve a ideia com substância
— Mistura análise técnica com exemplo real ou caso concreto
— Linguagem acessível mas não superficial
— Pode usar estrutura de lista quando natural (não forçado)
— Máximo 3.000 caracteres no total
— Sem bullets em série (parece IA)

FECHAMENTO
— Uma reflexão, conclusão ou convite
— CTA suave e ético
— Sem "deixe seu comentário abaixo" (todo mundo escreve isso)

ESTILOS PERMITIDOS:
1. Análise técnica de tendência (tom de especialista)
2. Caso real despersonalizado (narrativa)
3. Comparação antes/depois (mudança de lei ou decisão)
4. Desmistificação (quebrando um mito jurídico)
5. Alerta profissional (novidade que muda a prática)

PROIBIDO:
- Começar com "Hoje" (muito comum)
- Usar "é fundamental" ou "é crucial"
- Listar 5 dicas numeradas (clichê)
- Prometer resultado
- Conteúdo de autoajuda jurídica ("acredite em você")
- Emojis em excesso
- Post que parece press release"""


class AuthorityLinkedInAgent(BaseAgent):

    name = "authority-linkedin"
    role = "Editor de Autoridade no LinkedIn"

    def run(self, context: dict) -> dict:
        self._log("Iniciando produção de posts LinkedIn")

        pautas = context.get("pautas_aprovadas", [])
        jurisprudencia = context.get("data", {}).get("jurisprudencia", {}).get("data", {}).get("conteudo_md", "")

        pautas_linkedin = [p for p in pautas if p.get("formato_ideal") in ("linkedin", "todos")]
        if not pautas_linkedin:
            pautas_linkedin = pautas[:2]

        if not pautas_linkedin:
            pautas_linkedin = [{
                "tema": "responsabilidade bancária no golpe do Pix",
                "angulo": "O banco não pode simplesmente dizer que foi culpa do cliente",
                "fundamento_juridico": "CDC art. 14, Resolução BACEN 4.935/2021",
                "tom": "tecnico-humano",
            }]

        posts = []

        for pauta in pautas_linkedin[:2]:
            tema = pauta.get("tema", "")
            angulo = pauta.get("angulo", "")
            fundamento = pauta.get("fundamento_juridico", "")
            tom = pauta.get("tom", "tecnico-humano")

            user_message = f"""Escreva um post de autoridade jurídica para o LinkedIn sobre:

TEMA: {tema}
ÂNGULO: {angulo}
FUNDAMENTO JURÍDICO: {fundamento}
TOM: {tom}

CONTEXTO JURISPRUDENCIAL DISPONÍVEL:
{jurisprudencia[:1000] if jurisprudencia else "Use o seu conhecimento especializado"}

REQUISITOS:
- Total: 1.500 a 3.000 caracteres
- A primeira linha deve parar o scroll (sem "Hoje", "Você sabia?", "Dica:")
- Linha 3 em branco (para criar o "ver mais" natural)
- Corpo com análise real e substância — não superficial
- Deve soar como advogado real, não como robô
- CTA ético e sutil no final
- 3-5 hashtags relevantes no final

ENTREGUE:

**POST COMPLETO:**
[o post completo, pronto para copiar e colar]

---

**ANÁLISE:**
- Gancho: [por que a primeira linha funciona]
- Tipo de post: [análise técnica / caso / desmistificação / alerta]
- Público esperado: [quem vai interagir]
- Previsão de performance: [engajamento esperado e por quê]"""

            self._log(f"Gerando post LinkedIn: {tema}")
            resultado = self._call_claude(SYSTEM_PROMPT, user_message, max_tokens=3000)

            posts.append({"tema": tema, "angulo": angulo, "post": resultado})

            output_name = tema.lower().replace(" ", "_")[:40]
            self._save_output(f"linkedin_{output_name}", resultado, "md")

        output_path = self._save_output("linkedin_posts", posts, "json")

        return {
            "agent": self.name,
            "status": "success",
            "output_path": str(output_path),
            "data": {"posts": posts},
            "summary": f"{len(posts)} posts LinkedIn de autoridade gerados",
        }
