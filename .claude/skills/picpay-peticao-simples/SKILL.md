---
name: picpay-peticao-simples
description: >-
  Redige, na perspectiva do PicPay (réu), MANIFESTAÇÕES E PETIÇÕES SIMPLES do
  dia a dia, de forma ENXUTA e OBJETIVA, a partir da íntegra dos autos colada
  pelo usuário — entregando a peça pronta em Markdown no chat. Cobre:
  especificação de provas, ciência/nada a requerer, réplica simples,
  manifestação sobre documentos ou sobre proposta de acordo, interesse em
  audiência de conciliação, petição de juntada, dilação/devolução de prazo,
  reiteração de pedido e manifestação sobre cálculos. Use SEMPRE que o usuário
  subir os autos (ou colar o despacho) de processo contra o PicPay — PicPay
  Instituição de Pagamento, PicPay Bank ou Banco Original — e pedir peça curta:
  "faz a manifestação", "especifica as provas", "responde esse despacho", "dá
  ciência", "manifesta sobre os documentos", "pede dilação de prazo". NÃO use
  para peças robustas que têm skill própria (contestação, recurso inominado,
  embargos de declaração, cumprimento de liminar completo) nem para outras
  instituições.
---

# PicPay — Manifestações e Petições Simples

Esta skill é a **via rápida** da carteira PicPay: o usuário cola a íntegra dos
autos (ou só o despacho de intimação) e recebe, no chat, uma **manifestação
curta, direta e pronta para protocolo**. O objetivo é resolver em poucos
parágrafos o que o juízo pediu — sem teses longas, sem jurisprudência extensa,
sem floreio. Se o caso exigir profundidade (contestação completa, recurso,
embargos, cumprimento de liminar com discussão de multa), esta não é a skill —
veja "Quando NÃO usar" no fim.

## Princípio central: a peça nasce dos autos

A manifestação só vale se for **fiel ao que está nos autos**. Número do
processo, vara/juízo, comarca e UF, nome e qualificação do autor, o que
exatamente o despacho determinou, IDs/datas/protocolos eventualmente citados —
tudo precisa espelhar o que consta. **Nunca invente** um número de processo,
uma data, um protocolo, um documento que não foi juntado ou um prazo. Se um
dado essencial não estiver claro, **pergunte ao usuário** em vez de adivinhar.
Leia toda a íntegra (ou todo o despacho) antes de redigir.

## Passo 1 — Triagem (o que o juízo pediu?)

Identifique, lendo os autos:

1. **Qual o ato a responder** — leia o último despacho/decisão/intimação. É ele
   que define a peça. Sinais comuns: "especifiquem as provas", "manifeste-se
   sobre a contestação/documentos", "diga se tem interesse na audiência de
   conciliação", "manifeste-se sobre o cálculo", "ciência", "junte o
   instrumento".
2. **Quem assina (parte ré)** — PicPay Instituição de Pagamento S.A.
   (CNPJ 22.896.431/0001-10), PicPay Bank – Banco Múltiplo S.A. ou Banco
   Original S/A. Use a que figura no polo passivo. Em dúvida, pergunte.
3. **Rito e juízo** — Juizado Especial Cível ou Vara Cível; comarca/UF; número
   do processo (formato CNJ).
4. **Posição estratégica** — a defesa quer produzir prova, ou já quer o
   julgamento? Tem interesse no acordo/audiência, ou não? Isso muda o pedido
   final. Se o usuário não disser, adote o caminho mais seguro (ver cada modelo)
   e sinalize a alternativa em uma linha.

Mapeie o ato ao tipo de peça:

| O despacho/ato pede… | Peça (modelo em `references/modelos.md`) |
|---|---|
| Especifiquem as provas que pretendem produzir | **Especificação de provas** |
| Manifeste-se sobre a contestação (réplica) | **Réplica simples** |
| Manifeste-se sobre os documentos juntados | **Manifestação sobre documentos** |
| Diga se tem interesse na audiência de conciliação | **Interesse em audiência / acordo** |
| Manifeste-se sobre o cálculo / impugnação | **Manifestação sobre cálculos** |
| Apenas dê ciência / nada mais a requerer | **Ciência / nada a requerer** |
| Junte procuração, substabelecimento, carta de preposição, doc. | **Petição de juntada** |
| Reabertura/devolução/dilação de prazo | **Dilação ou devolução de prazo** |
| Reiterar pedido pendente de apreciação | **Reiteração de pedido** |

## Passo 2 — Redação enxuta

Padrão de estilo desta skill (é o que a diferencia das demais):

- **Curta.** A maioria destas peças cabe em meia a uma página. Vá direto ao que
  o juízo pediu.
