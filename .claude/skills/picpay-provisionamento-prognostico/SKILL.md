---
name: picpay-provisionamento-prognostico
description: "Decide e ensina a lançar o prognóstico/provisionamento dos pedidos no Projuris da carteira PicPay (BFAP): quanto de cada pedido vai em \"Valor Perda Provável\", \"Valor Perda Possível\" e \"Valor Perda Remota\", conforme a fase do processo e a decisão, sempre na ótica do PicPay (réu). Cobre Obrigação de Fazer (OBF/OBP), multa, acordo, honorários, o passo a passo no Projuris (Recálculo de Prognóstico), os reflexos no Astrea e o motivo de encerramento. USE SEMPRE que o usuário tiver dúvida sobre em qual campo lançar o valor ou disser coisas como \"vai em provável ou possível\", \"como faço o recálculo de prognóstico\", \"está tudo em possível e agora\", \"como provisiono esse caso\", \"houve acordo/sentença, como ajusto os pedidos\", \"qual o motivo de encerramento\", ou colar/descrever um processo PicPay pedindo para classificar os valores. NÃO use para teses, contestação, recursos, cadastro inicial ou requisições."
license: MIT
metadata:
  carteira: PicPay
  escritorio: BFAP
  fonte: Manual_PicPay_BFAP_v1.0 (cap. 29.5, 34.4, 38, 39)
---

# Provisionamento / Lançamento de Prognóstico — PicPay (BFAP)

Esta skill resolve a dúvida mais comum no lançamento dos pedidos no Projuris: **qual valor vai em
"Valor Perda Provável", em "Valor Perda Possível" e em "Valor Perda Remota"**. Acertar isso importa
porque esses campos alimentam *diretamente* o provisionamento contábil do passivo cível do PicPay —
um valor na coluna errada distorce o balanço do cliente.

A regra inteira gira em torno de duas ideias simples. Guarde-as antes de tudo:

1. **A análise é sempre feita na ótica do PicPay (o réu).** "Favorável" = bom para o PicPay
   (improcedência). "Desfavorável" = condenação. Uma sentença improcedente em 1º grau é favorável,
   mesmo que o autor recorra.
2. **A classificação acompanha a fase do processo.** Antes de qualquer decisão, todo o risco é
   apenas *possível*. Depois que sai uma decisão, o risco deixa de ser hipotético: o que foi
   condenado vira *provável* e o que caiu (não condenado) vira *remoto*. **Depois da sentença,
   NENHUM valor pode continuar em "Possível"** — é justamente esse o erro que mais aparece.

## Passo 1 — Identifique a fase e a decisão

Antes de classificar, descubra em que ponto o processo está. Pergunte ao usuário (ou leia do que
ele descreveu) o seguinte, porque a resposta muda tudo:

- **Fase:** Conhecimento (ainda sem sentença) · Recursal — Sentença · Recursal — Acórdão · Execução.
- **Houve decisão?** Qual? (improcedente, procedente, procedente em parte, acordo homologado,
  extinção sem mérito, desistência).
- **Valores dos pedidos:** o valor de cada pedido pecuniário (dano moral, dano material) e se há
  Obrigação de Fazer (OBF/OBP).
- **Valor efetivamente condenado / valor do acordo**, quando já houver decisão.

Se faltar alguma dessas informações para decidir, pergunte — não chute. É melhor uma pergunta curta
do que um provisionamento errado no balanço do cliente.

## Passo 2 — Tabela mestra de classificação

Esta é a regra (Manual cap. 39.1, consolidada com 29.5 e 38.2). Aplique a linha correspondente à
situação do processo:

| Situação | Valor Perda Provável | Valor Perda Possível | Valor Perda Remota |
|---|---|---|---|
| **Conhecimento** (antes da sentença) | — | **Valor total do pedido** | — |
| **Sentença improcedente** (favorável) | — | — | **Valor total** |
| **Sentença procedente total** (desfavorável) | **Valor total** | — | — |
| **Sentença procedente em parte** (desfavorável em parte) | **Parcela condenada** | — | **Diferença não condenada** |
| **Acordo homologado** | **Valor do acordo** | — | **Diferença (pedido − acordo)** |
| **Acórdão favorável** (mantém/torna improcedente) | — | — | **Valor total** |
| **Acórdão desfavorável** (condena/mantém condenação) | **Valor condenado** | — | **Diferença** |
| **Execução definitiva** | **Valor da execução** | — | — |
| **Extinção sem mérito / desistência** | — | — | **Valor total** |

