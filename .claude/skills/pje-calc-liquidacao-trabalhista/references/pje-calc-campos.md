# Mapa fiel dos módulos e campos do PJe-Calc — e de onde vem cada dado

Referência baseada no Manual oficial do PJe-Calc (CSJT). A ordem e os nomes
abaixo seguem o menu real do sistema (perfil calculista / PJe-Calc Cidadão). Para
cada campo relevante, indica-se **a origem do dado nos autos** e os pontos onde
mais se erra. Use isto para montar o roteiro na mesma sequência das telas.

## Índice
1. Atualizar tabelas (pré-requisito)
2. Novo Cálculo → Dados do Processo
3. Novo Cálculo → Parâmetros do Cálculo
4. Faltas
5. Férias
6. Histórico Salarial
7. Verbas (Lançamento Manual/Expresso e parâmetros)
8. Cartão de Ponto (horas extras)
9. Salário-família
10. Seguro-desemprego
11. FGTS
12. Contribuição Social (INSS)
13. Previdência Privada
14. Pensão Alimentícia
15. Imposto de Renda
16. Multas e Indenizações
17. Honorários
18. Custas Judiciais
19. Correção, Juros e Multa
20. Operações → Liquidar / Imprimir / Exportar

---

## 1. Atualizar tabelas (pré-requisito)
Antes de tudo, garanta tabelas/índices atualizados (atualização on-line no
próprio sistema). Índice desatualizado calcula com base velha — erro silencioso.

## 2. Novo Cálculo → Dados do Processo
Só é preenchida para vincular o cálculo a um processo. Opções: **Manualmente** ou
**Obter do PJe**. Campos: número único do processo, valor da causa, partes
(Reclamante/Reclamado) e advogados. Origem: capa/qualificação na inicial.
Atenção à opção **Inverter Partes** quando o exequente for o réu da ação.

## 3. Novo Cálculo → Parâmetros do Cálculo
Aba que define a moldura. **Campos obrigatórios (*): Estado, Município, Admissão,
Ajuizamento.** Além disso, pelo menos um entre **Data de Demissão** e **Data
Final** deve ser preenchido.

- **Admissão / Demissão** → CTPS/TRCT/sentença. Sem vínculo reconhecido, em
  Admissão use o início da relação de trabalho.
- **Ajuizamento** → autos (marco de juros).
- **Data Inicial / Data Final** → use para limitar o período quando as verbas não
  forem devidas por todo o pacto (ex.: período fixado na sentença).
- **Prescrição Quinquenal** e **Prescrição FGTS** → marque conforme a sentença. O
  período sugerido = maior data entre Admissão/Prescrição/Data Inicial até a menor
  entre Demissão/Data Final.
- **Regime de Trabalho** (Tempo Integral / Parcial / Intermitente) → define prazo
  de férias (30 vs 18 dias); Intermitente não exibe a página Férias.
- **Maior Remuneração** → base de Aviso Prévio, Férias + 1/3 e Multa do art. 477;
  preencha sempre que essas verbas existirem. Origem: holerites/TRCT.
- **Última Remuneração** → só preencha se quiser apurar todas as verbas pela
  última remuneração (gera histórico automático com incidência em Contribuição
  Social).
- **Prazo do Aviso Prévio**: *Não Apurar* (mantém 30) / *Calculado* (Lei
  12.506/2011: 30 + 3 dias por ano, teto 90) / *Informado*. Marque **Projetar
  Aviso Prévio Indenizado** para projetar avos de férias/13º. → o que a sentença
  determinou sobre proporcionalidade do aviso.
- **Limitar Avos ao Período do Cálculo**, **Zerar Valor Negativo** → conforme o
  caso e a sentença.
- **Carga Horária mensal** (padrão 220) e **exceções**; **Sábado como dia útil**;
  feriados estaduais/municipais e pontos facultativos → relevantes quando houver
  verba com divisor Carga Horária ou Dias Úteis.

