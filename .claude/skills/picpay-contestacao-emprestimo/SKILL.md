---
name: picpay-contestacao-emprestimo
description: >-
  Redige a CONTESTAÇÃO completa do PicPay (réu) em ações de consumidor sobre
  EMPRÉSTIMO e CRÉDITO: empréstimo pessoal não reconhecido ou alegado como
  fraude, consignado (portabilidade, refinanciamento, cessão de crédito,
  RMC), PicPay Parcela, Crédito Pessoal, aditamento/renegociação, PicPay
  Card e a negativação ou descontos deles decorrentes (inexistência de
  débito/contrato, exclusão de negativação, repetição de indébito, danos
  morais). Lê minuciosamente os subsídios (cadastro, biometria, CCB, valor
  creditado na conta do autor, extrato, negativação) e a inicial. Entrega a
  peça DIRETO NO CHAT em Markdown, o mais completa possível, sem gerar
  .docx. Use SEMPRE que enviarem subsídios de caso de empréstimo ou crédito
  PicPay e pedirem "fazer a contestação", "redigir a defesa", "contestar
  essa ação de empréstimo/consignado/RMC/cartão" ou "analisa e faz a
  defesa". NÃO use para golpe/fraude Pix, bloqueio de conta, chargeback,
  cumprimento de liminar, recurso, embargos, outras instituições ou
  respostas administrativas.
---

# Contestação PicPay — Empréstimo e Crédito

Esta skill redige a contestação na perspectiva da defesa do PicPay (réu) nos
casos em que o consumidor discute um **empréstimo, crédito ou a negativação/
descontos** deles decorrentes: empréstimo pessoal, empréstimo consignado
(portabilidade, refinanciamento, cessão de crédito, RMC), PicPay Parcela,
Crédito Pessoal, aditamento/renegociação e PicPay Card. A tese central é
constante nos modelos do escritório: a **contratação foi legítima** (validada
por biometria facial, selfie, dispositivo cadastrado e assinatura eletrônica),
o **valor foi efetivamente creditado na conta do próprio autor** ou o desconto/
débito **decorre de contrato válido**, e a eventual negativação é **exercício
regular do direito** diante da inadimplência. Logo, não houve falha na
prestação do serviço nem ato ilícito, e inexiste dever de indenizar.

