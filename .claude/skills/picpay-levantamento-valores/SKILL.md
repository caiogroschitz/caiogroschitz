---
name: picpay-levantamento-valores
description: >-
  Redige a petição de LEVANTAMENTO DE VALORES / EXPEDIÇÃO DE ALVARÁ do escritório Barros
  Filho e Almeida Prado em favor do PICPAY (PicPay Instituição de Pagamento S.A.), DIRETO NO
  CHAT em Markdown, com os dados bancários fixos do PicPay e escolhendo automaticamente a OAB
  do Mario Thadeu Leme de Barros Filho conforme o estado do processo (SP principal; RJ, MG,
  ES, BA, GO, PE, DF e PR suplementares). Use SEMPRE que o usuário enviar um documento/print/PDF
  de processo (intimação, decisão ou sentença que libera o saque) e pedir "fazer o levantamento",
  "levantamento de valores", "petição/expedição de alvará", "levantar/sacar os valores",
  "transferir os valores pagos a maior", ou colar os dados do processo pedindo a peça. Detecta
  o estado pelo número CNJ e pela comarca e marca a inscrição suplementar quando não for SP.
  NÃO use para contestação, recurso inominado, contrarrazões, embargos ou cumprimento de
  sentença — cada um tem skill própria.
---

# Levantamento de valores / expedição de alvará — PicPay (Mario)

Esta skill monta a petição simples e repetitiva de **levantamento de valores** (pedido de
expedição de alvará / transferência) que o escritório **Barros Filho e Almeida Prado Sociedade
de Advogados** protocola em favor do **PicPay**. Ela quase não muda de um processo para outro:
o que varia é o cabeçalho (juízo/comarca), o número do processo, o autor, a referência da
intimação e — o ponto mais sensível — **qual OAB do Mario entra na assinatura**, porque ele tem
inscrição em vários estados e a peça vai assinada com a OAB do estado onde o processo corre.

O trabalho da skill é preencher isso sem erro e devolver o texto pronto no chat para o usuário
conferir, copiar e protocolar.

## Fluxo de trabalho

1. **Leia o documento do processo** que o usuário enviou (PDF/print da intimação, decisão ou
   sentença que autorizou o levantamento). Se ele apenas colar os dados no chat, use o que veio.
2. **Extraia os campos variáveis** (juízo, comarca/UF, nº do processo, autor, referência da
   intimação, e o motivo do levantamento). Veja a seção "Campos variáveis".
3. **Descubra o estado (UF)** do processo pelo número CNJ e confirme pela comarca do cabeçalho.
4. **Escolha a OAB do Mario** para essa UF na tabela abaixo e defina se é principal (SP) ou
   suplementar (as demais).
5. **Monte a petição** a partir do template, com os dados fixos do PicPay.
6. **Rode o checklist** antes de entregar.
7. **Entregue o texto no chat** em Markdown, pronto para copiar.

Se faltar algum dado essencial (autor, nº do processo, comarca ou a referência da intimação) e
você não conseguir extrair do documento, **pergunte de forma objetiva** em vez de inventar. Peça
apenas o que faltou.

## Dados fixos (não mudam de um processo para o outro)

Estes blocos são sempre iguais — o cliente é sempre o PicPay:

- **Escritório / peticionante:** BARROS FILHO E ALMEIDA PRADO SOCIEDADE DE ADVOGADOS
- **Cliente representado:** PICPAY INSTITUIÇÃO DE PAGAMENTO S.A
- **Signatário:** MARIO THADEU LEME DE BARROS FILHO
- **Local da assinatura (data):** São Paulo — é sempre São Paulo (sede do escritório),
  independentemente do estado onde corre o processo. Use a **data atual** (data do protocolo),
  no formato `São Paulo, DD de mês de AAAA` com o mês por extenso em minúsculas, salvo se o
  usuário pedir outra data.
- **Dados bancários de destino (conta do PicPay que recebe o valor):**

  ```
  PICPAY INST DE PAGAMENTOS S.A
  22.896.431/0001-10
  Bradesco
  Ag.: 2372
  C.C.: 0033937-7
  ```

  Observação: o modelo original do escritório trazia o CNPJ como `022.896.431/0001-10` (com um
  zero a mais na frente). O CNPJ do PicPay é `22.896.431/0001-10`. Use este último, salvo
  orientação em contrário do usuário.

