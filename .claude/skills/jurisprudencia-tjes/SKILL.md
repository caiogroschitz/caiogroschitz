---
name: jurisprudencia-tjes
description: Lê a última peça processual da conversa (contestação, recurso inominado, contrarrazões, apelação, manifestação) ou um tema informado pelo usuário, identifica a favor de quem a peça argumenta e quais teses precisam de reforço, e busca no sistema de Consulta de Jurisprudência do TJES (sistemas.tjes.jus.br/consulta-jurisprudencia) acórdãos REAIS e favoráveis, cobrindo tanto as Câmaras quanto as Turmas Recursais dos Juizados Especiais capixabas. Devolve cada julgado com citação no padrão CNJ e a ementa transcrita ipsis litteris, pronta para colar na peça, além do formato da ementa-padrão (Recomendação CNJ 154/2024). Use SEMPRE que o usuário pedir "busca jurisprudência no TJES", "acha julgados do Espírito Santo pra essa tese", "precedentes do TJES", "jurisprudência das Turmas Recursais capixabas" ou, depois de redigir ou colar peça de processo capixaba (Vitória, Serra, Cachoeiro, Vila Velha), "agora busca jurisprudência no ES". NÃO use para redigir a peça nem para decidir se cabe recurso.
---

# Jurisprudência TJES favorável à tese da peça

## Objetivo

A partir da última peça da conversa (ou de um tema que o usuário indicar), encontrar no sistema de Consulta de Jurisprudência do TJES acórdãos reais que sustentem as teses da peça e entregá-los prontos para citação: identificação completa no padrão CNJ, ementa transcrita literalmente e o caminho para reabrir o inteiro teor.

O sistema capixaba foi substituído em outubro de 2025. O endereço atual é `https://sistemas.tjes.jus.br/consulta-jurisprudencia/` e ele integra, em bases separadas, PJe de 1º e 2º graus, decisões monocráticas, acórdãos físicos antigos e as Turmas Recursais do Projudi. Duas dessas bases interessam ao trabalho recursal do dia a dia, e é nelas que esta skill opera:

- **2º Grau PJe** (`pje2g`): acórdãos colegiados. Reúne, na mesma base, as Câmaras do Tribunal de Justiça (desde 2020) e as Turmas Recursais dos Juizados Especiais (desde 2018). É a única base com campo de ementa próprio.
- **2º Grau Monocrático PJe** (`pje2g_mono`): decisões monocráticas de desembargador e de relator de Turma Recursal, sem campo de ementa (só inteiro teor).

As demais bases (1º grau, físicos, Projudi) existem e estão documentadas em `references/tjes-consulta-jurisprudencia-campos.md`, mas só devem ser acionadas se o usuário pedir ou se a tese for antiga o bastante para exigir isso.

## REGRA DE OURO: integridade

Isto é inegociável, porque uma citação inventada destrói a peça e a credibilidade de quem assina:

- Só cite acórdãos que você efetivamente localizou e abriu no sistema do TJES NESTA sessão. **Nunca invente, complete de memória ou "reconstrua" número de processo, relator, órgão julgador, data ou texto de ementa.** Números de processo têm dígitos verificadores; um número plausível quase sempre é um número errado.
- A ementa citada para uso na peça é transcrição literal (ipsis litteris) do que consta no acórdão. Cortes são permitidos e sinalizados com "(...)"; alterações, não. Ajustar espaçamento e quebras de linha excedentes é permitido, porque o sistema devolve o texto com espaços em branco de sobra.
- Confirme a direção do julgado antes de citar: a ementa e o dispositivo têm de decidir a favor da tese, não apenas tangenciar o tema. Um acórdão que "menciona golpe via pix" mas condena a instituição financeira não serve à defesa.
- Se a busca falhar (site fora do ar, navegador não conectado, zero resultados reais), diga isso ao usuário e pare. Não preencha o buraco com "jurisprudência de conhecimento geral".

## Passo 1: ler a peça, a favor de quem e quais teses

Localize a última peça na conversa (redigida por você antes ou colada pelo usuário). Antes de buscar, responda duas perguntas:

