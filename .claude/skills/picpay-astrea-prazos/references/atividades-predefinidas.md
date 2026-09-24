# Atividades Predefinidas no Astrea (11 fluxos)

Prazos em dias uteis relativos a data de criacao ou de evento. "Responsavel pelo prazo/audiencia" = advogado
titular na agenda. "Conforme atividade predefinida" = colaborador alocado aquela funcao (cadastro vigente).

## 30.1 CIVEL: Audiencia (5 tarefas) -- controladoria
A tarefa "Elaborar Defesa" gera automaticamente as etiquetas CONTESTACAO + AUDIENCIA DESIGNADA.
1. Confirmar modalidade da audiencia -- D-10 -- predefinida -- Baixa
2. Elaborar Defesa (protocolo antes da audiencia) -- D-10 -- resp. prazo/audiencia -- Alta
3. Contratar advogado e preposto correspondente (se presencial) -- D-7 -- predefinida -- Baixa
4. Verificar providencias (e-mail preposto/advogado + substabelecimento + carta de preposicao) -- D-5 -- resp. prazo/audiencia -- Baixa
5. Obter ATA e verificar prazos/providencias -- D+1 -- predefinida -- Baixa

## 30.2 CIVEL: Audiencia Pre-Processual PicPay (8 tarefas, tag PRE-PROCESSUAL) -- controladoria
1. Preparar subsidios -- D+0(criacao) -- resp. prazo/audiencia
2. Regularizar a representacao -- D+0(evento) -- criador da tarefa
3. Verificar proposta de acordo com ponto focal PicPay -- D+0(evento) -- predefinida
4. Abrir requisicao de subsidios -- D+1(criacao) -- predefinida
5. Conferir ata e providenciar cumprimento do acordo -- D+1(evento) -- resp. prazo/audiencia
6. Confirmar quem realizara a audiencia (PP/Escritorio/Correspondente) -- D+3(criacao) -- resp. prazo/audiencia
7. Comprovar cumprimento do acordo -- D+5(evento) -- resp. prazo/audiencia
8. Enviar pasta para encerramento -- D+10(evento) -- resp. prazo/audiencia

## 30.3 Interesse Recursal - PicPay/Original (5 tarefas) -- controladoria (conclui gerando etiqueta RECURSO)
1. Analisar Recurso/Dispensa Automatica e Acordo Pos -- D+1 -- resp. prazo/audiencia
2. Verificar se houve resposta do interesse recursal / Acordo Pos -- D+1 -- predefinida
3. Verificar se houve retorno do interesse recursal / Acordo Pos -- D+2 -- resp. prazo/audiencia
4. Elaborar guia recursal (se autorizado nos comentarios) -- D+3 -- predefinida
5. Verificar pagamento no Projuris - Guia (gera etiqueta RECURSO) -- D+6 -- predefinida

## 30.4 PICPAY: OBF / LIMINAR / Complementacao de Subsidios (3 tarefas, prioridade Alta) -- controladoria
1. Preparar solicitacao -- D+0 -- resp. prazo/audiencia
2. Inserir requisicao no Projuris -- D+0 -- predefinida (assistente)
3. Analisar requisicao e enviar para aprovacao -- D+0 -- predefinida

## 30.5 Subsidios - PICPAY (6 tarefas)
1. Conferir prazos/audiencia no Astrea -- D+2 -- resp. prazo/audiencia
2. Analise do caso (estrategico/middle-sensivel) e eventual preparacao de subsidios -- D+7 -- resp. prazo/audiencia
3. Habilitar -- D+7 -- predefinida
4. Enviar subsidios (se nao enviado pela OITO ou se reprovado) -- D+8 -- predefinida
5. Conferir prazos/audiencia (apos habilitacao) -- D+9 -- predefinida
6. Analisar subsidios e acordo -- D+16 -- resp. prazo/audiencia

