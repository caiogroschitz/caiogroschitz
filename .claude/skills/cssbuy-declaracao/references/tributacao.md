# Tributação, penalidades e liberação — remessas internacionais para o Brasil

Referência para consulta quando o usuário perguntar quanto vai pagar, por que foi taxado, o que acontece se o pacote for retido, ou o que muda nas regras.

## Índice

1. Situação da CSSBUY perante o Remessa Conforme
2. Alíquotas vigentes
3. Alíquota de ICMS por estado
4. Fórmula de cálculo
5. O que muda em 12/05/2026
6. Casos realmente desonerados
7. Itens proibidos e restritos
8. Infrações e penalidades
9. Como o tributo é pago e quais os prazos
10. O que não funciona (mitos)

---

## 1. Situação da CSSBUY perante o Remessa Conforme

A CSSBUY é um **agente de compras** (shipping agent) sediado em Hong Kong, não uma plataforma de e-commerce certificada no **Programa Remessa Conforme (PRC)** da Receita Federal.

Consequência prática: **nenhuma remessa da CSSBUY tem direito à faixa de alíquota zero abaixo de US$ 50 nem ao desconto de US$ 30 acima disso.** Toda remessa dela é tributada na alíquota cheia, e o tributo é cobrado na chegada ao Brasil, não no checkout.

Isso muda toda a estratégia de custo: como não existe degrau de valor, **dividir o pacote não reduz alíquota**. O único lugar onde ainda dá para economizar de forma legítima é na base de cálculo — peso, frete e seguro.

## 2. Alíquotas vigentes

| Origem | Faixa | Imposto de Importação | ICMS |
|---|---|---|---|
| Site certificado no PRC | US$ 0,01 – 50,00 | 0% | 17% a 20% |
| Site certificado no PRC | US$ 50,01 – 3.000 | 60% com desconto de US$ 30 | 17% a 20% |
| **Fora do PRC (caso da CSSBUY)** | **US$ 0,01 – 3.000** | **60%, sem desconto** | **17% a 20%** |

Acima de US$ 3.000 a remessa sai do regime de tributação simplificada e passa a exigir despacho de importação comum — outro processo, com outros custos.

## 3. Alíquota de ICMS por estado

O Convênio ICMS 81/2023 uniformizou a alíquota de remessas internacionais em **17%**. Em 2025, dez estados elevaram para **20%**: Alagoas, Bahia, Ceará, Maranhão, Paraíba, Pernambuco, Piauí, Rio Grande do Norte, Sergipe e Tocantins.

**São Paulo permanece em 17%** para remessas internacionais. (Cuidado com fontes que citam 18% — 18% é a alíquota interna geral de SP, não a de remessa internacional.)

Se o usuário for de um dos dez estados acima, use 20% e recalcule: a carga efetiva sobe de ~92,8% para 100% do valor aduaneiro.

## 4. Fórmula de cálculo

```
VA   = valor do produto + frete internacional + seguro
II   = VA × 0,60
ICMS = (VA + II) ÷ (1 − a) × a          onde a = 0,17 ou 0,20
```

O ICMS é calculado **por dentro** (o próprio imposto compõe sua base), e é daí que veio a polêmica do "imposto de 92%".

**Multiplicadores de custo total desembarcado:**

| ICMS | Total = VA × |
|---|---|
| 17% | **1,9277** |
| 20% | **2,0000** |

A conversão para reais usa a taxa de câmbio da data de **registro da Declaração de Importação de Remessa**, não a da data da compra.

**Leitura prática:** com ICMS de 17%, cada US$ 1 economizado em frete ou seguro devolve **US$ 1,93** ao bolso. Cortar US$ 20 de frete tirando caixas de tênis vale US$ 38,55.

## 5. O que muda em 12/05/2026

As regras valem para Declarações de Importação registradas a partir de **12/05/2026**:

| Origem | Faixa | Imposto de Importação |
|---|---|---|
| Certificado no PRC | US$ 0,01 – 50 | 0% |
| Certificado no PRC | US$ 50,01 – 3.000 | 60% com desconto de US$ 30 |
| Fora do PRC | US$ 0,01 – 3.000 | 60%, sem desconto |

Para quem compra pela CSSBUY, **nada muda na prática** — a alíquota fora do PRC continua sendo 60% cheia em toda a faixa. As mudanças beneficiam apenas plataformas certificadas.

## 6. Casos realmente desonerados

Casos concretos, não brechas:

- **Medicamentos** para uso próprio de pessoa física: alíquota zero de II até US$ 10.000, com condições específicas.
- **Livros, jornais, periódicos e o papel destinado à sua impressão**: imunidade tributária constitucional (art. 150, VI, "d", da CF). Não pagam II nem ICMS.

Fora disso, para remessa fora do PRC, não existe faixa isenta.

