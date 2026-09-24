---
name: jurisprudencia-tjsp
description: Lê a última peça processual da conversa (contestação, apelação, recurso inominado, contrarrazões, agravo) ou um tema informado pelo usuário, identifica a favor de quem a peça argumenta e quais teses precisam de reforço, e busca no eSAJ do TJSP (Consulta de Jurisprudência de 2º Grau) acórdãos REAIS e favoráveis — cobrindo tanto as Câmaras de Direito Privado/Público quanto os Colégios e Turmas Recursais (recursos de Juizado Especial). Devolve cada julgado com citação no padrão CNJ e a ementa transcrita ipsis litteris, pronta para colar na peça, além do formato da ementa-padrão (Recomendação CNJ 154/2024). Use SEMPRE que o usuário pedir "busca jurisprudência no TJSP", "acha julgados de São Paulo pra essa tese", "precedentes do TJSP", "acórdãos das Câmaras de Direito Privado", "jurisprudência das Turmas Recursais", "ementas do TJSP pra colar na peça" ou, após redigir/colar uma peça, "agora busca jurisprudência em SP". NÃO use para redigir a peça em si nem para decidir se cabe recurso.
---

# Jurisprudência TJSP favorável à tese da peça

## Objetivo

A partir da última peça da conversa (ou de um tema que o usuário indicar), encontrar no buscador de jurisprudência de segundo grau do TJSP (eSAJ / CJSG) acórdãos reais que sustentem as teses da peça e entregá-los prontos para citação: identificação completa no padrão CNJ + ementa transcrita literalmente + link para o inteiro teor. A busca cobre as duas instâncias recursais do TJSP: as **Câmaras** (apelação, agravo — segundo grau) e os **Colégios/Turmas Recursais** (recurso inominado dos Juizados Especiais), porque muitas causas — sobretudo as de consumo e bancárias de menor valor — são julgadas no Juizado e o precedente útil está lá.

## REGRA DE OURO — integridade

Isto é inegociável, porque uma citação inventada destrói a peça e a credibilidade de quem assina:

- Só cite acórdãos que você efetivamente localizou e abriu no eSAJ do TJSP NESTA sessão. **Nunca invente, complete de memória ou "reconstrua" número de processo, relator, câmara/turma, data ou texto de ementa.** Números de processo do TJSP têm dígitos verificadores; um número plausível quase sempre é um número errado.
- A ementa citada para uso na peça é transcrição literal (ipsis litteris) do que consta no acórdão. Cortes são permitidos e sinalizados com "(...)"; alterações, não.
- Confirme a direção do julgado antes de citar: a ementa e o dispositivo têm de decidir a favor da tese, não apenas tangenciar o tema. Um acórdão que "menciona golpe via pix" mas condena o banco não serve à defesa.
- Se a busca falhar (site fora do ar, navegador não conectado, zero resultados reais), diga isso ao usuário e pare. Não preencha o buraco com "jurisprudência de conhecimento geral".

## Passo 1 — Ler a peça: a favor de quem, e quais teses

Localize a última peça na conversa (redigida por você antes ou colada pelo usuário). Antes de buscar, responda duas perguntas:

1. **A favor de quem eu busco?** A peça defende o autor ou o réu? O julgado útil é o que dá razão a esse lado. Se a peça é uma contestação do banco, você procura acórdãos que julgam *improcedente* o pedido do consumidor; se é a apelação do autor, procura os que *reformam* a sentença a favor dele. Se o usuário só deu um tema (sem peça), pergunte de que lado ele está — ou assuma o lado que o tema deixa óbvio e diga qual assumiu.
2. **Quais teses precisam de reforço?** Extraia de 2 a 4 teses centrais. Não busque a peça inteira de uma vez; cada tese vira uma ou duas buscas próprias. Exemplos recorrentes:
   - Consumo/bancário: culpa exclusiva da vítima ou fato de terceiro (art. 14, §3º, CDC); fortuito externo; golpe/engenharia social via pix; contratação por biometria; enriquecimento sem causa; Súmula 479/STJ (quando desfavorável, para antecipar e distinguir).
   - Dano moral: mero aborrecimento/dissabor; Súmula 385/STJ (negativação preexistente); quantum e proporcionalidade.
   - Repetição de indébito: ausência de má-fé afasta a dobra (engano justificável); art. 42, parágrafo único, CDC.
   - Processual: cerceamento de defesa; ônus da prova; prescrição.

Escreva as teses numa lista curta antes de ir ao site. Isso mantém cada busca focada.

## Passo 2 — Montar os termos de busca

Para cada tese, monte a consulta com o vocabulário que aparece nas ementas, não com o nome das partes. Um acórdão útil raramente cita a instituição pelo nome; ele decide a *tese*.

- Prefira expressões compostas entre aspas: `"culpa exclusiva da vítima" golpe pix`, `"engenharia social" "fortuito externo"`, `"mero aborrecimento" inscrição`.
- Combine de 3 a 5 termos. Termos demais zeram o resultado; de menos trazem milhares e nada específico.
- A **Pesquisa Livre** (inteiro teor) do eSAJ tem **limite de 120 caracteres** — seja econômico. Se a tese for longa, quebre em duas buscas.
- Quando quiser resultado favorável à ré, inclua marcadores de improcedência: `improcedente`, `"afastada a responsabilidade"`, `"recurso improvido"` / `"negaram provimento"`; a favor do autor apelante: `"deram provimento"`, `"reformada a sentença"`.
- Termos úteis por família: golpe, estelionato, "engenharia social", pix, "culpa exclusiva", "fato de terceiro", "fortuito externo", "instituição de pagamento", "biometria facial", "empréstimo consignado", "descontos indevidos", "bloqueio de conta", "mero dissabor", "quantum indenizatório", "repetição de indébito", "má-fé".

