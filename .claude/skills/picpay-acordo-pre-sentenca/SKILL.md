---
name: picpay-acordo-pre-sentenca
description: "Lê a íntegra dos autos + os subsídios internos do PicPay e decide se o caso se enquadra em Acordo Pré-Sentença: checa as hipóteses de proibição (item 9) e as 15 de elegibilidade (item 5), aplica os critérios de mérito/risco (item 4), classifica como ELEGÍVEL, NÃO ELEGÍVEL, DOSSIÊ INSUFICIENTE ou REVISÃO DO ADVOGADO RESPONSÁVEL, e redige o Parecer Jurídico + mensagens de negociação quando elegível."
---

# PicPay — Acordo Pré-Sentença (Massificado Cível)

Esta skill transforma a **íntegra do processo** + os **subsídios internos do PicPay** (dossiê judicial) em
uma decisão fundamentada sobre Acordo Pré-Sentença: cabe ou não cabe, por quê, e — quando cabe — a mensagem
pronta para negociar com o advogado da parte autora.

## Princípio central: só propor com alta probabilidade de perda, nunca inventar

O Acordo Pré-Sentença só deve ser proposto em casos com **alta probabilidade de perda da ação**. Não é
ferramenta de gestão de estoque sem critério — é mitigação técnica de risco. Por isso duas regras protegem
o trabalho:

1. **Elegibilidade se sustenta nos autos e no dossiê, não na narrativa isolada da parte autora.** Uma
   hipótese do item 5 só está confirmada quando os autos e/ou o subsídio trazem elemento objetivo (dossiê
   conclusivo, ausência de documento, perícia, etc.) — a mera alegação da inicial não basta, especialmente
   nas hipóteses que a própria Diretriz exige comprovação nos autos (autora analfabeta/incapaz).
2. **Quando um dado não estiver nos autos ou no subsídio, escreva `Não localizado nos autos` / `Não
   localizado no dossiê`.** Nunca estime CPF, valor, data, prazo ou conclusão de dossiê "por dedução". Um
   parecer errado leva a propor acordo onde não cabe (ou a perder uma oportunidade real); um "não
   localizado" honesto leva a pedir o dado certo.

## 1. Âmbito — confirme que o caso está na carteira certa antes de analisar

Aplica-se a processos do **massificado cível**: Juizados Especiais Cíveis, Varas da Justiça Comum e Justiça
Federal. Estão **excluídos** (tratamento individualizado pelo advogado interno da carteira):

- **Middle**: valor ≥ R$ 100k–500k, lucros cessantes, ou casos de Nome Social.
- **Estratégico**: valor ≥ R$ 500k, ACP, Inquérito Civil, risco reputacional, ou casos de sócio/indicação da
  gestão.

Se o caso cair em Middle/Estratégico, ou houver dúvida real sobre a classificação, não continue a análise de
elegibilidade — classifique como **REVISÃO DO ADVOGADO RESPONSÁVEL** e explique o motivo.

## 2. Passo a passo da análise

1. Leia a íntegra por completo (petição inicial, contestação se houver, decisões, provas juntadas aos
   autos) e os subsídios/dossiê interno na íntegra — não pule seções nem se limite ao resumo da inicial.
2. Confirme o âmbito (seção 1). Se excluído, pare e classifique como REVISÃO DO ADVOGADO RESPONSÁVEL.
3. Verifique **primeiro** as hipóteses de proibição (seção 3) — se qualquer uma incidir, o caso está fora
   independentemente de eventual hipótese de elegibilidade também presente.
4. Verifique se incide alguma das 15 hipóteses de elegibilidade (seção 4) — cumulativa ou
   alternativamente. Mais de uma pode se aplicar; cite todas as que se sustentarem. **Antes de aceitar uma
   conclusão do subsídio como suficiente para afastar uma hipótese, confira o escopo real da análise** —
   ver seção 4.1.
