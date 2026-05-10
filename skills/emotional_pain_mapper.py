"""Skill: Mapeia dores emocionais das vítimas de golpes para uso em conteúdo."""

from typing import Literal


PAIN_PROFILES = {
    "golpe_pix": {
        "emocao_primaria": "vergonha",
        "emocao_secundaria": "raiva",
        "emocao_terciaria": "impotencia",
        "narrativa_interna": "Fui idiota de cair nisso",
        "medo_principal": "Nunca mais vou ver esse dinheiro",
        "gatilho_de_acao": "Descobrir que o banco pode ser responsável",
        "objecoes": [
            "Fui eu que autorizei, então não adianta reclamar",
            "Isso vai levar anos na Justiça",
            "O banco nunca vai me devolver",
            "Já fiz BO, não adiantou nada",
        ],
        "vocabulario": [
            "cai no golpe", "passei vergonha", "perdi tudo", "fui enganado",
            "o banco não quis saber", "disseram que eu autorizei",
            "o dinheiro simplesmente sumiu", "não sei o que fazer",
        ],
        "hook_emocional": "Você caiu no golpe do Pix. O banco disse que foi culpa sua.",
        "quebra_vergonha": "Isso não é falta de inteligência. É engenharia social — uma técnica profissional de manipulação.",
    },
    "consignado_nao_autorizado": {
        "emocao_primaria": "raiva",
        "emocao_secundaria": "incredulidade",
        "emocao_terciaria": "medo",
        "narrativa_interna": "Como isso pode ter acontecido sem eu saber?",
        "medo_principal": "Minha aposentadoria vai ser comprometida",
        "gatilho_de_acao": "Ver o desconto no benefício mês após mês",
        "objecoes": [
            "Já tentei cancelar e não consegui",
            "O banco/correspondente diz que eu assinei",
            "O INSS não me ajuda",
            "Isso é muito complicado para resolver",
        ],
        "vocabulario": [
            "empréstimo que não peguei", "desconto que não reconheço",
            "não autorizei nada", "assinaram por mim", "correspondente bancário",
            "meu benefício foi cortado", "ficou sem o dinheiro",
        ],
        "hook_emocional": "Apareceu um desconto na sua aposentadoria que você não reconhece.",
        "quebra_vergonha": "Você não assinou. Foram eles que fraudaram. E tem como provar.",
    },
    "invasao_conta": {
        "emocao_primaria": "panico",
        "emocao_secundaria": "impotencia",
        "emocao_terciaria": "desconfianca",
        "narrativa_interna": "Como entraram na minha conta? O que mais eles podem fazer?",
        "medo_principal": "Minha vida financeira foi comprometida e não sei a extensão",
        "gatilho_de_acao": "Perceber transações que não reconhece",
        "objecoes": [
            "O banco diz que eu precisaria provar que não fiz",
            "Não tenho como provar que não fui eu",
            "Minha senha era só minha — como eles conseguiram?",
        ],
        "vocabulario": [
            "invadiram minha conta", "fizeram transações sem eu saber",
            "minha senha era segura", "o banco disse que fui eu",
            "não reconheço nada disso", "bloqueei o cartão mas já era tarde",
        ],
        "hook_emocional": "Sua conta foi invadida. O banco diz que a responsabilidade é sua.",
        "quebra_vergonha": "O banco tem obrigação de detectar transações atípicas. Se não detectou, falhou.",
    },
    "whatsapp_clonado": {
        "emocao_primaria": "vergonha",
        "emocao_secundaria": "culpa",
        "emocao_terciaria": "preocupacao_relacional",
        "narrativa_interna": "Usaram meu nome para enganar as pessoas que eu amo",
        "medo_principal": "Perder a confiança das pessoas próximas",
        "gatilho_de_acao": "Amigos e família reclamando que caíram no golpe",
        "objecoes": [
            "A operadora disse que não tem como devolver o número",
            "As transferências foram feitas pelas minhas vítimas, não por mim",
            "Não sei se tenho responsabilidade por quem foi enganado",
        ],
        "vocabulario": [
            "clonaram meu WhatsApp", "usaram meu nome", "pediram dinheiro para meus contatos",
            "minha família transferiu achando que era eu", "perdi o acesso",
            "número portado sem minha autorização", "SIM swap",
        ],
        "hook_emocional": "Clonaram seu WhatsApp e pediram dinheiro para todo mundo que você conhece.",
        "quebra_vergonha": "Você foi a primeira vítima. Os seus contatos, a segunda. A responsabilidade é da operadora.",
    },
    "fake_store": {
        "emocao_primaria": "raiva",
        "emocao_secundaria": "frustracao",
        "emocao_terciaria": "resignacao",
        "narrativa_interna": "Fui ingênuo de comprar num site duvidoso",
        "medo_principal": "Nunca vou receber o produto nem o dinheiro de volta",
        "gatilho_de_acao": "Descobrir que o site era falso e a empresa não existe",
        "objecoes": [
            "Paguei no Pix — não tem como estornar",
            "A empresa não existe — não tenho como processar",
            "Já tentei chargeback e não deu certo",
        ],
        "vocabulario": [
            "site falso", "não chegou", "não entregou", "golpe de loja virtual",
            "produto nunca chegou", "site sumiu", "boleto falso", "CNPJ inexistente",
        ],
        "hook_emocional": "Comprou online, pagou, e o produto nunca chegou. O site sumiu.",
        "quebra_vergonha": "Existem mecanismos legais de contestação. A plataforma pode ser responsável.",
    },
}

