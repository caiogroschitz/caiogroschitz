---
name: indagacao-recursal-bfap
description: >-
  Lê a íntegra dos autos de um processo da carteira BFAP (PicPay Instituição de
  Pagamento, PicPay Bank ou Banco Original) e redige, direto no chat, a INDAGAÇÃO
  RECURSAL, o one-pager que o escritório envia ao Jurídico Interno resumindo
  inicial, contestação, dossiê e sentença, e concluindo, à luz das Diretrizes
  Recursais, se cabe recorrer ou dispensar, com prazos de ED e de Recurso
  Inominado/Apelação e estimativa de custas recursais. Use SEMPRE que o usuário
  enviar/colar os autos de um caso BFAP e pedir para "fazer/preencher/montar a
  indagação recursal", "analisa os autos e diz se recorre", "vê se cabe recurso e
  me dá os prazos", "faz o resumo recursal pro jurídico", ou colar uma sentença
  BFAP esperando o parecer de recorribilidade nesse formato. Também aciona com
  "indagação recursal", "indagação de recurso", "preenche a indagação do
  Original/PicPay". NÃO use para redigir as razões do recurso em si, para o
  cadastro da requisição no Projuris (skill picpay-requisicoes-projuris) nem para
  cálculo de liquidação.
---

# Indagação Recursal, BFAP (PicPay e Banco Original)

A Indagação Recursal é o one-pager que o escritório (BFAP) submete ao Jurídico Interno do
cliente para indicar, em um só lugar, o que o caso é e se vale a pena recorrer. Ela condensa os
quatro resumos do processo, traz o Parecer do Escritório (recorrer ou dispensar, com o racional
e o principal risco) e fecha com os prazos e o custo do recurso. Não é a peça recursal: é a
recomendação fundamentada que autoriza ou dispensa a peça.

Seu trabalho: ler a íntegra dos autos, identificar o réu BFAP, decidir internamente pela leitura
das Diretrizes e entregar a indagação pronta, sem devolver "confirmar" para o usuário. Você
deduz tudo dos autos.

## A indagação é uma comunicação com o cliente

Quem lê é o Jurídico Interno do banco. O texto precisa soar como um advogado experiente
escreveu, com prosa corrida, sóbria e profissional. Duas regras valem para tudo que sai:

**Não exponha o vocabulário interno de decisão.** Os critérios das Diretrizes servem para você
decidir, mas não entram no texto. Nunca escreva no parecer expressões como "regra de ouro",
"gatilho obrigatório", "hipótese de dispensa", "análise conjunta", "tabela de dano moral por
UF", "item 1.2.1", nem percentuais do tipo "custas representam 13% da condenação". Traduza o
raciocínio para argumento jurídico corrente: equívoco na valoração probatória, reconhecimento da
obrigação, exercício regular de direito, economicidade do recurso, jurisprudência consolidada.

**Escreva como gente, não como IA.** Sem travessão (—); onde ele apareceria, use vírgula, ponto
ou dois-pontos. Evite o reframe "não é só X, é Y", os conectivos repetidos em série ("ademais",
"outrossim", "cabe destacar" a cada frase) e o corporativês inflado (alavancar, robusto,
otimizar). Prefira o verbo simples e a frase direta, variando o ritmo. O alvo é o registro do
seu modelo: argumento limpo, encadeado, sem floreio.

## Passo 1, ler os autos e identificar o réu

Leia inicial, emenda (se houver), contestação, dossiê/subsídios e a sentença. Identifique qual
réu BFAP figura no polo passivo, porque isso orienta o dossiê e o parecer:

- PicPay Instituição de Pagamento S.A. ou PicPay Bank Banco Múltiplo S.A.: conta de pagamento,
  PicPay Card, empréstimo (CCB), Pix, antecipação salarial.
- Banco Original: empréstimo pessoal, renegociações sucessivas, cartão, financiamento.

Capte o órgão e a UF, porque definem prazo, recurso e custas. JEC (Juizado Especial Cível): o
recurso é Recurso Inominado. Vara Cível (Justiça Comum): o recurso é Apelação.

## Passo 2, decidir recorrer ou dispensar (raciocínio interno)

Esta etapa é interna. Você usa as Diretrizes Recursais BFAP para chegar à conclusão, mas o
vocabulário delas não aparece no texto (ver a seção acima). O resumo operacional dos critérios
está em `references/diretrizes-resumo.md`; consulte antes de concluir. O que mais decide os casos
BFAP:

- Provas e subsídios favoráveis (biometria aprovada, contrato ou CCB assinado, renegociações que
  reconhecem a dívida, transações para conta de própria titularidade) puxam para recorrer.
- Custas recursais altas frente à condenação (a partir de cerca de 70% do total) puxam para
  dispensar, por economicidade.
- Dano moral acima da média da UF e do órgão (tabela no resumo) puxa para recorrer; abaixo da
  média, isoladamente, aponta dispensa, mas pondere com o impacto econômico das demais verbas e
  com o custo do recurso.
