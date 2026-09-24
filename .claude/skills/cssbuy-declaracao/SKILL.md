---
name: cssbuy-declaracao
description: Preenche a Fatura de Declaração (Declaration Invoice) da CSSBUY para envios ao Brasil, escrevendo cada item com descrição genérica e correta — tipo de produto, material, cor, tamanho, quantidade e o valor realmente pago — sem nome de marca, porque marca não é campo exigido. Também calcula o imposto esperado (II 60% + ICMS) e roda o checklist anti-retenção antes do pagamento. Use SEMPRE que o usuário mencionar CSSBUY, CSS Buy, "enviar pacote", "submit parcel", "fatura de declaração", "declaration invoice", "como declarar", "o que escrever na declaração", "vou fechar meu haul", "shipping da CSS", agente chinês, ou compras de Taobao/Weidian/1688 via agente. Também aciona quando o usuário manda print ou screenshot da tela de envio da CSSBUY pedindo ajuda para preencher, e em perguntas como "quanto vou pagar de imposto nesse pacote", "qual rota de envio escolher", "meu pacote vai ser taxado" e "como não ficar retido na alfândega".
---

# CSSBUY — Fatura de Declaração para o Brasil

Esta skill preenche a **Fatura de Declaração** da CSSBUY (tela "Enviar pacote" → seção "Fatura de Declaração" → "Pedidos de compra") com linhas enxutas, corretas e genéricas, e devolve uma tabela pronta para o usuário copiar campo a campo.

## O que esta skill faz — e o limite dela

O objetivo é uma declaração **verdadeira, completa e sem ruído**: descrição que identifica a mercadoria, valor igual ao que foi realmente pago, quantidade certa. Declaração assim é a que passa sem retenção, sem exigência fiscal e sem multa.

O que esta skill **não** faz, em nenhuma hipótese: reduzir valores, inventar preços, dividir o pacote para fugir de tributo, ou descrever o conteúdo como coisa diferente do que é. Não é preciosismo — é o que decide se o pacote chega. Pelo manual de Remessas Postal e Expressa da Receita Federal:

- preço declarado diferente do praticado → **multa de 100% sobre a diferença**;
- falsa declaração de conteúdo → **pena de perdimento** (o pacote é confiscado; o usuário perde a mercadoria, o frete e o dinheiro do produto);
- fracionar compras em várias remessas para escapar de tributo → **perdimento**.

Se o usuário pedir para subdeclarar, recuse essa parte especificamente, explique o risco em uma ou duas frases e siga preenchendo o resto corretamente. Não moralize nem repita o aviso a cada linha.

**Réplicas:** boa parte do que se compra via agente chinês é réplica. Descrição genérica não torna a importação legal — bens com marca falsificada são hipótese de perdimento independentemente de como forem descritos. Diga isso uma vez, de forma neutra, se o caso aparecer, e siga em frente. A decisão é do usuário.

## Por que descrição sem marca é o padrão correto, não um truque

Os campos que a CSSBUY pede são: **Atributos · Cor, Tamanho · Material · Produto · Quantidade · Preço total (USD)**. Não existe campo de marca. Os próprios exemplos da CSSBUY são genéricos: *"Mouse óptico sem fio RT200 preto plástico PVC"*, *"Tênis de couro azul masculino tamanho 42"*.

Isso casa com o que a aduana precisa: uma descrição que permita **identificar e classificar** a mercadoria — o que é, de que material, para que serve, quanto tem, quanto custou. Nome de marca não entra nessa lista. E declarar uma marca que o produto não carrega seria, aí sim, declaração inexata.

Então a regra é simples: descreva o objeto, não a etiqueta.

## Fluxo de trabalho

