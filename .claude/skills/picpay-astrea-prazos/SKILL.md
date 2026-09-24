---
name: picpay-astrea-prazos
description: >-
  Operacao interna BFAP da carteira PicPay no Astrea: sistema de etiquetas, SLA D-2, controle diario de
  prazos e atividades predefinidas (fluxos automatizados do caso). Use SEMPRE que o usuario precisar saber
  qual etiqueta inserir no Astrea, quando dar baixa em prazo/tarefa, como funciona o D-2, o que fazer
  quando nao vai cumprir o prazo (reagendamento), como responder o e-mail de CONTROLE DE PRAZOS, ou qual
  o fluxo de atividades predefinidas de um momento processual (audiencia, audiencia pre-processual,
  interesse recursal, OBF/liminar, subsidios, acordos, agravo, pagamento, encerramento). Aciona com
  pedidos como "qual etiqueta uso no Astrea", "posso baixar esse prazo", "o que e D-2", "nao vou cumprir o
  prazo, e agora", "como reagendo", "etiqueta de prazo / status / fluxo / resultado", "quais tarefas da
  audiencia", "fluxo de subsidios no Astrea", "controle diario de prazos". NAO use para Projuris/cadastro,
  teses, diretrizes recursais, requisicoes ou encerramento de pasta (skills proprias).
---

# Astrea, Etiquetas e Controle de Prazos (BFAP - PicPay)

O Astrea e o sistema **interno BFAP** de gestao da carteira: concentra prazos, tarefas e fluxos. Ele
**complementa, nao substitui** o Projuris (cliente). A insercao correta das etiquetas e de **inteira
responsabilidade do advogado titular** do caso, porque o controle diario de prazos depende delas para
funcionar.

Use esta skill para: escolher a etiqueta certa, aplicar o SLA D-2, conduzir o controle diario e disparar/
seguir as atividades predefinidas. O catalogo completo de etiquetas e os fluxos de tarefas estao em
`references/`.

## 1. Etiquetas de cadastro (toda pasta PicPay)

Tres etiquetas de identificacao obrigatorias na abertura:
- **CONTRATANTE = PICPAY** (verde)
- **FASE = CONHECIMENTO / SENTENCA / ACORDAO / EXECUCAO** (laranja)
- **AREA = CIVEL** (azul claro)

Adicionais quando aplicaveis: **MIDDLE**, **ESTRATEGICO**, **ADVOGADO LITIGANTE** (parte adversa no rol monitorado).

O catalogo operacional completo (Prazos, Status, Automaticas, Fluxo, Resultado) esta em `references/etiquetas.md`.

## 2. Etiqueta de tipo de prazo (obrigatoria desde 27/04/2026)

Toda insercao de prazo exige a etiqueta do tipo correspondente -- sem ela, o controle diario nao funciona:
ACORDO, SUBSIDIOS, CONTESTACAO, RECURSO, OBRIGACAO DE FAZER, LIMINAR, MANIFESTACAO, CONDENACAO, URGENTE.
(tabela completa em `references/etiquetas.md`).

## 3. Etiqueta de status do prazo (vigencia 30/04/2026)

- **PRAZO EM SEGURANCA** -- dentro do D-2 (ainda 2+ dias uteis ate o fatal).
- **PRAZO EM CURSO** -- fora do D-2, execucao iminente: atencao redobrada e priorizacao.
- **REAGENDADO** -- prazo reagendado, **sempre com justificativa** na planilha CONTROLE DE PRAZOS. Quando "Em Seguranca"/"Em Curso" forem aplicadas a prazo reagendado, vir junto com "REAGENDADO".

## 4. SLA D-2 -- regra geral

Toda atividade processual deve estar **concluida ate dois dias uteis antes do prazo fatal**. Essa margem
garante revisao, correcoes, contingencia de protocolo e validacao por terceiros. O D-2 vale para todos os
prazos, **exceto** quando um SLA especifico se sobrepoe:

| Atividade | SLA especifico |
|---|---|
| Liminar / Tutela de Urgencia | Conforme prazo judicial (em regra inferior ao D-2). |
| Subsidios (normal e urgente) | Aberta no dia do cadastro da pasta. |
| Cumprimento de OBF | 2 a 5 dias uteis de antecedencia (2 dias com justificativa). |
| Pagamentos (Acordo/Condenacao/Custas) | Minimo 5 dias uteis antes do fatal. |
| Analise Recursal | Minimo 5 dias uteis antes do fatal recursal. |
| Casos Estrategicos | E-mail individual com a coordenacao + tarefa no Astrea (fluxo proprio). |

## 5. Baixa de prazos e tarefas -- quando dar baixa

So baixar **APOS o protocolo** da atividade processual (prazo) ou **APOS a conclusao** da atividade
administrativa (tarefa nao-processual). Em audiencias, so baixar quando a **Ata for analisada** pelo
advogado responsavel. **Baixa por antecipacao ou para "limpar agenda" e VEDADA** -- vale para advogados e
assistentes.

## 6. Quando o D-2 nao for cumprido -- reagendamento

1. Inserir a etiqueta **REAGENDADO** no Astrea.
2. Registrar a **justificativa** na coluna correspondente da planilha CONTROLE DE PRAZOS diaria.
3. Responsabilidade: advogado do prazo.

Nao ha fluxo paralelo (ex.: e-mail isolado para a coordenacao) -- a planilha diaria e o canal unico, para
evitar duplicacao. A justificativa na planilha deve ser **identica** a associada a etiqueta REAGENDADO.

## 7. Controle diario de prazos

1. Todo dia util a controladoria envia "CONTROLE DE PRAZOS - DD/MM/AAAA" com a planilha de prazos do dia.
2. Cada advogado filtra seus casos e, para cada um, **informa o ID do caso ja protocolado** OU **apresenta justificativa** para nao protocolados.
3. Todos respondem ao e-mail diariamente, ao final do prazo, **ate as 17h**.

Colunas-chave: ID do caso (apos protocolo), Reagendado? (motivo, coincidente com a etiqueta), Justificativa.

## 8. Atividades predefinidas (fluxos)

As atividades predefinidas estruturam o fluxo automatizado: cada momento processual tem dono, prazo (em
dias uteis, D+/D-) e checagem subsequente. Dividem-se em atividades **criadas pela controladoria**
(disparadas no cadastro/evento) e **criadas pelo advogado** (momentos especificos). O catalogo completo
dos 11 fluxos (com tarefas, prazos e responsaveis) e o mapa por momento do caso estao em
`references/atividades-predefinidas.md`. Consulte-o sempre que precisar disparar ou seguir um fluxo.

Detalhe importante: criar a tarefa **"Elaborar Defesa"** (fluxo de Audiencia) gera automaticamente as
etiquetas **CONTESTACAO** e **AUDIENCIA DESIGNADA**.

## Principio operacional

As etiquetas nao sao burocracia: elas alimentam o controle diario, o SLA e a leitura de status pela
coordenacao e pelo cliente. Etiqueta faltante ou baixa antecipada quebra o controle de toda a equipe --
por isso a regra e baixar so depois do feito e manter Astrea e planilha sempre consistentes.
