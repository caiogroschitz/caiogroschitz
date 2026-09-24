---
name: peticao-golpe-bancario
description: Redige PETIÇÃO INICIAL completa na ótica do CONSUMIDOR vítima de golpe bancário / engenharia social (falso gerente, falsa central, falso investimento com aportes progressivos, falso advogado, consignado fraudulento) contra bancos e instituições de pagamento, com tutela de urgência para suspender descontos, nulidade por vício de consentimento, repetição em dobro e danos morais pelo método bifásico. Lê minuciosamente TODOS os documentos da pasta do cliente, pesquisa jurisprudência atual na web com números verificados, audita a fidelidade documental e gera o .docx forense. Use SEMPRE que o usuário pedir "petição inicial de caso de golpe/fraude bancária", "cliente caiu em golpe, quero processar o banco", "liminar para cancelar empréstimos fraudulentos", "idoso vítima de estelionato bancário", ou apontar pasta de vítima de golpe pedindo a peça. NÃO use para defesa de banco (réu), contestação, recurso, nem carteira PicPay (skills picpay-*).
---

# Petição Inicial — Consumidor Vítima de Golpe Bancário

Esta skill captura um fluxo de trabalho completo e aprovado em caso real: da leitura
da pasta do cliente até o .docx pronto para protocolo. O produto é uma inicial densa,
com jurisprudência verificada e fidelidade absoluta aos documentos que serão juntados.
Trabalhe em conjunto com as skills `redator-juridico-br` (estilo anti-IA, tipografia,
citação) e `escrita-humana-ptbr` quando disponíveis; os princípios delas valem aqui.

## Regra de ouro: a peça só afirma o que os documentos juntados provam

Antes de escrever qualquer fato, pergunte: **qual documento da pasta prova isso, e ele
será juntado?** Relatórios internos do escritório (relatórios forenses, pareceres,
roteiros) NÃO serão juntados, salvo ordem expressa do usuário: use-os como mapa de
leitura, mas ancore cada afirmação da peça no documento primário (extrato, contrato,
fatura, BO, laudo médico). Se um dado só existe no relatório interno (ex.: uma compra
internacional que não aparece na fatura extraída), **corte a alegação**. Confirme com
o usuário, logo no início, quais documentos serão juntados.

## Passo 1 — Ler TODOS os documentos da pasta, minuciosamente

Liste a pasta inteira (subpastas inclusive) e extraia o texto de cada PDF/DOCX
(`pdftotext -layout`; python-docx para .docx). Documentos típicos e o que colher:

- **Procuração**: qualificação exata da parte (estado civil, RG, CPF, endereço) e
  nomes/OAB dos advogados. A qualificação da peça segue a procuração, não a memória.
- **Contratos/comprovantes de empréstimo**: número, data, modalidade, valor, prazo,
  parcela, taxa, forma de assinatura (ex.: "Mobile Bank PF"), convênio consignado.
- **Extratos bancários**: o coração da prova. Localize o padrão crédito → esvaziamento
  (PIX/TED) em até 24h, os nomes/CNPJs das receptoras, bloqueios e desbloqueios
  cautelares, resgates atípicos (aplicações, depósito judicial), saldo negativo.
- **Faturas de cartão**: totais, limites, portadores adicionais estranhos, pagamentos
  recusados. Só afirme o que o texto extraído da fatura efetivamente mostra.
- **Boletim de Ocorrência**: número, delegacia, data, tipificação, narrativa da vítima
  (frases da própria vítima, como "liberou sem me contatar", são ouro probatório) e o
  rol de empresas receptoras com CNPJ.
- **Relatório/declaração médica**: CRM, CIDs, medicação, datas. O nexo temporal entre o
  agravamento clínico e o início do golpe sustenta hipervulnerabilidade, vício de
  consentimento e o dano moral concreto.

Monte notas internas com todos os números e depois **confira as somas** (total de
empréstimos, total de faturas, parcela mensal agregada, valor da causa).

## Passo 2 — Confirmar lacunas e decisões estratégicas com o usuário

Pergunte de forma agrupada o que faltar: réus (regra prática: apenas as instituições
onde correm os contratos/contas impugnados; cartões de bancos terceiros entram como
contexto, não como pedido), foro, documentos que serão juntados, valor de danos morais
pretendido, existência de declaração de hipossuficiência assinada.