EMOTIONAL_STAGES = {
    "descoberta": {
        "reacao": "Choque, negação, verificação compulsiva",
        "duracao": "0-2 horas",
        "acao_tipica": "Tenta contato com banco, ligar para o número que ligou",
    },
    "negacao": {
        "reacao": "Tenta resolver sozinho, não aceita que perdeu",
        "duracao": "2-24 horas",
        "acao_tipica": "Vai ao banco presencialmente, busca o número que ligou",
    },
    "busca": {
        "reacao": "Pesquisa no Google, grupos de WhatsApp, Reclame Aqui",
        "duracao": "1-7 dias",
        "acao_tipica": "Busca 'como recuperar dinheiro golpe pix', acha conteúdos",
    },
    "decisao": {
        "reacao": "Decide se vai agir juridicamente ou aceitar a perda",
        "duracao": "7-30 dias",
        "acao_tipica": "Busca advogado, Procon, ou desiste",
    },
}


def get_profile(golpe_tipo: str) -> dict:
    """Retorna o perfil emocional completo de um tipo de golpe."""
    profile = PAIN_PROFILES.get(golpe_tipo.lower().replace(" ", "_"), None)
    if not profile:
        for key, val in PAIN_PROFILES.items():
            if any(word in golpe_tipo.lower() for word in key.split("_")):
                return val
    return profile or _generic_profile()


def map_content_to_pain(conteudo_tema: str) -> dict:
    """Mapeia um tema de conteúdo às dores emocionais para otimizar a comunicação."""
    profile = get_profile(conteudo_tema)
    if not profile:
        return _generic_profile()

    return {
        "tema": conteudo_tema,
        "perfil_emocional": profile,
        "estagio_alvo": "busca",
        "detalhes_estagio": EMOTIONAL_STAGES["busca"],
        "recomendacoes_conteudo": {
            "abertura": f"Começar reconhecendo a emoção: '{profile['hook_emocional']}'",
            "desenvolvimento": f"Quebrar a vergonha/culpa: '{profile['quebra_vergonha']}'",
            "vocabulario": "Usar palavras do consumidor: " + ", ".join(profile["vocabulario"][:5]),
            "objecoes": "Antecipar e quebrar: " + "; ".join(profile["objecoes"][:2]),
            "gatilho_cta": f"Ativar com: '{profile['gatilho_de_acao']}'",
        },
    }


def _generic_profile() -> dict:
    return {
        "emocao_primaria": "raiva",
        "emocao_secundaria": "impotencia",
        "emocao_terciaria": "esperanca",
        "narrativa_interna": "Não sei o que fazer com isso",
        "medo_principal": "Não conseguir resolver",
        "gatilho_de_acao": "Descobrir que tem saída",
        "objecoes": ["É complicado demais", "Vai demorar muito"],
        "vocabulario": ["fui prejudicado", "não sei o que fazer", "bank não ajuda"],
        "hook_emocional": "Isso aconteceu com você. Tem como resolver.",
        "quebra_vergonha": "Você não é o único. E tem proteção legal.",
    }
