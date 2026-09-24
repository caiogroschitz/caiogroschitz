---
name: picpay-contestacao-bloqueio
description: >-
  Redige a CONTESTAÇÃO do PicPay (réu) em ações de consumidor sobre BLOQUEIO,
  LIMITAÇÃO ou SUSPENSÃO de conta e indisponibilidade de saldo (restrição no
  DICT/BACEN, violação de Políticas e Termos de Uso, bloqueio cautelar
  antifraude, pedido de desbloqueio/restabelecimento), lendo minuciosamente os
  subsídios da PicPay (cadastro, data/hora do bloqueio e desbloqueio, motivo,
  saldo, saques, atendimentos, inicial) e seguindo FIELMENTE os modelos do
  escritório. Use SEMPRE que o usuário enviar os subsídios de um caso de
  bloqueio/limitação de conta PicPay e pedir para "fazer a contestação",
  "redigir a defesa", "fazer a preliminar e o mérito", "contestar essa ação de
  bloqueio" ou "analisa os subsídios e faz a defesa". NÃO use para outros temas
  com skill própria (golpe/fraude Pix, empréstimo, chargeback, cumprimento de
  liminar, recurso, embargos), outras instituições ou respostas
  administrativas.
---

# Contestação PicPay — Bloqueio / Limitação de Conta

Esta skill redige a contestação na perspectiva da defesa do PicPay (réu) nos
casos em que o consumidor reclama do **bloqueio, limitação ou suspensão da
conta** e da indisponibilidade do saldo, pedindo desbloqueio/restabelecimento e
danos morais. A tese central é constante nos quatro modelos do escritório: o
bloqueio foi **legítimo e cautelar**, decorre de **prerrogativa contratual**
(itens 3 e 4 dos Termos de Uso) e/ou de **determinação do BACEN** (restrição no
DICT), o PicPay **prestou as informações** e **não houve falha** nem ato
ilícito, logo inexiste dever de indenizar.

A peça pode sair completa ou apenas nas seções pedidas (o fluxo mais comum do
escritório é "só a preliminar e o mérito"). A saída padrão é **texto no chat em
Markdown**, pronto para copiar; só gere arquivo se o usuário pedir.

A peça precisa soar como trabalho de advogado sênior, com voz própria e sem os
vícios que denunciam texto de máquina. Leia `references/estilo.md` antes de
redigir; não é cosmético, é credibilidade perante o juízo.

## Princípio central: a peça nasce dos subsídios

A força da defesa está na **fidelidade aos documentos**. Datas de abertura da
conta, data e hora do bloqueio e do desbloqueio, motivo (DICT ou violação de
Termos de Uso), valor de saldo, datas de saque, protocolos de atendimento,
número da conta e agência: tudo precisa espelhar exatamente o que consta nos
subsídios. Um número inventado destrói a credibilidade e pode configurar
litigância de má-fé. Leia **todos** os subsídios minuciosamente antes de
escrever, pensando como o advogado civilista/consumerista do PicPay: o que cada
tela prova e como ela derruba a narrativa da inicial.

## Passo 0 — Triagem rápida

Identifique nos subsídios e na inicial (pergunte só se não for dedutível):

1. **Rito e juízo:** Juizado Especial Cível / Vara de Relações de Consumo ou
   Justiça Comum, e a vara/comarca exata (vai no endereçamento).
2. **Motivo do bloqueio**, que define a narrativa da Realidade dos Fatos:
   - **Restrição no DICT / BACEN** (a instituição é obrigada a não transacionar;
     o bloqueio não foi feito pelo PicPay, e sim automático pelo Banco Central);
   - **Violação de Políticas e Termos de Uso** (conta limitada de forma
     cautelar; abre também a tese de culpa exclusiva do consumidor);
   - **Bloqueio cautelar antifraude / análise de segurança** (proteção do
     próprio usuário).
3. **Estado atual da conta:** já foi desbloqueada? Saldo já foi liberado/sacado?
   Conta encerrada a pedido? Isso decide a **preliminar de perda do objeto**.
4. **Pedidos da inicial:** valor de danos morais pleiteado, pedido de
   obrigação de fazer (desbloqueio), gratuidade.

## Passo 1 — Leitura minuciosa dos subsídios

Extraia e anote (são os dados que entram na Síntese e na Realidade dos Fatos):