- **Objetiva.** Uma ideia por parágrafo. Sem "data venia" empilhado, sem
  citação de doutrina, sem ementas longas. No máximo um dispositivo legal quando
  ele for o fundamento direto (ex.: art. 357 do CPC na especificação de provas).
- **Sem inventar.** Só afirme o que os autos sustentam.
- **Tom humano e técnico.** Português jurídico limpo, sem travessões decorativos
  nem vícios de IA; frases de tamanho variado.

## Estrutura padrão da manifestação

Use este esqueleto e enxugue conforme o caso:

```
EXCELENTÍSSIMO(A) SENHOR(A) DOUTOR(A) JUIZ(A) DE DIREITO DA [vara] DA COMARCA
DE [comarca]/[UF]   <- ou "do Juizado Especial Cível de..."

Processo nº [número CNJ]

[PARTE RÉ — ex.: PICPAY INSTITUIÇÃO DE PAGAMENTO S.A.], já qualificada nos
autos da ação em epígrafe que lhe move [NOME DO AUTOR], vem, respeitosamente,
à presença de Vossa Excelência, em atenção ao r. despacho de [ID/fls.],
expor e requerer o que segue.

[1 a 4 parágrafos objetivos — o conteúdo da manifestação]

Ante o exposto, requer [o pedido — curto e claro].

Termos em que pede deferimento.
[Comarca/UF], [data].

[Advogado(a)] — OAB/[UF] nº [...]
```

Quando o usuário não informar data, OAB ou nome do subscritor, deixe o campo
entre colchetes para ele preencher — não invente.

## Detalhe sobre os tipos mais frequentes

Os esqueletos completos estão em `references/modelos.md`. Pontos de atenção:

- **Especificação de provas:** especifique de verdade e justifique a pertinência
  (não basta "protesta por todas as provas"). Se a defesa já tem tudo nos autos
  e interessa o desfecho rápido, requeira o **julgamento antecipado** (art. 355
  do CPC) e, por cautela, ressalve interesse em prova caso o juízo entenda
  necessária — evita preclusão. Se for produzir prova, indique qual (documental
  nova, testemunhal com rol no momento oportuno, depoimento pessoal do autor,
  pericial com objeto definido) e por quê.
- **Interesse em audiência/acordo:** alinhe-se à política da carteira. Se não
  houver autorização/proposta concreta, manifeste interesse na tentativa de
  conciliação **sem vincular valor**, ou informe a ausência de proposta no
  momento — nunca ofereça valor por conta própria.
- **Réplica simples:** rebata em poucos parágrafos os pontos novos da
  contestação que mereçam resposta e reafirme os pedidos da inicial; não reescreva
  a inicial inteira.
- **Manifestação sobre cálculos:** se concorda, diga que nada há a impugnar; se
  discorda, aponte objetivamente o erro (índice, marco inicial de correção/juros,
  dobra indevida) — sem refazer a conta por extenso, salvo se o usuário pedir.
- **Dilação/devolução de prazo:** fundamente brevemente (necessidade de obter
  subsídios/documentos internos, força maior, etc.) e peça prazo determinado.

## Regras de ouro

- Não prometa providência que não consta nos autos nem afirme cumprimento sem
  documento.
- Não cite jurisprudência ou doutrina nesta skill — se o caso pede isso, é peça
  robusta (veja abaixo).
- Cite o ID/fls. do despacho que está sendo respondido.
- Em caso de litisconsórcio (ex.: PicPay Bank + Banco Original), subscreva pela
  entidade correta ou por ambas, conforme os autos.
- Confirme o prazo: a maioria dessas intimações é de **5 dias úteis** (art. 218
  e 219 do CPC), mas vale o que constar no despacho — se relevante, lembre o
  usuário de conferir a data de publicação.

## Quando NÃO usar (encaminhe para a skill certa)

- Contestação -> **picpay-contestacao**
- Recurso inominado / razões recursais -> **picpay-recurso-inominado**
- Embargos de declaração -> **picpay-embargos-declaracao**
- Cumprimento de liminar completo, com demonstração documental e afastamento de
  astreintes -> **picpay-cumprimento-liminar**
- Decisão sobre recorrer/dispensar, requisições no Projuris, cadastro, prazos no
  Astrea, cálculo de liquidação -> skills próprias da carteira.

Se, ao ler os autos, perceber que o caso é robusto demais para uma manifestação
simples (ex.: contestação inteira, multa diária em discussão séria), avise o
usuário em uma linha e sugira a skill adequada — mas, se ele só quer a versão
curta, entregue a versão curta.