⚠ Conferir típico: prescrição (marcação e marco), limitação temporal das verbas,
prazo/projeção do aviso prévio — itens que a sentença costuma fixar.

## 4. Faltas
Lançar **todas** as faltas do contrato (mesmo anteriores ao período de cálculo):
Data Inicial, Data Final, justificada/não justificada, descrição. Marcar
**Reiniciar Período Aquisitivo** nos casos de perda de férias (art. 133 CLT).
Origem: cartão de ponto/autos. Impacto: férias, DSR, verbas com exclusão de
faltas.

## 5. Férias
Geradas automaticamente a partir de Admissão, Demissão, Regime e faltas não
justificadas. Conferir e ajustar: **Situação** (Gozadas / Indenizadas /
Perdidas), **Dobra** (período concessivo vencido), **Abonos**, **Períodos de
Gozo** efetivos (até 3 por aquisitivo), **Prazo**. Origem: ficha de férias/recibos
e o que a sentença reconheceu. ⚠ A marcação automática de **Dobra** deve ser
conferida verba a verba.

## 6. Histórico Salarial
Armazena as bases usadas em Verbas, Salário-família, Seguro-desemprego, FGTS e
Contribuição Social. Por base: **Nome**, **Parcela Fixa/Variável**, **Incidência
no FGTS**, **Incidência sobre Contribuição Social**, período, e **Tipo de Valor**:
- **Base Informada**: valor do mês integral por competência (variáveis como HE/
  comissão são lançadas pelo valor do mês). Marcar se já houve recolhimento de
  FGTS/Contribuição sobre o valor.
- **Base Calculada**: Quantidade × (Salário Mínimo ou Piso Salarial/categoria).

Clicar **Gerar Ocorrências** e **Salvar** (sair sem salvar perde tudo). Origem:
holerites/ficha financeira; na ausência, o que a sentença fixou. Lance a evolução
**mês a mês ou por faixas** (ex.: "07/2014–04/2015 R$935,00").

## 7. Verbas (a parte mais sensível)
Inclusão por **Lançamento Manual** (define todos os parâmetros) ou **Lançamento
Expresso** (verbas pré-cadastradas com parâmetros sugeridos — sempre conferir em
"Parâmetros da Verba"). Parâmetros comuns de cada verba:

- **Nome** (até 50 caracteres).
- **Assunto CNJ** → assunto da Tabela Processual Unificada correspondente.
- **Parcela**: Fixa ou Variável.
- **Valor**: *Calculado* (Base × Multiplicador ÷ Divisor × Quantidade, com Dobra)
  ou *Informado* (digita o Devido).
- **Incidência** (marcar conforme a natureza e a lei): **FGTS, IRPF, Contribuição
  Social, Previdência Privada, Pensão Alimentícia**.
- **Característica**: Comum, 13º Salário, Aviso Prévio, Férias (define a ocorrência
  de pagamento: Mensal, Dezembro, Desligamento, Período Aquisitivo).
- **Juros — Súmula 439 do TST**: "Não" → vencidas a partir do ajuizamento,
  vincendas do vencimento; "Sim" → ambas do ajuizamento. Siga a sentença.
- **Tipo**: Principal ou **Reflexa** (a reflexa incide sobre **uma** verba
  principal e, opcionalmente, reflexas dela). **Compor Principal** (Sim/Não):
  "Não" quando a verba só serve de base ou é obrigação de fazer.
- Para **Valor Calculado**, definir **Base de Cálculo** (bases cadastradas,
  histórico, salário mínimo/piso/vale-transporte ou outra verba), **Divisor**
  (Carga Horária / Dias Úteis / Cartão de Ponto / Informado), **Multiplicador**,
  **Quantidade** (Calendário / Cartão de Ponto / Informada) e **Dobra**.
- Para **Reflexa**, o **Comportamento** da base: Valor Mensal, Média pelo Valor
  Absoluto, Média pelo Valor Corrigido, Média pela Quantidade.

