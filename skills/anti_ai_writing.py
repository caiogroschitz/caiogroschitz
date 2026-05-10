"""Skill: Remove aparência de IA do conteúdo jurídico gerado."""

import re


AI_PHRASES = [
    "é fundamental", "é crucial", "é essencial", "é imprescindível",
    "vale ressaltar", "vale destacar", "vale lembrar", "vale salientar",
    "neste sentido", "nesse sentido", "neste contexto", "nesse contexto",
    "em última análise", "em síntese", "em suma", "a título de conclusão",
    "portanto", "dessa forma", "desta forma", "sendo assim",
    "em consonância", "em conformidade", "à luz de", "sob a égide",
    "no que tange", "no que diz respeito", "no que concerne",
    "conforme supramencionado", "conforme mencionado acima",
    "isso posto", "diante do exposto",
    "certamente", "evidentemente", "claramente", "obviamente",
    "não obstante", "todavia", "outrossim", "ademais",
    "faz-se mister", "cumpre ressaltar", "impende destacar",
    "é de suma importância", "tem relevância ímpar",
    "no cenário atual", "no contexto atual", "nos dias atuais",
    "cada vez mais", "cada vez menos",  # overused
    "é importante salientar", "é importante ressaltar",
    "como é de conhecimento", "como é sabido",
    "abrangente", "robusto", "holístico", "paradigma",
]

OPENER_CLICHES = [
    "Você sabia que",
    "Você sabia?",
    "Você conhece",
    "Já parou para pensar",
    "Imagine a seguinte situação",
    "Veja como",
    "Descubra como",
    "Aprenda como",
    "Entenda por que",
    "Fique atento",
    "Procure um advogado",
    "Conheça seus direitos",
    "Dica:",
    "Dica jurídica:",
    "Curiosidade jurídica:",
    "Hoje quero falar",
    "Olá, tudo bem?",
    "Hoje vou falar",
]

HUMAN_OPENERS = [
    "O banco negou.",
    "Você caiu.",
    "O dinheiro saiu.",
    "Isso não é culpa sua.",
    "Existe um limite para o que o banco pode dizer.",
    "Nem toda perda precisa ser aceita.",
    "Tem algo que os bancos contam com você não saber.",
    "Tem uma diferença entre o que o banco alega e o que a lei diz.",
    "O golpe aconteceu. Mas a história não termina aí.",
    "Sua conta foi invadida. Isso é falha de segurança.",
]

STRUCTURAL_PATTERNS = [
    r"(\d+\.\s+.+\n){4,}",
    r"(•\s+.+\n){4,}",
    r"(-\s+.+\n){5,}",
]


def analyze(text: str) -> dict:
    """Analisa o texto e retorna um relatório de artificialidade."""
    issues = []
    score = 100

    text_lower = text.lower()
    for phrase in AI_PHRASES:
        if phrase.lower() in text_lower:
            count = text_lower.count(phrase.lower())
            issues.append({
                "type": "ai_phrase",
                "phrase": phrase,
                "count": count,
                "severity": "medium",
            })
            score -= min(count * 5, 15)

    for opener in OPENER_CLICHES:
        if text.startswith(opener) or f"\n{opener}" in text:
            issues.append({
                "type": "cliche_opener",
                "phrase": opener,
                "severity": "high",
            })
            score -= 20

    for pattern in STRUCTURAL_PATTERNS:
        if re.search(pattern, text, re.MULTILINE):
            issues.append({
                "type": "ai_structure",
                "pattern": "Lista longa e repetitiva",
                "severity": "medium",
            })
            score -= 10

    sentences = [s.strip() for s in text.replace("\n", " ").split(".") if s.strip()]
    if len(sentences) > 3:
        lengths = [len(s) for s in sentences]
        avg = sum(lengths) / len(lengths)
        variance = sum((l - avg) ** 2 for l in lengths) / len(lengths)
        if variance < 200:
            issues.append({
                "type": "monotone_rhythm",
                "description": "Frases muito uniformes em tamanho (robótico)",
                "severity": "medium",
            })
            score -= 8

    score = max(0, score)
    return {
        "score_humanidade": score,
        "nivel": _level(score),
        "publicavel": score >= 70,
        "total_issues": len(issues),
        "issues": issues,
        "recomendacoes": _recommendations(issues),
    }


def clean(text: str) -> str:
    """Remove automaticamente as piores frases de IA."""
    result = text

    replacements = {
        "é fundamental que": "é necessário que",
        "é crucial": "é decisivo",
        "vale ressaltar que": "",
        "vale destacar que": "",
        "vale lembrar que": "",
        "neste sentido,": "",
        "dessa forma,": "",
        "sendo assim,": "",
        "em última análise,": "",
        "certamente": "",
        "evidentemente": "",
        "faz-se mister": "é necessário",
        "cumpre ressaltar": "é importante notar",
        "impende destacar": "destaque-se que",
        "nos dias atuais": "hoje",
        "no cenário atual": "agora",
        "é de suma importância": "importa muito",
        "abrangente": "amplo",
        "robusto": "sólido",
    }

    for old, new in replacements.items():
        result = re.sub(re.escape(old), new, result, flags=re.IGNORECASE)
        result = re.sub(re.escape(old.capitalize()), new.capitalize() if new else "", result)

    result = re.sub(r"\n{3,}", "\n\n", result)
    result = re.sub(r"  +", " ", result)

    return result.strip()


def _level(score: int) -> str:
    if score >= 85:
        return "HUMANO"
    elif score >= 70:
        return "ACEITÁVEL"
    elif score >= 50:
        return "ARTIFICIOSO"
    return "IA APARENTE"


def _recommendations(issues: list) -> list:
    recs = []
    has_phrases = any(i["type"] == "ai_phrase" for i in issues)
    has_opener = any(i["type"] == "cliche_opener" for i in issues)
    has_structure = any(i["type"] == "ai_structure" for i in issues)
    has_rhythm = any(i["type"] == "monotone_rhythm" for i in issues)

    if has_phrases:
        recs.append("Substituir frases-clichê de IA por linguagem direta e natural")
    if has_opener:
        recs.append("Reescrever a abertura — comece com a dor ou o fato, não com pergunta genérica")
    if has_structure:
        recs.append("Quebrar a estrutura de lista excessiva — misture parágrafos e listas")
    if has_rhythm:
        recs.append("Variar o tamanho das frases — misture frases curtas com parágrafos mais longos")
    if not recs:
        recs.append("Texto aprovado — aparência humana satisfatória")
    return recs