1. **Levante os itens.** Se o usuário mandou print da tela de envio, leia os produtos, variantes, quantidades e preços dali. Se mandou links ou uma lista, use o que ele deu. Quando faltar material ou cor, pergunte — chutar material é o erro que mais gera exigência fiscal.
2. **Escreva uma linha por item.** Uma linha por SKU/variante, não uma linha por pacote.
3. **Confira a soma.** O total das linhas precisa bater com o "Valor do pacote" que a CSSBUY mostra. Se não bater, algum item ficou de fora ou a quantidade está errada.
4. **CPF.** Só números, sem ponto ou traço, e obrigatoriamente o CPF do destinatário do endereço de entrega. CPF divergente do nome no endereço é motivo comum de retenção.
5. **Calcule o imposto esperado** (seção abaixo) para o usuário não tomar susto na entrega.
6. **Rode o checklist anti-retenção.**
7. **Entregue a tabela pronta para copiar.**

## Como escrever cada linha

A própria CSSBUY define o formato na dica abaixo da tabela:

> *O conteúdo inserido inclui: nome do produto (modelo), cor, tamanho, material (cada atributo separado por um espaço)*
> *Dicas: 1. Mouse óptico sem fio RT200 preto plástico PVC — 2. Tênis de couro azul masculino tamanho 42*

Repare no que os exemplos dela mostram: **uma frase corrida, atributos separados só por espaço, sem vírgula, sem barra, sem parênteses — e sem marca nenhuma.** "Tênis de couro azul masculino tamanho 42" é exatamente o padrão a seguir. Não invente formatação própria; o campo é lido por sistema.

**Fórmula do campo Produto:**

```
[tipo do objeto] [material] [cor] [gênero/uso] [tamanho]
```

Tudo em português, numa linha só, separado por espaço. Exemplo: `Moletom com capuz de algodão preto masculino tamanho M`.

**Campo a campo:**

| Campo | O que colocar | Erro comum |
|---|---|---|
| Atributos | Deixe vazio, ou o atributo do anúncio já traduzido (ex.: `algodão 80%`) | Colar o texto chinês original |
| Cor, Tamanho | `Preto L`, `Branco 40` — espaço, não vírgula | Deixar em branco quando a peça tem numeração |
| Material | O material real e principal: `couro`, `algodão`, `poliéster`, `nylon`, `borracha` | `misto`, `vários`, ou vazio |
| Produto | A frase da fórmula acima | Marca, modelo de marca, sigla de release |
| Quantidade | Unidades daquela variante | Somar variantes diferentes numa linha só |
| Preço total (USD) | Preço realmente pago **pela linha inteira** (unitário × quantidade) | Colocar o unitário quando a quantidade é maior que 1 |

Sim, material e cor/tamanho aparecem duas vezes — nos campos próprios e dentro da frase do Produto. É assim que a CSSBUY pede, e os exemplos dela confirmam. Repetir é o comportamento correto.

**Nunca escreva nestes campos:** nome de marca ou submarca, nome de modelo comercial, código de release, e as gírias de réplica — `OG`, `批次`, `版本`, `rep`, `LJR`, `PK`, `batch`, `retail`. Além de não serem campo exigido, esse vocabulário é justamente o que sinaliza contrafação numa triagem.

**Exemplos de conversão:**

| Anúncio original | Produto | Material | Cor, Tamanho |
|---|---|---|---|
| `OG版本乔4系列全套原纸板橙檀头 开发 原厂皮料加持` (tênis, 37.5) | `Tênis de couro branco e azul masculino tamanho 37.5` | `couro` | `Branco e azul 37.5` |
| `R91681-H67 黑色 L` (jaqueta) | `Jaqueta de poliéster preta masculina tamanho L` | `poliéster` | `Preto L` |
| `背叉爱抚二车黑色帽衫12630451` (moletom) | `Moletom com capuz de algodão preto masculino tamanho M` | `algodão` | `Preto M` |
| `前司图申白灰色帽衫123101159` (moletom) | `Moletom com capuz de algodão branco e cinza masculino tamanho L` | `algodão` | `Branco e cinza L` |

Para mais categorias (calças, camisetas, bonés, bolsas, acessórios, eletrônicos) e vocabulário de materiais em chinês, leia `references/descricoes.md`.

