---
name: picpay-especificacao-provas
description: >-
  Lê a íntegra dos autos de um processo da carteira PicPay (PicPay Instituição
  de Pagamento, PicPay Bank ou Banco Original) e redige, DIRETO NO CHAT em
  Markdown, a PETIÇÃO DE ESPECIFICAÇÃO DE PROVAS na ótica do RÉU, em resposta ao
  despacho de saneamento (art. 357 do CPC) que manda especificar as provas a
  produzir com relação clara ao ponto controvertido e justificativa de
  pertinência. Postura padrão: defesa documental, requerer JULGAMENTO ANTECIPADO
  (art. 355, I) e, por cautela, ressalvar depoimento pessoal e prova testemunhal
  contra preclusão. Sem travessão e sem escrita de IA. Use SEMPRE que o usuário
  colar os autos ou o despacho de um caso PicPay e pedir para 'especificar as
  provas', 'responder o despacho de provas', 'fazer a petição de provas',
  'manifestar sobre provas' ou 'pedir julgamento antecipado'. NÃO use para
  contestação, réplica, recurso, embargos, cumprimento de liminar ou outras
  instituições.
---

# PicPay — Especificação de Provas (art. 357 do CPC)

Skill focada em UMA peça só: a **petição de especificação de provas** do PicPay
(réu), em resposta ao despacho de saneamento que intima as partes a dizerem
quais provas ainda pretendem produzir, com relação clara e direta ao ponto
controvertido e justificativa de adequação e pertinência. O usuário cola a
íntegra dos autos (ou só o despacho) e recebe, **no próprio chat, em Markdown**,
a peça pronta para protocolo. Não gera .docx.

## Princípio central: a peça nasce dos autos

A petição só vale se for **fiel ao que está nos autos**. Antes de escrever uma
linha, leia **toda a íntegra** com atenção (ou todo o despacho, se for só ele) e
extraia:

- Número do processo (formato CNJ), vara/juízo, comarca e UF, rito (JEC ou Vara
  Cível).
- Nome e qualificação do autor.
- Qual entidade figura no polo passivo: **PicPay Instituição de Pagamento S.A.**
  (CNPJ 22.896.431/0001-10), **PicPay Bank – Banco Múltiplo S.A.** ou **Banco
  Original S.A.** Use a que consta. Em litisconsórcio, subscreva pela(s)
  correta(s).
- O que o autor pediu na inicial e qual a **causa de pedir** (golpe/fraude,
  empréstimo contestado, bloqueio de conta, cobrança indevida, negativação
  etc.).
- O que a **contestação** já alegou e, principalmente, **quais documentos já
  foram juntados** pela defesa (cadastro, biometria, logs de dispositivo, termos
  de uso, extratos, comprovantes de Pix, telas de chargeback, prints).
- O teor exato do **despacho** que está sendo respondido: ID/fls., o que
  determinou, e o prazo.
- Quais são os **pontos controvertidos** do caso (o que o autor afirma e a
  defesa nega).

Nunca invente número de processo, data, ID, protocolo, documento não juntado ou
prazo. Se faltar dado essencial, **pergunte ao usuário** em vez de adivinhar.

## Passo 1 — Confirmar que é mesmo especificação de provas

Sinais no despacho: "especifiquem as provas que ainda pretendem produzir",
"digam as provas que pretendem produzir, justificando a pertinência",
"manifestem-se sobre provas", "saneamento", "art. 357 do CPC". Se o despacho
pedir outra coisa (réplica, manifestação sobre documentos, sobre cálculos,
cumprimento de liminar), esta não é a skill. Encaminhe (ver "Quando NÃO usar").

## Passo 2 — Definir a postura (padrão: julgamento antecipado)

**Postura padrão da carteira.** Na esmagadora maioria dos casos do PicPay a
defesa é **documental** e a controvérsia é de direito ou já está integralmente
documentada nos autos. Logo, o caminho padrão é:

1. Afirmar que a prova pertinente já está produzida (a documental que instruiu a
   contestação), sendo desnecessária dilação probatória.
2. Requerer o **julgamento antecipado do mérito** (art. 355, I, do CPC).
3. **Por cautela, para afastar preclusão**, ressalvar o interesse na produção de
   **depoimento pessoal do autor** (art. 385 do CPC) e de **prova testemunhal**,
   caso Vossa Excelência entenda necessária a instrução, com apresentação de rol
   no momento oportuno.
4. Não requerer prova pericial nem diligências inúteis (art. 370, parágrafo
   único, do CPC).

**Quando fugir do padrão.** Só especifique ativamente uma prova quando os autos
mostrarem que ela é útil à defesa e ainda não está nos autos. Exemplos:
depoimento pessoal do autor quando há contradição relevante entre a inicial e os
documentos; prova testemunhal quando a defesa depende de fato presenciado;
exibição de documento em poder do autor; perícia (grafotécnica, em dispositivo)
quando o autor nega autoria de operação e isso é o núcleo da lide. Nesses casos,
**especifique de verdade**: diga qual prova, sobre qual ponto controvertido
recai e por que é adequada e pertinente. Se o usuário indicar a linha (quer
julgamento antecipado ou quer produzir prova), siga a instrução dele.