5. Aplique os critérios de mérito/risco (seção 5) para embasar a análise — eles sustentam a "Análise de
   mérito e risco" do parecer mesmo quando a hipótese de elegibilidade já parece clara.
6. Classifique o caso (seção 6).
7. Monte a saída no formato da seção 7. Se NÃO ELEGÍVEL ou REVISÃO DO ADVOGADO RESPONSÁVEL, entregue apenas
   o parecer com a recomendação — não redija mensagem de negociação para um caso que não deve ser
   negociado.

## 3. Hipóteses de proibição (item 9) — checar antes de tudo

- **a) Alta probabilidade de êxito do PicPay**: provas/informações favoráveis ao PicPay, ou questão
  processual impeditiva (parte ilegítima, litispendência, coisa julgada, conexão, prescrição, decadência,
  responsabilidade diversa do PicPay), ou entendimento jurisprudencial favorável à matéria.
- **b) Litigância abusiva**: padrão documentado de litigância abusiva pelo patrono ou pela parte autora
  (petições copy-paste, procurações ZapSign, autor multi-ação, pedidos padronizados — ver skill
  `picpay-litigancia-predatoria` para os sinais completos e o procedimento de identificação).

Se incidir qualquer uma: classifique **NÃO ELEGÍVEL**, explique qual hipótese de proibição se aplica e por
quê, e recomende reportar ao advogado interno para análise específica via requisição no Projuris (skill
`picpay-requisicoes-projuris`).

## 4. Hipóteses de elegibilidade (item 5) — 15 hipóteses, cumulativas ou alternativas

| # | Hipótese | O que precisa estar confirmado |
|---|---|---|
| a | Fraude confirmada | Dossiê judicial confirma a fraude |
| b | Contrato sem comprovação da jornada de contratação | Ausência de assinatura, biometria OU comprovante de disponibilização do crédito |
| c | Perícia judicial desfavorável ao PicPay | Conclusão pericial já produzida nos autos é contrária ao PicPay |
| d | Bloqueio ou cancelamento indevido | Bloqueio/cancelamento de conta e/ou cartão sem prévio aviso ao cliente |
| e | Renegociação sem consentimento inequívoco | Sem comprovação idônea do aceite, ou sem previsão contratual/legal |
| f | Cobrança ou negativação indevida | Dossiê judicial conclui pela cobrança/negativação indevida |
| g | Averbação indevida decorrente de empréstimo | Dossiê judicial indica a averbação como indevida |
| h | Incorreção de dados do Nome Social | Falha no registro/manutenção do nome social da parte autora |
| i | Parte autora analfabeta (art. 595, CC) | Só se há discussão judicial sobre nulidade por ausência de assinatura a rogo + 2 testemunhas, **e** comprovação nos autos (declaração judicial, atestado médico ou doc. idôneo) — mera alegação não basta |
| j | Parte autora incapaz | Só se a contratação não foi autorizada pelo curador/responsável e há discussão judicial, **e** comprovação nos autos da incapacidade e da ausência de autorização — mera alegação não basta |
| k | Manutenção de descontos indevidos | Dossiê confirma quitação/antecipação e os descontos indevidos não foram regularizados no mês corrente do pagamento |
| l | Cancelamento de produto/serviço mantido indevidamente | Dossiê conclui que a cobrança/operação foi mantida mesmo após o registro de cancelamento pelo cliente |
| m | Pagamento não processado / não baixado | Dossiê aponta falha interna no processamento do pagamento |
| n | Seguro sem adesão inequívoca | Sem comprovação idônea do aceite na contratação do seguro |
| o | Outras falhas operacionais | Qualquer falha operacional identificada pelo dossiê judicial que tenha causado prejuízo ao cliente |

As hipóteses **i** e **j** são as únicas que a própria Diretriz condiciona expressamente a comprovação
documental nos autos. Se a única base for a alegação da parte autora, sem declaração judicial, atestado
médico ou documento idôneo constante do processo, **não marque a hipótese como confirmada** — trate como
`DOSSIÊ INSUFICIENTE` e explique exatamente o que falta.