Regra de ouro para conferir o resultado: **na fase de conhecimento, 100% em Possível; depois de
qualquer decisão, 0% em Possível** — o valor se reparte apenas entre Provável (o que pesa contra o
PicPay) e Remota (o que foi afastado).

### Por que "Possível" some depois da decisão

"Possível" representa incerteza pura — ainda não se sabe se o PicPay vai perder. Quando a decisão
sai, a incerteza acaba: ou aquele pedido virou condenação (Provável) ou foi rejeitado (Remota).
Por isso, em procedência parcial e em acordo o valor **sempre se divide** entre as duas colunas, e
nunca sobra nada em Possível. Se você vê valor em Possível num processo que já tem sentença ou
acordo, está errado e precisa ser remanejado.

## Passo 3 — Casos especiais

### Obrigação de Fazer (OBF / OBP)

No **cadastro inicial**, todo pedido de Obrigação de Fazer é provisionado em **R$ 0,01** (valor
simbólico), classificado como **Possível** (fase de conhecimento). Esse centavo é proposital — não
"arredonde" para zero nem para o valor da multa.

Se a decisão aplicar **multa cominatória (astreintes)**, aí sim provisione a multa **conforme o
valor da decisão**, seguindo a mesma tabela acima (multa imposta = Provável; afastada = Remota).

### Acordo — cuidado com a aba PEDIDOS

A aba PEDIDOS **nunca é alterada "por causa do acordo" em si**. Ela só muda em dois momentos:

1. **Cadastro inicial:** dano material + dano moral + R$ 0,01 de OBF, **tudo como Possível**.
2. **Após a decisão/homologação:** reclassifica conforme a tabela — valor do acordo em **Provável**,
   o restante do pedido em **Remota**. Nada permanece em Possível.

Para o registro da decisão na aba INSTÂNCIA: use "Acordo Cumprido" **apenas** em casos
pré-sentença (sem decisão judicial). Se já houver decisão, registre a decisão como foi proferida.

### Honorários (procedimento comum)

Em **procedimento comum** com condenação, depois de lançar o valor condenado como Provável,
verifique o rito e **adicione os "Honorários Advocatícios"** já calculados, conforme o
provisionamento. (No Juizado/JEC, em regra, não há condenação em honorários na 1ª instância.)

### Atualização monetária

A regra padrão, salvo decisão judicial diversa, é **INPC + 1% ao mês desde a Data do Fato**. O
Projuris aplica isso automaticamente — basta o campo "Data do Fato" estar preenchido corretamente.
Você não lança a correção à mão.

## Passo 4 — Passo a passo no Projuris (Recálculo de Prognóstico)

Para efetivar a reclassificação depois de uma decisão:

1. Busque o processo no Projuris.
2. Aba **Resumo → Alterar →** mude a fase (ex.: "Recursal — Sentença").
3. Aba **Instância →** selecione a linha **→ Registrar Decisão →** informe a data **→** selecione o
   tipo de decisão (Improcedente, Procedente, Procedente em Parte, etc.). Em qualquer condenação
   pecuniária, a **Decisão Predominante = DESFAVORÁVEL**; em homologação de acordo, **Favorável em
   Parte**.
4. Aba **Pedidos →** selecione a linha do pedido **→ Recálculo de Prognóstico → "Valor" →** lance o
   valor na coluna correta conforme a tabela do Passo 2 **→ justifique** citando a sentença/acórdão.
   - Procedente: lance o valor condenado como **Provável**.
   - Improcedente: **zere Provável e Possível** e deixe o valor total como **Remota** (justifique
     com a sentença improcedente).
   - Procedente em parte / acordo: **Provável** = parcela condenada/acordo; **Remota** = diferença.
