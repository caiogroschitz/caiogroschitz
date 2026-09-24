# Extração dos autos — o que ler, em que ordem, e como resolver conflitos

Este arquivo orienta a leitura da íntegra do processo trabalhista para liquidação.
O objetivo é sair daqui com **todos os parâmetros localizados e com a fonte
citada (ID/página)**, e com as ambiguidades sinalizadas — nunca resolvidas no
escuro.

## Índice
1. Ordem de leitura
2. O que extrair de cada documento
3. Hierarquia das fontes (o que prevalece em conflito)
4. Conflitos típicos e como sinalizá-los
5. Lacunas que obrigam a parar e avisar

## 1. Ordem de leitura

Leia de trás para frente em termos de autoridade, mas monte o quadro nesta ordem:

1. **Sentença** (e eventual **acórdão** e decisão de embargos) — define O QUE
   liquidar. É o título executivo. Sem ela, não há liquidação.
2. **Certidão de trânsito em julgado** — confirma o que efetivamente transitou
   (pode haver reforma parcial em grau de recurso). O comando a liquidar é o que
   restou após o último pronunciamento transitado.
3. **Petição inicial** — ajuda a entender o pedido e o alcance das verbas, e traz
   datas (admissão, demissão, ajuizamento) e a causa de pedir.
4. **Contestação** — fatos incontroversos, valores reconhecidos, documentos
   juntados pela ré (fichas financeiras, controles de ponto).
5. **CTPS / contrato de trabalho** — admissão, demissão, função, salário inicial,
   anotações de evolução, modalidade de rescisão.
6. **Holerites / recibos / ficha financeira** — evolução salarial mês a mês,
   verbas pagas, base para diferenças e reflexos.
7. **TRCT (Termo de Rescisão)** — verbas rescisórias já pagas, modalidade de
   afastamento, projeção do aviso prévio, saldo, datas.
8. **Extrato de FGTS / guias** — depósitos efetuados (para deduzir do FGTS
   devido), saldo, multa de 40%.
9. **Comprovantes de pagamento já realizados / acordos parciais** — valores a
   deduzir, para evitar enriquecimento e excesso de execução.

## 2. O que extrair de cada documento

**Da sentença/acórdão (núcleo da precisão):**
- Lista literal das verbas deferidas e dos reflexos de cada uma.
- Parâmetros fixados: jornada reconhecida, divisor, adicional (%), base de
  cálculo de cada verba, limitação temporal, evolução salarial a adotar.
- Verbas indeferidas/excluídas (não lançar).
- Honorários (percentual, base, a favor de quem), justiça gratuita.
- Determinação de dedução de valores pagos.
- Regime de correção/juros, se fixado expressamente.
- Critérios de INSS e IRPF, se a sentença dispôs algo específico.

**Dos dados contratuais (inicial, CTPS, contestação, TRCT):**
- Data de admissão, data de demissão/afastamento, **modalidade** da rescisão
  (sem justa causa, pedido de demissão, justa causa, rescisão indireta, término
  de contrato) — define quais verbas rescisórias cabem.
- Data do ajuizamento (marco relevante para juros) e data-base da categoria.
- Carga horária mensal / jornada, função, maior e última remuneração.

**Dos holerites/ficha financeira:**
- Salário base mês a mês (montar o **histórico salarial**).
- Verbas pagas (para apurar diferenças e o que já foi quitado).
- Médias de variáveis (HE habituais, comissões) quando a verba dependa de média.

**Do TRCT e extrato de FGTS:**
- Verbas rescisórias já pagas e seus valores.
- FGTS depositado no curso do contrato e na rescisão (a deduzir).
- Saldo do FGTS informado e base para a multa de 40%.

## 3. Hierarquia das fontes (o que prevalece em conflito)

Quando dois documentos divergem, a ordem de prevalência para fins de liquidação
é, em regra:

1. **O título executivo** (sentença/acórdão transitado) — se fixou um valor,
   base, período ou critério, é ele que vale, ainda que um documento mostre coisa
   diferente. A liquidação obedece à coisa julgada.
2. **Fato reconhecido/incontroverso** nos autos (ex.: a ré confessa o salário).
3. **Documento oficial** mais específico e contemporâneo ao fato (holerite do mês
   prevalece sobre uma menção genérica; TRCT sobre estimativa).
4. **Petição inicial** como referência subsidiária do alcance do pedido.

Importante: a sentença frequentemente já resolve a controvérsia probatória
("fixo o salário em R$ X", "reconheço a jornada das 7h às 19h"). Nesse caso, **use
o que a sentença fixou** e ignore a divergência documental — apenas registre que
houve divergência e que se seguiu o título.

## 4. Conflitos típicos e como sinalizá-los

Não escolha silenciosamente. Para cada conflito, registre um item "⚠ Conferir" no
roteiro com: o conflito, as fontes (ID/página) e a regra aplicada.

- **Salário holerite ≠ CTPS ≠ inicial** → siga o que a sentença fixou; se a
  sentença remete "às fichas financeiras", use o holerite e sinalize.
- **Modalidade de rescisão divergente** (inicial diz dispensa sem justa causa, ré
  alega pedido de demissão) → veja o que a sentença decidiu; isso muda todas as
  verbas rescisórias.
- **Período de incidência da verba** ambíguo na sentença → não estreite nem
  amplie; sinalize a leitura adotada e peça confirmação.
- **Reflexos não listados expressamente** → liquide apenas os reflexos
  determinados pelo título; "reflexos legais" deve ser interpretado conforme a
  fundamentação, sinalizando.
- **Valores já pagos** sem comprovação clara → marque para conferência antes de
  deduzir.

## 5. Lacunas que obrigam a parar e avisar

Se faltar qualquer destes, **pare e liste ao usuário** antes de gerar o roteiro,
porque o cálculo ficaria inseguro:

- Ausência da **sentença/acórdão** ou da **certidão de trânsito em julgado**.
- Verba deferida que depende de **evolução salarial** sem que haja holerites/ficha
  financeira nem fixação na sentença.
- Verba que depende de **médias** (HE habituais, comissões) sem base documental.
- **FGTS** a deduzir mencionado, mas sem extrato/valor nos autos.
- Honorários/dedução determinados pela sentença sem o parâmetro (percentual,
  valor) localizável.

Avisar e pedir o documento é sempre melhor do que preencher por estimativa: em
liquidação, o dado faltante é a origem da impugnação.
