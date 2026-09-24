---
name: "picpay-pedido-subsidios"
description: "Lê a íntegra dos autos de um processo da carteira PicPay (BFAP) e redige o PEDIDO DE SUBSÍDIOS interno — resumo objetivo da demanda, campos de identificação (autor/CPF, liminar, audiência, prazo, citação, valor da causa), classificação em Causa raiz 1 e 2, e a lista de documentos a solicitar conforme a matriz do escritório, no formato EXATO da planilha de subsídios. Use SEMPRE que o usuário colar o teor dos autos (ou anexar a inicial/decisões) e pedir para \"fazer o subsídio\", \"elaborar o pedido de subsídios\", \"montar o dossiê\", \"pedir os subsídios desse caso\", \"analisa os autos e faz o subsídio\", \"qual a causa raiz e o que pedir\", ou variações. Também aciona quando o usuário cola uma petição inicial do PicPay pedindo o resumo + documentos a requisitar. NÃO use para abrir a requisição em si no Projuris (use picpay-requisicoes-projuris), redigir contestação/recurso, decidir recurso, nem cálculo de liquidação."
---

# PicPay — Pedido de Subsídios

Esta skill transforma a íntegra dos autos em um **pedido de subsídios** interno: um texto curto que (1) resume objetivamente a ação, (2) preenche os campos de identificação, (3) classifica a causa raiz e (4) indaga os documentos certos para montar o dossiê de defesa do PicPay.

O destinatário do texto é o time interno que vai buscar os documentos. Por isso o texto é técnico, direto e enxuto. Você **não** redige defesa, não antecipa tese de mérito e não faz contestação. Apenas resume e pede os subsídios corretos.

O usuário desta skill é **Caio Groschitz**, que só elabora subsídios dos casos da própria carteira (ver "Triagem" abaixo).

## Princípio fundamental: nunca inventar

**Só escreva o que estiver nos autos.** Quando um dado não for localizado, escreva exatamente `Não localizado nos autos`. Nunca preencha CPF, valor ou data "por estimativa". Um campo errado faz o time buscar a coisa errada; um `Não localizado nos autos` honesto faz o time conferir. A única exceção é o prazo para defesa sem citação, que segue a regra fixa descrita abaixo.

## Causa raiz: somente a divisão oficial do escritório

A **Causa raiz 1** só pode ser uma das categorias da tabela "3.1 Divisão por Causa Raiz" abaixo. Não use nenhuma outra categoria como Causa raiz 1 (não use "Golpe", "Transação/Pix", "Roubo/Furto", "Fraude" etc.). A **Causa raiz 2** é o subtipo específico e objetivo do caso (ex.: golpe da falsa central, acesso indevido à conta, empréstimo não reconhecido, Pix não reconhecido, pagamento de boletos não reconhecido, seguro não contratado).

| Advogado | Atribuição (categorias válidas de Causa raiz 1) |
|---|---|
| Bianca | Nome Social |
| Juliana | Middle, Estratégico e GuiaBolso |
| Ana Luiza | Superendividamento |
| Millena | Renegociação e Revisional (PicPay); Dano Material acima de R$ 50 mil (PicPay) |
| Juliana Nascimento | Renegociação e Revisional (Original); SCR (Original) |
| Ana Carla | Processos com apenas o Banco Original no polo passivo (exceto SCR, Renegociação e Revisional) |
| **Caio Groschitz** | **Crédito Pessoal, Cash-in, Cash-out, Seguro** |
| Amanda | Consignado, Crédito do Trabalhador e Antecipação Salarial (PicPay e Original) |
| Bruna | Pix e Boleto |
| Luana | Negativação (100%), Residual (Aline) PicPay Card |
| Caio Cordeiro, Giovanna, Rodrigo, Andreza | Pix |
| Aline | PicPay Card (Contestação de Transação, Contactless, Transação não reconhecida, Chargeback, Limite) |
| Bárbara | Chargeback (Boleto, Conta), Conta |
| Renata | Aguardando adaptação |

"Dano Material acima de R$ 50 mil (PicPay)" é categoria própria: confira o valor do dano material pedido (não o valor total da causa) antes de classificar.

## Triagem: o caso é da carteira de Caio Groschitz?

Depois de classificar, confira se a Causa raiz 1 é **Crédito Pessoal, Cash-in, Cash-out ou Seguro**.

- **Se for**, elabore o pedido de subsídios completo no formato abaixo.
- **Se não for**, NÃO elabore o subsídio. Responda em uma ou duas linhas apenas: a Causa raiz 1 identificada, o subtipo, o advogado responsável segundo a tabela e que o caso está fora da carteira de Caio Groschitz.
- **Se a classificação for duvidosa** entre uma categoria dele e a de outro advogado, diga isso em uma linha, indicando as duas opções e o advogado de cada uma, e aguarde a decisão do usuário antes de redigir.

## Fluxo de trabalho

1. **Leia a íntegra dos autos.** Priorize petição inicial, comprovantes, extratos, boletim de ocorrência, reclamações administrativas, decisões liminares, mandados/cartas de citação, certidões de audiência, intimações, procuração e documentos pessoais.
2. **Extraia os campos de identificação.**
3. **Identifique o papel do PicPay na operação** (conta de origem, conta recebedora, credor, emissor, estipulante de seguro, corré sem relação direta etc.).
4. **Classifique a Causa raiz 1 (tabela oficial) e a Causa raiz 2.**
5. **Faça a triagem da carteira.** Se não for caso de Caio Groschitz, pare conforme a regra acima.
6. **Monte o campo de subsídios** a partir da lista da categoria (seção abaixo), ajustada ao caso concreto, sem pedir documento incompatível com a narrativa. Se houver duas categorias da carteira no mesmo caso, junte as listas sem duplicar itens.
7. **Entregue a resposta no formato exato**, sem preâmbulo e sem fecho.

