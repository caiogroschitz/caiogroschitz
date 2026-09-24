# Sistema de Etiquetas Astrea - Operacional (6 categorias)

## 1. Identificacao (cadastro)
CONTRATANTE (PICPAY, verde) / FASE (CONHECIMENTO-SENTENCA-ACORDAO-EXECUCAO, laranja) / AREA (CIVEL, azul claro).
Adicionais: MIDDLE, ESTRATEGICO, ADVOGADO LITIGANTE.

## 2. Tipo de Prazo (desde 27/04/2026)
| Tipo de Prazo | Etiqueta |
|---|---|
| Acordo Pre-Processual | ACORDO |
| Acordo Pos-Sentenca | ACORDO |
| Subsidios | SUBSIDIOS |
| Contestacao | CONTESTACAO |
| Recurso | RECURSO |
| Comprovar OBF | OBRIGACAO DE FAZER |
| Comprovar Liminar | LIMINAR |
| Manifestacao | MANIFESTACAO |
| Pagamento de Condenacao | CONDENACAO |
| Casos urgentes (todos os tipos) | URGENTE |

## 3. Status do Prazo (vigencia 30/04/2026)
| Etiqueta | Significado |
|---|---|
| PRAZO EM SEGURANCA | Dentro do D-2 (2+ dias uteis ate o fatal). |
| PRAZO EM CURSO | Fora do D-2, execucao iminente -- priorizar. |
| REAGENDADO | Prazo reagendado, sempre com justificativa na planilha. |
Obs.: "Em Seguranca"/"Em Curso" em prazo reagendado devem vir junto com "REAGENDADO".

## 4. Automaticas (a partir de tarefa predefinida)
- CONTESTACAO e AUDIENCIA DESIGNADA -- inseridas automaticamente ao criar a tarefa de audiencia.

## 5. Fluxo (acompanhamento)
AGUARDA COMPROVANTE DE PGTO / AGUARDA DECISAO DE SEGUNDA INSTANCIA / AGUARDA NEGOCIACAO DE ACORDO PRE /
AGUARDA NEGOCIACAO DE ACORDO POS / AGUARDA QUITACAO / AGUARDA TRANSITO EM JULGADO / RECURSO - AUTOR / RECURSO - REU.

## 6. Resultado (sempre que houver decisao, em paralelo ao Projuris)
Sentencas (1a inst.): Improcedente / Procedente em Parte / Totalmente Procedente / Extinto sem resolucao do merito.
2a Instancia: Negado Provimento / Dado Provimento / Dado Parcial Provimento (Cliente ou Parte Contraria) / Nao conhecido o recurso da parte contraria.
Instancia Superior: Dado Provimento / Negado Provimento (Cliente ou Parte Contraria).
Acordos: Acordo / Acordo realizado por outra Reclamada / Acordo Pos / Acordo Pos infrutifero / Acordo Pre / Acordo Pre infrutifero / Acordo Pre reprovado.