## Passo 3 — Justificar com relação clara e direta

O despacho exige o que o art. 357, II, do CPC pede: vincular cada prova ao ponto
controvertido. Não basta "protesta por todas as provas em direito admitidas",
isso é genérico e pode ser desconsiderado. Sempre que indicar uma prova (ou a
ressalva cautelar), diga **o que ela visa demonstrar**. Ex.: "depoimento
pessoal do autor, para esclarecer as circunstâncias em que voluntariamente
forneceu suas credenciais a terceiro, ponto controvertido central da demanda".

## Estrutura da peça (esqueleto padrão)

Use este esqueleto e ajuste ao caso. Modelos completos, incluindo a variação
para "especificar provas ativamente", estão em `references/modelos.md`.

```
EXCELENTÍSSIMO(A) SENHOR(A) DOUTOR(A) JUIZ(A) DE DIREITO DA [vara] DA COMARCA
DE [comarca]/[UF]        (ou "do Juizado Especial Cível de [comarca]/[UF]")

Processo nº [número CNJ]

[PARTE RÉ, ex.: PICPAY INSTITUIÇÃO DE PAGAMENTO S.A.], já qualificada nos autos
da ação em epígrafe que lhe move [NOME DO AUTOR], vem, respeitosamente, à
presença de Vossa Excelência, em atenção ao r. despacho de [ID/fls.] que
determinou a especificação de provas, expor e requerer o que segue.

[Parágrafo 1: a defesa é documental e a matéria comporta julgamento antecipado.]

[Parágrafo 2: os documentos já juntados com a contestação (indicar quais) provam
o que interessa; a controvérsia é de direito ou está documentada.]

[Parágrafo 3: por cautela, e para afastar preclusão, ressalva o interesse em
depoimento pessoal do autor e prova testemunhal, caso o juízo entenda necessária
a instrução, vinculando cada prova ao ponto controvertido.]

Ante o exposto, requer:

a) o julgamento antecipado do mérito, nos termos do art. 355, I, do CPC, por
   desnecessária a dilação probatória;

b) subsidiariamente, caso Vossa Excelência entenda necessária a instrução, a
   produção de depoimento pessoal do autor e de prova testemunhal, com
   apresentação de rol no prazo a ser designado.

Termos em que pede deferimento.
[Comarca]/[UF], [data].

[Advogado(a)], OAB/[UF] nº [...]
```

Se o usuário não informar data, OAB ou nome do subscritor, deixe o campo entre
colchetes para ele preencher. Não invente.

## Regras de ouro

- Cite sempre o **ID/fls. do despacho** que está sendo respondido e o **número
  do processo** exatamente como consta.
- Relacione cada prova ao ponto controvertido (adequação e pertinência), nunca
  fórmula genérica.
- Fundamento legal direto e enxuto: **art. 355, I** (julgamento antecipado),
  **art. 357, II** (especificação/pertinência), **art. 370, parágrafo único**
  (indeferimento de prova inútil), **art. 385** (depoimento pessoal). Não
  empilhe doutrina nem ementas.
- Não afirme cumprimento de providência nem existência de documento que não
  esteja nos autos.
- Confira o prazo: em regra **5 dias úteis** (arts. 218 e 219 do CPC), mas vale o
  que constar no despacho; se relevante, lembre o usuário de conferir a data de
  publicação.
- Em litisconsórcio (ex.: PicPay Bank + Banco Original), subscreva pela entidade
  correta ou por ambas, conforme os autos.

## Estilo: sem travessão, sem escrita de IA

Este é um requisito duro desta skill. A peça deve soar redigida por advogado, não
por máquina.

- **Nunca use travessão (—).** Reescreva a frase ou use vírgula, ponto,
  parênteses ou dois-pontos.
- Evite os vícios típicos de IA: nada de "não se trata apenas de X, mas de Y",
  nada de aberturas e fechamentos genéricos, nada de conectivos repetidos em
  sequência ("ademais", "outrossim", "nesse sentido" a cada parágrafo), nada de
  adjetivação inflada.
- Frases de tamanhos variados, ritmo humano. Uma ideia por parágrafo.
- Português jurídico limpo e objetivo. Sem "data venia" empilhado, sem floreio.
- Não use emojis, não use listas com marcadores dentro da peça. A peça é texto
  corrido com, no máximo, os requerimentos em alíneas a), b), c).

## Quando NÃO usar (encaminhe para a skill certa)

- Contestação -> **picpay-contestacao** (ou **picpay-contestacao-bloqueio**)
- Réplica, manifestação sobre documentos, ciência, juntada, dilação de prazo ->
  **picpay-peticao-simples**
- Recurso inominado -> **picpay-recurso-inominado**
- Contrarrazões -> **picpay-contrarrazoes-apelacao** / **contrarrazoes-recurso-inominado**
- Embargos de declaração -> **picpay-embargos-declaracao**
- Cumprimento de liminar -> **picpay-cumprimento-liminar**
- Decidir se recorre, requisições, cadastro, prazos no Astrea, cálculo ->
  skills próprias da carteira.

Se o despacho não for de especificação de provas, avise o usuário em uma linha e
aponte a skill adequada.
