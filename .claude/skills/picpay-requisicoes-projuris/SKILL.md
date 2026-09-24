---
name: picpay-requisicoes-projuris
description: >-
  Modulo de Requisicoes do Projuris para a carteira PicPay (BFAP): subsidios (dossie), cumprimento de
  OBF/liminar, pagamento (condenacao/acordo/custas/reembolso), analise recursal (parecer + cadastro passo a
  passo) e proposta de acordo. Use SEMPRE que for abrir/preencher requisicao no Projuris, precisar do padrao
  de titulo (PRAZO DD/MM/AAAA - ...), atributos obrigatorios, exigiveis/anexos, SLAs (subsidios 8d,
  pagamento/recursal 5d, OBF 2-5d), limite 40MB, status (cores), data de corte, ou regras de acordo (10 dias
  uteis). Aciona com "como abro requisicao de subsidios", "titulo da requisicao de pagamento", "requisicao de
  analise recursal", "passo a passo da analise recursal no Projuris", "modelo de parecer recursal", "como
  cadastro a dispensa recursal", "status reprovada/devolvida", "reembolso". NAO use para decidir SE recorre
  (skill diretrizes-recursais), nem para cadastro, Astrea, teses ou encerramento.
---

# Requisicoes no Projuris - PicPay (BFAP)

Toda solicitacao ao PicPay (dossie, OBF/liminar, pagamento, analise recursal, acordo) passa pelo modulo de
**Requisicoes** do Projuris. Cada tipo tem SLA, exigiveis e **padrao de titulo obrigatorio**. Comunicacao
com o cliente sempre pelos canais oficiais (geral: `contencioso@picpay.com`; oficios/sigilo:
`oficios@picpay.com`; UOC Original: `juridicocontencioso@original.com.br`).

Padrao de titulo (memorize): **PRAZO DD/MM/AAAA - TIPO - NOME DA PARTE - Nº DO PROCESSO**. Exemplos por
tipo em `references/titulos-padrao.md`.

## 1. Solicitacao de Subsidios (dossie)

Abertura: `PROCESSOS -> TODOS -> Busca Rapida -> pasta -> REQUISICOES -> ADICIONAR`. Tipo: "Solicitacao de
Subsidios - PicPay" + BFAP. Preencher campos azuis em DADOS GERAIS e em ATRIBUTOS.

**Atributos obrigatorios:** Subsidios urgentes? (Sim/Nao + justificativa); Sintese da demanda; Causa Raiz;
Nome do autor; CPF/CNPJ do autor; Audiencia (Sim/Nao + data); Prazo para defesa (fatal util); Observacoes
(do que trata a acao e o que sera necessario na defesa).

**Titulo:** `PRAZO DD/MM/AAAA - SOLICITACAO DE SUBSIDIOS - NOME DA PARTE - Nº DO PROCESSO`.
Complementacao de dossie ja enviado: `PRAZO ... - RETORNO DO ESCRITORIO - NOME DA PARTE - Nº DO PROCESSO`.
- **Prazo normal: 8 dias uteis. Urgente: 2 dias uteis (com justificativa).** SLA: aberta **no dia do cadastro da pasta**.

**Exigiveis/envio:** guia EXIGIVEIS (excluir os nao necessarios) -> DOCUMENTOS (ADICIONAR + Tipo de Exigivel)
-> RESUMO -> ENVIAR PARA APROVACAO -> DADOS GERAIS preencher HISTORICO -> salvar. Status vira "AGUARDANDO
APROVACAO" (amarelo).

**Restricoes criticas:**
- **Premissa contrato assinado**: se voltar sem contrato, solicitar complementacao e sinalizar ao Juridico PicPay (o escritorio pode ser responsabilizado se nao pediu).
- **VEDADO juntar aos autos o historico de contatos do usuario (chat/SAC)** -- contem dados sensiveis. Para juntar tela/info especifica, validar antes com o Juridico PicPay.
- **Limite total de anexos: 40 MB** (evita falha no Zendesk dos dossies). Excedeu -> alterar fase para "Em requisicao", corrigir e reenviar.
- Sempre incluir a **carta de citacao** na pasta e na requisicao.