1. **A favor de quem eu busco?** A peça defende o autor ou o réu? O julgado útil é o que dá razão a esse lado. Se a peça é uma contestação da instituição financeira, procure acórdãos que julgam *improcedente* o pedido do consumidor ou que *dão provimento* ao recurso da ré; se é o recurso inominado do autor, procure os que *reformam* a sentença a favor dele. Se o usuário só deu um tema, pergunte de que lado ele está, ou assuma o lado óbvio e diga qual assumiu.
2. **Quais teses precisam de reforço?** Extraia de 2 a 4 teses centrais. Não busque a peça inteira de uma vez; cada tese vira uma ou duas buscas próprias. Exemplos recorrentes na carteira capixaba:
   - Consumo e bancário: culpa exclusiva da vítima ou fato de terceiro (art. 14, §3º, CDC); fortuito externo; golpe do falso funcionário e engenharia social; transferências via Pix feitas pelo próprio titular; contratação por biometria facial ou dispositivo já habilitado; enriquecimento sem causa; bloqueio cautelar por análise antifraude; Súmula 479/STJ (quando desfavorável, para antecipar e distinguir).
   - Dano moral: mero aborrecimento e dissabor; Súmula 385/STJ (negativação preexistente); quantum e proporcionalidade.
   - Repetição de indébito: ausência de má-fé afasta a dobra (engano justificável); art. 42, parágrafo único, CDC.
   - Processual: ilegitimidade passiva e teoria da asserção; cerceamento de defesa; ônus da prova; prescrição.

Escreva as teses numa lista curta antes de ir ao site. Isso mantém cada busca focada.

## Passo 2: montar os termos de busca

O buscador do TJES aceita sintaxe de consulta completa (é um Solr por trás), e isso muda tudo em relação a uma busca ingênua. Sem operador, os termos são combinados em **OU**, o que devolve dezenas de milhares de resultados inúteis. Compare, na base `pje2g`:

| Consulta | Resultados |
|---|---|
| `golpe pix` | 7.547 |
| `golpe AND pix` | 1.394 |
| `"golpe pix"` | 11 |
| `culpa exclusiva da vítima` | 73.110 |
| `ementa:"culpa exclusiva da vítima"` | 943 |
| `ementa:("culpa exclusiva da vítima" AND pix)` | 111 |

Regras práticas que decorrem disso:

- **Sempre use `AND` entre os conceitos** ou aspas para expressões compostas. Nunca solte termos soltos.
- **Prefixe com `ementa:` sempre que estiver na base 2º Grau PJe.** O acórdão inteiro traz relatórios, nomes de advogados e citações de precedentes de outros tribunais; a ementa traz a tese decidida. Buscar na ementa é o que separa o julgado que decide a matéria daquele que só a menciona. Use parênteses para agrupar: `ementa:("engenharia social" AND "fortuito externo")`.
- Na base **2º Grau Monocrático PJe não existe campo `ementa`**: o texto está em `inteiro_teor`. Use `inteiro_teor:(...)` ou simplesmente termos entre aspas com `AND`. Um `ementa:` ali não filtra nada e devolve lixo.
- `*` funciona como curinga (`consign*` pega consignado e consignação). `OR` funciona para sinônimos: `("recurso provido" OR "sentença reformada")`.
- Marcadores de direção do julgado ajudam muito, mas cuidado, porque a ementa costuma conter os dois lados. Para resultado favorável à ré: `improcedente`, `"culpa exclusiva"`, `"ausência de falha na prestação do serviço"`, `"recurso provido"` (quando a ré era a recorrente), `"recurso conhecido e improvido"` (quando a ré ganhou em primeiro grau). A favor do autor: `"sentença reformada"`, `"dano moral configurado"`, `"falha na prestação do serviço"`.
- Vocabulário que rende no ES: golpe, "golpe do falso funcionário", estelionato, "engenharia social", pix, "culpa exclusiva da vítima", "fato de terceiro", "fortuito externo", "instituição de pagamento", "biometria facial", "dispositivo previamente habilitado", "empréstimo consignado", "descontos indevidos", "bloqueio de conta", "mero dissabor", "quantum indenizatório", "repetição de indébito", "má-fé", "teoria da asserção".

