---
name: picpay-cadastro-projuris
description: >-
  Guia operacional para cadastrar e sanear processos da carteira PicPay no Projuris (sistema do cliente),
  pela equipe BFAP. Use SEMPRE que o usuario precisar cadastrar/incluir um novo processo, preencher os
  campos do Projuris (Dados Gerais, Polo Passivo/Ativo, Desdobramento Inicial, Advogados, Informacoes
  Financeiras, Atributos), definir a Causa Raiz (CR1/CR2), o Grupo Responsavel/UOC (PicPay x Original),
  classificar o caso (Massificado/Middle/Estrategico), registrar andamentos obrigatorios ou nomear
  documentos da pasta. Aciona com pedidos como "como cadastro esse processo do PicPay", "qual a causa raiz
  desse caso", "esse caso e do PicPay ou do Original", "isso e middle ou estrategico", "como preencho o
  polo passivo", "qual entidade/CNPJ do grupo", "como registro o andamento", "padrao de nomenclatura dos
  documentos" ou "saneamento da pasta". NAO use para sistema Astrea/prazos, teses de defesa, diretrizes
  recursais, requisicoes ou encerramento (skills proprias).
---

# Cadastro e Saneamento de Processos PicPay no Projuris (BFAP)

O Projuris e o sistema **do cliente PicPay**. A qualidade do cadastro alimenta o provisionamento contabil, a triagem da equipe, a estrategia de defesa e o controle de prazos. Erros de cadastro sao tratados como **falha do escritorio** e impactam a avaliacao e a distribuicao de novos processos -- por isso vale a pena preencher com cuidado e conferir sempre com o sistema processual (TJ).

Use esta skill para conduzir o cadastro de ponta a ponta e para o saneamento periodico. Os dados extensos (tabela de Causa Raiz por BU, CNPJs das entidades, regras de classificacao e o rol de andamentos) estao em `references/` -- leia-os quando o caso concreto exigir o detalhe.

## Sequencia de abas do cadastro

Ao incluir um novo processo (`Processos` -> `Incluir Processo`), preencha nesta ordem:
**Dados Gerais -> Polo Passivo -> Polo Ativo -> Desdobramento Inicial -> Advogados -> Informacoes Financeiras -> Atributos.**

## 1. Dados Gerais

| Campo | Como preencher |
|---|---|
| Pasta | Automatico. |
| Data de Inicio | Data da distribuicao do processo. |
| Data de Citacao | Apos o recebimento da citacao. |
| Natureza | Sempre **Civel**. |
| Tipo de Acao | Sempre a acao do **processo principal** (ver anexo de tipos aceitos no Projuris). |
| Procedimento | Administrativo, Cautelar, Especial, Execucao, Extrajudicial, Ordinario, Recursal, Sumario ou Sumarissimo. |
| Unidade Organizacional | Entidade do grupo no polo passivo (PicPay SP, PicPay Vix, PicPay Invest, PicPay Bank, Crednovo, GuiaBolso Financas, GuiaBolso Pagamentos, Liga Invest, BX Blue). |
| **UOC** (Unid. Org. Centralizadora) | So PicPay -> "Org - PicPay". So Original -> "Org - Banco Original". **PicPay E Original -> "Org - PicPay".** |
| **Data do Fato** | Data do efetivo prejuizo. **Determina o Grupo Responsavel** (ver secao 3). |
| Causa Raiz | Rol taxativo. Sempre CR1; CR2 quando aplicavel (ver `references/causa-raiz.md`). |
| Fase | Conhecimento / Recursal - Sentenca / Recursal - Acordao / Execucao Definitiva (definicoes abaixo). |
| Tipo de Processo | Judicial ou Administrativo (cartas-convite pre-processuais = Administrativo). |
| Parceiro Responsavel | So empresas parceiras que respondam pelo caso. Sem apontamento -> em branco. |
| Grupo Responsavel | PicPay ou Banco Original -- regra automatizada (ver secao 3). |
| Pedido de Liminar | Marcar sempre que houver tutela de urgencia. |
| Estrategico | Marcar conforme `references/classificacao.md`. |
| Resumo da Demanda | Produto envolvido, alegacao do autor, pedidos. |
| Terceiro Envolvido | Obrigatorio quando ha mais de uma empresa do grupo no polo. |

**Definicoes de Fase.** *Conhecimento*: antes da sentenca. *Recursal - Sentenca*: ha decisao de 1a instancia (com ou sem recurso). *Recursal - Acordao*: alterar logo apos o julgamento do recurso. *Execucao Definitiva*: apos o transito em julgado de sentenca procedente.

## 2. Polo Passivo, Polo Ativo e Desdobramento Inicial