O texto integral de cada hipótese (item 5) e dos itens 4 e 9 da Diretriz está em
`references/diretriz-texto-integral.md`, para consulta quando o caso for de leitura mais delicada.

### 4.1 Antes de aceitar "não identificamos falhas": confira o que o subsídio realmente analisou

Um subsídio que conclui "não identificamos falhas operacionais ou de segurança" não encerra sozinho a
análise das hipóteses "a) Fraude confirmada" e "o) Outras falhas operacionais". Em casos de golpe (falso
gerente, falsa central de atendimento, engenharia social em geral) o subsídio muitas vezes responde a uma
única pergunta — *foi o próprio titular quem autenticou a transação, com senha/biometria/token válidos?* —
e trata essa resposta como se encerrasse também uma pergunta diferente: *o mecanismo antifraude/motor de
risco deveria ter sinalizado ou bloqueado a operação, dado o padrão objetivo do caso?* A primeira pergunta
é sobre legitimidade da transação; a segunda é sobre adequação do sistema de prevenção a fraude. As
hipóteses "a" e "o" dependem da segunda, não da primeira, e uma resposta só à primeira não é dossiê
conclusivo sobre a segunda.

Sinais objetivos de que o padrão fático do caso pede exame do mecanismo antifraude — e não apenas da
autenticação — incluem: conta aberta pouco antes do recebimento do valor ("conta de passagem"/mula),
recebimento atípico para o histórico do cliente, dispersão total do valor em minutos ou poucas horas para
terceiros sem vínculo aparente com o titular, ou qualquer outro indício de que o padrão objetivo da
operação é compatível com os sinais que um sistema de scoring/antifraude normalmente é desenhado para
detectar. Havendo um ou mais desses sinais, verifique explicitamente se o subsídio (ou os documentos a ele
anexados) contém qualquer análise dos mecanismos de monitoramento antifraude, motor de risco/scoring, logs
de acesso, geolocalização ou dispositivo — e não apenas o extrato de movimentação e a confirmação de
autenticação. Verifique também se a contestação, a decisão de saneamento ou qualquer decisão dos autos já
determinou exibição documental ou perícia especificamente sobre esses mecanismos antifraude; se essa
produção ainda estiver pendente (prazo em curso, dilação requerida, etc.), isso é indício adicional de que
a questão técnica de mérito ainda não foi respondida pelo dossiê.

Quando o subsídio cobrir apenas a autenticação/legitimidade da transação, mas o padrão fático objetivo do
caso for compatível com falha de detecção ou bloqueio de fraude, **não classifique como NÃO ELEGÍVEL** com
base apenas nessa conclusão parcial. Classifique como **DOSSIÊ INSUFICIENTE**, especificando exatamente que
falta a análise técnica dos mecanismos antifraude/motor de risco para o padrão identificado no caso — não
apenas a confirmação de que a transação foi autenticada pelo titular — e, quando os autos já tiverem
determinado essa exibição/perícia, mencione o evento e o prazo em aberto.

## 5. Critérios de mérito e risco (item 4) — para fundamentar a análise

a) Probabilidade de êxito (mérito e provas disponíveis); b) Jurisprudência (Tribunal e local); c) Perfil do
juízo (histórico do magistrado/Câmara/Turma); d) Valores (causa e condenação estimada); e) Estágio
processual (aplicável a casos sem sentença); f) Histórico da parte autora (litispendência, coisa julgada,
outras demandas); g) Perfil do patrono (indícios de litigância abusiva); h) Dossiês judiciais (qualidade e
conclusividade); i) Tempo de tramitação (média na comarca); j) Custo da continuidade (custas, honorários);
k) Risco de precedente (repercussão negativa ou multiplicação de litígios).