Regra de ouro: **lance exatamente as verbas e os reflexos que o título deferiu**,
com a base e o adicional que a sentença fixou. A lista de reflexos vem da
sentença, não da praxe. ⚠ Erros mais comuns: reflexo a mais/a menos; natureza/
incidência errada; base de cálculo divergente do comando; período da ocorrência.

## 8. Cartão de Ponto (quando houver horas extras apuradas por ponto)
Critérios de Apuração: Período, **Forma de Apuração** (excedente diária/semanal/
mensal; critério mais favorável; Súmula 85; primeiras horas em separado; etc.),
Jornada Padrão, Períodos de Descanso (intervalos art. 71/253/384/72,
inter/intrajornada), **Horário Noturno** (urbano 22–5h, redução ficta, Súmula 60),
Preenchimento de Jornadas (Livre/Programação Semanal/Escala). Depois **Apurar
Cartão de Ponto**. Origem: controles de ponto + jornada reconhecida na sentença.
Use apenas se a HE for apurada por ponto; se a sentença fixou quantidade fixa
mensal (ex.: "50 HE mensais"), lance direto na verba.

## 9. Salário-família
Marcar **Apurar Salário-família**; definir Competências, Remuneração Mensal (base)
e **Quantidade de filhos menores de 14 anos** (cotas), com variações por
competência. Origem: sentença + documentos dos dependentes.

## 10. Seguro-desemprego
Marcar **Apurar**; Valor Calculado (Tipo de Solicitação, doméstico, Quantidade de
Parcelas, Remuneração) ou Informado. Origem: modalidade de rescisão e o que a
sentença deferiu (em regra indenização substitutiva).

## 11. FGTS
Página de parâmetros (base e recolhido vêm do Histórico Salarial e das Verbas):
- **Destino**: pagar ao reclamante (entra no líquido) ou recolher em conta
  vinculada.
- **Multa**: Calculada (20% ou 40%) ou Informada; base: Devido, Diferença, Saldo/
  Saque, Devido(±)Saldo/Saque.
- **Multa do art. 467 sobre Multa do FGTS** (marcar se o título mandou).
- **Saldo e/ou Saque** + **Deduzir do FGTS** → registrar depósitos para deduzir.
- Contribuições LC 110/2001 (10% e 0,5%) quando aplicável.

Origem: extrato do FGTS (depósitos a deduzir) e o comando da sentença sobre as
bases da multa. ⚠ Quase sempre há dedução do depositado — localize o extrato.

## 12. Contribuição Social (INSS)
- **Apurar Segurado** e **Cobrar do Reclamante** (desmarcar se cobrável da ré).
- **Contribuição Social sobre Salários Pagos** (marcar só se for apurar sobre o
  pago no contrato).
- Nas ocorrências: **Alíquota Segurado** (Empregado / Doméstico / Fixa), **Alíquota
  Empregador** (Empresa/SAT/Terceiros — por atividade, período ou fixa), períodos
  de incidência e isenção (SIMPLES).

Origem: legislação previdenciária + disposições da sentença (ex.: regime de
apuração mês a mês). ⚠ Verba indenizatória não integra salário de contribuição —
confira as marcações de incidência nas Verbas.

## 13. Previdência Privada
Marcar **Apurar**; base vem do campo "Incidência Previdência Privada" nas verbas;
definir alíquota por período. Em geral só quando há previdência privada no caso.

## 14. Pensão Alimentícia
Marcar **Apurar**; Alíquota; **Incidir sobre Juros**; base vem das marcações de
incidência nas verbas e da página FGTS. Origem: determinação judicial de pensão.

## 15. Imposto de Renda
Apura conforme arts. 12 e 12-A da Lei 7.713/1988 (a partir de 28/07/2010, RRA —
rendimentos recebidos acumuladamente: anos anteriores pela tabela acumulada; ano
da liquidação pela mensal). Opções: **Incidir sobre Juros de Mora**, **Cobrar do
Reclamado**, **Tributação Exclusiva (13º)**, **Tributação em Separado (férias)**,
**Regime de Caixa**, e **Deduções** (Contribuição Social do reclamante,
Previdência Privada, Pensão, Honorários do reclamante, aposentado >65,
Dependentes). Origem: legislação + eventual disposição da sentença. ⚠ Marcar IRPF
nas verbas tributáveis e não nas indenizatórias.