- Data de **abertura/cadastro** da conta (usuário legítimo desde …).
- Data e **hora** do bloqueio/limitação e o **motivo** documentado.
- Data e hora do **desbloqueio/liberação** (se houve) e da **liberação do
  saldo** para saque; data dos **saques** efetuados pelo autor.
- **Saldo** existente no bloqueio e saldo atual (se zerado, registrar).
- **Protocolos de atendimento** que provem que o motivo foi informado, e
  eventual tentativa de contato ativo do PicPay com o autor.
- **Encerramento** da conta a pedido do autor (data/protocolo), se houver.
- Número da **agência/conta**, quando o pedido for de desbloqueio.
- Da inicial: parte autora (nome, gênero), data de ajuizamento, tipo de ação,
  valor da causa, pedidos.

## Passo 2 — Confirmar dados faltantes ANTES de redigir

Se faltar elemento essencial (motivo do bloqueio, data/hora ilegível, se a
conta já foi desbloqueada, valor pleiteado), **pergunte ao usuário de forma
agrupada e objetiva antes de escrever**. Nunca preencha com dado presumido nem
invente. Sem o dado confirmado, o trecho correspondente é omitido, não
fabricado. Onde o modelo aponta para um documento/print que não veio, sinalize
com `[anexar print/doc: …]` no ponto exato, do jeito que o escritório faz.

## Passo 3 — Redigir seguindo os modelos

Leia, nesta ordem, antes de escrever:

1. `references/estilo.md` — voz, ritmo, regra de não usar travessão, vícios de
   IA a cortar. Mantenha ativo em cada parágrafo.
2. `references/modelo-estrutura.md` — a estrutura, a numeração e a ordem exata
   das seções, e qual preliminar usar em cada situação.
3. `references/merito-boilerplate.md` — os parágrafos do mérito praticamente
   constantes nos quatro modelos (inversão do ônus, o que é o PicPay, exercício
   regular do direito, culpa exclusiva, ausência de dever de indenizar,
   inocorrência de danos morais, redução subsidiária, requerimentos). Use como
   base, adaptando ao caso concreto, sem copiar dados de exemplo.
4. `references/fatos-e-preliminares.md` — como montar a Síntese da Demanda, a
   Realidade dos Fatos (as duas narrativas: DICT e violação de Termos) e as
   preliminares (perda do objeto, indeferimento da inicial).

Monte a peça plugando os dados reais dos subsídios na estrutura. O mérito é
reaproveitável quase na íntegra; a Síntese e a Realidade dos Fatos são
específicas e nascem dos subsídios. Trabalhe a fundo as teses fortes do caso e
não empilhe tese impertinente (ex.: culpa exclusiva do consumidor só entra
quando o motivo foi violação de Termos pelo próprio autor, não em bloqueio por
DICT).

## Estilo (resumo; detalhe em references/estilo.md)

- **Sem travessão.** Onde a tentação aparecer, encerre com ponto, use parênteses
  para o aparte ou dois-pontos para a explicação.
- **Sem vícios de IA.** Corte muletas ("crucial", "cristalino", "robusto"),
  aberturas automáticas repetidas e juridiquês decorativo. Os modelos usam
  "Outrossim", "Insta salientar", "Prima facie", "Compulsando aos autos": use
  com parcimônia, como nos modelos, sem transformar em tique.
- **Ritmo variado.** Alterne fundamentação longa com frases curtas e secas.
- **Ancorada no fato.** Cada afirmação jurídica grudada num dado dos subsídios
  (data, hora, valor, protocolo, item do Termo de Uso).
- **Terceira pessoa:** "o PicPay", "a Parte Autora"/"o Autor", "este Réu".
  Ajuste o gênero ao autor real.

## Checklist final antes de entregar

Confira que: não há travessão nem hífen usado como pausa; endereçamento, número
do processo e nome do autor corretos; a Síntese resume fielmente a inicial; toda
data, hora, valor, protocolo e número de conta batem com os subsídios; o motivo
do bloqueio (DICT x violação de Termos) está coerente em toda a peça e as teses
do mérito correspondem a esse motivo; itens 3 e 4 dos Termos de Uso citados
onde cabível; preliminar de perda do objeto presente se a conta já foi
desbloqueada/saldo liberado; artigos corretos (CDC 6º, 14 e §3º; CC 186, 187,
927, 884; CPC 373, 330 IV, 485 VI); pedido subsidiário de redução dos danos
morais presente por eventualidade; requerimentos finais e nome/OAB do advogado
para intimações; e nenhum dado inventado, com [anexar …] onde o documento não
veio.
