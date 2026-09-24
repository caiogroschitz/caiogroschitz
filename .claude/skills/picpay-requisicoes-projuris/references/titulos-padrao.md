# Padroes de Titulo das Requisicoes (Projuris)

Forma geral: **PRAZO DD/MM/AAAA - TIPO - NOME DA PARTE / Nº DO PROCESSO**.

| Requisicao | Tipo de Requisicao | Titulo |
|---|---|---|
| Subsidios (normal/urgente) | Solicitacao de Subsidios - PicPay + BFAP | PRAZO DD/MM/AAAA - SOLICITACAO DE SUBSIDIOS - NOME DA PARTE - Nº DO PROCESSO |
| Complementacao de dossie | (mesma) | PRAZO DD/MM/AAAA - RETORNO DO ESCRITORIO - NOME DA PARTE - Nº DO PROCESSO |
| Cumprimento OBF | Cumprimento de Obrigacao de Fazer - PicPay | PRAZO DD/MM/AAAA - CUMPRIMENTO DE OF - NOME DA PARTE - Nº DO PROCESSO |
| Cumprimento Liminar | Cumprimento de Liminar - PicPay | PRAZO DD/MM/AAAA - CUMPRIMENTO DE OF - NOME DA PARTE - Nº DO PROCESSO |
| Pagamento | Pagamento - Civel - PicPay | PRAZO DD/MM/AAAA - PAGAMENTO - TIPO (ACORDO/CONDENACAO/CUSTAS RECURSAIS/OFICIAL DE JUSTICA) - Nº DO PROCESSO |
| Reembolso | Pagamento Reembolso - Civel - PicPay | PRAZO DD/MM/AAAA - REEMBOLSO - TIPO - Nº DO PROCESSO |
| Interposicao de recurso | Analise Recursal - PicPay + BFAP | PRAZO DD/MM/AAAA - INTERPOSICAO DE RECURSO - TIPO DO RECURSO - Nº DO PROCESSO |
| Dispensa de recurso | Analise Recursal - PicPay + BFAP | PRAZO DD/MM/AAAA - DISPENSA DE RECURSO - TIPO DO RECURSO - Nº DO PROCESSO |
| Proposta de acordo | Analise de Proposta de Acordo - PicPay | PRAZO DD/MM/AAAA - PROPOSTA DE ACORDO - PARTE AUTORA - Nº DO PROCESSO |
| Contraproposta de acordo | Analise de Proposta de Acordo - PicPay | PRAZO DD/MM/AAAA - CONTRAPROPOSTA DE ACORDO - PARTE AUTORA - Nº DO PROCESSO |
| Caso estrategico (e-mail) | -- (e-mail a coordenacao Bianca) | BFAP - NOME DO AUTOR - Nº DO PROCESSO - Nº DA PASTA - CASO ESTRATEGICO - [ASSUNTO] |

## Demais campos do titulo (subsidios)
- Solicitante: BFAP. Grau de urgencia: Normal ou Urgente.
- Detalhes: sintese; causa raiz (tema); CPF do autor; nº da requisicao do Projuris; data da defesa e da audiencia; anexos (inicial, documentos, decisao se for OF).
- Unidade Organizacional: PicPay. Unidade de Controle: Juridica.

## SLAs por tipo
| Atividade | SLA |
|---|---|
| Subsidios normais | 8 dias uteis; aberta no dia do cadastro |
| Subsidios urgentes | 2 dias uteis (justificativa); aberta no dia do cadastro |
| OBF | 2 a 5 dias uteis (2 com justificativa) |
| Pagamentos | minimo 5 dias uteis antes do fatal |
| Analise Recursal | minimo 5 dias uteis antes do fatal recursal |
| Acordo - pagamento PicPay | minimo 10 dias uteis APOS homologacao |