- **Polo Passivo**: cadastrar a(s) entidade(s) **exata(s)** indicada(s) na inicial, conferindo com o sistema processual. Condicao sempre **REU**. Havendo mais de uma entidade do grupo, registrar todas e marcar o atributo "Mais de uma empresa do grupo no Polo? = Sim". CNPJs em `references/entidades-cnpj.md`.
- **Polo Ativo**: cadastrar a parte adversa com CPF (PF) ou CNPJ. Use "Cadastro Rapido" se ainda nao existir. Condicao **AUTOR**. OAB no formato `123456SP`. Litisconsorcio na Nota; se nao houver, "N/A". Autor sem CPF em pasta ja aberta e **excecao** -- incluir via `Entidades -> Todos`, validando homonimo antes.
- **Desdobramento Inicial**: e o cadastro inicial do processo principal (nao e apenso/incidente). Numero sempre no padrao **CNJ**. Para tribunais superiores, criar **nova linha** em Instancias -- nao alterar a originaria. Jurisdicao = VARA CIVEL ou JUIZADO ESPECIAL CIVEL. Comarca com nome "limpo".

## 3. UOC e Grupo Responsavel (PicPay x Original)

A atribuicao decorre da **UOC** e segue **data do fato + dossie**:

- **Data do fato >= 15/07/2023 -> sempre PICPAY.**
- **Data do fato < 15/07/2023 ->** pode ser PicPay ou Original, conforme o dossie. Historicamente, negativacao e produtos de credito eram do **Original**.

Regra pratica de canal: UOC PicPay -> time PicPay -> `contencioso@picpay.com`. UOC Original -> time Original -> `juridicocontencioso@original.com.br`. **Casos com PicPay E Original no polo sao cadastrados no ambiente do PicPay, com patrocinio em nome de ambos.**

## 4. Advogados

- **Parte adversa**: buscar em "Advogado Da Parte Adversa -> Busca Rapida". Se nao houver, criar Entidade (Dados Gerais com o nome -> Dados Complementares "Advogados (Processos)" -> Tipo de Documento OAB no formato `UFxxxx`) e retomar o cadastro. O principal adverso e preenchido automaticamente -- manter.
- **Escritorio do cliente**: incluir apenas o **escritorio** (BFAP Advogados), nunca o advogado individual.

## 5. Informacoes Financeiras e Atributos

- Natureza Financeira: **Passiva** (regra civel; Ativa so em Recuperacao de Credito).
- Valor da Causa: o da inicial. **Provisionar: sempre marcar.**
- Centro de Custo: conforme tabulacao da causa raiz -- nunca em branco/incorreto; em duvida, acionar o Juridico Interno.
- Atributos: **Fraude** = "Sim" so com fraude constatada no dossie; **Status Atual**; **Mais de uma empresa do grupo no Polo?** = "Sim" abre campo para indicar a outra empresa.

## 6. Classificacao do caso

Massificado (padrao automatizado), **Middle** (pedido R$ 100 mil-500 mil; lucros cessantes; Nome Social) e **Estrategico** (pedido >= R$ 500 mil; Inquerito Civil; ACP; risco de imagem; objeto nao consumerista; acoes de parceiros/concorrentes; ou definicao da gestao). Em conflito, **prevalece a classificacao mais restritiva**. Refletir em **ambos os sistemas**: atributo "Estrategico" no Projuris e etiqueta MIDDLE/ESTRATEGICO no Astrea. Detalhes e atribuicao da equipe em `references/classificacao.md`.

## 7. Pre-Processual

Carta-convite para audiencia de conciliacao -> **Tipo de Processo = ADMINISTRATIVO**. Sinalizar **imediatamente** o Juridico Interno PicPay (ha tratativa de pauta/limites de acordo). Casos com audiencia agendada **nao podem ficar sem proposta de acordo**. Oficios e quebra de sigilo vao para `oficios@picpay.com`.

## 8. Andamentos obrigatorios e documentos

Andamentos seguem **rol taxativo** com nomenclatura exata (essencial para retirar pauta e identificar status). Marcar "Listar como andamento"; "Relevante" so em audiencia e decisoes; para decisoes incluir **sempre o dispositivo** em Detalhes. Documentos: cadastrar na aba `Documentos`, peca e decisao com cadastro proprio, **numeracao antes da nomenclatura** e tudo em MAIUSCULAS (ex.: `1. PETICAO INICIAL`, `5. SENTENCA`). Rol completo de andamentos e adicionais de mai/2025 em `references/andamentos.md`.

## 9. Saneamento periodico

Verificar continuamente (a cada movimentacao relevante) e em ciclos da coordenacao: Causa Raiz (CR1/CR2), Data do Fato, UOC/Grupo Responsavel, classificacao Middle/Estrategico, Fase, Atributos, andamentos do rol e **consistencia Projuris x Astrea**. Inconsistencias -> corrigir imediatamente.

## Regra de ouro

Se nenhuma combinacao BU/Produto/CR1/CR2 refletir o caso, **NAO criar valores aleatorios** -- sinalizar a coordenacao BFAP, que trata a inclusao com o time interno PicPay. O mesmo vale para qualquer campo em que falte instrucao: pergunte a coordenacao em vez de improvisar, porque o cadastro errado se propaga para provisionamento e prazos.
