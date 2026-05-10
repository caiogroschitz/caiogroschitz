"""Skill: Gerador de hooks de alto impacto para conteúdo jurídico."""

import random
from typing import Literal

HOOK_TEMPLATES = {
    "revelacao": [
        "O {banco} sabe que tem que devolver. Ele conta com você não saber.",
        "Tem um artigo no CDC que o banco prefere que você nunca leia.",
        "{valor} saiu da sua conta sem você autorizar. Isso tem nome jurídico.",
        "O banco disse que foi culpa sua. A jurisprudência diz o contrário.",
        "A {fintech} desativou sua conta. Não existe forma legal de fazer isso sem aviso.",
    ],
    "confronto": [
        "Você não causou o golpe. O banco falhou na segurança.",
        "Não foi ingenuidade. Foi engenharia social — e o banco é responsável por isso.",
        "Aposentado não pede empréstimo que não solicitou. Banco aprova mesmo assim.",
        "O golpe do Pix não é culpa de quem caiu. É falha de segurança.",
        "Você não autorizou. O banco liberou. A responsabilidade é de quem deveria proteger.",
    ],
    "urgencia": [
        "Se isso aconteceu com você, você tem prazo para agir.",
        "Cada dia que passa sem registrar reduz suas chances.",
        "Você tem {prazo} para entrar com sua reclamação. Esse prazo está correndo agora.",
        "Existe um prazo prescricional. E ele já começou.",
        "Não espere o banco resolver sozinho. Ele não vai.",
    ],
    "pergunta_que_ja_sabe_resposta": [
        "O banco te devolveu o dinheiro do golpe? (A maioria não devolveu.)",
        "Você sabia que pode processar o banco mesmo sem BO?",
        "Empréstimo na sua conta que você não fez? Isso tem solução.",
        "Seu WhatsApp foi clonado e usaram para pedir dinheiro? O golpe tem responsáveis.",
    ],
    "narrativa": [
        "Uma aposentada de 71 anos perdeu R$ 12 mil. O banco disse que foi culpa dela.",
        "Ela acordou com R$ 0 na conta. O banco deu uma explicação que não fez sentido.",
        "Ligaram dizendo que eram do banco. Ele acreditou. Perdeu tudo.",
        "O Pix saiu enquanto ela dormia. O banco disse que foi ela quem fez.",
    ],
    "dado_chocante": [
        "O Brasil registrou {numero} golpes do Pix só no último trimestre.",
        "{percentual}% dos casos de invasão de conta resultam em indenização quando contestados.",
        "Bancos devolvem em menos de 30% dos casos sem ação judicial. Com ação: mais de 70%.",
        "O STJ decidiu: banco que aprova transação suspeita sem verificar é responsável.",
    ],
}

FORMATOS_PROIBIDOS = [
    "Você sabia que",
    "Dica:",
    "Hoje vou falar",
    "Veja como",
    "Aprenda",
    "Descubra",
    "Fique atento",
    "Conheça seus direitos",
]


def generate(
    tema: str,
    emocao: Literal["raiva", "medo", "urgencia", "esperanca", "empatia"] = "raiva",
    formato: Literal["carrossel", "reels", "linkedin", "headline"] = "carrossel",
    contexto: dict = None,
) -> dict:
    """
    Gera hooks de alto impacto para um tema jurídico específico.

    Returns:
        dict com hooks por categoria e score estimado de impacto
    """
    banco = contexto.get("banco", "banco") if contexto else "banco"
    valor = contexto.get("valor", "R$ 8.000") if contexto else "R$ 8.000"
    prazo = contexto.get("prazo", "5 anos") if contexto else "5 anos"
    fintech = contexto.get("fintech", "fintech") if contexto else "fintech"
    numero = contexto.get("numero", "2,4 milhões") if contexto else "2,4 milhões"
    percentual = contexto.get("percentual", "73") if contexto else "73"

    fill = {"banco": banco, "valor": valor, "prazo": prazo,
            "fintech": fintech, "numero": numero, "percentual": percentual}

    emotion_map = {
        "raiva": ["confronto", "revelacao"],
        "medo": ["urgencia", "dado_chocante"],
        "urgencia": ["urgencia", "revelacao"],
        "esperanca": ["pergunta_que_ja_sabe_resposta", "narrativa"],
        "empatia": ["narrativa", "confronto"],
    }

    preferred_cats = emotion_map.get(emocao, ["revelacao", "confronto"])
    all_cats = list(HOOK_TEMPLATES.keys())
    order = preferred_cats + [c for c in all_cats if c not in preferred_cats]

    hooks = {}
    for cat in order:
        templates = HOOK_TEMPLATES[cat]
        selected = random.choice(templates)
        try:
            filled = selected.format(**fill)
        except KeyError:
            filled = selected
        hooks[cat] = filled

    best_cat = preferred_cats[0]
    best_hook = hooks[best_cat]

    if formato == "reels":
        best_hook = best_hook.rstrip(".") + "."
    elif formato == "headline":
        best_hook = best_hook.replace(".", "").strip()

    return {
        "tema": tema,
        "emocao": emocao,
        "formato": formato,
        "hook_principal": best_hook,
        "hooks_alternativos": {k: v for k, v in hooks.items() if k != best_cat},
        "score_impacto_estimado": _score_hook(best_hook, emocao),
        "validacao": _validate(best_hook),
    }


def generate_bank(tema: str, contexto: dict = None) -> list[dict]:
    """Gera banco de hooks para todos os formatos e emoções."""
    emocoes = ["raiva", "medo", "urgencia", "esperanca", "empatia"]
    formatos = ["carrossel", "reels", "linkedin"]
    bank = []
    for emocao in emocoes:
        for formato in formatos:
            hook_data = generate(tema, emocao, formato, contexto)
            bank.append(hook_data)
    return sorted(bank, key=lambda x: x["score_impacto_estimado"], reverse=True)


def _score_hook(hook: str, emocao: str) -> int:
    score = 50
    if any(phrase.lower() in hook.lower() for phrase in FORMATOS_PROIBIDOS):
        score -= 30
    if len(hook) < 80:
        score += 10
    if "?" in hook:
        score += 5
    if any(word in hook.lower() for word in ["banco", "pix", "golpe", "fraude", "dinheiro"]):
        score += 10
    if emocao in ("raiva", "urgencia"):
        score += 5
    if hook[0].isupper() and not hook.startswith(tuple(FORMATOS_PROIBIDOS)):
        score += 10
    return min(score, 100)


def _validate(hook: str) -> dict:
    blocked = [p for p in FORMATOS_PROIBIDOS if hook.startswith(p)]
    return {
        "aprovado": len(blocked) == 0,
        "bloqueios": blocked,
        "tamanho_chars": len(hook),
        "tamanho_ok": 20 <= len(hook) <= 120,
    }