## 7. Itens proibidos e restritos

Hipóteses expressas de perdimento ou de recusa pela transportadora:

- **bens com marca falsificada** (contrafação) — a hipótese mais relevante para quem compra via agente chinês;
- máquinas eletrônicas programadas para jogos de azar, videoloteria;
- produtos que imitam cigarros;
- bens ofensivos à moral, à ordem pública ou à saúde;
- mercadoria oculta em fundo falso ou deliberadamente encoberta.

Restrições operacionais de transporte (variam por rota — a CSSBUY sinaliza com ícone):

líquidos · pós · aerossóis · perfumes · baterias de lítio avulsas · alimentos · sementes · medicamentos sem prescrição · produtos magnéticos · isqueiros.

Itens com bateria embutida exigem rota específica (a CSSBUY tem linhas dedicadas, como as `Battery-line`). Enviar por rota comum resulta em devolução ou descarte.

## 8. Infrações e penalidades

Do manual de Remessas Postal e Expressa da Receita Federal:

| Infração | Penalidade |
|---|---|
| Preço declarado diferente do arbitrado ou do efetivamente praticado | **Multa de 100% sobre a diferença** |
| Falta ou inexatidão de declaração | **75%** sobre a diferença de II (redutível a 50%); mínimo R$ 500; teto de 10% do valor total da encomenda |
| Declaração incompleta (dados administrativos/comerciais imprecisos) | **1%** sobre o valor aduaneiro |
| Falsa declaração de conteúdo | **Perdimento** dos bens |
| Mercadoria oculta / fundo falso | **Perdimento** |
| Fracionamento para escapar de tributo | **Perdimento** |
| Mercadoria não retirada em 60 dias após liberação ou exigência | **Perdimento por abandono** |

Bens apreendidos são destruídos, doados, leiloados ou incorporados ao patrimônio público. Cabe pedido de conversão do perdimento em multa, a critério da autoridade.

Vale registrar, para calibrar o risco sem exagero: há jurisprudência (STJ e TRFs) no sentido de que **subfaturamento isolado**, sem falsidade documental, comporta multa e não perdimento — a Súmula 138 do antigo TFR vai nessa linha. Mas essa é uma tese que se sustenta **depois** da apreensão, com advogado, tempo e custo, e não se aplica quando há documento falso ou descrição falsa junto. Não é planejamento; é litígio.

## 9. Como o tributo é pago e quais os prazos

**Via Correios** (rotas China Post, SAL, EMS):

1. O pacote chega, é submetido à triagem aduaneira e o tributo é lançado.
2. O destinatário recebe aviso (app Correios, e-mail ou SMS) com o valor.
3. Pagamento pelo site "Minhas Importações" dos Correios ou na agência, com CPF do destinatário.
4. Sobre o tributo incide ainda a **taxa de despacho postal dos Correios** (cerca de R$ 15).
5. Após pagamento, o pacote segue para entrega.
6. **Prazo:** não retirar/pagar dentro de 60 dias caracteriza abandono → perdimento.

**Via courier** (rotas expressas privadas):

1. O courier faz o desembaraço e cobra o tributo do destinatário antes da entrega.
2. Costuma haver taxa administrativa de desembaraço, além do tributo.
3. O prazo é definido pelo courier e costuma ser mais curto que o dos Correios; ignorar o aviso normalmente resulta em devolução ao remetente.

**Se discordar do valor lançado:** cabe pedido de revisão junto à Receita Federal, com apresentação da fatura e do comprovante de pagamento. Ter a declaração batendo com o extrato do cartão é o que faz esse pedido funcionar — mais um motivo para o valor declarado ser o valor real.

## 10. O que não funciona (mitos)

- **"Dividir em vários pacotes menores evita a taxa."** Fora do PRC não há degrau de valor: 60% incide igual em qualquer faixa. E fracionar com intuito de escapar de tributo é hipótese expressa de perdimento. Risco alto, benefício zero.
- **"Abaixo de US$ 50 é isento."** Só em site certificado no PRC. A CSSBUY não é.
- **"Marcar como presente isenta."** A antiga isenção de US$ 50 para presentes entre pessoas físicas não alcança compra de mercadoria, e declarar compra como presente é falsa declaração de conteúdo.
- **"Escolher rota mais barata sempre sai melhor."** Frete entra na base de cálculo, então rota barata realmente economiza — mas prazo, rastreio e índice de extravio da rota também contam. Compare pelo total desembarcado e pelo risco, não só pelo número do frete.
- **"Se não declarar nada, passa."** Declaração ausente ou vaga é o gatilho clássico de exigência fiscal: o pacote é aberto, o valor é arbitrado pela Receita — normalmente acima do que foi pago — e o tributo incide sobre o valor arbitrado.