## 2. Cumprimento de OBF / Liminar

`REQUISICOES -> ADICIONAR` -> Tipo "Cumprimento de Obrigacao de Fazer - PicPay" ou "Cumprimento de Liminar
- PicPay". Titulo: `PRAZO DD/MM/AAAA - CUMPRIMENTO DE OF - NOME DA PARTE - Nº DO PROCESSO`. Em DETALHES, a
**decisao judicial deve vir INTERPRETADA** (pontuar as determinacoes com acoes especificas a equipe de
dossies). Prazo de cumprimento: 2, 3, 4 ou 5 dias uteis (2 dias abre campo JUSTIFICATIVA). Exigiveis
obrigatorios: **decisao judicial e peticao inicial**.

**Casos especiais:**
- Declaracao de inexigibilidade de qualquer contrato -> **somente com esgotamento das vias recursais** e "de acordo" do Juridico Interno.
- Decisao liminar / sentenca nao definitiva com inexigibilidade -> **nao declarar inexigivel, apenas SUSPENDER cobrancas**.
- Reestabelecimento de limite no cartao / reativacao de conta -> obrigacao **impossivel** -> abrir requisicao de analise recursal (Agravo).

## 3. Solicitacao de Pagamento

Tipo "Pagamento - Civel - PicPay". Pagamentos com **minimo 5 dias uteis** de antecedencia do fatal
(reembolso e excepcional e pode ser falha do escritorio). Titulo: `PRAZO DD/MM/AAAA - PAGAMENTO - TIPO
(ACORDO/CONDENACAO/CUSTAS RECURSAIS/OFICIAL DE JUSTICA) - Nº DO PROCESSO`. Valor = igual a guia (nunca
zerado). Unidade Organizacional = entidade do polo responsavel pelo pagamento.

- **Atributos:** Tipo de Pagamento (Conta Contabil carrega automaticamente -- nao alterar); Centro de Custo (validar pela causa raiz); Guia (Sim -> codigo de barras); dados bancarios quando sem guia.
- **Documentos obrigatorios:** Condenacao -> Guia, Calculo, Acordao, Sentenca. Acordo -> Minuta. Custas -> Guia.
- **Guias em PDF:** salvar em PDF, **NAO usar "imprimir em PDF"** (fica protegido e ilegivel).
- **Reembolso** (excepcional): Tipo "Pagamento Reembolso - Civel - PicPay"; titulo `PRAZO ... - REEMBOLSO - TIPO - Nº`; em Detalhes informar o motivo; apos pagar, anexar comprovante e finalizar.
- Em pagamento de condenacao, **sempre sinalizar** se e caso de dispensa recursal ou esgotamento de vias (anexar acordao).

**Regras temporais e vedacoes:**
- Urgentes: cadastrar ate **10h do dia anterior** ao fatal, com tag URGENTE (aprova/rejeita no mesmo dia). Demais: aprovacao em D+1.
- Guias que vencem na emissao (ex.: DARE): encaminhar no **2º dia util** da solicitacao.
- Apos lancamento urgente: confirmar comprovante no Projuris **ate as 15h** do dia seguinte; senao sinalizar por e-mail e WhatsApp.
- **Ultimos 3 dias uteis do mes: VEDADO solicitar pagamentos** (data de corte -- liquidaria so no mes seguinte).
- Nome do arquivo <= 60 caracteres; abreviar atributos longos (limite da integracao).
- **NUNCA finalizar requisicoes** (especialmente reprovadas) -- a atualizacao de status e automatica; "Finalizada" so apos todo o fluxo, com baixa por robo.

Status das requisicoes (cores) e significado em `references/status-requisicoes.md`.

## 4. Analise Recursal

Enviar com **minimo 5 dias uteis** do fatal recursal. Tipo "Analise Recursal - PicPay" + BFAP. A decisao de
SE recorrer e o **formato do parecer** seguem a skill `picpay-diretrizes-recursais`. Cadastro em 5 passos:

**Passo 1 - Parecer.** Preencher o Parecer Recursal a partir do modelo padrao em Google Docs
(https://docs.google.com/document/d/1rSAe0T3E2RBwo-tE80tyNXe-G9dj-WYYIhF7GfvTh6I/edit -- fazer uma copia e
preencher). Estrutura: Objeto; Resumo da Inicial; Pedidos; Resumo do Dossie; Resumo da Sentenca; Resumo da
Condenacao; Prazos + media de preparo + valor atualizado; e a conclusao (**Parecer Recursal**). **Guarde o
ultimo topico (a conclusao) separadamente** -- ele vai no campo Observacoes do Passo 4.

**Passo 2 - Adicionar.** Na pasta do processo: aba **REQUISICOES -> ADICIONAR** (a aba fica no fim da barra
de navegacao; pode ser preciso rolar para a direita).

**Passo 3 - Dados Gerais.**
- **Titulo:** `Prazo: DD/MM - DISPENSA RECURSAL - APELACAO - Nº DO PROCESSO` (ou `INTERPOSICAO DE RECURSO -
  TIPO DO RECURSO - Nº`, conforme a conclusao). Ex.: `Prazo: 13/03 - DISPENSA RECURSAL - APELACAO -
  0731806-66.2025.8.07.0001`.
- **Tipo de Requisicao:** `Analise Recursal - PicPay`.
- **Detalhes:** colar **integralmente** o parecer do Passo 1.
- **Unidade Organizacional:** unidade correspondente (ex.: `Org - PicPay`).

**Passo 4 - Atributos.**
- **Tipo:** `Recurso` (ou `Oposicao ED` / `Dispensa Recursal`, conforme o caso).
- **Observacoes:** colar **somente o ultimo topico do parecer** (a conclusao/recomendacao).

**Passo 5 - Enviar e anexar.** `Salvar` ou `Salvar e Proximo`; com a requisicao aberta, **anexar os
documentos** do caso. Em duvida na anexacao, pedir orientacao antes de prosseguir.

> **Casos SEM valor e SEM parecer sao devolvidos** imediatamente, com nova contagem de prazo -- por isso o
> parecer completo em Detalhes e o valor (em inexigibilidade, sempre informar) sao indispensaveis.

## 5. Avaliacao de Proposta de Acordo

Tipo "Analise de Proposta de Acordo - PicPay". Titulo: `PRAZO DD/MM/AAAA - PROPOSTA DE ACORDO - PARTE
AUTORA - Nº` (ou `CONTRAPROPOSTA DE ACORDO`). Em ATRIBUTOS/Observacoes: resumo da demanda + proposta +
escritorio responsavel.

- **Prazo minimo de pagamento do acordo: 10 dias uteis APOS a homologacao.** Prazo inferior -> sinalizar coordenacao e Juridico Interno.
- **Extrajudicial** (acordo SEM defesa apresentada) -> andamento "Acordo Extrajudicial". **Judicial** (acordo COM defesa) -> andamento "Acordo"; cumprimento em 10 dias uteis do protocolo.
- Aba PEDIDOS **nunca** e alterada por motivo de acordo (so no cadastro inicial e apos sentenca). "Acordo Cumprido" na aba INSTANCIA so para casos **pre-sentenca** (sem decisao judicial); com decisao, registrar a decisao proferida (ver skill de decisoes/encerramento).

## 6. Casos Estrategicos

Edicao da planilha compartilhada **SUSPENSA desde 05/11/2024**. Identificacao agora por **e-mail
individual a coordenacao (Bianca)**: titulo `BFAP - NOME DO AUTOR - Nº DO PROCESSO - Nº DA PASTA - CASO
ESTRATEGICO - [ASSUNTO]`, escolhendo um dos assuntos (Autorizacao para envio de requisicao / Sem o retorno
do dossie / Com o retorno do dossie). Anexar inicial, documentos e dossie. Apos enviar, criar tarefa no
Astrea com o titulo do e-mail.

## Principio

O titulo padronizado e o parecer completo nao sao formalidade: requisicoes incompletas voltam e reiniciam
o prazo, e pagamentos fora do SLA viram responsabilidade do escritorio. Preencher certo na primeira vez e
o que protege o prazo e a avaliacao da BFAP.
