"""Skill: Gerador de CTAs éticos compatíveis com o Código de Ética da OAB."""

from typing import Literal


OAB_BLOCKED_PHRASES = [
    "entre em contato para consulta",
    "clique no link da bio para contratar",
    "agende sua consulta gratuita",
    "garantimos resultado",
    "ganhou na Justiça com certeza",
    "indenização garantida",
    "chame no whatsapp",
    "acesse o link",
    "contrate agora",
    "primeira consulta grátis",
    "sem custo inicial",
    "sem ganhar não cobramos",
    "honorários apenas no êxito",
    "somos os melhores em",
    "número 1 em",
]

APPROVED_CTAS = {
    "carrossel": {
        "salvamento": [
            "Salve esse conteúdo — pode precisar depois.",
            "Salva. Você pode precisar disso.",
            "Salva para ter sempre à mão.",
            "Guarda esse carrossel — compartilha com quem precisa.",
        ],
        "engajamento": [
            "Comenta DIREITO se isso aconteceu com você.",
            "Me conta nos comentários: o banco devolveu?",
            "Alguém que você conhece passou por isso? Marca aqui.",
            "Compartilha com quem precisa saber disso.",
        ],
        "seguimento": [
            "Me segue — posto mais conteúdo sobre seus direitos toda semana.",
            "Segue o perfil para saber quando o banco está errado.",
            "Ativa as notificações para não perder o próximo.",
        ],
        "informativo": [
            "Dúvidas específicas? Deixa nos comentários.",
            "Caso diferente do seu? Me conta no comentário.",
            "Quer saber mais sobre o seu caso? Comenta abaixo.",
        ],
    },
    "reels": {
        "salvamento": [
            "Salva esse vídeo — pode precisar.",
            "Compartilha com alguém que passou por isso.",
            "Manda pra quem você conhece que foi vítima.",
        ],
        "engajamento": [
            "O banco te devolveu? Comenta SIM ou NÃO.",
            "Passou por isso? Comenta aqui.",
            "Caso parecido? Me conta.",
        ],
        "seguimento": [
            "Me segue para mais conteúdo sobre direitos bancários.",
            "Ativa o sininho — tem mais vindo.",
        ],
    },
    "linkedin": {
        "discussao": [
            "Qual a sua experiência com casos assim?",
            "O que você tem visto na prática?",
            "Como os bancos têm respondido nas suas demandas?",
            "Esse tema merece mais atenção dos escritórios?",
        ],
        "reflexao": [
            "O cenário está mudando. A pergunta é a que velocidade.",
            "Informação preventiva ainda é o melhor ativo.",
            "O consumidor que conhece seus direitos é um consumidor diferente.",
        ],
    },
    "seo_blog": {
        "informativo": [
            "Cada caso tem suas particularidades. As informações deste artigo têm caráter educativo.",
            "Para entender melhor sua situação específica, consulte um advogado especializado.",
            "Este artigo é atualizado regularmente com base nas decisões mais recentes dos tribunais.",
        ],
    },
}


def generate(
    formato: Literal["carrossel", "reels", "linkedin", "seo_blog"] = "carrossel",
    objetivo: Literal["salvamento", "engajamento", "seguimento", "informativo", "discussao", "reflexao"] = "salvamento",
    tema: str = "",
    personalizado: str = "",
) -> dict:
    """
    Gera CTAs éticos para cada formato e objetivo.

    Returns:
        dict com CTA principal, alternativas e validação OAB
    """
    if personalizado:
        validacao = validate(personalizado)
        return {
            "cta_principal": personalizado if validacao["aprovado"] else "",
            "aprovado": validacao["aprovado"],
            "validacao": validacao,
            "alternativas": [],
        }

    format_ctas = APPROVED_CTAS.get(formato, APPROVED_CTAS["carrossel"])
    objetivo_ctas = format_ctas.get(objetivo, list(format_ctas.values())[0])

    principal = objetivo_ctas[0]
    alternativas = objetivo_ctas[1:]

    return {
        "formato": formato,
        "objetivo": objetivo,
        "tema": tema,
        "cta_principal": principal,
        "alternativas": alternativas,
        "aprovado": True,
        "validacao": {"oab_compliant": True, "problemas": []},
        "nota": "CTA pré-aprovado — dentro dos limites do Código de Ética OAB",
    }


def validate(cta_text: str) -> dict:
    """Valida um CTA customizado contra as regras da OAB."""
    text_lower = cta_text.lower()
    problemas = []

    for phrase in OAB_BLOCKED_PHRASES:
        if phrase.lower() in text_lower:
            problemas.append({
                "frase_bloqueada": phrase,
                "motivo": _get_reason(phrase),
                "norma": _get_norm(phrase),
            })

    return {
        "aprovado": len(problemas) == 0,
        "oab_compliant": len(problemas) == 0,
        "problemas": problemas,
        "sugestao": _suggest_fix(cta_text, problemas) if problemas else cta_text,
    }


def generate_full_set(tema: str, formato: str = "carrossel") -> dict:
    """Gera conjunto completo de CTAs para uso em um conteúdo."""
    format_ctas = APPROVED_CTAS.get(formato, APPROVED_CTAS["carrossel"])
    result = {}
    for objetivo, ctas in format_ctas.items():
        result[objetivo] = {
            "cta_principal": ctas[0],
            "alternativas": ctas[1:],
            "aprovado": True,
        }
    return {"tema": tema, "formato": formato, "ctas": result}


def _get_reason(phrase: str) -> str:
    reasons = {
        "entre em contato": "Captação direta de clientela (art. 39, EOAB)",
        "consulta gratuita": "Publicidade enganosa implícita sobre honorários",
        "garantimos resultado": "Promessa de resultado vedada (art. 34, XX, EOAB)",
        "honorários apenas no êxito": "Divulgação inadequada de pacto de honorários",
        "número 1": "Publicidade comparativa vedada (art. 40, EOAB)",
        "somos os melhores": "Publicidade comparativa vedada (art. 40, EOAB)",
    }
    for key, reason in reasons.items():
        if key.lower() in phrase.lower():
            return reason
    return "Viola o Código de Ética e Disciplina da OAB (Resolução CFO-02/2015)"


def _get_norm(phrase: str) -> str:
    if any(w in phrase.lower() for w in ["garantimos", "resultado", "ganhou"]):
        return "Art. 34, XX, Lei 8.906/94 — EOAB"
    if any(w in phrase.lower() for w in ["melhor", "número 1"]):
        return "Art. 40, Resolução CFO-02/2015"
    if any(w in phrase.lower() for w in ["contrato", "contratar", "consulta grátis"]):
        return "Art. 39, Resolução CFO-02/2015"
    return "Resolução CFO-02/2015 — Código de Ética OAB"


def _suggest_fix(original: str, problemas: list) -> str:
    fix = original
    replacements = {
        "entre em contato": "deixa nos comentários",
        "consulta gratuita": "mais informações nos comentários",
        "garantimos resultado": "entenda seus direitos",
        "chame no whatsapp": "comenta aqui",
        "acesse o link": "salva esse conteúdo",
    }
    for old, new in replacements.items():
        fix = fix.replace(old, new)
    return fix
