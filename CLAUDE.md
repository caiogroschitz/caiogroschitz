# Sistema Operacional Editorial Jurídico

## Identidade do Sistema

Este repositório contém um sistema de redação jurídica automatizada de alto nível
especializado em golpes digitais, fraude bancária e direito do consumidor bancário.

O sistema opera como uma equipe editorial real, composta por 10 agentes especializados,
coordenados por um agente-chefe que garante qualidade, ética e precisão jurídica.

## Áreas de Especialização

- Golpe do Pix (clonagem de número, falso atendente, QR Code malicioso)
- Fraude bancária (transações não reconhecidas, chargeback, responsabilidade do banco)
- Engenharia social (phishing, vishing, smishing)
- Invasão de conta (account takeover, autenticação comprometida)
- Empréstimos fraudulentos (consignado não solicitado, crédito sem autorização)
- Responsabilidade civil bancária (falha na segurança, dever de vigilância)
- Fintechs e bancos digitais (Nubank, Inter, C6, PicPay, Mercado Pago)
- Direito do consumidor bancário (CDC, BACEN, PROCON)
- Golpes digitais em geral (marketplace, WhatsApp, fake store)

## Arquitetura do Sistema

```
/agents/              — 10 agentes especializados (Python)
/skills/              — 8 skills reutilizáveis (Python)
/memory/              — Memória contextual persistente (JSON)
/contexts/            — Contextos jurídicos base (Markdown)
/pipelines/           — Orquestrador do pipeline diário (Python)
/prompts/             — Templates de prompts dos agentes (Markdown)
/ranking/             — Motor de scoring de pautas (Python)
/output/templates/    — Templates de output (Markdown)
/output/daily/        — Outputs gerados diariamente
/data/                — Dados de referência jurídica (JSON)
/editorial-calendar/  — Calendário editorial (JSON)
/jurisprudencia/      — Banco de jurisprudências indexadas
/trends/              — Cache de tendências capturadas
/logs/                — Logs de execução do pipeline
/cache/               — Cache de buscas para evitar redundância
/mcp-jusbrasil/       — MCP Server para coleta real de jurisprudência
```

## Como Executar o Pipeline Diário

```bash
# Instalar dependências
pip install -r requirements.txt

# Configurar variáveis de ambiente
cp .env.example .env
# Editar .env com: ANTHROPIC_API_KEY, JUSBRASIL_EMAIL, JUSBRASIL_PASSWORD

# Executar pipeline completo
python pipeline_runner.py --mode=full

# Executar agente específico
python pipeline_runner.py --agent=trend-hunter

# Gerar apenas conteúdo (sem pesquisa)
python pipeline_runner.py --mode=content-only

# Ver relatório do último ciclo
python pipeline_runner.py --report
```

## Agentes do Sistema

| Agente | Função | Output |
|--------|--------|--------|
| trend-hunter | Detecta tendências emergentes | JSON com score |
| jurisprudencia | Pesquisa decisões jurídicas | Markdown jurídico |
| social-pain | Mapeia dores do consumidor | JSON emocional |
| content-strategist | Prioriza pautas | Ranking de conteúdo |
| legal-risk | Auditoria ética e jurídica | Relatório de riscos |
| carousel-writer | Escreve carrosséis premium | Slides textuais |
| reels-script | Cria roteiros curtos | Roteiro formatado |
| seo-blog | Artigos SEO jurídicos | Artigo estruturado |
| authority-linkedin | Posts de autoridade | Post profissional |
| editorial-chief | Orquestra e aprova tudo | Relatório executivo |

## Skills Disponíveis

| Skill | Função |
|-------|--------|
| detect-high-conversion-topic | Score de conversão por tema |
| jurisprudencia-summarizer | Resume decisões complexas |
| anti-ai-writing | Remove aparência de IA |
| hook-generator | Cria hooks de alto impacto |
| ethical-cta | CTAs compatíveis com OAB |
| emotional-pain-mapper | Mapeia emoções da vítima |
| trend-score | Calcula score de tendência |
| fake-jurisprudence-validator | Valida existência de decisões |

## Padrões Obrigatórios

### Conteúdo
- Nunca prometer resultado judicial
- Nunca inventar jurisprudência
- Nunca usar linguagem mercantilista
- Nunca usar clichês de IA ("é fundamental", "é crucial", "vale ressaltar")
- Sempre citar fundamento jurídico real
- Sempre usar linguagem do consumidor, não do jurista

### Qualidade antes de qualquer output
- [ ] Naturalidade — parece humano?
- [ ] Clareza — consumidor leigo entende?
- [ ] Profundidade — tem substância jurídica real?
- [ ] Credibilidade — advogado real assinaria?
- [ ] Retenção — prende do início ao fim?
- [ ] Ética — está dentro dos limites da OAB?
- [ ] Precisão — jurisprudência e base legal verificadas?

## Contexto de Uso

O sistema foi projetado para produção diária de conteúdo jurídico especializado.
O pipeline roda automaticamente, mas toda aprovação final é humana.
Os outputs são sugestões de alta qualidade para revisão editorial antes de publicar.