Monte todas as consultas antes de abrir o navegador. Sem captcha e sem sessão a preservar, o custo de cada consulta é baixo, mas a disciplina de listar antes evita busca circular.

## Passo 3: buscar no sistema do TJES

**Claude in Chrome é obrigatório aqui.** A API do sistema responde 403 para qualquer requisição de fora do navegador (WebFetch, curl, biblioteca HTTP): há um WAF na frente. Se o navegador não estiver conectado, avise o usuário e peça para conectar o Chrome e liberar `sistemas.tjes.jus.br` na extensão. Não insista em fetch externo.

1. Navegue para `https://sistemas.tjes.jus.br/consulta-jurisprudencia/`.
2. **Confira a aba de base.** A aba ativa por padrão é "2º Grau Monocrático PJe", não a de acórdãos. Clique em **"2º Grau PJe"** e confirme visualmente que o botão ficou destacado (clique por coordenada na aba; clique por referência de elemento às vezes não registra) e que o rótulo abaixo da contagem de resultados passou a dizer "2º Grau PJe". Trocar de aba zera os filtros já escolhidos, então defina a base primeiro e preencha os filtros depois.
3. Preencha os campos:
   - **Termos da busca**: a consulta montada no Passo 2. Deixe **"Busca Exata" desmarcada** quando estiver usando sintaxe própria, porque essa caixa envolve tudo o que você digitou em aspas e transforma a consulta inteira numa frase literal.
   - **Jurisdição**: é aqui que se separam as duas instâncias dentro da mesma base. "Tribunal de Justiça" traz as Câmaras; "Turma Recursal" traz os Juizados. Rode **duas passadas**, uma para cada, salvo se o usuário pediu instância só. Para peça de JEC, a passada de Turma Recursal é a que mais pesa.
   - **Órgão Julgador**: 1ª a 4ª Câmara Cível, Câmaras Criminais, Câmaras Reunidas, 1ª a 5ª Turma Recursal, Turma de Uniformização. Deixe amplo primeiro; estreite se vier ruído.
   - **Classe Judicial**: "APELAÇÃO CÍVEL" para 2º grau, "RECURSO INOMINADO CÍVEL" para Turma Recursal (o rótulo aparece duplicado em caixa alta e em caixa mista, porque vem de cadastros diferentes; se restringir demais, prefira deixar em "Todos").
   - **Lista de Assuntos**: útil para bancário e consumo ("Indenização por Dano Moral", "Contratos Bancários", "Empréstimo consignado", "Práticas Abusivas", "Repetição de indébito").
   - **Data Inicial / Data Final**: prefira os últimos 3 anos. O filtro incide sobre a data de juntada do documento.
   - **Ordenação**: "Relevância" para triar tese; "Data Juntada (Recente)" quando o usuário quiser o entendimento mais atual.
   - **Itens por página**: suba para 50 ou 100 e economize paginação.
4. Antes de ler os resultados, confira as etiquetas de "Filtros ativos" logo abaixo do botão Buscar: elas mostram exatamente o que está sendo aplicado, e a contagem ao lado de cada opção dos seletores se ajusta à base escolhida. É a forma mais rápida de perceber que a busca saiu na base ou na jurisdição errada. Depois leia a lista: cada linha traz número do processo, classe, magistrado, órgão julgador e data, com um trecho do documento abaixo. Descarte de cara os de direção contrária.
5. **Abra o documento** dos candidatos pelo ícone de olho na coluna "Ações". Abre um modal com o inteiro teor e os botões "Baixar PDF" e "Baixar DOCX". Leia a ementa e o dispositivo inteiros para confirmar que sustentam a tese e para transcrever a ementa por completo. Anote: número do processo, magistrado relator, órgão julgador, jurisdição, classe, data exibida e, se o corpo do acórdão declarar a data da sessão de julgamento, também essa data.