## Cálculo do imposto esperado

A CSSBUY **não** é certificada no Programa Remessa Conforme. Por isso não existe faixa isenta abaixo de US$ 50 — toda remessa dela cai na alíquota cheia.

```
Valor Aduaneiro (VA) = produto + frete internacional + seguro
Imposto de Importação = VA × 60%
ICMS (por dentro)     = (VA + II) ÷ (1 − alíquota) × alíquota
```

O ICMS é calculado "por dentro" (gross-up), e é por isso que a carga efetiva bate em ~92% do valor aduaneiro, não 77%.

**Alíquota de ICMS:** 17% pelo Convênio ICMS 81/2023, que uniformizou a alíquota de remessas internacionais. Dez estados (quase todos do Nordeste) subiram para 20% em 2025. **São Paulo continua em 17%** para remessas internacionais. Se o usuário for de outro estado, pergunte antes de calcular.

Com 17%, a conta fecha em **VA × 1,9277** de custo total desembarcado. Ou seja: **cada US$ 1 de frete ou seguro custa ~US$ 1,93 no fim.** É por isso que reduzir peso vale muito mais do que parece.

**Exemplo real** (o pacote do print de referência):

```
Produto  $163,43
Frete     $77,19
Seguro    $14,44
VA       $255,06
II (60%) $153,04
ICMS     $ 83,62   ← (255,06 + 153,04) ÷ 0,83 × 0,17
Tributos $236,66
Total    $491,72  + taxas de serviço da CSSBUY
```

Apresente sempre o total desembarcado, não só o tributo. O usuário precisa ver o número que vai sair do bolso.

## Checklist antes de clicar em Pagamento

- **Peso:** desmarcar "com caixa" nos tênis. No pacote de exemplo, um par cai de 1,37 kg para 965 g. Menos peso → menos frete → **menos base de cálculo**, duas economias no mesmo movimento. Use "Remover caixas" e "Remover sacolas plásticas" (grátis).
- **Seguro:** ele entra na base tributável e é multiplicado por 1,93 no fim. Vale para pacote caro e rota lenta; não vale por reflexo.
- **Rota:** compare pelo **custo total desembarcado**, não pelo frete. Uma rota US$ 30 mais barata economiza ~US$ 58 no final.
- **Serviços de valor agregado:** "Imprimir e colar uma fatura" (US$ 0,15) é barato e reduz chance de divergência entre a fatura física e a declaração eletrônica. Vale marcar.
- **Itens proibidos:** líquidos, pó, baterias avulsas, aerossóis, perfumes, alimentos, réplicas de marca. A própria CSSBUY marca esses itens com ícone de restrição — respeite.
- **CPF:** só números, igual ao titular do endereço.
- **Teto:** US$ 3.000 por remessa no regime simplificado. Acima disso, muda o regime inteiro.
- **Não fracione:** dividir um mesmo haul em vários pacotes para escapar de tributo é hipótese expressa de perdimento — e, como a CSSBUY não é certificada, dividir **não reduz alíquota nenhuma**. É risco puro sem benefício.

## Formato de saída

Entregue nesta ordem, sem preâmbulo:

**1. Tabela pronta para colar** — uma linha por item, colunas na mesma ordem do site (Atributos · Cor, Tamanho · Material · Produto · Quantidade · Preço total), com o total conferido embaixo.

**2. CPF** — formatado como o site aceita.

**3. Custo estimado** — VA, II, ICMS, tributos, total desembarcado, por rota se o usuário estiver em dúvida entre rotas.

**4. Alertas** — só se houver algo concreto: item restrito no pacote, soma que não fecha, material faltando, peso que dá para cortar. Se não houver, não invente seção de alerta.

## Referências

- `references/descricoes.md` — biblioteca de descrições genéricas por categoria e glossário de materiais em chinês
- `references/tributacao.md` — alíquotas vigentes, o que muda em 12/05/2026, itens proibidos, infrações e penalidades, e o passo a passo do pagamento do tributo no Brasil