- Súmula 385/STJ (negativação anterior legítima) e Súmula 479/STJ (fortuito interno) costumam ser
  o eixo desses casos; verifique em que pé a sentença os deixou.
- Obrigação de fazer já cumprida no prazo, sem multa, em regra dispensa o recurso, porque o foco
  passa a ser encerrar.

Pese os fatores em conjunto. Havendo tensão (por exemplo, prova favorável mas custas altas) ou
padrão regional anômalo de condenações, conclua pela abertura de requisição de análise recursal
para validação do Jurídico Interno, e diga isso no parecer em linguagem corrente.

## Passo 3, calcular prazos e custas

Prazos em dias úteis (arts. 219 e 224 do CPC, exclui o dia do começo e conta a partir do primeiro
dia útil seguinte à intimação):

- Recurso Inominado (JEC): 10 dias úteis.
- Apelação (Vara Cível): 15 dias úteis.
- Embargos de Declaração: 5 dias úteis.

Conte a partir da intimação ou publicação da decisão recorrida que constar nos autos. Se a
publicação não estiver nos autos, a decisão ainda não foi publicada: registre que o prazo ainda
não começou a correr e que o fatal será contado da futura publicação. Nunca escreva "confirmar a
data".

Custas e preparo: sempre estime uma faixa, com a base de cálculo (tabela do TJ local). No JEC
(Recurso Inominado), o preparo soma as custas de 1º grau (não pagas no Juizado) e as custas
recursais; em causas de cerca de R$ 15 mil a R$ 50 mil costuma ficar em torno de R$ 1.300 a
R$ 1.950. Na Vara Cível (Apelação), as custas iniciais já foram pagas no ajuizamento, e o preparo
recursal é só o percentual recursal sobre o valor do pedido, com o piso do TJ. Apresente a faixa;
o valor exato sai na guia.

Risco recursal: em regra, registre o risco de honorários. No JEC, recurso improvido implica
condenação do recorrente em custas e honorários (10% a 20%, art. 55 da Lei 9.099/95). No texto,
porém, mencione o risco de forma corrente, como no modelo: "o principal risco recursal consiste
na fixação de honorários sucumbenciais em caso de manutenção da sentença pela Turma Recursal".
Não despeje a citação do artigo nem o percentual no parecer; isso é fundamentação interna.

## Passo 4, redigir a Indagação Recursal

Entregue nesta estrutura e ordem, preenchendo cada campo a partir dos autos. Datas em DD/MM/AAAA;
valores em R$. Os quatro resumos são objetivos e descritivos. O Parecer do Escritório é prosa
corrida argumentativa, no registro do modelo.

```
RESUMO DA INICIAL: <o que o autor alega e o contexto do débito ou da negativação, em poucas linhas>

RESUMO DA CONTESTAÇÃO: <as teses centrais da defesa do réu BFAP: preliminares, mérito, excludentes, súmulas invocadas>

RESUMO DO DOSSIÊ: <subsídios e provas do réu, encadeados: contratação, datas, renegociações, biometria, evolução da dívida, saldo devedor, legitimidade da negativação>

RESUMO DA SENTENÇA: <o que foi julgado procedente ou improcedente; o fundamento do juízo (documentos reputados unilaterais, Súmula 385 ou 479); o que foi declarado, condenado ou afastado>

PARECER DO ESCRITÓRIO: <prosa corrida. Abra com a recomendação direta ("Sugerimos a interposição de recurso inominado" ou "Sugerimos a dispensa recursal"). Em seguida, o porquê em argumento jurídico corrente: o que a sentença reconheceu, o que o dossiê demonstra em contrário, e por que há fundamentos para a reforma (ou por que não compensa recorrer). Sem jargão interno das Diretrizes. Feche com o principal risco recursal, em regra a fixação de honorários sucumbenciais em caso de manutenção pela Turma Recursal ou Tribunal.>

Valor da condenação atualizada até DD/MM/AAAA: <total das verbas pecuniárias, ou "Somente OBF" quando não houver condenação a pagar>

Embargos de Declaração: <opinião pela oposição ou não oposição, fundamentada. ED só cabe com omissão, contradição, obscuridade ou erro material; sem vício, não opor>

Prazo de ED: DD/MM/AAAA <ou "não iniciado, pendente de publicação da sentença">

Prazo Recursal - RI: DD/MM/AAAA <ou "Apelação", conforme o órgão; ou "não iniciado, pendente de publicação">

Valor médio das custas recursais: R$ <faixa ou valor estimado>
```

### Notas de preenchimento

- RESUMO DA CONTESTAÇÃO existe porque o réu BFAP já se defendeu. Sintetize as teses efetivamente
  arguidas; não invente preliminares que não constam.
- Valor da condenação: some todas as verbas pecuniárias (restituição, em dobro quando for o caso,
  dano moral, multa). Se a procedência for só obrigação de fazer (por exemplo, exclusão de
  negativação) sem pagar nada, escreva "Somente OBF", como 