Use os que os autos e o dossiê realmente permitem avaliar — não force um critério sem base. O objetivo é
demonstrar, de forma objetiva, por que a perda é provável (ou não). No parecer, cite cada critério pelo
**nome** (ex. "Probabilidade de êxito: ..."), não pela letra sozinha — as letras do item 4 colidem com as
letras do item 5, e repetir "a)", "b)"... nas duas seções do mesmo parecer confunde a leitura.

## 6. Classificação final

- **ELEGÍVEL** — incide ao menos uma hipótese do item 5, nenhuma hipótese de proibição do item 9 incide, e
  os autos/dossiê sustentam a hipótese com elemento objetivo (não só a alegação da parte autora).
- **NÃO ELEGÍVEL** — incide alguma hipótese de proibição do item 9, OU nenhuma hipótese de elegibilidade se
  sustenta nos autos/dossiê, desde que o próprio dossiê tenha efetivamente examinado os pontos técnicos
  relevantes ao padrão fático do caso (ver seção 4.1) — não apenas a autenticação da transação.
- **DOSSIÊ INSUFICIENTE** — a narrativa dos autos sugere uma hipótese plausível, mas o dossiê/subsídio não
  traz o elemento conclusivo necessário (típico nas hipóteses i/j, nos casos descritos na seção 4.1 em que
  o subsídio só analisou autenticação sem tocar no mecanismo antifraude, ou quando o subsídio está
  incompleto de qualquer outra forma). Diga exatamente qual documento/informação falta.
- **REVISÃO DO ADVOGADO RESPONSÁVEL** — caso fora do âmbito (Middle/Estratégico), hipótese de acordo não
  prevista na Diretriz (item 10), contraproposta fora da alçada, ou qualquer situação que a própria
  Diretriz manda reportar ao advogado interno antes de negociar.

## 7. Saída — formato obrigatório

Entregue sempre o Parecer Jurídico. Só inclua a pré-mensagem e a mensagem de proposta quando a classificação
for **ELEGÍVEL** — não redija mensagem de negociação para um caso que não deve ser negociado.

```
PARECER JURÍDICO — ACORDO PRÉ-SENTENÇA

IDENTIFICAÇÃO DO PROCESSO
Número do processo: [CNJ ou "Não localizado nos autos"]
Vara / Juizado / TJ: [...]
Comarca / UF: [...]
Parte autora: [...]
Patrono da parte autora: [nome + OAB, ou "Não localizado nos autos"]

1. SÍNTESE DO CASO
[3 a 5 linhas: objeto da demanda, pedidos da parte autora, estágio processual atual]

2. HIPÓTESE DE ELEGIBILIDADE APLICÁVEL
[Cite a(s) hipótese(s) do item 5 pela letra e nome — ex. "b) Contrato sem comprovação da jornada de
contratação" — ou "Nenhuma hipótese de elegibilidade se sustenta nos autos/dossiê" ou "Hipótese de
proibição aplicável: <a ou b>, item 9"]

3. ANÁLISE DE MÉRITO E RISCO
[Elementos objetivos que sustentam (ou afastam) a alta probabilidade de perda: provas disponíveis,
jurisprudência aplicável, perfil do juízo, e os demais critérios do item 4 que forem pertinentes ao caso]

4. TERMOS DA PROPOSTA (preencher apenas se ELEGÍVEL)
Ticket de referência: R$ [se houver base para estimar, com a justificativa; senão "Não estimado — depende de
enquadramento na Tabela de Alçadas"]
Valor da proposta: R$ [idem]
Prazo de pagamento pelo PicPay: mínimo 10 dias úteis após o protocolo do instrumento nos autos
Forma de pagamento: [conforme praxe do escritório, se não houver dado específico]
Obrigações de fazer / não fazer: [ex. baixa de negativação, encerramento de cobrança, se aplicável ao caso]

5. CONCLUSÃO
Classificação: [ELEGÍVEL / NÃO ELEGÍVEL / DOSSIÊ INSUFICIENTE / REVISÃO DO ADVOGADO RESPONSÁVEL]
[Justificativa objetiva da classificação e o próximo passo recomendado — negociar dentro da alçada,
escalar ao advogado interno via Projuris, ou solicitar complementação de subsídio]
```