## OAB do Mario por estado

O Mario tem inscrição na OAB em vários estados. **SP é a inscrição principal**; todas as outras
são **suplementares**. Use a OAB do estado onde o processo tramita:

| UF | Código CNJ (tribunal) | OAB do Mario | Tipo |
|----|----------------------|--------------|------|
| SP | 26 | OAB/SP nº 246.508 | principal |
| RJ | 19 | OAB/RJ nº 242.778 | suplementar |
| MG | 13 | OAB/MG nº 230.285 | suplementar |
| PR | 16 | OAB/PR nº 122.193 | suplementar |
| BA | 05 | OAB/BA nº 77.639  | suplementar |
| DF | 07 | OAB/DF nº 75.486  | suplementar |
| GO | 09 | OAB/GO nº 68.355  | suplementar |
| PE | 17 | OAB/PE nº 63.181  | suplementar |
| ES | 08 | OAB/ES nº 39.165  | suplementar |

**Se o processo for de um estado que não está nesta tabela** (ex.: SC, RS, CE, AM…), o Mario
não tem OAB cadastrada aqui. Não chute um número. Avise o usuário — "O processo é do [UF] e não
tenho a OAB do Mario nesse estado; me passa o número (ou confirmo se assina com a principal
OAB/SP)?" — e siga só depois da resposta.

## Como descobrir o estado do processo

Use as duas fontes e confira se batem:

1. **Número CNJ do processo** — formato `NNNNNNN-DD.AAAA.J.TR.OOOO`. Separando por pontos, o
   3º campo é o segmento da Justiça (`8` = Justiça Estadual) e o **4º campo é o código do
   tribunal (TR)**, que identifica o estado. Exemplo: em `5031775-08.2022.8.08.0024`, os campos
   são `[5031775-08] [2022] [8] [08] [0024]` → TR = `08` → **TJES → ES**.

   > Cuidado para não confundir o `TR` com o dígito verificador. No exemplo há dois "08": o
   > primeiro (logo após o hífen) é o verificador; o que vale é o **depois do `.8.`**.

   Tabela TR → UF (Justiça Estadual): 01 AC · 02 AL · 03 AP · 04 AM · 05 BA · 06 CE · 07 DF ·
   08 ES · 09 GO · 10 MA · 11 MT · 12 MS · 13 MG · 14 PA · 15 PB · 16 PR · 17 PE · 18 PI ·
   19 RJ · 20 RN · 21 RS · 22 RO · 23 RR · 24 SC · 25 SE · 26 SP · 27 TO.

2. **Comarca no cabeçalho** do documento (ex.: "Comarca de Vitória/ES") — confirma o estado.

Se o número CNJ e a comarca apontarem estados diferentes, **não adivinhe**: avise o usuário da
divergência e confirme qual é o estado correto antes de assinar.

## Regra da inscrição suplementar

- Se a UF for **SP**, o Mario assina com a inscrição principal e **não** se escreve "suplementar".
- Se a UF for **qualquer outra**, assina com a OAB daquele estado e a peça **identifica que é
  inscrição suplementar** — o escritório faz questão disso ("sempre identificar a suplementar").
  Coloque a observação no bloco de assinatura, assim:

  ```
  MARIO THADEU LEME DE BARROS FILHO
  OAB/ES nº 39.165 (inscrição suplementar)
  ```

  No pedido de publicações, mantenha a OAB do estado sem repetir a observação, para não poluir a
  frase: `... em nome de MARIO THADEU LEME DE BARROS FILHO (OAB/ES nº 39.165) ...`.

## Template da petição

Preencha os campos entre `[colchetes]` e remova qualquer trecho opcional que não se aplique.
O texto final vai sem colchetes.