**Atalho recomendado quando forem muitas consultas.** Estando com a página do sistema aberta, dá para chamar a API de dentro do contexto da página com `javascript_tool` e ler ementa e inteiro teor direto do JSON, sem clicar em nada. É o caminho mais rápido para rodar 6 ou 8 consultas e triar por ementa antes de abrir qualquer documento. O endpoint, os nomes exatos dos parâmetros, os campos devolvidos por cada base e as armadilhas estão em `references/tjes-consulta-jurisprudencia-campos.md`. Leia esse arquivo antes de usar o atalho. Mesmo usando a API, confirme no modal do site os julgados que forem efetivamente citados.

**Critérios de seleção**, nesta ordem:

1. A ementa e o dispositivo efetivamente decidem a favor da tese (não basta citar o tema).
2. Casos análogos (mesma causa raiz: golpe do falso funcionário, Pix, consignado, bloqueio, negativação) e recentes (últimos 3 anos).
3. Coerência de instância: para reforçar peça de Juizado, acórdão de Turma Recursal capixaba pesa mais que acórdão de Câmara; para apelação, priorize as Câmaras Cíveis.
4. De 2 a 3 julgados por tese é o ideal. Qualidade acima de quantidade.

## Passo 4: entregar as ementas no formato correto

Para cada tese, entregue no chat (Markdown, prosa natural, sem travessão decorativo, sem cara de IA):

**a) Linha de citação no padrão CNJ** (Recomendação 154/2024, art. 3º, §2º: tribunal, classe, número, relator, unidade julgadora, data de julgamento). Ajuste a unidade conforme a instância:

> Câmara: TJES, Apelação Cível nº 5001234-56.2023.8.08.0024, Rel. Des. Fulano de Tal, 3ª Câmara Cível, j. 10.03.2024.
>
> Turma Recursal: TJES, Recurso Inominado Cível nº 5012965-16.2025.8.08.0012, Rel. Juíza Fulana de Tal, 3ª Turma Recursal, j. 05.08.2026.

Sobre a data, atenção: na base 2º Grau PJe o sistema expõe apenas a data de juntada do documento, exibida na coluna "Data" com o rótulo "Julg.". Se o corpo do acórdão trouxer a data da sessão de julgamento, use essa e cite como `j.`. Se não trouxer, use a data do sistema e diga ao usuário, em uma linha, que aquela é a data de juntada do acórdão, para que ele decida como citar. Não apresente data de juntada como data de julgamento sem avisar.

**b) Ementa transcrita**, bloco literal do acórdão, na caixa e pontuação do original, com cortes sinalizados por "(...)" quando longa. Remova o rótulo inicial ("Ementa:", "EMENTA:", "Ementa.") e comprima os espaços em branco excedentes que o sistema devolve, sem tocar nas palavras. É esse bloco que o usuário cola na peça. Vale notar: as Turmas Recursais capixabas já vêm redigindo no padrão CNJ (I. Caso em exame, II. Questão em discussão, III. Razões de decidir, IV. Dispositivo e tese), o que costuma render blocos longos; corte com "(...)" preservando cabeçalho, razões de decidir e dispositivo.

**c) Por que serve**, uma ou duas frases ligando o julgado ao trecho ou tese específica da peça.

**d) Como reabrir o julgado.** O sistema é uma página única e não gera link permanente por acórdão. Informe o número do processo e a base onde ele está (2º Grau PJe ou 2º Grau Monocrático PJe), lembrando que basta buscar `nr_processo:"5012965-16.2025.8.08.0012"` no campo de termos para reabrir aquele documento. Se o usuário quiser o inteiro teor em arquivo, use "Baixar PDF" no modal.

Ao final, se o usuário pedir a ementa "como tem que ser" para minutar (uma ementa nova, um memorial, uma síntese estruturada), redija-a na estrutura da ementa-padrão do CNJ descrita em `references/ementa-padrao-cnj.md` (Cabeçalho em versalete, I. Caso em exame, II. Questão em discussão, III. Razões de decidir, IV. Dispositivo e tese, remissões). Leia esse arquivo antes de redigir. Ao apenas TRANSCREVER a ementa de um acórdão real, mantenha o texto original do tribunal mesmo que ele não siga o padrão CNJ.

## Fechamento

Ofereça, em uma linha, o próximo passo: ampliar a busca (mais teses, outro período, decisões monocráticas, bases legadas) ou inserir os julgados selecionados diretamente na peça.
