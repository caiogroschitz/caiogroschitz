---
name: picpay-decisoes-encerramento
description: >-
  Registro de decisoes (sentenca, acordao, embargos), encerramento de pasta e provisionamento da carteira
  PicPay (BFAP), em paralelo no Projuris e no Astrea. Use SEMPRE que o usuario precisar registrar uma
  sentenca improcedente/procedente/parcial, lancar acordao (10 tipos, otica do PicPay), tratar
  embargos de declaracao no registro, atualizar a aba PEDIDOS (Perda Provavel/Remota/Possivel), verificar
  se a pasta esta apta para encerramento, executar o roteiro de encerramento (Instancia/Pedidos/Documentos/
  Solicitar Encerramento), ou provisionar por fase (Possivel/Provavel/Remoto, INPC+1% a.m.,
  OBF R$ 0,01). Aciona com "como registro essa sentenca/acordao", "qual tipo de acordao lanço", "isso e
  favoravel ou desfavoravel pra gente", "como atualizo os pedidos", "essa pasta pode encerrar", "roteiro
  de encerramento", "motivo de encerramento", "como provisiono esse caso", "perda provavel ou remota".
  NAO use para abrir requisicoes (skill requisicoes), decidir recurso (skill diretrizes) ou cadastro inicial.
---

# Registro de Decisoes, Encerramento e Provisionamento - PicPay (BFAP)

O registro de decisoes e feito **em paralelo** no Projuris (cliente) e no Astrea (interno). Cada decisao
tem nome especifico no rol taxativo do Manual do Projuris e dispara um conjunto proprio de etiquetas no
Astrea. **Regra de leitura central: a analise e sempre feita pela otica do PicPay (cliente)** -- favoravel
ou desfavoravel para nos, nao para a parte.

Os roteiros detalhados, os 10 tipos de acordao e as regras de provisionamento estao em `references/`.

## 1. Sentenca Improcedente (favoravel)

**Projuris:** Resumo -> Alterar -> Fase "Recursal - Sentenca". Instancia -> Registrar Decisao -> data ->
"Sentenca Improcedente". Pedidos -> Recalculo de Prognostico -> **zerar o pedido**, justificando com a
sentenca. Andamento -> "Sentenca" + anexar documento. Resumo -> Cumprir evento -> "aguardando decurso de
prazo para recurso".
**Astrea:** etiqueta "Resultado: Sentenca Improcedente" + fluxo "Aguarda Transito em Julgado" + tarefa
"Verificar transito em julgado".

## 2. Sentenca Procedente / Procedente em Parte (desfavoravel)

**Projuris:** Resumo -> Fase "Recursal - Sentenca". Instancia -> Registrar Decisao -> "Procedente" (todos
os pedidos) ou "Procedente em Parte". Decisao Predominante = **DESFAVORAVEL** em qualquer condenacao
pecuniaria; **Favoravel em Parte** em homologacao de acordo. Pedidos -> Recalculo -> inserir o valor
condenado como **PROVAVEL**, justificando. Procedimento Comum: conferir o rito e Adicionar os Honorarios
Advocaticios ja calculados conforme o provisionamento.
**Astrea:** "Resultado: Sentenca Totalmente Procedente" ou "Procedente em Parte" (ou "Extinto sem
resolucao do merito").

## 3. Acordao (10 tipos)

Mesma logica da sentenca, adaptando o nome conforme o rol. **Sempre pela otica do PicPay** -- ex.:
improcedencia em 1ª instancia (favoravel) + apelacao do autor nao provida = improcedencia mantida ->
"ACORDAO APELACAO - IMPROCEDENCIA RECURSO AUTOR", marcado **FAVORAVEL**. Os 10 tipos (Apelacao e Agravo,
Improcedencia/Provimento, Autor/Reu/Ambos) em `references/tipos-decisao.md`. No Astrea: etiqueta de
resultado de 2ª Instancia (cap. 26.6) e atualizar fluxo (ex.: remover "Aguarda Decisao de Segunda
Instancia").

## 4. Embargos de Declaracao

**NAO** precisam ser registrados como decisao no Projuris pelo escritorio. O fluxo segue normalmente -- so
sentenca, acordao ou decisao monocratica sao registrados. (No encerramento, o rol inclui "Embargos de
Declaracao Favoravel/Desfavoravel" como tipo de decisao final -- ver `references/tipos-decisao.md`.)

## 5. Pedidos - registro do valor

- Procedencia total: valor total em **"Valor Perda Provavel"**.
- Parcial/acordo: parcela condenatoria em **Perda Provavel** e o restante em **Perda Remota**.
- Improcedencia/extincao/desistencia: valor total em **Perda Remota**.
- (No cadastro inicial, dano material + dano moral + R$ 0,01 de OBF entram como **Perda Possivel**; apos
  sentenca, nenhum valor fica em Possivel.)

## 6. Criterios de aptidao para encerramento

Quatro cenarios (detalhe em `references/provisionamento.md`):
1. **Decisao desfavoravel** -- apos pagamento da condenacao + cumprimento de OBF + lancamento no Projuris + sem pendencias.
2. **Decisao favoravel** -- apos transito em julgado (etiqueta "Aguarda Transito" removida) + honorarios ao escritorio (se houver) + sem recurso do autor/esgotamento.
3. **Acordo cumprido** -- comprovacao nos autos + homologacao (se judicial) + lancamento + andamentos atualizados.
4. **Extincao/Desistencia** -- transito da extincao/homologacao + sem recurso + verificacao de custas/honorarios.

## 7. Roteiro de encerramento (Projuris)

1. **Aba INSTANCIA** -> Registrar Decisao -> tipo final conforme rol taxativo (15 tipos, incluindo ED Favoravel/Desfavoravel) -- sempre pela otica do PicPay.
2. **Aba PEDIDOS** -> atualizacao final (Perda Provavel/Remota conforme secao 5).
3. **Aba DOCUMENTOS** -> anexar decisao final, comprovantes, termo de quitacao, certidao de transito -- nomenclatura padronizada (numero + MAIUSCULAS).
4. **Aba RESUMO** -> Solicitar Encerramento -> 1 dos 6 motivos: (1) Decisao Favoravel com Transito; (2) Decisao Desfavoravel com Pagamento Realizado; (3) Acordo Extrajudicial Cumprido; (4) Acordo Judicial Cumprido; (5) Extincao sem Resolucao do Merito; (6) Desistencia da Parte Autora.

**Astrea (baixa coordenada, apos encerramento aprovado pelo cliente):** remover etiquetas de fluxo
pendentes; inserir etiqueta de resultado final + "encerrar pasta apos faturamento"; concluir tarefas
pendentes; arquivar conforme padrao BFAP.

## 8. Provisionamento

O Projuris alimenta o provisionamento contabil do passivo civel do PicPay com base na **fase, classificacao
e decisao**. O escritorio classifica os pedidos como **Possivel, Provavel ou Remoto** conforme a fase.
Regra por fase, atualizacao monetaria (**INPC + 1% a.m. desde a Data do Fato**, automatica pelo Projuris) e
OBF (R$ 0,01 simbolico no cadastro; multa cominatoria conforme a decisao) em `references/provisionamento.md`.

## Principio

Registro e provisionamento corretos sao o que o cliente enxerga do trabalho da BFAP no balanco. O erro
mais comum e inverter a otica -- lembre que "favoravel/desfavoravel" e sempre do ponto de vista do PicPay,
e que o valor nos Pedidos tem de espelhar exatamente a decisao (Provavel = condenado; Remoto = afastado).