```
EXCELENTÍSSIMO(A) SENHOR(A) DOUTOR(A) JUIZ(A) DE DIREITO DA [VARA OU JUIZADO] DA COMARCA DE [CIDADE]/[UF]


Autos nº [NÚMERO DO PROCESSO]


BARROS FILHO E ALMEIDA PRADO SOCIEDADE DE ADVOGADOS, neste ato representada por seus advogados infra-assinados, na qualidade de patrono de PICPAY INSTITUIÇÃO DE PAGAMENTO S.A, já qualificado e representado nos autos da ação em epígrafe, movida por [NOME DO AUTOR], igualmente qualificado, vem, em atenção [REFERÊNCIA DA INTIMAÇÃO], expor e requerer o que segue.

O Exequente, escritório de advocacia devidamente constituído por PicPay Instituição de Pagamento S.A., requer o levantamento dos valores [MOTIVO DO LEVANTAMENTO], mediante transferência para os seguintes dados bancários:

PICPAY INST DE PAGAMENTOS S.A
22.896.431/0001-10
Bradesco
Ag.: 2372
C.C.: 0033937-7

Por fim, requer-se ainda que as publicações ocorridas nestes autos sejam feitas em nome de MARIO THADEU LEME DE BARROS FILHO (OAB/[UF] nº [NÚMERO]), sob pena de nulidade.

Termos em que,
Pede deferimento.

São Paulo, [DATA ATUAL].


MARIO THADEU LEME DE BARROS FILHO
OAB/[UF] nº [NÚMERO][ (inscrição suplementar) — só quando a UF não for SP]
```

## Campos variáveis — como extrair do documento

- **[VARA OU JUIZADO] + [CIDADE]/[UF]** — copie fielmente do cabeçalho da intimação/decisão
  (ex.: "2º JUIZADO ESPECIAL CÍVEL", "Comarca de Vitória/ES"). Mantenha maiúsculas do original.
- **[NÚMERO DO PROCESSO]** — o número CNJ completo, com pontuação.
- **[NOME DO AUTOR]** — o autor da ação (a parte adversa do PicPay). Nos autos costuma aparecer
  como "movida por…", "autor:", "exequente:", "requerente:", "reclamante:".
- **[REFERÊNCIA DA INTIMAÇÃO]** — o ato ao qual a petição responde. Use a linguagem do próprio
  sistema/tribunal:
  - eproc / PJe: `ao Id. [número]` (ex.: "ao Id. 88497844");
  - Projudi (PR, GO, BA…): `ao mov. [número]` ou `à intimação de seq. [número]`;
  - ESAJ/e-SAJ (SP…): `à intimação de fls. [número]` ou `ao r. despacho de fls. [número]`;
  - se não houver um identificador claro: `à r. decisão que autorizou o levantamento dos valores`.
- **[MOTIVO DO LEVANTAMENTO]** — a natureza do valor a levantar, inferida do documento. Exemplos:
  - `pagos a maior` (quando o PicPay pagou em excesso e quer a devolução da diferença) — é o
    padrão do modelo;
  - `depositados nos autos` / `de titularidade do PicPay depositados nos autos`;
  - `objeto de restituição` / `remanescentes`.
  Se o valor exato constar e for útil, você pode acrescentar `, no valor de R$ [valor],`. Na
  dúvida entre motivos, mantenha o padrão do modelo (`pagos a maior`) ou pergunte em uma linha.

## Antes de entregar (checklist rápido)

Confirme, em silêncio, antes de mostrar a peça:

- A **UF da OAB** na assinatura e no pedido de publicações é a mesma do estado do processo?
- O **número da OAB** confere com a tabela para aquela UF?
- Se a UF **não for SP**, você escreveu `(inscrição suplementar)` no bloco de assinatura?
- Se a UF **for SP**, você **não** escreveu "suplementar"?
- O **nº do processo**, o **autor** e a **comarca** batem com o documento enviado?
- O **bloco bancário do PicPay** está exatamente como o padrão (CNPJ 22.896.431/0001-10)?
- A **data** é a de hoje, e o local é **São Paulo**?

Se algum item não fechar, resolva ou pergunte antes de entregar.

## Formato de saída

Entregue a petição **no chat, em Markdown**, dentro de um bloco de código (para o usuário copiar
sem quebrar a formatação), sem gerar arquivo `.docx`. Não escreva comentários no meio da peça.

Depois da petição, em uma ou duas linhas fora do bloco, registre as escolhas sensíveis para o
usuário conferir rápido — por exemplo: "Assinei com **OAB/ES nº 39.165 (suplementar)** porque o
processo é da comarca de Vitória/ES." Se você teve de assumir algo (motivo do levantamento,
data, estado sem OAB cadastrada), diga em uma linha o que assumiu, para ele validar.