## Passo 3 — Pesquisar jurisprudência na web (obrigatório, com número verificado)

Nunca cite de memória. Pesquise e confirme número, relator, órgão e data. O quadro de
precedentes verificados até jul/2026, com as transcrições prontas e a linha divisória
favorável/desfavorável, está em `references/teses-e-jurisprudencia.md`. **Leia esse
arquivo antes de redigir o capítulo de direito** e busque na web julgados mais novos
("STJ golpe engenharia social transação atípica [ano]"), porque a matéria evolui
trimestre a trimestre.

Duas regras táticas aprendidas em caso real:

1. **Precedente desfavorável sem número verificado não entra na inicial.** Enfrentar
   julgado contrário é papel da réplica, quando a defesa o trouxer identificado. A
   inicial se blinda de forma implícita: demonstra em concreto aquilo que a tese
   restritiva exige (ex.: prova documental do abalo psíquico, em vez de presunção pela
   idade).
2. **Cuidado com fatos de dois gumes.** Bloqueio cautelar aplicado pelo banco é prova
   de que o sistema detectou a fraude, mas jamais o descreva de modo que sugira que o
   cliente foi avisado. Afirme o que os autos mostram (nenhuma comunicação à correntista)
   e transfira o ônus: se o banco alegar aviso, que exiba logs e gravações (art. 400 CPC).

## Passo 4 — Redigir a peça

Siga a estrutura, as teses e a ordem de capítulos de
`references/teses-e-jurisprudencia.md` (endereçamento → prioridade idoso → gratuidade →
fatos → direito → tutela de urgência → pedidos → provas → valor da causa). Pontos que
diferenciam a peça:

- **Fatos com storytelling**: perfil da vítima (inclusive quadro clínico), mecânica do
  golpe, tabela dos contratos, padrão de esvaziamento, o episódio-síntese (ex.: bloqueio
  ignorado), colapso financeiro. Cada parágrafo ancorado em doc numerado.
- **Direito em subcapítulos**, cada tese desenvolvida com norma + ratio + doutrina
  nominada + ementa transcrita em bloco `>` com grifos e `(grifou-se)` + subsunção
  explícita ao caso (nunca colar ementa sem trabalhar a ratio, art. 489, § 1º, CPC).
- **Danos morais em três tempos**: configuração (três lesões concretas: mínimo
  existencial, integridade psíquica documentada, projeção existencial da dívida),
  quantificação pelo método bifásico (REsp 1.152.541/RS) e funções da condenação.
  Não inclua capítulo de superendividamento/repactuação salvo pedido expresso: a via
  desta ação é a nulidade, não o plano de pagamento.
- **Tutela de urgência**: suspensão de exigibilidade/descontos de TODOS os contratos
  (identificados um a um), vedação de negativação, suspensão de faturas dos cartões dos
  réus, e exibição de logs/gravações/registros de alerta, com astreintes.
- **Valor da causa** = soma dos contratos impugnados + faturas de cartão impugnadas +
  danos morais (art. 292, V e VI, CPC). Recalcule e mostre a conta.
- **Estilo**: aplique integralmente o padrão anti-IA (sem travessões, sem conectivos de
  abertura repetidos, ritmo variado, latim mínimo). Se a skill `redator-juridico-br`
  estiver disponível, siga as referências dela.

## Passo 5 — Auditoria final (não é opcional)

Rode a varredura de `references/checklist-auditoria.md`: cada número da peça contra o
documento-fonte, somas recalculadas em script, referências de docs (doc. 01, 02...)
consistentes em todas as menções, nenhuma citação de documento não juntado, nenhum
identificador de julgado não verificado, estilo limpo. Corrija antes de entregar.

## Passo 6 — Gerar o .docx

Gere o Word forense com `scripts/gerar_docx.py`:

```
python scripts/gerar_docx.py peca.md "PETICAO_INICIAL_[Cliente]_vs_[Reus].docx"
```

Salve na subpasta de peças processuais do cliente (ex.: `04 - PECAS PROCESSUAIS`).
Entregue com um resumo curto e os alertas práticos (ex.: falta declaração de
hipossuficiência; cartões de bancos não demandados exigirão ação própria).
