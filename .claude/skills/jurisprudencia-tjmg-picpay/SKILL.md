---
name: jurisprudencia-tjmg-picpay
description: Lê a última peça processual da conversa (contestação, recurso, contrarrazões, apelação), extrai as teses defensivas do PicPay/Banco Original e busca no TJMG (formEspelhoAcordao.do) jurisprudência FAVORÁVEL a essas teses — resolvendo sozinha o captcha do site via 2Captcha (Rube MCP), sem pedir intervenção manual. Devolve cada julgado com citação no padrão CNJ e a ementa transcrita pronta para colar na peça, além do formato da ementa-padrão (Recomendação CNJ 154/2024). Use SEMPRE que o usuário pedir "busca jurisprudência no TJMG", "acha julgados favoráveis pra essa peça", "precedentes do TJMG", "ementas pra colar na peça", "o TJMG está pedindo captcha", ou, após redigir uma peça, "agora busca jurisprudência". NÃO use para redigir a peça em si (picpay-contestacao, picpay-recurso-inominado etc.) nem para decidir se cabe recurso (picpay-diretrizes-recursais).
---

# Jurisprudência TJMG favorável ao PicPay

## Objetivo

A partir da última peça da conversa, encontrar no buscador de jurisprudência do TJMG acórdãos reais que sustentem as teses defensivas da peça e entregá-los prontos para citação: identificação completa + ementa transcrita + link do espelho do acórdão.

O captcha que o TJMG dispara na submissão da busca é resolvido automaticamente dentro deste fluxo (Passo 3). O usuário não deve ser chamado para digitar código nenhum — se ele precisar intervir, a automação falhou e isso deve ser dito com todas as letras.

## REGRA DE OURO — integridade

- Só cite acórdãos que você efetivamente localizou e leu no site do TJMG NESTA sessão. **NUNCA invente, complete de memória ou "reconstrua" número de processo, relator, câmara, data ou texto de ementa.**
- A ementa citada para uso na peça deve ser transcrição literal (ipsis litteris) do que consta no espelho do acórdão. Cortes são permitidos com "(...)", alterações não.
- Se a busca falhar (site fora do ar, navegador indisponível, captcha não resolvido após as tentativas previstas), informe o usuário e pare. Não substitua por jurisprudência "de conhecimento geral". Uma peça protocolada com precedente inexistente é dano concreto ao cliente e risco disciplinar — por isso a barra aqui é intransigente.

## Passo 1 — Ler a peça e extrair as teses

Localize a última peça processual na conversa (redigida por você ou colada pelo usuário). Extraia 2 a 4 teses centrais que precisam de reforço jurisprudencial. Exemplos típicos da carteira PicPay:

- Golpe/engenharia social: culpa exclusiva da vítima ou fato de terceiro (art. 14, § 3º, CDC); fortuito externo; transações precedidas de senha/biometria/dispositivo cadastrado.
- Empréstimo contestado: contratação regular por biometria facial; valor creditado na conta do autor; vedação ao enriquecimento sem causa.
- Bloqueio de conta: exercício regular de direito; prevenção à fraude; Termos de Uso.
- Dano moral: mero aborrecimento; Súmula 385/STJ (negativação anterior); quantum excessivo.
- Repetição de indébito: ausência de má-fé afasta a dobra (engano justificável).

## Passo 2 — Montar os termos de busca

Para cada tese, monte 1-2 consultas com o vocabulário que aparece em ementas (não use "PicPay"):

- Use expressões entre aspas para termos compostos: `"culpa exclusiva" golpe pix`, `"engenharia social" "fortuito externo"` etc.
- Combine 3 a 5 termos no máximo. Muitos termos = zero resultados; poucos = milhares.
- Termos úteis: golpe, estelionato, engenharia social, pix, "culpa exclusiva da vítima", "fato de terceiro", "fortuito externo", "instituição de pagamento", "biometria facial", "empréstimo consignado", "bloqueio de conta", "mero dissabor", improcedente.
- Como se busca resultado FAVORÁVEL à ré, inclua termos de improcedência quando ajudar: "improcedente", "afastada a responsabilidade", "recurso provido" (quando a ré era apelante).

Monte todas as consultas ANTES de abrir o navegador. O captcha do TJMG é resolvido uma vez por sessão e vale para as buscas seguintes enquanto o cookie de sessão viver — logo, quanto mais consultas você rodar na mesma janela, menos captchas você paga e menos tempo perde.

## Passo 3 — Preparar o solucionador de captcha (antes de abrir o site)

Fazer isso ANTES de navegar evita o pior cenário: descobrir que o 2Captcha não está disponível já com a sessão do TJMG aberta e o relógio do captcha correndo.

1. Confirme que o Rube MCP responde (`RUBE_SEARCH_TOOLS` existe entre as ferramentas). Se as ferramentas do Rube estiverem em modo diferido, carregue-as antes.
2. Descubra os slugs atuais do toolkit 2Captcha — os schemas mudam, então nunca chute nomes de ferramenta:

```
RUBE_SEARCH_TOOLS
queries: [{use_case: "submit a reCAPTCHA v2 sitekey and page URL to 2Captcha and retrieve the solved token; also solve normal image captcha from base64", known_fields: "sitekey, pageurl, body(base64), captcha id"}]
session: {generate_id: true}
```