Saída padrão: **a peça INTEIRA, no chat, em Markdown**, pronta para copiar, o
**mais completa e robusta possível** (todas as seções, fundamentação
desenvolvida). Não gere .docx a menos que o usuário peça expressamente. A peça
sai completa por padrão; só entregue seções isoladas se o usuário pedir ("só a
preliminar e o mérito", por exemplo).

A peça precisa soar como trabalho de advogado sênior, com voz própria e sem os
vícios que denunciam texto de máquina. Leia `references/estilo.md` antes de
redigir. Não é cosmético: uma defesa que parece gerada automaticamente perde
credibilidade com o juízo antes do primeiro argumento.

## Princípio central: a peça nasce dos subsídios

A força da defesa está na **fidelidade aos documentos**. Data de abertura da
conta, número do contrato/CCB, valor contratado, valor líquido creditado, data
e hora do crédito, dispositivo (modelo e Android ID), data da validação
biométrica, número e valor das parcelas, vencimentos, data e valor da
negativação, protocolos de atendimento, dados da portabilidade/cessão: tudo
precisa espelhar exatamente o que consta nos subsídios. Um número inventado
destrói a credibilidade e pode configurar litigância de má-fé. Leia **todos** os
subsídios minuciosamente antes de escrever, pensando como o advogado do PicPay:
o que cada tela e cada print prova, e como derruba a narrativa da inicial.

Quando o usuário enviar imagens/prints (biometria, cadastro autenticado, extrato
com o valor creditado, jornada de contratação, áudios/WhatsApp, extrato do INSS,
negativação), **analise cada uma minuciosamente** e extraia os dados que entram
na peça. Como a saída é texto no chat, você não incorpora a imagem: sinalize o
ponto exato onde ela entra com `[anexar print/doc: descrição]`, do jeito que o
escritório faz, para o advogado colar a prova ao montar a versão final.

## Passo 0 — Triagem

Identifique nos subsídios e na inicial (pergunte só o que não for dedutível):

1. **Entidade ré correta.** Confira na inicial e nos subsídios qual entidade foi
   demandada / consta no contrato:
   - **PICPAY BANK - BANCO MÚLTIPLO S.A.** (CNPJ 22.896.431/0001-10) nos casos de
     empréstimo, consignado, CCB, cessão de crédito (padrão dos casos de crédito
     mais recentes).
   - **PICPAY INSTITUIÇÃO DE PAGAMENTO S.A.** nos casos mais antigos e nos de
     cartão/PicPay Card/negativação em que assim consta.
   Use a que efetivamente figura no polo passivo/contrato. Na dúvida, pergunte.
2. **Rito e juízo:** Juizado Especial Cível / Vara Cível ou de Relações de
   Consumo, e a vara/comarca exata (vai no endereçamento).
3. **Produto e arquétipo** (ver `references/produtos-e-fatos.md`), pois define a
   Realidade dos Fatos e as teses:
   - **Empréstimo pessoal não reconhecido / alegada fraude** (autor diz que não
     contratou): provar contratação por biometria/dispositivo e valor creditado
     na conta do próprio autor.
   - **Consignado: portabilidade, refinanciamento, cessão de crédito, RMC**
     (autor alega desconto/contrato não autorizado no benefício).
   - **PicPay Parcela / Crédito Pessoal / aditamento (renegociação)** que virou
     inadimplência e negativação.
   - **PicPay Card / cartão** com fatura inadimplida e negativação.
4. **Pedidos da inicial:** declaração de inexistência de débito/contrato,
   exclusão da negativação (obrigação de fazer), repetição de indébito (simples
   ou em dobro), valor de danos morais, gratuidade, tutela de urgência.
5. **Estado atual:** houve negativação? já foi excluída? há liminar cumprida?
   Isso decide preliminar de perda do objeto quanto à obrigação de fazer.

## Passo 1 — Leitura minuciosa dos subsídios

Extraia e anote (são os dados da Síntese e da Realidade dos Fatos):

- **Conta:** data de abertura/cadastro (usuário legítimo desde …), validação
  biométrica/selfie do cadastro, dispositivo(s) vinculado(s) e Android ID,
  histórico de senha (alterações legítimas), score/"Cadastro Autenticado".
- **Contrato/empréstimo:** número do contrato/CCB, data da contratação, valor
  contratado e valor líquido, número e valor das parcelas, vencimentos, taxa,
  data e forma da validação biométrica na contratação (selfie, plataforma
  Único/"match", assinatura eletrônica, token por SMS/e-mail).
- **Crédito do valor:** data, hora e valor do crédito na carteira/conta do
  autor; movimentação posterior feita pelo próprio autor (ex.: Pix a terceiro —
  anote beneficiário, banco, e eventual vínculo, como sobrenome em comum).
- **Consignado (se for o caso):** contrato originário e instituição, portabilidade
  (para quem, data, correspondente/promotora), refinanciamento (troco, valor,
  data de pagamento), cessão de crédito (data da compra do contrato pelo PicPay,
  cláusula que a autoriza), extrato do INSS com os descontos.
- **Inadimplência/negativação:** parcelas/faturas em aberto, dias de atraso,
  saldo devedor atualizado (com a data da apuração), data e valor da negativação,
  cláusula da CCB/Termos que prevê a inscrição em atraso, protocolos de
  atendimento/Ouvidoria.
- **Da inicial:** parte autora (nome, gênero), data de ajuizamento, tipo de ação,
  valor da causa, pedidos, se há gratuidade e elementos para impugná-la, e se o
  autor litiga em série (vários processos idênticos) para a preliminar de conexão.

## Passo 2 — Confirmar dados faltantes ANTES de redigir

Se faltar elemento essencial (entidade ré, número do contrato, valor creditado,
data/valor da negativação, se já houve exclusão), **pergunte ao usuário de forma
agrupada e objetiva antes de escrever**. Nunca preencha com dado presumido nem
invente. Sem o dado confirmado, o trecho é omitido, não fabricado. Onde o modelo
aponta para um print/documento que não veio, sinalize com `[anexar print/doc: …]`
no ponto exato.

## Passo 3 — Redigir seguindo os modelos

Leia, nesta ordem, antes de escrever:

1. `references/estilo.md` — voz, ritmo, a regra de não usar travessão, os vícios
   de IA a cortar. Mantenha ativo em cada parágrafo.
2. `references/modelo-estrutura.md` — a estrutura, a numeração e a ordem exata das
   seções, a seleção da entidade ré, a tempestividade e o catálogo de
   preliminares (qual usar em cada situação).
3. `references/produtos-e-fatos.md` — como montar a Síntese e a Realidade dos
   Fatos para cada arquétipo de produto, e como tratar cada prova/print.
4. `references/merito-e-jurisprudencia.md` — os parágrafos reaproveitáveis do
   mérito (inversão do ônus, o que é o PicPay, culpa exclusiva, exercício regular,
   ausência de dever de indenizar, inocorrência de danos morais, redução
   subsidiária, repetição simples), os fundamentos legais, as cláusulas
   contratuais pertinentes e o banco de jurisprudência já usado pelo escritório.

Monte a peça plugando os dados reais dos subsídios na estrutura. O mérito é
reaproveitável quase na íntegra; a Síntese e a Realidade dos Fatos são
específicas e nascem dos subsídios. Trabalhe a fundo as teses fortes do caso
concreto e não empilhe tese impertinente (ex.: culpa exclusiva por inadimplência
não cabe quando o autor não reclama de dívida, e sim de contrato que diz nunca
ter feito; nesse caso a espinha é legitimidade da contratação + exercício
regular).

## Jurisprudência: robustez sem invenção

Os modelos do escritório citam julgados reais e recorrentes. Para deixar a peça
completa e robusta **sem alucinar**, use apenas: (a) os julgados do banco em
`references/merito-e-jurisprudencia.md`, que são os que o escritório repete e
foram conferidos nos modelos; ou (b) julgados que o próprio usuário fornecer.
**Nunca invente número de REsp, apelação, processo, data ou relator.** Se quiser
reforço adicional e específico, peça ao usuário ou use formulação genérica
("jurisprudência consolidada dos Tribunais de Justiça").

## Estilo (resumo; detalhe em references/estilo.md)

- **Sem travessão.** Onde a tentação aparecer, encerre com ponto, use parênteses
  para o aparte ou dois-pontos para a explicação. Vírgula resolve a pausa interna.
- **Sem vícios de IA.** Corte muletas ("crucial", "cristalino", "robusto"),
  aberturas automáticas repetidas e juridiquês decorativo. Os modelos usam
  "Prima facie", "Insta salientar", "Compulsando aos autos", "Outrossim": use com
  parcimônia, como nos modelos, sem transformar em tique.
- **Ritmo variado.** Alterne fundamentação longa com frases curtas e secas.
- **Ancorada no fato.** Cada afirmação jurídica grudada num dado dos subsídios
  (número do contrato, data, hora, valor creditado, Android ID, data da biometria,
  dias de atraso, valor e data da negativação).
- **Terceira pessoa:** "o PicPay"/"o PicPay Bank", "a Parte Autora"/"o Autor",
  "este Réu". Ajuste o gênero ao autor real.

## Checklist final antes de entregar

Confira que: não há travessão nem hífen usado como pausa; a entidade ré está
correta e coerente na peça inteira (PicPay Bank x PicPay Instituição de
Pagamento); endereçamento, número do processo e nome do autor corretos; a Síntese
resume fielmente a inicial e seus pedidos com valores; todo número de contrato/
CCB, data, hora, valor creditado, dispositivo/Android ID, data de biometria,
dias de atraso, saldo devedor e data/valor da negativação batem com os subsídios;
o arquétipo do produto está coerente com as teses escolhidas; as cláusulas da
CCB/Termos de Uso citadas existem nos subsídios (item 12/14 sobre negativação em
atraso, item "3"/cláusula 14 sobre cessão, cláusulas 14 e 16 do cartão); os
julgados são do banco do escritório ou fornecidos pelo usuário (nenhum inventado);
artigos corretos (CDC 6º, 14 caput/§1º/§3º I e II, 42 §único; CC 186, 187, 286,
287, 290, 884, 927; CPC 330 §1º III, 373, 485 VI); preliminar de perda do objeto
presente se a negativação já foi excluída; pedido subsidiário de redução dos
danos morais presente por eventualidade; requerimentos finais e nome/OAB do
advogado para intimações (confirme com o usuário); marcadores `[anexar print/doc:
…]` onde a prova não veio; e nenhum dado inventado.