5. Aba **Andamento → Adicionar →** "Sentença" (ou "Acórdão") e anexe o documento.
6. Procedimento comum com condenação: adicione os **Honorários Advocatícios** (Passo 3).

No **Astrea**, em paralelo: insira a etiqueta de **Resultado** correspondente (ex.: "Resultado:
Sentença Improcedente"), a etiqueta de **fluxo** ("Aguarda Trânsito em Julgado", "Aguarda
Quitação", etc.) e crie a **tarefa** de acompanhamento (ex.: "Verificar trânsito em julgado").

## Passo 5 — Encerramento (quando o caso chega ao fim)

Quando os valores já estão corretos e o caso está apto, o encerramento se faz no Projuris em
**Resumo → Solicitar Encerramento**, escolhendo um dos motivos:

| # | Motivo de Encerramento (Projuris) | Quando usar |
|---|---|---|
| 1 | Decisão Favorável com Trânsito em Julgado | Improcedência transitada (valor todo em Remota) |
| 2 | Decisão Desfavorável com Pagamento Realizado | Condenação paga (valor em Provável, depois quitado) |
| 3 | Acordo Extrajudicial Cumprido | Acordo sem homologação judicial, já cumprido |
| 4 | Acordo Judicial Cumprido | Acordo homologado e cumprido |
| 5 | Extinção sem Resolução do Mérito | Extinção sem mérito (valor em Remota) |
| 6 | Desistência da Parte Autora | Desistência homologada (valor em Remota) |

No **Astrea**, após o encerramento aprovado pelo cliente: remova as etiquetas de fluxo pendentes,
insira a etiqueta de **resultado final**, conclua as tarefas e marque "encerrar pasta após
faturamento".

Observação: o cliente trabalha com uma lista própria de motivos aprovados (Improcedência, Acordo,
Acordo Pós Sentença, Procedência Parcial, Procedência Total, Desistência da Ação, Extinto sem
Julgamento do Mérito e — só em RPP — Extinto com Julgamento do Mérito; "Cadastro Indevido" exige
autorização do cliente por e-mail). Se o usuário precisar do motivo na taxonomia do cliente, mapeie
a partir da decisão real do caso.

## Formato da resposta

Responda de forma direta e acionável. Use este modelo:

```
Fase identificada: <fase + decisão>

Lançamento dos pedidos:
- <Pedido 1>: R$ <valor> em "Valor Perda <Provável/Possível/Remota>"
- <Pedido 2 / OBF>: R$ <valor> em "Valor Perda <...>"
(soma confere com o valor total do pedido)

Por quê: <1-2 frases citando a regra>

Como lançar no Projuris:
1. <passos do Recálculo de Prognóstico>
Astrea: <etiquetas/tarefa>

Encerramento (se aplicável): <motivo>
```

Sempre **confira se a soma das três colunas bate com o valor total do pedido** e avise o usuário se
algo não fecha. Quando faltar um dado essencial (fase, valor condenado), pergunte antes de
classificar.

## Exemplo

**Entrada:** "Processo 5003078-61, em conhecimento, dano moral R$ 10.000 + obrigação de fazer.
Vai ser encerrado por acordo de R$ 4.000. Hoje está tudo em Possível."

**Saída:**

Fase: houve acordo homologado → não pode mais ficar em Possível.

Lançamento:
- Dano moral: R$ 4.000,00 em **Valor Perda Provável** + R$ 6.000,00 em **Valor Perda Remota**.
- Obrigação de Fazer: R$ 0,01 — segue conforme a decisão sobre a OBF (se afastada, Remota; se
  imposta, Provável). Não permanece em Possível.

Por quê: acordo homologado reparte o pedido entre Provável (valor do acordo) e Remota (diferença);
após a decisão nenhum valor fica em Possível (cap. 29.5 e 39.1).

Como lançar: Resumo → Alterar fase; Instância → Registrar Decisão (Acordo / Favorável em Parte);
Pedidos → Recálculo de Prognóstico → lançar R$ 4.000 em Provável e R$ 6.000 em Remota → justificar.
Astrea: etiqueta de resultado + "Aguarda Quitação".

Encerramento: "Acordo Judicial Cumprido" (motivo 4) após o cumprimento.