3. Verifique a conexão: `RUBE_MANAGE_CONNECTIONS` com `toolkits: ["twocaptcha"]`. Só siga se o status estiver ACTIVE. Se não estiver, mostre o link de autenticação retornado e pare — sem 2Captcha ativo não há busca automatizada.
4. Guarde o `session_id`: você vai reusá-lo em todas as chamadas seguintes deste fluxo.

Se o Rube MCP não estiver conectado nesta sessão, diga isso ao usuário em uma linha (o endpoint é `https://rube.app/mcp`) e pergunte se ele prefere conectar ou resolver o captcha manualmente uma vez. Não fique tentando ferramentas que não existem.

Os detalhes de cada tipo de captcha, o payload de cada chamada, o polling do resultado e o código de injeção do token estão em `references/captcha-tjmg.md`. Leia esse arquivo assim que detectar um captcha — ele é curto e evita as armadilhas clássicas (token expirado, callback não disparado, iframe errado).

## Passo 4 — Buscar no TJMG

**Via preferencial — Claude in Chrome** (navegador conectado):

1. Navegue para `https://www5.tjmg.jus.br/jurisprudencia/formEspelhoAcordao.do`.
2. No campo **Palavras**, digite a consulta. Marque **Pesquisar por: Ementa**. Ordene por data de publicação (mais recente primeiro).
3. Submeta.
4. **Se aparecer captcha** (ou uma tela de verificação de segurança no lugar dos resultados): identifique o tipo lendo a página, resolva pelo 2Captcha e reenvie — o procedimento completo está em `references/captcha-tjmg.md`. Em resumo: leia o `data-sitekey` e a URL da página, mande para o 2Captcha, faça polling do resultado (normalmente 15-40s), injete o token no campo de resposta, dispare o callback e submeta de novo.
5. Confirme que os resultados carregaram de fato. Uma lista vazia logo após um captcha costuma significar token expirado ou submissão perdida, não ausência de julgados — refaça a busca antes de concluir que "não há resultados".
6. Leia a lista de resultados. Ignore acórdãos desfavoráveis (procedência contra a instituição financeira).
7. Abra o **espelho do acórdão** dos candidatos e leia a ementa inteira para confirmar que sustenta a tese. Anote: número do processo (padrão CNJ), relator(a), câmara julgadora, data de julgamento, data de publicação e a URL do espelho.
8. Rode as demais consultas na mesma aba, reaproveitando a sessão já validada. Se o captcha reaparecer no meio (a sessão expira, tipicamente após alguns minutos de inatividade), repita o passo 4 — é normal, não é erro.

**Via alternativa — fetch direto** (só se o navegador não estiver disponível; o site frequentemente exige sessão e retorna vazio — nesse caso, use o navegador):

```
https://www5.tjmg.jus.br/jurisprudencia/pesquisaPalavrasEspelhoAcordao.do?palavras=TERMOS+CODIFICADOS&pesquisarPor=ementa&orderByData=2&linhasPorPagina=10&paginaNumero=1&pesquisaPalavras=Pesquisar
```

Outros parâmetros aceitos: `dataPublicacaoInicial`/`dataPublicacaoFinal` (DD/MM/AAAA), `listaOrgaoJulgador`, `pesquisaTesauro=true`. Atenção: o site usa charset ISO-8859-1 — codifique os acentos de acordo. Sem navegador não há como resolver captcha nem injetar token: se essa via devolver a tela de verificação, mude para o Chrome.

**Critérios de seleção** (nesta ordem):

1. A ementa efetivamente decide a favor da tese (não basta mencionar o tema).
2. Preferir acórdãos dos últimos 3 anos; Câmaras Cíveis; casos análogos (mesma causa raiz: golpe pix, consignado, bloqueio…).
3. 2 a 3 julgados por tese é o ideal. Qualidade > quantidade.

## Passo 5 — Entregar as ementas no formato correto

Para cada tese, entregue no chat (Markdown, sem travessão, sem cara de IA):

**a) Linha de citação no padrão CNJ** (Recomendação 154/2024, art. 3º, § 2º: tribunal, classe, número, relator, unidade julgadora, data de julgamento):

> TJMG, Apelação Cível nº 1.0000.00.000000-0/000, Rel. Des. Fulano de Tal, 15ª Câmara Cível, j. 00.00.0000, DJe 00.00.0000.

**b) Ementa transcrita** — bloco literal do espelho do acórdão, em caixa alta como consta no original, com cortes sinalizados por "(...)" quando longa. É esse bloco que o usuário cola na peça.

**c) Por que serve** — 1-2 frases ligando o julgado ao trecho/tese específica da peça.

**d) Link** do espelho do acórdão.

Ao final, se o usuário pedir a ementa "como tem que ser" para minutar (sugestão de ementa em memorial, minuta ou peça), redija-a na estrutura da ementa-padrão do CNJ descrita em `references/ementa-padrao-cnj.md`: Cabeçalho em versalete (ramo do direito, classe, tema, conclusão) + I. Caso em exame + II. Questão em discussão + III. Razões de decidir + IV. Dispositivo e tese + dispositivos e jurisprudência relevantes citados. Leia esse arquivo antes de redigir.

## Fechamento

Não narre o captcha no meio do trabalho: ele é infraestrutura, não resultado. Mencione-o apenas se tiver falhado, ou em uma linha no fim se tiver consumido tentativas fora do normal (por exemplo, "o TJMG pediu verificação três vezes; resolvido automaticamente").

Ofereça em uma linha: ampliar a busca (mais teses, outro período, Turmas Recursais) ou inserir os julgados diretamente na peça.