Quando **ELEGÍVEL**, acrescente as duas mensagens abaixo. A pré-mensagem abre contato sem revelar valor; a
mensagem de proposta formaliza os termos depois que o advogado da parte autora sinalizar interesse — é
assim que o fluxo de negociação com o advogado adverso normalmente acontece na prática.

```
PRÉ-MENSAGEM

Prezado(a) Dr(a). [patrono da parte autora],

Espero que esteja bem. Atuo em nome do PicPay nos autos do processo nº [número], em trâmite perante [vara/
juizado, comarca/UF].

Gostaria de saber se há interesse em avaliarmos uma possível composição amigável para o encerramento
consensual do feito, evitando o prosseguimento até sentença. Fico à disposição para alinharmos os detalhes.

Atenciosamente,
[Advogado(a) responsável — BFAP Advogados]
```

```
MENSAGEM DE PROPOSTA DE ACORDO

Prezado(a) Dr(a). [patrono da parte autora],

Diante do interesse manifestado, formalizo a proposta de acordo para o processo nº [número]:

- Valor: R$ [valor dentro da alçada]
- Prazo de pagamento: mínimo de 10 (dez) dias úteis, contados do protocolo do instrumento nos autos
- Quitação total e irrestrita quanto ao objeto do litígio e aos fatos descritos nos autos
- [demais condições e obrigações de fazer/não fazer aplicáveis ao caso]

Peço a gentileza de retorno em até [prazo de resposta combinado com a praxe do escritório] para viabilizarmos
a formalização e o protocolo da homologação judicial.

Atenciosamente,
[Advogado(a) responsável — BFAP Advogados]
```

**Sempre que a classificação for ELEGÍVEL**, encerre com esta linha antes das mensagens (ela substitui um
valor de alçada que a skill não tem como calcular sozinha):

> ⚠️ Confirmar o valor da proposta na Tabela de Alçadas (Anexo I) antes de enviar a mensagem. Se o valor
> estimado ultrapassar a alçada do escritório, escalar ao advogado interno via requisição no Projuris (skill
> `picpay-requisicoes-projuris`) antes de negociar.

## 8. Regras de redação

- **Sem preâmbulo** ("segue a análise...") **e sem fecho** ("espero ter ajudado") — entregue direto o
  parecer (e as mensagens, quando aplicável).
- **Nunca invente** número de processo, valor, data, prazo ou conclusão de dossiê. Falta um dado → escreva
  `Não localizado nos autos` (íntegra) ou `Não localizado no dossiê` (subsídios).
- **Nunca informe um valor de alçada específico** que não tenha sido fornecido pelo usuário — a Tabela de
  Alçadas (Anexo I) não está nesta skill; sempre sinalize a necessidade de conferi-la (ver seção 7).
- Tom das mensagens: profissional e cordial, mas objetivo — serão lidas pelo advogado da parte contrária.
- A pré-mensagem **não revela valor**; só a mensagem de proposta revela valor e condições.
- Se mais de uma hipótese de elegibilidade se sustentar, cite todas — não escolha só a mais forte e ignore
  as demais, pois isso enfraquece o parecer caso a hipótese principal seja questionada depois.

## 9. Fora do escopo desta skill

- **Abrir/cadastrar a requisição no Projuris** (parecer, minuta, requisição de pagamento) → skill
  `picpay-requisicoes-projuris`, seção "Avaliação de Proposta de Acordo".
- **Etiquetas e prazo do acordo no Astrea** → skill `picpay-astrea-prazos`.
- **Procedimento completo de litigância predatória** (etiqueta, manifestação, reporte) → skill
  `picpay-litigancia-predatoria`.
- **Decidir recurso** (se já houve sentença, isto não é mais acordo pré-sentença) → skill
  `picpay-diretrizes-recursais`.
- **Contestação e teses de defesa** → skill `picpay-teses-defesa`.