## Passo 3 — Buscar no eSAJ do TJSP

**Via preferencial — Claude in Chrome** (o eSAJ depende de sessão/cookies do navegador; é o caminho mais confiável). Se o navegador não estiver conectado, avise o usuário e peça para conectar o Chrome e liberar `esaj.tjsp.jus.br` na extensão.

1. Navegue para a busca completa: `https://esaj.tjsp.jus.br/cjsg/consultaCompleta.do`.
2. Preencha os campos visíveis do formulário:
   - **Pesquisa Livre** (inteiro teor) e/ou **Ementa**: os termos do Passo 2. Comece pela Pesquisa Livre; se vier ruído demais, repita restringindo pela **Ementa**.
   - **Pesquisar com sinônimos**: deixe marcado para ampliar; desmarque se estiver trazendo resultados fora do tema.
   - **Origem**: rode **duas passadas** para cobrir as duas instâncias — uma marcando só "2º grau" (Câmaras) e outra marcando só "Colégios Recursais" (Juizado). Na prática, com as duas caixas marcadas juntas a aba visível de resultados traz só o 2º grau; os Colégios Recursais aparecem em contagem/aba própria e escapam se você não isolar a origem. Por isso, para não perder o precedente de Juizado, faça a passada dedicada de Colégios Recursais. Pule uma das passadas apenas se o usuário pediu uma instância só.
   - **Órgão julgador**: para consumo/bancário, filtre pelas **Câmaras de Direito Privado** (as de nº mais alto e os "Núcleos 4.0" concentram bancário) na passada de 2º grau; na passada recursal, os julgados vêm das **Turmas Recursais Cíveis** (classe "Recurso Inominado Cível"). Deixe amplo se não tiver certeza; estreite depois.
   - **Data de julgamento**: prefira os últimos ~3 anos (campo início/fim, dd/mm/aaaa). O TJSP filtra por julgamento/registro, não por publicação.
   - **Ordenação**: por data (mais recente primeiro) ou por relevância.
3. Submeta e leia a lista (o eSAJ mostra **20 resultados por página** na aba "Acórdãos(N)"; pagine com atenção). Cada item já traz uma ementa resumida com o número CNJ, classe/assunto, relator(a), comarca, órgão julgador e datas — bom para triar. Descarte de cara os de direção contrária.
4. **Abra o inteiro teor** dos candidatos (ícone de PDF / link "Visualizar Inteiro Teor" / `getArquivo.do?cdAcordao=...`) e leia a ementa e o dispositivo inteiros para confirmar que sustentam a tese e para transcrever a ementa por completo. Anote: número do processo (padrão CNJ), relator(a), órgão julgador (Câmara de Direito Privado ou Turma Recursal Cível), comarca, data de julgamento, data de publicação e a URL do inteiro teor.

O detalhamento técnico dos campos, endpoints, códigos de origem/decisão, paginação e armadilhas de codificação está em `references/esaj-cjsg-campos.md` — consulte quando precisar de precisão (por exemplo, montar a URL de um acórdão, entender o fluxo POST→GET, ou se um dia recorrer a uma busca por requisição direta).

**Critérios de seleção**, nesta ordem:

1. A ementa e o dispositivo efetivamente decidem a favor da tese (não basta citar o tema).
2. Casos análogos (mesma causa raiz: golpe pix, consignado, bloqueio, negativação…) e recentes (últimos 3 anos).
3. Coerência de instância: para reforçar uma peça de Juizado, um acórdão de Turma/Colégio Recursal pesa tanto ou mais que um de Câmara; para apelação, priorize as Câmaras.
4. 2 a 3 julgados por tese é o ideal. Qualidade acima de quantidade.

## Passo 4 — Entregar as ementas no formato correto

Para cada tese, entregue no chat (Markdown, prosa natural, sem travessão decorativo, sem cara de IA):

**a) Linha de citação no padrão CNJ** (Recomendação 154/2024, art. 3º, §2º: tribunal, classe, número, relator, unidade julgadora, data de julgamento). Ajuste a unidade conforme a instância:

> Câmara: TJSP, Apelação Cível nº 1234567-89.2023.8.26.0100, Rel. Des. Fulano de Tal, 15ª Câmara de Direito Privado, j. 10.03.2024, DJe 12.03.2024.
>
> Turma/Colégio Recursal: TJSP, Recurso Inominado nº 1001234-56.2023.8.26.0016, Rel. Juiz Fulano de Tal, 3ª Turma Cível do Colégio Recursal Central da Capital, j. 10.03.2024.

**b) Ementa transcrita** — bloco literal do acórdão, na caixa e pontuação do original, com cortes sinalizados por "(...)" quando longa. É esse bloco que o usuário cola na peça.

**c) Por que serve** — uma ou duas frases ligando o julgado ao trecho/tese específico da peça.

**d) Link** do inteiro teor no eSAJ.

Ao final, se o usuário pedir a ementa "como tem que ser" para minutar (uma ementa nova, um memorial, uma síntese estruturada), redija-a na estrutura da ementa-padrão do CNJ descrita em `references/ementa-padrao-cnj.md` (Cabeçalho em versalete + I. Caso em exame + II. Questão em discussão + III. Razões de decidir + IV. Dispositivo e tese + remissões). Leia esse arquivo antes de redigir. Ao apenas TRANSCREVER a ementa de um acórdão real, mantenha o texto original do tribunal mesmo que ele não siga o padrão CNJ.

## Fechamento

Ofereça, em uma linha, o próximo passo: ampliar a busca (mais teses, outro período, outra instância) ou inserir os julgados selecionados diretamente na peça.