## Regra do prazo para defesa

- Se houver citação efetivada nos autos, use o prazo que decorre dela (ou o indicado no mandado/intimação).
- **Se a citação não tiver sido efetivada, ou nem sequer expedida, o prazo para defesa (fatal) é sempre 20 dias úteis após a data do pedido de subsídios (data de hoje).** Conte a partir do primeiro dia útil seguinte, excluindo sábados, domingos e feriados nacionais, e informe a data no formato dd/mm/aaaa. Nesses casos, a Data de citação fica `Ainda não ocorreu`.

## Documentos por categoria (carteira de Caio Groschitz)

**Crédito Pessoal:** cadastro dispositivo e autorização, validação biometria, alteração de senha, telas de adesão/contratação do empréstimo, contrato ou CCB com dados de validação, comprovação de depósito do valor contratado, tela que comprove a notificação via e-mail e/ou SMS, histórico de parcelas, informação se há ou não débito em aberto, valor, e se houve eventual quitação, tela de ausência de negativação (se houver), nos casos de renegociação o detalhamento (quantidade de parcelas, valor total, valor das parcelas, dados de validação, parcelas em aberto, pagamentos e datas); indicação de responsabilidade.

**Cash-in:** cadastro dispositivo e autorização, validação biometria, alteração de senha, comprovante e extrato da conta com os créditos recebidos, origem dos recursos (instituição, titular e se há relação entre as partes), perfil de consumo e perfil transacional do cliente, eventual bloqueio cautelar, MED e resultado, extrato de conta comprovando o reembolso ou comprovante de estorno; indicação de responsabilidade.

**Cash-out:** cadastro dispositivo e autorização, validação biometria, alteração de senha, comprovante de pagamento e extrato da conta, indicação se as transações foram realizadas por biometria ou inserção manual de senha/digital, passo a passo dentro do App sobre os alertas quanto aos destinatários, notificação de eventual impossibilidade de pagamento, dados dos destinatários/recebedores (e, se boleto, emissor e recebedor), se há relação entre as partes, perfil de consumo e perfil transacional do cliente, MED, extrato de conta comprovando o reembolso ou comprovante de estorno; indicação de responsabilidade.

**Seguro:** cadastro dispositivo e autorização, validação biométrica, alteração de senha, telas de adesão ao seguro, contrato/apólice e condições gerais, histórico de cobranças do prêmio, eventual pedido de cancelamento e sinistro, indicação de responsabilidade, tratativas e fluxo.

Quando compatível com o caso, acrescente ao final: cumprimento do KYC; LOGs de utilização de senha manual/biometria digital.

## Formato de saída — obrigatório e exclusivo

A resposta final contém **apenas** o que está no modelo abaixo, nesta ordem. Sem pontos de atenção, observações, checklist, análise crítica ou justificativa da classificação.

```
Trata-se de [tipo da ação] ajuizada por [autor] em face de [réus], na qual [resumo curto do fato]. [Dinâmica essencial em uma frase, com data e valor total]. Requer [pedidos principais].

AUTOR: [nome completo] - CPF: [CPF ou "Não localizado nos autos"]

Liminar: [Sim/Não. Se sim, resumir em uma frase o teor]

Audiência: [Sim/Não. Se sim, indicar data e horário]

Prazo para defesa: [data]

Data de citação: [data / "Ainda não ocorreu"]

Valor da causa: [valor]

Causa raiz 1: [categoria da tabela oficial]
Causa raiz 2: [subtipo específico]

Documentos anexos: [documentos identificados nos autos]

Para a elaboração do dossiê, indagamos: [documentos da categoria, em frase corrida]
```

## Regras de redação

- **O resumo é curto: um único parágrafo de no máximo 5 a 6 linhas (cerca de 80 a 100 palavras).** Só o essencial: tipo da ação, partes, data, valor total e dinâmica em poucas palavras, e os pedidos principais. Não liste cada transação, horário, beneficiário, precedente, fundamento legal ou pedido acessório.
- Primeiro parágrafo sempre começa com "Trata-se de".
- O campo final ("Para a elaboração do dossiê, indagamos:") é frase corrida, sem tópicos.
- Nenhum bullet/lista na resposta final; os campos são linhas simples, como no modelo.
- Não explique por que algo não foi localizado.
- Não faça análise de mérito, tese defensiva ou contestação.
- Linguagem técnica e direta, sem travessões e sem vícios de texto gerado por IA.

## Exemplo de referência (resumo no tamanho certo)

"Trata-se de Ação Declaratória de Inexistência de Débito c/c Indenização por Danos Materiais e Morais ajuizada por [autor] em face de [banco] e PicPay, na qual o autor não reconhece empréstimo pessoal de R$ 8.000,00 contratado em seu nome em 10/05/2026 e o posterior esvaziamento da conta. Requer tutela para suspender a cobrança, declaração de inexistência do débito, restituição de R$ 8.000,00 e danos morais de R$ 10.000,00."