## 30.6 ACORDO PRE-PROCESSUAL (4 tarefas) -- gatilho: acordo em audiencia pre-processual
1. Alimentar Projuris: Fase, Instancia, Pedidos e Andamentos -- D+0 -- resp. prazo/audiencia
2. Solicitar pagamento - Acordo Pre-Processual -- D+1 -- predefinida
3. Verificar comprovante de pagamento e protocolar -- D+4 -- resp. prazo/audiencia
4. Encaminhar pasta para encerramento -- D+6 -- resp. prazo/audiencia

## 30.7 PICPAY - ACORDO POS - ETAPA 01 (4 tarefas)
1. Atualizar condenacao + OBF + andamentos -- PRIORIZAR -- D+0 -- resp. prazo/audiencia
2. Preencher planilha de acordos -- D+0 -- predefinida
3. Validar valor nos autos. Preencher CONFERIDO POR + DATA -- D+0 -- predefinida
4. Contatar patrono adverso com as ofertas -- D+1 -- predefinida

## 30.8 Pagamento da Condenacao - Equipe Consumidor (4 tarefas)
1. Registrar decisao e provisionar (Projuris) -- D+1 -- resp. prazo/audiencia
2. Elaborar calculo -- D+2 -- resp. prazo/audiencia
3. Inserir requisicao de pagamento -- D+3 -- predefinida
4. Verificar pagamento no Projuris (gera etiqueta PAGAMENTO - CONDENACAO) -- D+5 -- predefinida

## 30.9 PICPAY - AGRAVO DE INSTRUMENTO (4 tarefas)
1. Abrir requisicao de pagamento de custas - Agravo -- D+2 -- predefinida
2. Aprovar requisicao de pagamento - Agravo -- D+2 -- predefinida
3. Alimentar Projuris - Agravo (Instancia + Andamentos) -- D+7 -- resp. prazo/audiencia
4. Informar agravo nos autos principais -- D+8 -- resp. prazo/audiencia

## 30.10 PICPAY/ORIGINAL - ACORDO PRE-SENTENCA (12 tarefas)
1. Preparar parecer + enviar requisicao de autorizacao de acordo -- D+0 -- predefinida
2. Atualizar andamentos (autorizacao/negativa + justificativa) -- D+1 -- predefinida
3. Preencher planilha de acordos -- D+2 -- predefinida
4. Validar valor (requisicao x planilha). CONFERIDO POR + DATA -- D+2 -- predefinida
5. Contatar patrono adverso com as ofertas -- D+3 -- predefinida
6. Elaborar minuta (se autorizado) -- D+5 -- predefinida
7. Enviar minuta ao advogado contrario + assinatura interna -- D+5 -- predefinida
8. Validar minuta (acordo x requisicao) e autorizar -- PRIORIZAR -- D+5 -- resp. prazo/audiencia
9. Analisar necessidade de OBF e inserir atividades -- D+6 -- resp. prazo/audiencia
10. Protocolar minuta + atualizar andamento Projuris -- D+6 -- predefinida
11. Solicitar pagamento (se autorizado) -- D+6 -- predefinida
12. Peticionar pagamento + preparar encerramento + agendar (atencao com custas) -- D+11 -- resp. prazo/audiencia

## 30.11 PicPay/Original - Encerramento (2 tarefas)
Gatilho: caso apto -> criar prazo "ENCERRAMENTO: INSERIR MOTIVO".
1. Preparar a pasta para encerrar -- D+1 -- criador da tarefa
2. Analise para aprovacao do encerramento -- D+2 -- predefinida

## Mapa de fluxos por momento do caso
- ENTRADA: 30.5 (Subsidios) + 30.4 (OBF/Liminar se necessario). 30.1 (Audiencia) ou 30.2 (Pre-Processual) + 30.6 (Acordo Pre-Processual). 30.10 (Acordo Pre) se identificado.
- APOS SENTENCA/ACORDAO: 30.3 (Interesse Recursal). -> Dispensa Recursal -> 30.7 (Acordo Pos Etapa 01) -> se infrutifero -> 30.8 (Pagamento da Condenacao). -> Recurso autorizado -> 30.9 (Agravo) ou demais recursos.
- ENCERRAMENTO: 30.11.
