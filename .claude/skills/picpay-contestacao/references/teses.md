# Banco de teses: Defesa judicial PicPay

Selecione apenas as teses pertinentes ao caso concreto. Cada tese indica o
fundamento legal e, quando houver, a cláusula do Termo de Uso que a reforça
(ver `termos-de-uso.md`). Não cite número de julgado (REsp, processo) que não
tenha sido fornecido pelo usuário. Se quiser jurisprudência específica, peça
ao usuário ou use formulação genérica ("jurisprudência consolidada dos
Tribunais de Justiça").

## A. Núcleo comum (avaliar em todo caso)

### A1. Ilegitimidade passiva (preliminar)
O PicPay é instituição de pagamento autorizada pelo BACEN que atuou como mero
meio de pagamento, sem reter ou se beneficiar dos valores. A ação deveria ser
dirigida aos beneficiários finais (nominar razão social + CNPJ) e às
instituições recebedoras (nominar), que podem identificar seus clientes
mediante ordem judicial. Fundamentos: arts. 339, caput, 485, VI, e 486 do CPC.
Reforço contratual: cláusulas 18, 18.1 e 8(j) ("somos meros intermediários").
Fechar sempre com a ressalva de mérito ("Caso assim não seja entendido…").

### A2. Inexistência de defeito no serviço
CDC, art. 14, §3º, I. O serviço funcionou exatamente como contratado e
regulado: a transação só se concretiza com senha ou biometria (cláusula 8(d)),
em dispositivo cadastrado com autenticação de dois fatores (cláusula 4.2.2.4).
Demonstrar com os logs: dispositivo vinculado e validado, ausência de troca de
senha ou recuperação de conta antes do fato, biometria facial aprovada.

### A3. Culpa exclusiva da vítima ou de terceiro
CDC, art. 14, §3º, II. Em engenharia social, todos os atos decisivos são da
parte autora: ela compartilhou credenciais, validou biometria ou confirmou as
operações no próprio dispositivo. Reforço contratual: cláusula 7(c) (dever de
não compartilhar senha e responsabilidade pelos atos decorrentes do uso dos
dados de acesso) e cláusula 7.1 (dever de guarda de senha, token e biometria;
dever de comunicação imediata de perda/furto/roubo, hipótese em que o PicPay não responde por
prejuízos anteriores à comunicação). Vedação ao venire contra factum proprium:
a autora não pode se voltar contra as próprias operações que validou.

### A4. Fortuito externo: distinguishing da Súmula 479/STJ
A Súmula 479 pressupõe fraude e delito praticados POR TERCEIRO DENTRO do
ambiente de operações bancárias (fortuito interno). Golpe de engenharia social
ocorre FORA dos sistemas do PicPay, sem qualquer violação do seu ambiente
tecnológico. O fraudador age sobre a vítima, não sobre o sistema. É fortuito
externo, que rompe o nexo causal (CC, art. 393). Esta é a tese central do
mérito em casos de golpe: sempre explicitar a distinção, nunca apenas negar a
súmula.

### A5. Conformidade regulatória BACEN
Autorização como instituição de pagamento (Lei 12.865/2013; Res. BCB 80/2021).
Observância do Regulamento Pix (Res. BCB 1/2020), inclusive cadastro de
dispositivo e limites (cláusula 4.2.2.4). Acionamento do Mecanismo Especial de
Devolução, o MED (Res. BCB 103/2021; cláusulas 4.2.2.1 e 4.2.2.3), com seus
limites estruturais: a devolução depende de saldo existente na conta de
destino; o PicPay não tem gestão sobre a conta do recebedor em outra
instituição.

### A6. Boa-fé e diligência pós-fato
Listar cronologicamente: MED acionado (data, resultado, valor recuperado),
orientação para registro de BO, cooperação com autoridades, cumprimento
integral de liminar (suspensão de descontos, inibição de negativação). Mostra
o réu como agente diligente e esvazia o argumento de descaso.

## B. Teses específicas por tema

### B1. Golpe/fraude Pix e engenharia social
Além do núcleo comum: o Pix é liquidação instantânea e irrevogável por desenho
regulatório do BACEN, não existe "estorno" unilateral; o único mecanismo é o
MED, já acionado (A5). Detalhar cada transação (data, hora, valor,
beneficiário + CNPJ, E2E, instituição recebedora) para demonstrar que os
valores saíram da esfera do PicPay imediatamente.

### B2. Empréstimo contestado
A contratação exigiu validação biométrica e dispositivo cadastrado (provar com
logs); o valor líquido foi creditado NA CONTA DA PRÓPRIA AUTORA (data, hora,
valor). Quem dispôs do dinheiro depois foi ela. Se a autora transferiu o
valor a terceiros, isso confirma a engenharia social e a culpa exclusiva (A3).
Se houver pedido de anulação do contrato: por eventualidade, a devolução do
valor principal creditado é consequência necessária (vedação ao enriquecimento
sem causa, CC, arts. 884-886), com compensação de eventuais condenações.
Contratos válidos: pacta sunt servanda; aditamento/troco com confissão de
saldo devedor reforça a ciência da autora.

### B3. Chargeback / contestação de compra
Identificar primeiro o papel do PicPay na cadeia (emissor do cartão,
credenciador ou mero intermediário de pagamento). A relação é trilateral
(portador-emissor-credenciador-lojista) e regida pelas regras do arranjo
(bandeira), inclusive prazos e hipóteses de contestação. Compra reconhecida ou
produto/serviço fruído afasta o estorno (venire). Problema de
entrega/qualidade do produto é responsabilidade do vendedor, não do meio de
pagamento, conforme cláusulas 18, 18.1, 18.2 e a analogia da própria cláusula (casa da
moeda/boleto/cartão). Se o chargeback foi processado conforme as regras do
arranjo, não há defeito (A2).

### B4. Bloqueio cautelar de conta ou valores
O bloqueio é exercício regular de direito (CC, art. 188, I) com tríplice
fundamento: (a) contratual, cláusula 3 (bloqueio/suspensão sem aviso prévio
em caso de indícios de fraude, lavagem de dinheiro ou violação do contrato),
cláusula 4.2.2.1 (bloqueio cautelar Pix em suspeita de fraude, nos termos da
regulação) e cláusula 8(j) (autorização de débito/bloqueio em contestação,
suspeita de fraude ou falha operacional); (b) legal, dever de prevenção à
lavagem de dinheiro (Lei 9.613/98; Circular BCB 3.978/2020); (c) regulatório,
MED e travas do Regulamento Pix. Demonstrar razoabilidade temporal (datas de
início/fim) e ausência de dano: valores preservados, não confiscados; saldo
liberado ou devolvido conforme apuração. Cláusula 15.7 reforça o dever
sistêmico de registro e compartilhamento de indícios de fraude.

### B5. Falha genérica na prestação de serviços
A2 + A3 + ausência de nexo causal: exigir da autora a demonstração concreta do
defeito (qual operação falhou, quando, com que prejuízo). Mera insatisfação ou
frustração com golpe de terceiro não é defeito do serviço.

## C. Teses subsidiárias (incluir SEMPRE, por eventualidade)

### C1. Inexistência de dano moral
Não há defeito nem nexo causal; o dissabor decorre de ato de terceiro
(fraudador) ou da própria autora. Mero aborrecimento não gera dano moral.
Ausência de prova de abalo concreto.

### C2. Eventualidade: quantum
Se houver condenação: arbitramento moderado, proporcional, sem enriquecimento
sem causa; correção monetária da data do arbitramento (Súmula 362/STJ).

### C3. Dano material limitado e abatimento
Limitado ao efetivamente comprovado; abater valores recuperados via MED ou
devolvidos administrativamente.

### C4. Repetição simples, não em dobro
CC/CDC: a devolução em dobro (art. 42, parágrafo único, CDC) exige cobrança de
má-fé; havendo controvérsia fundada (engano justificável), a repetição é
simples.

### C5. Inversão do ônus da prova
A inversão (art. 6º, VIII, CDC) não é automática: exige verossimilhança ou
hipossuficiência. Tendo o réu apresentado logs, extratos e contratos, não há
hipossuficiência técnica remanescente; e a verossimilhança é afastada pela
prova documental.

### C6. Litigância de má-fé (usar com critério)
Apenas quando os documentos provarem que a própria autora realizou as
operações e omitiu fatos relevantes (CPC, arts. 80 e 81). Não usar como
retórica genérica.

## D. Preliminares e prejudiciais adicionais (conforme rito)

- **JEC, incompetência por complexidade probatória** (Lei 9.099/95, arts. 3º
  e 51, II): quando a solução exigir perícia técnica (ex.: análise forense de
  dispositivo). Usar somente se a perícia for realmente necessária à defesa.
- **Justiça Comum, impugnação à gratuidade** (CPC, art. 100): somente com
  elementos documentais concretos (movimentações de alto valor na própria
  conta, contratações de crédito relevantes).
- **Prescrição/decadência**: avaliar prazo de 5 anos (CDC, art. 27, reparação
  por fato do serviço) ou 3 anos (CC, art. 206, §3º, V) conforme o
  enquadramento; decadência do art. 26 do CDC para vício de serviço.