## 16. Multas e Indenizações
Incidem sobre valor da causa ou da condenação. Por lançamento: Descrição, par
**Credor/Devedor**, Valor *Calculado* (Base: Principal / Principal(−)Contribuição
/ ...; Alíquota) ou *Informado* (Vencimento, Valor, índice de correção, juros).
Use para dano moral (valor informado com vencimento = data do arbitramento) e
multas normativas. Origem: sentença (valor, data, índice).

## 17. Honorários
Por lançamento: **Tipo de Honorário** (rubrica PJe-JT), Descrição, **Devedor**
(Reclamante/Reclamado), Valor *Calculado* (Alíquota + Base: Bruto / Bruto(−)
Contribuição / ...) ou *Informado*. Dados do credor (advogado) e apuração de IR.
Origem: percentual, base e beneficiário fixados na sentença. ⚠ Conferir base
(bruto x líquido) e percentual exatamente como no título.

## 18. Custas Judiciais
Abas Custas Devidas/Recolhidas. Base (Bruto Devido ao Reclamante [+ Outros
Débitos]); Conhecimento (2%, mínimo R$10,64, teto pós-10/11/2017), Liquidação
(0,5%, teto R$638,46), Fixas (art. 789-A), Autos, Armazenamento. Em regra, na
liquidação da parte autora, conferir o que a sentença determinou.

## 19. Correção, Juros e Multa
Duas abas. **Dados Gerais**:
- **Índice Trabalhista**: Tabela Única da JT (Diário/Mensal), TR, IGP-M, INPC,
  IPC, IPCA, IPCA-E, IPCA-E/TR. A **Tabela Única da JT** já incorpora o IPCA-E a
  partir de 01/01/2000 (julgamento das ADC 58/59 e ADI 5.867/6.021, que afastou a
  TR).
- **Combinar com Outro Índice** + "A partir de" → para regimes bifásicos.
- **Ignorar Taxa Negativa**.
- **Juros de Mora**: Juros Padrão (0,5% a.m. até 26/02/1987; 1% capitalizado até
  03/03/1991; 1% simples a partir de 04/03/1991); opção **Fazenda Pública**.
- **Não Aplicar Juros** (períodos).

**Dados Específicos**: Base de Juros das Verbas (Verba / Verba(−)Contribuição /
Verba(−)Contribuição(−)Previdência); critérios de FGTS (índice trabalhista vs
JAM), Previdência Privada, Custas e Contribuição Social (Lei 11.941/2009,
Atualização Trabalhista/Previdenciária, multa).

**Regra de precisão**: o regime (índice, marco, juros) é o que a sentença/acórdão
fixou; na ausência, o vigente das tabelas atualizadas. Detalhe e árvore de decisão
(ADC 58, Lei 14.905/2024) em `correcao-juros.md`. Não preencher índice de memória.

## 20. Operações → Liquidar / Imprimir / Exportar
- **Liquidar**: definir **Data da Liquidação** e o critério de **Acumular Índices
  de Correção** (mês subsequente ao vencimento; mês do vencimento; ou misto —
  mensais x anuais/rescisórias). O sistema lista **Pendências** (Alerta não impede;
  **Erro** impede). Corrigir os Erros e liquidar.
- **Imprimir**: gera o Relatório (Resumo de Cálculo, Critério e Fundamentação
  Legal, demonstrativos por parcela). Conferir o Resumo contra o dispositivo da
  sentença.
- **Exportar**: gera o arquivo (XML/.pjc). No TRT2, juntar o PDF e,
  preferencialmente, o arquivo exportado, no momento da petição.

No roteiro, encerre sempre com: rodar Liquidar → corrigir pendências → conferir
Resumo contra a sentença → Exportar (.pjc + PDF) → juntar na petição.
