---
name: "picpay-contestacao"
description: "Redige contestações judiciais do PicPay em ações de consumidor (golpes/Pix, empréstimos, chargebacks, bloqueios, falhas de serviço, Seguro Carteira Digital Kovr e seguros negados pela seguradora parceira), com extração exaustiva de provas cadastrais/segurança."
---

# Contestação Judicial PicPay (JEC e Justiça Comum)

Esta skill redige contestações na perspectiva da defesa do PicPay (réu),
sustentando que não houve falha na prestação de serviço e que a causa do
alegado dano é ato da própria parte autora ou de terceiro. Pode produzir a
peça completa ou apenas as seções pedidas pelo usuário (ex.: "só a preliminar
e o mérito fático", fluxo mais comum do escritório), e pode produzir a peça
completa com as provas documentais embutidas, pronta para protocolo em
.docx, quando o caso o pedir (ver Passo 4).

A peça precisa soar como trabalho de advogado, com voz própria e sem os vícios
que denunciam texto de máquina. Isso não é cosmético: uma defesa que parece
gerada automaticamente perde credibilidade com o juízo antes mesmo do primeiro
argumento. O guia `references/estilo-autentico.md` trata disso.

**Padrão de numeração (prevalece sobre qualquer numeração antiga usada em
peças anteriores):** a numeração oficial do escritório é a de
`references/modelo.md`, confirmada em caso real: **1** (Endereçamento e
qualificação, com a tempestividade embutida no fim do próprio item, sem seção
numerada à parte), **2** (Síntese da demanda), **3** (Preliminarmente, com
3.1, 3.2, 3.3... conforme as preliminares cabíveis ao caso), **4**
(Prejudiciais de mérito, só quando houver prescrição/decadência), **5**
(Mérito, com 5.1 regime aplicável e conduta do PicPay, 5.2 realidade dos
fatos, 5.3 do direito/tese central e 5.4 dos danos) e **6** (Dos pedidos),
fechando sem numeração própria. Os itens 5.1 a 5.4 podem abrir uma terceira
casa decimal (5.2.1, 5.3.1, 5.4.1 etc.) quando o caso pedir granularidade por
fato ou por subtese, como no próprio "Modelo de referência ampliado" abaixo.
**Quando o item 4 (prejudiciais) não for aplicável, omita-o inteiramente e
siga direto de 3 para 5: um "4" ausente na numeração final é o comportamento
correto, não uma lacuna a corrigir.** Nunca troque essa numeração pela
numeração em algarismos romanos (I, II, III...) nem por outro esquema, ainda
que uma peça antiga ou um exemplo de referência tenha usado numeração
diferente: se o usuário dizer que a peça deve seguir "o padrão do escritório"
ou "o padrão BFAP", é esta numeração. O "Modelo de referência ampliado" mais
abaixo já está organizado nela.

**Padrão de extensão e profundidade:** o escritório forneceu duas
contestações reais, efetivamente protocoladas (processos
5009602-94.2024.8.13.0439 e 5004124-21.2024.8.13.0079), como o padrão de
extensão e profundidade argumentativa que a peça completa deve reproduzir.
Os blocos reaproveitáveis dessas duas peças foram remapeados, abaixo, para a
numeração de `references/modelo.md` descrita acima (na origem, essas duas
peças usavam uma numeração diferente, com "Tempestividade" como item isolado
e o mérito repartido de outra forma; não volte a essa numeração antiga). Não
encurte a peça para caber num tamanho menor: cada tópico do esqueleto abaixo
deve ser desenvolvido com parágrafos próprios, no mesmo nível de extensão dos
exemplos, e não resumido em uma ou duas frases.

Para o tema **Seguro Carteira Digital (Kovr)**, existe ainda uma terceira
contestação real, protocolada (processo 5012977-80.2024.8.13.0382, TJMG),
transcrita na íntegra na seção "Modelo de contestação completa: Seguro
Carteira Digital (Kovr)", mais abaixo. Naquele tema, ela é o modelo a seguir
com prioridade.

## Princípio central: a peça nasce dos documentos

A força desta defesa está na **fidelidade aos documentos**. Datas, horários,
valores, CNPJs, IDs de transação, Device ID, números de contrato, tudo precisa
espelhar exatamente o que consta nos docs. Um número inventado destrói a
credibilidade da peça e pode configurar litigância de má-fé. Leia **todos** os
documentos de defesa minuciosamente antes de redigir. A mesma regra vale para
jurisprudência: os blocos reaproveitáveis abaixo já foram usados e são de
autoria do escritório, portanto podem ser citados verbatim sempre que a tese
se aplicar; jurisprudência nova, fora desses blocos, só entra se fornecida
pelo usuário no caso concreto ou produzida, depois da peça pronta, pela skill
de busca de jurisprudência do tribunal do caso — escolha pela UF/tribunal do
processo, nunca use sempre a mesma: `jurisprudencia-tjmg-picpay` para Minas
Gerais, `jurisprudencia-tjes` para o Espírito Santo, `jurisprudencia-tjsp`
para São Paulo, e assim por diante conforme a numeração do CNJ do processo
(dígitos de tribunal, ex. `.8.08.` = TJES, `.8.13.` = TJMG, `.8.26.` = TJSP)
indicar. Nunca invente ementa, número de processo ou relator.

## Passo 0: Triagem

Antes de tudo, identifique (pergunte se não estiver claro):

1. **Rito**: Juizado Especial Cível (Lei 9.099/95) ou Justiça Comum. Isso muda
   preliminares disponíveis e o tom (no JEC, preliminar de incompetência por
   necessidade de chamamento de terceiro costuma caber; na Justiça Comum,
   avalie denúnciá à lide em vez disso).
2. **Tema(s)**, lembrando que um caso pode combinar mais de um:
   - Golpe/fraude Pix e engenharia social
   - Empréstimo contestado (PicPay Parcela, Crédito Pessoal, consignado)
   - Chargeback / contestação de compra com cartão (físico, contactless ou
     online com 3DS)
   - Bloqueio cautelar de conta ou valores
   - Falha genérica na prestação de serviços
   - Seguro ou assistência vendidos dentro do app (Renda Protegida, Vida,
     Celular, Assistência Saúde) cujo sinistro foi negado ou está em disputa
     com a seguradora parceira (Icatu, Kovr etc.), quando o PicPay figura no
     polo passivo apenas como estipulante/intermediário da contratação
   - Seguro Carteira Digital (seguro da carteira PicPay, parceira Kovr)
     cobrado em cartão de crédito (de terceiro cadastrado no app ou PicPay
     Card) e alegado pelo autor como não contratado, com pedido de retirada
     de negativação e indenização (ver "Modelo de contestação completa:
     Seguro Carteira Digital (Kovr)")
3. **Formato de entrega**: texto no chat (padrão), ou peça completa em .docx
   com as provas embutidas e pronta para protocolo (ver Passo 4). Pergunte se
   não estiver claro, junto com as demais perguntas de triagem, para não
   redigir duas vezes.

## Passo 1: Leitura minuciosa dos documentos

Leia cada documento (PDFs, prints, planilhas, extratos). Extraia e organize:

- **Cadastro:** data/hora de abertura da conta, username, ID PicPay, CPF,
  telefone e e-mail verificados, validação de identidade (biometria facial,
  documento).
- **Segurança, extração exaustiva (regra obrigatória):** o levantamento de
  segurança não é uma amostra ilustrativa, é um inventário completo. Extraia
  TODOS os dispositivos vinculados à conta ao longo de todo o histórico
  disponível nos autos, não apenas o mais recente ou o único citado na
  inicial: se o documento de origem lista dois, três ou mais aparelhos
  (modelo, Device ID, Installation ID, data de vínculo, validação documental,
  status de cada instalação), cada um deles é um dado autônomo a ser usado,
  nunca só o primeiro ou o mais conveniente ao argumento. O mesmo vale para o
  histórico de recuperação/redefinição de senha: extraia cada ocorrência
  (data, hora, resultado) e também a ausência de ocorrências no período
  relevante, quando for esse o caso; não resuma o histórico inteiro numa
  única frase genérica de "houve/não houve pedido de recuperação de senha"
  quando os autos permitem listar as ocorrências uma a uma. Quando um único
  print ou página do dossiê já reúne várias dessas informações (por exemplo,
  uma tela de "dispositivos e histórico" que mostra três aparelhos e dois
  eventos de redefinição de senha juntos), trate cada aparelho e cada evento
  como um fato separado para fins de redação e de recorte de imagem (ver
  Passo 4, item 2, e a abertura do 5.2): a origem estar combinada numa única
  tela não autoriza combinar os fatos na peça. Procure especificamente por um
  registro de **biometria facial com prova de vida** (foto capturada no ato,
  status "Aprovada", liveness/prova de vida aprovada, e as fotos de frente e
  verso do documento oficial quando existirem), normalmente em documentos de
  análise de prevenção a fraude ou de autorização de dispositivo. Esse
  registro é mais forte do que um log textual de "IDENTITY concluído": mostra
  que foi o rosto da própria parte autora que autorizou o aparelho, não
  apenas uma senha ou token. Quando existir, é **obrigatório** usá-lo como
  exhibit próprio na peça completa em .docx (Passo 4), com a foto da
  biometria facial e as fotos do documento (frente e verso) embutidas, e
  discutido explicitamente no texto (não basta citar o log genérico de
  biometria); não presuma que a tela de "dispositivos e histórico de
  autorizações" já cobre esse ponto, são documentos distintos.
  **Sobre avisos internos nesses documentos:** dossiês e telas de análise
  interna do PicPay costumam trazer, como rodapé, um aviso do tipo "estas
  informações contêm dados sensíveis e somente podem ser apresentadas nos
  autos mediante autorização judicial" ou similar. Esse é um aviso de manuseio
  interno, dirigido a quem monta o dossiê, e não impede o uso do material pelo
  próprio time de defesa do PicPay no processo a que ele se refere: inclua a
  biometria, o documento e os demais dados normalmente, sem pedir confirmação
  ao usuário a cada caso. O que nunca pode acontecer é esse aviso aparecer
  dentro do recorte que vai para a peça: ao preparar a imagem (Passo 4),
  enquadre o corte para excluir qualquer nota, rodapé ou disclaimer de
  manuseio interno, exatamente como se exclui nome de atendente ou de time
  interno.
- **Transações contestadas:** para cada uma, data, horário, valor, beneficiário
  (razão social mais CNPJ/CPF), ID/E2E, instituição recebedora, forma de
  autorização (senha, biometria, contactless/POS Entry 07, 3DS, chip e senha).
- **Crédito/contratos:** número, emissão, valor entregue, valor total, parcelas,
  vencimentos; CCB, lastro, aditamento/troco (saldo devedor confessado, valor
  renegociado, financiado, líquido creditado); biometria na contratação.
- **Chargeback (se tema):** dados da compra, bandeira/arranjo, papel do PicPay
  (emissor/credenciador), método de autorização (contactless, 3DS, chip e
  senha), prazo e motivo da contestação, posição do lojista, se o cliente
  concluiu o fluxo de contestação na central de cartões ou abandonou.
- **Bloqueio (se tema):** motivo (suspeita de fraude/PLD/ordem judicial/MED),
  data de início e fim, valores afetados, comunicações ao cliente.
- **Seguro/assistência (se tema):** seguradora parceira e CNPJ, número da
  apólice coletiva e do certificado/proposta, data de contratação e de início
  de vigência, valor do prêmio, coberturas contratadas; se houve sinistro,
  data do evento, protocolo de acionamento, e a carta ou comunicação de
  negativa da seguradora (data, número de referência, motivo técnico da
  negativa); confirme sempre quem, entre PicPay e seguradora, praticou a
  análise e a decisão sobre a cobertura, pois disso depende a preliminar de
  ilegitimidade passiva do PicPay como mero estipulante (ver Modelo de
  referência ampliado, item 3.1, variante seguro).
- **Seguro Carteira Digital / Kovr (se tema):** em qual conta PicPay o seguro
  foi contratado (titular da conta, com nome e CPF, e a relação dessa pessoa
  com o autor, se houver, como filiação, comprovada por documento dos autos);
  data de abertura da conta do autor; cartão que pagou a mensalidade (bandeira,
  emissor, final, titular do cartão) e a data em que foi cadastrado no app e
  em qual conta; plano contratado e valor da mensalidade; data da contratação
  e forma de autorização (senha ou biometria); data e autor do cancelamento
  (manual pelo próprio titular da conta, por exemplo); data da exclusão do
  cartão da conta; protocolo de SAC do autor (número, data do contato, data e
  resultado da análise interna e o que foi orientado ao consumidor). Cada um
  desses eventos é um fato autônomo, com imagem própria (ver Passo 4, item 2).
- **Pós-fato:** contato da parte autora, com data e número de protocolo; se o
  contato foi imediato ou tardio em relação às transações (a demora é tese
  central de culpa exclusiva); medidas adotadas (MED com data, resultado,
  valor recuperado; bloqueio do cartão com data); orientação de Boletim de
  Ocorrência (há BO nos autos? Se não houver e a causa de pedir depender dele,
  isso sustenta a preliminar de indeferimento da inicial, ver Modelo de
  referência ampliado); cumprimento de liminar.
- **Da inicial:** quem é a parte autora, o que alega, valor da causa, pedidos,
  data de designação da audiência (para a tempestividade), se há gratuidade
  deferida e elementos para impugná-la, se há terceiro beneficiário não
  incluído no polo passivo.

Se houver mais de um réu na ação (ex.: PicPay e outra instituição de
pagamento/banco) e apenas um débito tiver relação com o PicPay, separe com
clareza, desde a leitura, quais fatos e documentos pertencem a cada débito.
Isso normalmente sustenta uma preliminar de ilegitimidade passiva quanto ao
débito estranho ao PicPay (ver `references/teses.md`).

## Passo 2: Confirmar dados faltantes ANTES de redigir

Se algum elemento essencial não estiver claro (ex.: falta CNPJ de beneficiário,
horário ilegível, número de contrato ausente, data da audiência para a
tempestividade), **pergunte ao usuário antes de escrever**, de forma agrupada
e objetiva. Nunca preencha com dado presumido nem invente. Só prossiga quando
os dados estiverem confirmados ou o usuário autorizar seguir sem eles (caso em
que o trecho correspondente é omitido, não fabricado). Aproveite essa rodada
de perguntas para fechar também a estratégia (quais preliminares priorizar:
ilegitimidade passiva, chamamento de terceiro, ausência de documento
essencial, impugnação à gratuidade, uniformização jurisprudencial; interesse
em conciliação) e o formato de entrega do Passo 0.3, tudo de uma vez,
agrupado.

## Passo 3: Redigir

Leia, nesta ordem, antes de redigir:

1. `references/estilo-autentico.md`, o guia de voz e ritmo, para a prosa
   NARRATIVA (os parágrafos de análise e de fatos que você escreve do zero).
   Continua valendo para essa parte: nada de travessão como pausa, conectivo
   repetido à exaustão, ritmo uniforme. Essa regra NÃO se aplica aos blocos
   reaproveitáveis do "Modelo de referência ampliado" abaixo (o parágrafo
   institucional sobre o PicPay, as ementas de jurisprudência, o título "X –
   O QUE É O PICPAY"), nem à contestação transcrita em "Modelo de contestação
   completa: Seguro Carteira Digital (Kovr)": esses trechos são citados
   verbatim, como redigidos pelo escritório, inclusive quando repetem
   conectivo ou usam meia-risca no título.
2. `references/teses.md`, banco de teses por tema, para decidir qual tese
   central do mérito desenvolver (culpa exclusiva, exercício regular do
   direito, ausência de falha, fortuito externo etc.) dentro do esqueleto do
   Modelo de referência ampliado, e qual(is) preliminar(es) da seção A1/D
   cabem no item 3.
3. `references/termos-de-uso.md`, cláusulas do Termo de Uso do PicPay mapeadas
   para cada tese. Cite a cláusula pelo número e transcreva o trecho pertinente
   quando reforçar o argumento, tanto na "Realidade dos Fatos" quanto no
   desenvolvimento da tese central.
4. A seção "Modelo de referência ampliado", mais abaixo neste arquivo, para a
   estrutura, a numeração (que segue `references/modelo.md`, ver nota no topo
   deste arquivo), a extensão, a ordem das seções e os blocos reaproveitáveis.
   Reproduza fielmente esse padrão, adaptando nomes, valores, datas, artigos e
   fatos ao caso concreto; os dados do modelo são exemplo, nunca os copie
   literalmente.
5. Se o tema for Seguro Carteira Digital (Kovr), a seção "Modelo de
   contestação completa: Seguro Carteira Digital (Kovr)", que prevalece sobre
   o modelo genérico do item 4 na descrição da jornada do seguro, nas teses de
   mérito e na redação dos pedidos, respeitada a numeração oficial (a tabela
   de correspondência está na própria seção).

Depois da peça pronta, se o usuário quiser jurisprudência real adicional para
reforçar as teses, use a skill de jurisprudência do tribunal do caso (ver
"Princípio central" acima para como escolher qual), nunca antes da peça e
nunca por conhecimento geral.

Saída padrão: **texto no chat**, pronto para copiar. Vá para o Passo 4 quando
o usuário pedir a peça completa em arquivo, com as provas embutidas.

## Modelo de referência ampliado (peça completa)

Esqueleto e blocos extraídos de duas contestações reais do escritório
(processos 5009602-94.2024.8.13.0439 e 5004124-21.2024.8.13.0079), já
organizados na numeração oficial de `references/modelo.md` (ver nota no topo
deste arquivo). Este é o padrão de estrutura, extensão e profundidade a
seguir por padrão na peça completa. Cada seção abaixo deve virar parágrafo(s)
próprio(s) na peça, nunca uma frase única resumindo o tópico.

### 1. Endereçamento e qualificação

"EXCELENTÍSSIMO SENHOR DOUTOR JUIZ DE DIREITO DA [N]ª VARA CÍVEL DA COMARCA DE
[COMARCA] - [UF]", número do processo, qualificação completa do PicPay (razão
social, CNPJ, sede) e, se for o caso, da PicPay Bank quando o débito envolver
conta bancária vinculada, seguida de: "nos autos da Ação [classe da ação]
movida por [PARTE AUTORA], já qualificada, vem, por meio de seus procuradores
que esta subscrevem, respeitosamente, apresentar sua CONTESTAÇÃO, nos termos
adiante expostos." Feche o item com um parágrafo curto de tempestividade, sem
abrir seção numerada própria para isso. Exemplo de construção: "Compulsando
aos autos verifica-se que [a audiência foi designada para [DATA] / o prazo
para defesa se encerra em [DATA]]. Portanto, inegável a TEMPESTIVIDADE da
presente contestação[, protocolada antes mesmo da referida audiência]."

### 2. Síntese da demanda

Resumo objetivo e neutro do que a inicial alega e pede, sempre em discurso
indireto ("alega", "sustenta", "pleiteia"), incluindo os valores pedidos
(devolução simples ou em dobro, dano moral). Depois, uma enumeração curta dos
motivos de fato narrados na inicial. Fecha com uma frase de transição do tipo
"Ocorre que, conforme demonstrado adiante, não assiste razão à parte autora.
Dessa forma, os pedidos desta demanda deverão ser julgados improcedentes. É o
que se passa a expor."

### 3. Preliminarmente

Selecione as preliminares que o caso realmente sustenta (não empilhe as
mecanicamente). Quando a natureza da causa não comportar nenhuma preliminar de
mérito processual (por exemplo, um incidente não adversarial de identificação
de bens digitais em inventário, sem pedido indenizatório), omita a seção
inteira e explique ao usuário, ao final, por que nenhuma preliminar foi
suscitada. Numere apenas as preliminares realmente usadas, em sequência a
partir de 3.1, sem pular número dentro do item 3:

**3.1. DA ILEGITIMIDADE PASSIVA DO PICPAY** (quase sempre cabível quando há
beneficiário final identificável). Desenvolva em vários parágrafos: (a)
afirmação da ilegitimidade; (b) retomada dos fatos narrados na inicial; (c)
esclarecimento de que o PicPay tomou as medidas de segurança cabíveis
(biometria/senha obrigatória, criptografia); (d) concluir que o imbróglio se
deu entre a parte autora, o fraudador e o terceiro recebedor, sendo o PicPay
mero intermediário; (e) fechar com o art. 17 c/c art. 485, VI, do CPC.

**3.1 (variante seguro/produto de terceiro em apólice coletiva). DA
ILEGITIMIDADE PASSIVA DO PICPAY POR ATUAR COMO MERO ESTIPULANTE.** Cabível
quando o produto contestado é um seguro ou assistência vendido dentro do
aplicativo (Seguro Renda Protegida, Seguro Vida, Seguro Celular, Assistência
Saúde), a seguradora parceira (Icatu Seguros S/A, CNPJ 42.283.770/0001-39,
Kovr etc.) também figura no polo passivo, e foi ela quem analisou e decidiu
sobre o sinistro. Desenvolva em parágrafos: (a) qualificação da relação
securitária (apólice coletiva nº [N], certificado/proposta nº [N], vigência a
partir de [DATA], prêmio mensal de R$ [VALOR]); (b) o bloco reaproveitável
abaixo, situando o PicPay como estipulante nos termos do art. 801 do Código
Civil; (c) a demonstração documental, com os próprios documentos da
seguradora (carta de negativa, protocolo de regulação de sinistro), de que a
análise técnica, a regulação do sinistro e a decisão sobre a cobertura
partiram exclusivamente dela, sem qualquer participação do PicPay; (d) o
fechamento com o art. 485, VI, do CPC:

> O produto contratado pela parte autora é o [SEGURO/PRODUTO], garantido pela
> [SEGURADORA] S/A, CNPJ [CNPJ], no âmbito da apólice coletiva nº [N],
> certificado/proposta nº [N]. A contratação ocorreu em [DATA], com início de
> vigência em [DATA], de forma direta pela parte autora, sem vínculo com
> outros produtos.
>
> Nessa relação, o PicPay atua exclusivamente como estipulante da apólice
> coletiva, nos termos do art. 801 do Código Civil, intermediando a
> contratação entre a segurada e a seguradora. Conforme consta expressamente
> no Certificado Individual, a assunção do risco securitário, a regulação de
> sinistros e a decisão sobre coberturas são de competência exclusiva da
> seguradora [SEGURADORA].
>
> A negativa de cobertura securitária, quando houver, é ato exclusivo da
> seguradora: a análise do sinistro, a emissão de parecer técnico e a decisão
> pela negativa são praticadas exclusivamente por ela, sem qualquer
> participação do PicPay, que legalmente não poderia fazê-lo. Inexiste,
> portanto, lastro de legitimidade para que o PicPay figure no polo passivo
> quanto à pretensão indenizatória securitária, impondo-se sua exclusão da
> lide, nos termos do art. 485, VI, do Código de Processo Civil.

Fonte: contestação real do escritório nos autos nº 0822366-09.2025.8.07.0016
(2º JEC de Brasília/DF), Seguro Vida PicPay garantido pela Icatu Seguros,
sinistro de invalidez negado por origem patológica da sequela. Se o Juízo,
ainda assim, mantiver o PicPay no polo passivo, desenvolva em 5.3 a tese
subsidiária de ausência de falha na prestação de serviços descrita abaixo.

**3.2. DA INCOMPETÊNCIA DO JUIZADO ESPECIAL CÍVEL / DA NECESSIDADE DE
CHAMAMENTO DE TERCEIROS AO FEITO** (quando há beneficiário ou terceiro não
incluído no polo passivo cuja oitiva é necessária). No JEC: incompetência por
necessidade de chamamento incompatível com o rito (art. 3º, Lei 9.099/95). Na
Justiça Comum: peça a inclusão do beneficiário/terceiro no polo passivo ou,
subsidiariamente, expedição de ofício para identificá-lo.

**3.3. DO INDEFERIMENTO DA INICIAL POR AUSÊNCIA DE DOCUMENTO ESSENCIAL**
(quando a causa de pedir depende de um fato, como furto/roubo, que não veio
comprovado por Boletim de Ocorrência ou documento equivalente nos autos). Cite
o art. 330, IV, c/c art. 320 do CPC.

**3.4. DA IMPUGNAÇÃO À GRATUIDADE DE JUSTIÇA** (Justiça Comum; somente com
elementos documentais concretos que contradigam a hipossuficiência alegada,
como movimentações de alto valor na própria conta ou contratações de crédito
relevantes — ver `references/teses.md`, seção D, e CPC, art. 100). Quando
houver jurisprudência real do tribunal do caso sobre o tema (buscada com a
skill de jurisprudência correspondente, ver "Princípio central"), cite-a aqui
no padrão CNJ, com ementa transcrita ipsis litteris.

**3.5. DA UNIFORMIZAÇÃO JURISPRUDENCIAL, ART. 926 DO CPC** (somente quando o
usuário fornecer precedente local em caso análogo contra o PicPay; nunca
invente). Cite o julgado fornecido na íntegra e amarre ao art. 926 do CPC.

### 4. Prejudiciais de mérito (quando houver)

Avalie sempre prescrição (CDC, art. 27, reparação por fato do serviço, 5 anos;
ou CC, art. 206, §3º, V, 3 anos, conforme o enquadramento) e decadência (CDC,
art. 26, para vício de serviço), mas só inclua a seção quando o prazo
realmente favorecer o PicPay no caso concreto. **Quando não houver
prejudicial aplicável, omita o item 4 inteiro e siga direto para o item 5**:
um "4" ausente na numeração final da peça é o comportamento correto, não uma
lacuna a corrigir ou uma renumeração a fazer.

### 5. Mérito

#### 5.1. Do regime aplicável e da conduta do PicPay

Abra com um ou dois parágrafos situando o PicPay como instituição de
pagamento autorizada pelo BACEN e o vínculo contratual com a parte autora
(Termo de Uso, cláusula 1), introduzindo a tese central que será desenvolvida
em 5.3. Em seguida, o bloco institucional reaproveitável verbatim (a
meia-risca no título é intencional e faz parte do padrão do escritório). Este
bloco também serve, adaptado, para casos não adversariais (ex.: incidentes de
identificação de bens digitais), onde ajuda a delimitar que o PicPay só guarda
ativo financeiro, ao contrário de plataformas que armazenam conteúdo pessoal:

> Antes de informar/esclarecer os motivos pelos quais o Requerido não possui
> qualquer pendência e inexiste o dever de indenizar suscitado pela parte
> Requerente, pede-se vênia para explicar resumidamente a sua forma de
> atuação.
>
> Fundado em julho de 2012, na capital do Estado do Espírito Santo, o PICPAY
> é uma instituição de pagamento, autorizada pelo Banco Central do Brasil –
> BACEN, que abraça os mais diversos tipos de público, em especial aqueles
> consumidores desbancarizados, oferecendo aos seus clientes uma vasta gama
> de produtos e serviços digitais para facilitar o seu dia a dia.
>
> Para a melhor compreensão de sua natureza e atividades, pertinente se faz
> colacionar a definição dada pelo BACEN a uma instituição de pagamento:
> "Instituições de pagamento são pessoas jurídicas não financeiras que
> executam os serviços de pagamento no âmbito do arranjo de pagamento e que
> são responsáveis pelo relacionamento com os usuários finais do serviço de
> pagamento, pagadores e recebedores. São exemplos de instituições de
> pagamento os credenciadores de estabelecimentos comerciais para a
> aceitação de cartões e as instituições não financeiras que recebem
> recursos do público que serão utilizados para fazer pagamentos ou
> transferir fundos, utilizando, por exemplo, moeda eletrônica."
>
> As instituições de pagamento possibilitam ao cidadão realizar pagamentos
> independentemente de relacionamentos com bancos e outras instituições
> financeiras. Com o recurso financeiro movimentável, por exemplo, por meio
> de um cartão pré-pago ou de um telefone celular, o usuário pode portar
> valores e efetuar transações sem estar com moeda em espécie. Graças à
> interoperabilidade, o usuário pode, ainda, receber e enviar dinheiro para
> bancos e outras instituições de pagamento.
>
> Neste ponto, considerando que a atuação do PicPay se dá "no âmbito do
> arranjo de pagamento", cumpre esclarecer que este "é o conjunto de regras
> e procedimentos que disciplina a prestação de determinado serviço de
> pagamento ao público", objetivando facilitar "as transações financeiras que
> usam dinheiro eletrônico", ou seja, é a tecnologia que permite que as
> transações financeiras sejam possíveis, através de cartões (crédito ou
> débito), boletos ou telefones celulares.
>
> Feita essa breve digressão, de rigor mencionar que, com o PicPay, o
> consumidor pode efetuar, via aplicativo, pagamentos com cartão de crédito,
> enviar e receber dinheiro, pagar boletos, emitir cobranças, transferir
> dinheiro, realizar recarga de celular e de cartões de transporte, utilizar
> o saldo da carteira virtual em milhões de estabelecimentos cadastrados,
> além de armazenar dinheiro em sua "carteira virtual". Trata-se, em outras
> palavras, de um aplicativo de pagamentos, com sistema operacional Android
> ou iOS, que funciona como uma "carteira digital" e se tornou um dos
> maiores aplicativos de pagamentos do país, facilitando a vida financeira
> de seus usuários.
>
> Desta forma, relevante apontar a Vossa Excelência que, nessa função, o
> PicPay agiu adequadamente conforme a sua função institucional, não havendo
> o que se falar em responsabilização por quaisquer prejuízos suscitados
> pela parte adversa.

#### 5.2. Da realidade dos fatos

**Abertura obrigatória do item 5.2 (padrão BFAP), sempre antes de qualquer
outra coisa:** o item 5.2 não começa direto na cronologia. Ele abre com um
bloco fixo de quatro momentos, nesta ordem, cada um seu próprio parágrafo:

1. Um parágrafo que resume, em uma frase, o que a narrativa da inicial
   revela quando lida com atenção (no tema golpe/fraude, que a conclusão da
   transação dependeu da atuação consciente da própria parte autora junto ao
   golpista; adapte ao tema do caso concreto nos demais temas, mas mantenha a
   mesma função: dizer, de saída, qual é o verdadeiro fio condutor dos fatos).
2. Um parágrafo de transição quase fixo: "Nesse contexto, conforme se verá a
   seguir, todos os indícios e provas existentes sobre o fato narrado na
   inicial dão conta de que não houve qualquer falha nos serviços prestados
   pelo PicPay ou mesmo responsabilidade deste Réu sobre [o suposto golpe/a
   transação impugnada/o débito reclamado] objeto desta lide", trocando
   apenas o trecho final pelo tema do caso.
3. Um parágrafo curto registrando que há uma série de medidas tomadas
   voluntariamente pela própria parte autora para a realização do fato
   reclamado (ex.: "Neste ponto, cabe ressaltar que há uma série de medidas
   tomadas voluntariamente pela Parte Autora para realização da transação
   reclamada.").
4. A frase de transição, quase fixa, para a lista que segue: "A história
   real da relação entre o PicPay e [a Autora/o Autor], da abertura da conta
   às operações reclamadas, está registrada nos documentos anexos e se
   resume assim:".

Depois dessa frase vem uma lista numerada em algarismos romanos minúsculos
entre parênteses, (i), (ii), (iii)..., cobrindo, nessa ordem, TODO o
inventário levantado no Passo 1 sobre a fundação da relação entre a parte
autora e o PicPay, sem curadoria nem resumo: abertura da conta (data, hora,
CPF, nome, e-mail e telefone verificados, resultado positivo em
bureau/análise de prevenção à fraude); em seguida, um item PRÓPRIO PARA CADA
dispositivo vinculado à conta (modelo, sistema, Device ID, Installation ID, e
se o registro de instalação é único ou repetido naquele momento) — havendo
dois, três ou mais dispositivos nos autos, são dois, três ou mais itens da
lista, nunca um único item agregando "os dispositivos vinculados"; em
seguida, um item para cada evento de recuperação/redefinição de senha
efetivamente registrado nos autos (data, hora, resultado), e, quando não
houver nenhum no período relevante, um item afirmando a ausência; por fim,
biometria facial/selfie na verificação de identidade, com o status
retornado. Cada item é uma frase completa e afirmativa, nunca um fragmento
nem um item que acumula mais de um fato, e é seguido imediatamente pela
imagem que o comprova (ver posicionamento de imagens no Passo 4, que também
vale aqui: a imagem vem colada no item, nunca todas empilhadas ao final da
lista, e nunca uma imagem só ilustrando dois itens ao mesmo tempo — ver
Passo 4, item 2, sobre recortar a tela-fonte em fatias quando ela reúne mais
de um dado). Essa lista, texto e imagem intercalados a cada item, é uma
exceção deliberada à regra de "sem bullets" da peça (ver "Estilo e tom"): a
mesma exceção que já vale para a síntese da demanda e os pedidos finais em
algarismos romanos passa a valer também para este bloco de abertura do 5.2.
Não estenda essa forma numerada a nenhuma outra parte da peça (nem ao
restante do 5.2, nem a 5.3 ou 5.4).

**Formato alternativo, para casos com muitos fatos cadastrais pequenos e
independentes** (por exemplo, vários dispositivos e vários eventos de
segurança a documentar): em vez da lista em algarismos romanos, é aceitável
abrir cada fato com uma frase curta e autônoma, no estilo "O Autor possui
cadastro legítimo e ativo junto ao PicPay, com todos os dados verificados.",
seguida imediatamente da imagem que a comprova, e assim sucessivamente, uma
frase e uma imagem por fato, sem lista numerada e sem agrupar fatos na mesma
frase ou na mesma imagem. Use este formato ou a lista em algarismos romanos,
nunca os dois misturados no mesmo bloco de abertura; em qualquer um dos dois,
a regra de um fato por parágrafo e por imagem, sem exceção para dispositivos
múltiplos ou eventos de senha, é a mesma.

Feche o bloco de abertura com um parágrafo que amarra essa lista à própria
inicial ou ao Boletim de Ocorrência, sempre que a parte autora admitir ali
algum ato próprio (por exemplo, ter seguido orientação do golpista para
capturar a própria biometria facial ou inserir códigos recebidos por SMS):
cite as palavras da própria parte autora entre aspas, extraídas literalmente
da inicial ou do BO constante dos autos, nunca parafraseadas ou inventadas
(se o documento não estiver disponível para conferência, não invente a
citação, omita o parágrafo), e explique em uma frase por que esse próprio
relato confirma os documentos apresentados. Quando não houver admissão desse
tipo nos autos (ex.: empréstimo contestado, chargeback, bloqueio, nulidade de
registro no SCR), omita apenas este parágrafo de fechamento por admissão,
mantendo os quatro parágrafos de abertura e a lista numerada.

Exemplo real, efetivamente usado pelo escritório (caso de golpe/fraude; ajuste
nomes, datas, dados e o tema das frases 1 e 2 ao caso concreto, mantendo a
estrutura):

> Toda a narrativa da Autora sobre fraude gira em torno de tratativas
> realizadas de forma consciente com o golpista, restando claro que a
> conclusão da transação dependeu exclusivamente da atuação direta da parte
> autora.
>
> Nesse contexto, conforme se verá a seguir, todos os indícios e provas
> existentes sobre o fato narrado na inicial dão conta de que não houve
> qualquer falha nos serviços prestados pelo PicPay ou mesmo responsabilidade
> deste Réu sobre o suposto golpe objeto desta lide.
>
> Neste ponto, cabe ressaltar que há uma série de medidas tomadas
> voluntariamente pela Parte Autora para realização da transação reclamada.
>
> A história real da relação entre o PicPay e a Autora, da abertura da conta
> às operações reclamadas, está registrada nos documentos anexos e se resume
> assim:
>
> (i) A conta foi aberta em 25/03/2026, às 18h34min59s, com os dados
> verdadeiros da Autora: seu CPF (913.788.506-53), seu nome, o e-mail
> mlourdescota@gmail.com e o telefone verificado (31) 99225-2304. O cadastro
> retornou positivamente nas bases de dados (bureau), conforme a análise de
> prevenção à fraude.
> [imagem]
>
> (ii) A abertura ocorreu em dispositivo identificado (aparelho Moto g22,
> sistema Android, Device ID e9edd71a20f40449, ID de instalação
> 303d8a61-a529-4a70-9ecc-3d76c2411815), com registro único de instalação
> naquela mesma data e hora.
> [imagem]
>
> (iii) Não há qualquer pedido de recuperação de senha antes ou durante as
> movimentações, o que afasta a hipótese de invasão da conta por alteração de
> credenciais.
> [imagem]
>
> (iv) A identidade do usuário foi submetida a verificação por biometria
> facial, com envio de selfie, e o status retornou como aprovado.
> [imagem]
>
> A própria Autora admite, na inicial e no boletim de ocorrência que instrui
> os autos, que, orientada pelos golpistas, realizou "o posicionamento para
> captura de imagem facial" e "a inserção de dados e códigos" em seu aparelho.
> Foi essa biometria, fornecida por ela, que validou a operação.
> [imagem]

Só depois desse bloco de abertura é que entra a cronologia detalhada dos
fatos específicos do caso: uma frase situando que a narrativa dos documentos
mostra o cumprimento do art. 6º do CDC pelo PicPay (ou, em incidentes não
adversariais, situando que os próprios registros internos contradizem o
quadro genérico da inicial), seguida de cronologia introduzida por verbos de
exibição ("como se vê", "vejamos", "conforme evidenciado a seguir"), cada
afirmação seguida do print/imagem correspondente (na peça completa em .docx,
ver a regra de posicionamento de imagens no Passo 4) ou da referência ao
documento (na peça em texto): detalhamento de cada transação contestada
(data, horário, valor, forma de autorização); se contactless ou 3DS, explique
o padrão técnico (POS Entry, ACS) com a mesma profundidade do exemplo;
contato do cliente com o suporte (protocolo, data); bloqueio do cartão/conta
(data); cláusulas do Contrato de Adesão ou Termo de Uso que respaldam a
responsabilidade do titular (citar e transcrever, ver
`references/termos-de-uso.md`); fatura/cobrança e eventual pagamento sem
ressalva. Feche com um parágrafo de transição para o mérito (esse parágrafo
de fechamento também é o que garante que a seção não termine em imagem, ver
Passo 4). Esta parte, diferente do bloco de abertura, segue em prosa corrida,
sem lista numerada.

Quando o caso pedir granularidade por fato (por exemplo, quatro transações
contestadas, cada uma com autorização própria e prova documental distinta),
abra subitens `####` 5.2.1, 5.2.2... um por fato ou grupo homogêneo de fatos,
em vez de amontoar tudo num único parágrafo corrido, mantendo o bloco de
abertura (parágrafos fixos + lista numerada) como o primeiro conteúdo do
"5.2.", antes do primeiro subitem `####`. Quando a cronologia for simples, um
único bloco de texto sob "5.2." já basta, sem subitens, sempre precedido do
bloco de abertura.

#### 5.3. Do direito

Selecione a tese central do tema (`references/teses.md`, seções A e B):
DA CULPA EXCLUSIVA DA CONSUMIDORA/DE TERCEIRO, DO EXERCÍCIO REGULAR DO
DIREITO, DA AUSÊNCIA DE DEVER DE INDENIZAR/INEXISTÊNCIA DE FALHA, FORTUITO
EXTERNO E DISTINGUISHING DA SÚMULA 479/STJ, conforme o caso concreto.
Desenvolva com: transcrição do art. 14, § 3º, II, do CDC (culpa exclusiva) ou
dos arts. 186 e 927 do CC (exercício regular/ausência de ato ilícito);
explicação técnica de como a transação foi autorizada (chip e senha,
contactless/POS Entry 07, 3DS, biometria facial com prova de vida); e, quando
aplicável, os dois julgados abaixo, verbatim:

> "Consoante a jurisprudência do Superior Tribunal de Justiça, a
> responsabilidade da instituição financeira deve ser afastada quando o
> evento danoso decorre de transações que, embora contestadas, são realizadas
> com a apresentação física do cartão original." (AgInt no AREsp
> 1005026/MS, Rel. Min. MARCO AURÉLIO BELLIZZE, 3ª Turma, julgado em
> 03/12/2018, DJe 06/12/2018)
>
> "RECURSO ESPECIAL. RESPONSABILIDADE CIVIL. INSTITUIÇÃO BANCÁRIA. [...] De
> acordo com a jurisprudência do Superior Tribunal de Justiça, a
> responsabilidade da instituição financeira deve ser afastada quando o
> evento danoso decorre de transações que, embora contestadas, são realizadas
> com a apresentação física do cartão original e mediante uso de senha
> pessoal do correntista. [...] O cartão magnético e a respectiva senha são
> de uso exclusivo do correntista, que deve tomar as devidas cautelas para
> impedir que terceiros tenham acesso a eles. [...] Recurso especial
> provido." (REsp 1633785/SP, Rel. Min. RICARDO VILLAS BÔAS CUEVA, 3ª Turma,
> julgado em 24/10/2017, DJe 30/10/2017)

Feche esta subseção retomando o art. 14, § 1º, I a III, do CDC, para concluir
que não há defeito no serviço e que o PicPay cumpriu com as obrigações de
informação e de bloqueio imediato assim que notificado.

**Tese subsidiária para seguro/assistência de terceiro: DA AUSÊNCIA DE FALHA
NA PRESTAÇÃO DE SERVIÇOS PELO PICPAY QUANDO A NEGATIVA É TÉCNICA DA
SEGURADORA.** Use quando o tema for seguro/assistência vendido no app
(ver a preliminar 3.1, variante seguro) e, ainda que subsidiariamente à
ilegitimidade passiva, for preciso enfrentar o mérito. Desenvolva que a
controvérsia não reside em falha operacional do PicPay, mas na negativa
técnica da seguradora sobre a natureza do sinistro (por exemplo, origem
patológica versus traumática, em seguros de acidentes pessoais); que os
arts. 757 e 760 do Código Civil delimitam a cobertura estritamente aos
riscos predeterminados na apólice ou no bilhete de seguro; que a Circular
SUSEP 667/2022 disciplina a distinção entre eventos cobertos e hipóteses de
exclusão; e que o PicPay se limita a disponibilizar o produto no aplicativo,
processar o pagamento do prêmio e encaminhar o aviso de sinistro à
seguradora, sem qualquer ingerência na análise médico-pericial ou na decisão
final sobre a cobertura. Feche retomando que a eventual discussão sobre o
acerto ou desacerto da negativa da seguradora não pode justificar a
responsabilização do PicPay, à luz do art. 14 do CDC, devendo ser reconhecida
a regularidade da prestação dos seus próprios serviços (disponibilização do
produto e processamento do prêmio). Fonte: mesma contestação real citada na
preliminar 3.1 (variante seguro), autos nº 0822366-09.2025.8.07.0016.

Quando houver mais de uma subtese de mérito (por exemplo, a tese central do
golpe em 5.3.1, a validade de um contrato de empréstimo conexo em 5.3.2, e a
conformidade regulatória/diligência pós-fato em 5.3.3), abra um `####` por
subtese, numerado em sequência a partir de 5.3.1. Quando houver jurisprudência
real do tribunal do caso reforçando alguma subtese (buscada com a skill de
jurisprudência correspondente, ver "Princípio central"), cite-a no padrão
CNJ, com ementa transcrita ipsis litteris e o parágrafo de *ratio decidendi*
ligando o julgado ao fato concreto; inclua também, por lealdade processual,
eventual precedente do mesmo tribunal em sentido contrário que o usuário ou a
busca tiverem localizado, seguido do distinguishing.

#### 5.4. Dos danos

Reúna aqui as teses subsidiárias de `references/teses.md` (seção C), sempre
introduzidas por eventualidade ("ad argumentandum, caso se entenda..."). Abra
um `####` por subtópico quando houver mais de um, numerado em sequência a
partir de 5.4.1:

**5.4.1. Da impossibilidade de inversão do ônus da prova** (bloco
reaproveitável, use quase verbatim, ajustando gênero/singular-plural da parte
autora):

> O pedido da parte autora para a inversão do ônus da prova deve ser
> rejeitado, haja vista que o artigo 6º, inciso VIII, do CDC, estabelece que
> deve haver a comprovação da hipossuficiência da Requerente e a
> verossimilhança de suas alegações, sendo que a produção dessas provas deve
> ser realizada com base nas regras do CPC, não devendo ser presumidas.
>
> In casu, as alegações da parte autora estão em confronto com os fatos.
> Vê-se, assim, que a inversão não terá cabimento, pois diante dos indícios
> anexos a esta peça, não é verossímil a narrativa trazida.
>
> Quanto à hipossuficiência, trata-se de impotência do consumidor, seja de
> origem econômica ou de outra natureza, para apurar e demonstrar a causa do
> dano cuja responsabilidade é imputada ao fornecedor. Pressupõe uma
> situação em que concretamente se estabeleça uma dificuldade muito grande
> para o consumidor de desincumbir-se de seu natural onus probandi, estando
> o fornecedor em melhores condições para elucidar o evento danoso. Não
> estão presentes, no caso em tela, a hipossuficiência que justificaria a
> medida.
>
> Além disso, a inversão não deve ser automática, ocorrendo somente por
> decisão do Juiz diante dos requisitos previstos em lei, sendo este o
> entendimento dos Tribunais:
>
> "AGRAVO INTERNO NO RECURSO ESPECIAL. AÇÃO DECLARATÓRIA DE INEXISTÊNCIA DE
> DÉBITO C/C REPARAÇÃO POR DANOS MORAIS. ALEGAÇÃO DE OMISSÃO E DEFICIÊNCIA DE
> FUNDAMENTAÇÃO. NÃO OCORRÊNCIA. INVERSÃO DO ÔNUS DA PROVA. NECESSIDADE DE
> COMPROVAÇÃO MÍNIMA DAS TESES DEDUZIDAS. AGRAVO DESPROVIDO. (...) A
> jurisprudência desta Corte Superior se posiciona no sentido de que a
> inversão do ônus da prova não dispensa a comprovação mínima, pela parte
> autora, dos fatos constitutivos do seu direito." (STJ, AgInt no REsp:
> 1717781/RO, Rel. Min. MARCO AURÉLIO BELLIZZE, 3ª Turma, DJe 15/06/2018)
>
> "Não comprovação dos alegados danos materiais e morais sofridos. [...] Em
> que pese a indiscutível aplicação da inversão do ônus da prova ao CDC, tal
> instituto não possui aplicação absoluta. A inversão deve ser aplicada
> quando, a critério do juiz, for verossímil a alegação ou quando for ele
> hipossuficiente [...]" (STJ, REsp: 741393/PR, Rel. Min. NANCY ANDRIGHI, 3ª
> Turma, DJe 22/08/2008)
>
> No caso em tela não há que se falar em inversão, tendo em vista que o dano
> pleiteado deve ser provado pela parte autora, não sendo possível ser
> produzida prova pelo PicPay a esse respeito. A concessão da inversão do
> ônus da prova sem o preenchimento dos requisitos legais afronta o
> princípio constitucional da igualdade (CF, art. 5º).

**5.4.2. Da inocorrência de danos morais** (bloco parcialmente reaproveitável;
omita esta subseção inteira quando não houver pedido indenizatório na
inicial, como em incidentes não adversariais). Argumente primeiro a
improcedência total (ausência de ato ilícito, mero dissabor, ausência de
prova do abalo, `references/teses.md` C1), citando o princípio da boa-fé
objetiva (CDC, art. 4º, III; CC, arts. 422, 113 e 187). Quando houver
jurisprudência real do tribunal do caso sobre inocorrência de dano moral
(inclusive por culpa concorrente, o que reforça a tese por argumento a
fortiori quando a defesa é de culpa exclusiva), cite-a aqui no padrão CNJ com
ementa ipsis litteris. Em seguida, por eventualidade, o pedido subsidiário de
moderação do quantum:

> Por outro lado, deve o juiz, ao fixar o valor, e à falta de critérios
> objetivos, agir com prudência, atendendo em cada caso às suas
> peculiaridades e à repercussão econômica da indenização, de modo que o
> valor da mesma não deve ser nem tão grande que se converta em fonte de
> enriquecimento, nem tão pequeno que se torne inexpressivo. (GONÇALVES,
> Carlos Roberto. Direito Civil Brasileiro: Responsabilidade Civil, 2016, p.
> 407)

Seguida, quando fornecido pelo usuário ou localizado pela skill de
jurisprudência do tribunal do caso, de um julgado reduzindo o quantum a
patamar moderado, e do fechamento: "caso o pedido não seja julgado
improcedente, na eventual condenação em indenização por danos morais, requer
que estes sejam reduzidos segundo os critérios de razoabilidade e
proporcionalidade".

**Item obrigatório que passa despercebido com frequência:** sempre que houver
pedido de dano moral na inicial, o fechamento do pedido subsidiário de
quantum precisa trazer JUNTOS os dois encargos, não só um deles:
**correção monetária** (Súmula 362/STJ, incidente a partir do arbitramento) E
**juros de mora** (art. 405 do Código Civil, incidentes a partir da citação
válida, por se tratar de responsabilidade contratual). `references/teses.md`
(tese C2) menciona só a correção monetária; inclua também os juros mesmo
assim, redija algo como "com correção monetária incidente somente a partir
do arbitramento, na forma da Súmula 362 do STJ, e juros de mora incidentes
somente a partir da citação válida, nos termos do art. 405 do Código Civil", e reflita os dois encargos no item correspondente de "6. Dos pedidos".

**Jurisprudência reaproveitável para 5.4.2, exclusiva de casos no TJES**
(mero dissabor, real e verificada; não usar em processos de outros
tribunais, buscar o precedente local correspondente com a skill de
jurisprudência do tribunal do caso):

> "CONSUMIDOR. APELAÇÃO CÍVEL. AÇÃO DE INDENIZAÇÃO. ATENDIMENTO EM AGÊNCIA
> BANCÁRIA. TEMPO DE ESPERA. DANO MORAL. INEXISTÊNCIA DE CIRCUNSTÂNCIAS
> PECULIARES. MERO DISSABOR. RECURSO DESPROVIDO. O mero dissabor ou
> aborrecimento cotidiano, peculiar às relações comerciais, que não exponha o
> consumidor a uma situação de perigo, humilhação ou constrangimento, sem
> causar-lhe abalo à honra e à dignidade, não gera dano moral indenizável."
> (TJ-ES, AC 0001085-95.2019.8.08.0021, Rel. Des. Annibal de Rezende Lima, 1ª
> Câmara Cível, julgado em 02/03/2021, DJe 16/03/2021)
>
> "CIVIL E PROCESSUAL CIVIL. APELAÇÃO CÍVEL. DANOS MORAIS. AUSÊNCIA DE
> NEGATIVAÇÃO. MERO DISSABOR. INEXISTÊNCIA DE DANO MORAL. Para a
> caracterização do dano moral, impõe-se seja a parte vítima de uma situação
> tal que a impinja verdadeira dor e sofrimento, sentimentos esses capazes de
> lhe incutir transtorno psicológico de grau relevante ou, no mínimo, abalo
> que exceda a normalidade. O vexame, a humilhação ou a frustração devem
> interferir de forma intensa no âmago do indivíduo, causando-lhe aflições,
> angústia e desequilíbrio em seu bem-estar." (TJ-ES, AC 0011184-63.2011.8.08.0035,
> Rel. Des. Subst. Júlio César Costa de Oliveira, 1ª Câmara Cível, julgado em
> 15/09/2015, DJe 24/09/2015)

**5.4.3. Da impugnação à restituição em dobro** (quando a inicial pedir
devolução em dobro; `references/teses.md`, tese C4). A repetição em dobro
(CDC, art. 42, parágrafo único) pressupõe cobrança de má-fé; havendo
controvérsia fundada ou engano justificável, a repetição é simples.

### 6. Dos pedidos

Cascata numerada em algarismos romanos minúsculos entre parênteses, cobrindo
na ordem, quando aplicável ao caso: (i) acolhimento de cada preliminar
suscitada, com a consequência processual específica (extinção sem mérito,
indeferimento da inicial, chamamento de terceiro); (ii) afastamento da
inversão do ônus da prova; (iii) subsidiariamente, improcedência total dos
pedidos, com o fundamento de culpa exclusiva/exercício regular do
direito/ausência de falha (ou, em incidente não adversarial, os pedidos
próprios do caso: reconhecimento da identificação já cumprida, condições
para liberação de saldo etc.); (iv) subsidiariamente, redução do quantum de
eventual condenação em danos morais, **com os dois encargos do item 5.4.2:
correção monetária (Súmula 362/STJ) e juros de mora (art. 405 do CC)**,
quando houver pedido dessa natureza; (v) quando cabível, restituição apenas
simples e não em dobro (item 5.4.3). Depois: "Protesta por todos os meios de
prova em direito admitidos, ainda que não especificamente pleiteados." E o
requerimento de que as publicações sejam feitas em nome do advogado
subscritor, sob pena de nulidade.

### Fecho

"Termos em que, pede deferimento." seguido de local e data, e nome/OAB do
advogado subscritor (dado real do caso, nunca do modelo).

## Modelo de contestação completa: Seguro Carteira Digital (Kovr)

Contestação real do escritório, efetivamente protocolada em 29/05/2025, nos
autos nº 5012977-80.2024.8.13.0382 (Comarca de Lavras/MG, TJMG), em ação de
obrigação de fazer c/c indenizatória (retirada de negativação, R$ 5.000,00 de
danos morais e R$ 80,00 de danos materiais) movida contra o PicPay e contra
uma varejista emissora de cartão, por cobrança de "seguro carteira" na fatura
do cartão da varejista, com o autor alegando desconhecer a contratação. Na
origem, a contratação do seguro (parceria com a Kovr) foi feita na conta PicPay
da mãe do autor, que havia cadastrado o cartão do filho no aplicativo; a mãe
cancelou o seguro manualmente e o cartão foi excluído da conta dela em
16/12/2024, mesmo dia em que o SAC identificou a origem da cobrança.

**Quando usar.** Seguro Carteira Digital (proteção do saldo da carteira,
Proteção PicPay Card, Proteção cartão protegido, Proteção segurança digital)
cobrado em cartão de crédito e alegado como não contratado, com ou sem
negativação, e pedido de danos morais e materiais. É o modelo a seguir com
prioridade sobre o modelo genérico para a jornada de contratação, para as
teses de mérito e para os pedidos.

**Como usar.** A peça abaixo é a redação do escritório e fica transcrita
verbatim: os blocos de texto que forem reaproveitados (jornada de contratação
do seguro, informações sobre cadastro de cartão de crédito e segurança PCI/BACEN,
natureza dos serviços do PicPay, culpa exclusiva, exercício regular do direito,
ausência de dever de indenizar, inocorrência de danos morais e pedido
subsidiário de redução) mantêm a linguagem original, inclusive meia-risca e
conectivos repetidos, e a regra de "sem travessão" da prosa narrativa não
se aplica a eles. O que muda a cada caso são os dados: nomes, datas, número
do processo, protocolo de SAC, valores, quem contratou o seguro, qual cartão
foi usado e quem o cadastrou. Onde o caso concreto diferir do modelo, escreva
do zero só o trecho que difere e conserve o restante. Em especial:

1. **Se o cartão cobrado não for de terceiro cadastrado em outra conta**, mas
   o próprio PicPay Card do autor ou cartão cadastrado na conta dele, o item
   3.2 do modelo (contratação na conta da mãe) não se aplica. Substitua-o pela
   demonstração de que a contratação ocorreu na própria conta do autor, com
   autorização por senha ou biometria (a jornada do item 3.1 já registra que
   "as contratações só podem ser realizadas mediante o uso de senha ou
   biometria"), com data e hora da contratação, dispositivo, e o inventário de
   segurança do Passo 1 e a abertura do 5.2. Não afirme autoria da contratação
   por terceiro sem prova documental.
2. **Se houver Kovr também no polo passivo**, ou se a inicial tratar de
   sinistro negado, acrescente a preliminar 3.1 (variante seguro) e a tese
   subsidiária de 5.3, ambas já descritas no "Modelo de referência ampliado".
   Na peça-fonte, o PicPay afirmou no mérito que atuou apenas como
   disponibilizador da contratação e que a análise coube exclusivamente à
   Kovr, sem arguir preliminar formal de ilegitimidade.
3. **Imagens.** Cada marcador `[IMAGEM: ...]` do texto abaixo indica o ponto em
   que, na peça original, há um print ou documento. Na peça em .docx, siga o
   Passo 4 (imagem colada logo após o parágrafo, abaixo do trecho
   argumentativo, uma por fato, sem nome de área interna nem aviso de manuseio
   no recorte).

**Tabela de correspondência com a numeração oficial.** A peça-fonte usa
numeração anterior à padronizada (tempestividade como item 1 isolado, "Realidade
dos fatos" no item 3, mérito no item 4, pedidos no item 5, e dois itens
numerados 4.5). Ao redigir uma peça nova, use sempre a numeração oficial desta
skill, mapeando assim:

| Peça-fonte | Numeração oficial |
|---|---|
| 1. Preambularmente: da tempestividade | Embutida no fim do item 1 (endereçamento e qualificação) |
| 2. Síntese da demanda | 2. Síntese da demanda |
| 3. Da realidade dos fatos (3.1 passo a passo do seguro; 3.2 legitimidade da contratação e utilização) | 5.2. Da realidade dos fatos (5.2.1 e 5.2.2), precedida do bloco de abertura obrigatório do 5.2 |
| 4.1 Impossibilidade de inversão do ônus da prova | 5.4.1 |
| 4.2 Da natureza dos serviços prestados: o que é o PicPay? | 5.1 |
| 4.3 Da culpa exclusiva do autor | 5.3.1 |
| 4.4 Do exercício regular do direito | 5.3.2 |
| 4.5 (primeiro) Da ausência de dever de indenizar, da inexistência de falha | 5.3.3 |
| 4.5 (segundo) Da inocorrência de danos morais e 4.5.1 pedido subsidiário de redução | 5.4.2 |
| 5. Dos requerimentos finais | 6. Dos pedidos |

**Conferências antes de reaproveitar (apontadas na leitura desta peça-fonte,
não conferidas na fonte do tribunal nesta sessão):** (a) o requerimento (i) da
peça-fonte pede acolhimento de "preliminar arguida de ilegitimidade passiva",
mas o corpo não traz preliminar nenhuma; em peça nova, ou se arguir a
preliminar ou se retira o pedido, nunca se mantém um sem o outro; (b) a
ementa do AREsp 1790408/PR aparece reproduzida truncada e com trecho estranho
ao julgado ("Requer, em consequência da declaração de ilegalidade..."), e a
do AREsp 1.548.458/PB trata, no trecho transcrito, de responsabilidade do
Estado por acidente de trânsito, com aderência pouco evidente à tese de ônus
da prova do dano moral: antes de repetir qualquer dos dois, localize e
confira a ementa na fonte do STJ; (c) o pedido (iii) da peça-fonte tem vírgula
duplicada e concordância de gênero oscilante ("o Autor", "a consumidora",
"experimentado por ela"), a ajustar ao gênero da parte no caso novo; (d) a
peça-fonte não traz, no pedido subsidiário de danos morais, os dois encargos
exigidos por esta skill (correção monetária pela Súmula 362/STJ e juros de
mora pelo art. 405 do CC): em peça nova, inclua os dois no fechamento do
5.4.2 e no pedido correspondente de "6. Dos pedidos"; (e) o número
CNJ e os dados pessoais de terceiros do caso-fonte (nome do autor, nome da
mãe, protocolo de SAC, ID de comprovante) não são reaproveitáveis.

### Texto integral da peça-fonte (verbatim)

```text
EXCELENTÍSSIMO SENHOR DOUTOR JUIZ DE DIREITO DA UNIDADE JURISDICIONAL DA COMARCA DE LAVRAS - MG

Autos nº 5012977-80.2024.8.13.0382

PICPAY INSTITUIÇÃO DE PAGAMENTO S.A, empresa regularmente inscrita no CNPJ/ME sob o nº22.896.431/0001-10, com sede na Avenida Manuel Bandeira, nº291, Vila Leopoldina, na cidade de São Paulo - SP, CEP 05317-020, nos autos da ação movida por GUSTAVO EXPEDITO SILVA LIMA, já qualificado, vem, por meio de seus procuradores que esta subscrevem, respeitosamente, apresentar sua CONTESTAÇÃO, nos termos adiante expostos:

1.  PREAMBULARMENTE: DA TEMPESTIVIDADE

Compulsando aos autos, verifica-se que a audiência de conciliação foi designada para 10/06/2025 às 08hs, portanto, inegável a TEMPESTIVIDADE da presente contestação apresentada mesmo antes da referida data.

2.  SÍNTESE DA DEMANDA

O autor ajuizou em 10/12/2024, Ação de Obrigação de Fazer c/c Indenizatória por Danos Morais e Materiais, em face do PicPay e Arthur Lundgren Tecidos S.A. Casas Pernambucanas. Pleiteia liminarmente a retirada do seu nome do cadastro de inadimplentes, o pagamento de R$5.000,00 (cinco mil reais) à título de indenização por danos morais, bem como, o pagamento de R$80,00 (oitenta reais) a título de indenização por danos materiais.

Narra na peça inicial os seguintes fatos para fundamentar sua demanda:

-   Que entre os dias 01 e 08 de dezembro de 2024, começou a receber cobranças reiteradas de uma suposta dívida referente a um "seguro carteira" vinculado ao cartão Pernambucanas, contratado via aplicativo PicPay.

-   O Autor afirma desconhecer tal contratação, embora a cobrança conste em suas faturas desde setembro de 2024.

Alega, sem fundamento, que experimentou danos de natureza moral no decorrer dos acontecimentos, se socorrendo ao Judiciário para se ver indenizada pelos alegados danos.

Conforme demonstrado adiante, não assiste razão ao Autor. Dessa forma, os pedidos desta demanda deverão ser julgados improcedentes. É o que se passa a expor.

3.  DA REALIDADE DOS FATOS

  3.1. DO PASSO A PASSO PARA CONTRATAÇÃO DO SEGURO CARTEIRA

Cabe esclarecer que o seguro é ofertado em parceria com a seguradora Kovr. Esse seguro protege o saldo da Carteira PicPay em circunstâncias que envolvem movimentações bancárias como: pagamentos PIX, P2P, boleto, transferências (TED), saques e recarga de celular, realizados sob coação, ameaça física, roubo ou perda do celular. Além disso, os clientes também contam com a cobertura do saldo do Cofrinho, uma carteira separada na qual o usuário segmenta seu dinheiro de acordo com objetivos específicos.

O propósito do serviço é oferecer ao cliente a flexibilidade de escolher a cobertura de produtos que melhor atenda às suas necessidades na carteira, por isso, é possível contratar proteções adicionais, como:

-   “Proteção PicPay Card”: para transações realizadas sob coação ou ameaça física com o PicPay Card, ou após perda ou roubo do cartão;

-   “Proteção cartão protegido”: para transações realizadas sob coação ou ameaça física feitas com outros cartões cadastrados na Carteira PicPay, ou após perda ou roubo do cartão;

-   “Proteção segurança digital”: para transações que não forem realizadas pelo usuário, em caso de roubo de informações pessoais ou invasão de conta.

Destaca-se que este seguro não cobre a perda ou roubo do aparelho celular. O seguro da carteira digital é uma cobertura de segurança para o cliente, então ele só beneficia os produtos que forem cobertos pelo plano contratado.

Para contratar o seguro, o cliente deve acessar “Carteira” > “Proteger carteira”. Em seguida, ele escolhe o seguro que melhor atende às suas necessidades entre as opções disponíveis, conforme descrito na página anterior deste dossiê, e toca em “Contratar”. É importante destacar que as contratações só podem ser realizadas mediante o uso de senha ou biometria. As telas anexas demonstram que, ao longo da jornada de contratação, o cliente é previamente informado sobre cada etapa do processo e deve aceitar todos os procedimentos envolvidos.

[IMAGEM: jornada de contratação do seguro, telas 1 de 2]

[IMAGEM: jornada de contratação do seguro, telas 2 de 2]

Jornada de contratação do seguro

Logo após realizar a contratação do seguro digital, o cliente terá acesso ao Manual do Segurado, onde ele poderá verificar todas as regras de utilização e características da cobertura contratada. O manual também será disponibilizado no aplicativo para consultas posteriores, basta acessar a aba “Carteira” > “Proteger Carteira” > “Documentos” > “Manual do Segurado”.

Para adquirir o seguro, é necessário o pagamento de uma mensalidade de acordo com o plano escolhido pelo cliente. É possível realizar o pagamento com PicPay Card, saldo em conta, ou qualquer outro cartão cadastrado em carteira. O pagamento é realizado automaticamente, com a cobrança da mensalidade feita no mesmo dia da contratação, mês a mês, utilizando o método de pagamento previamente selecionado.

Assim, se o cliente escolher pagar com cartão de crédito, o próximo pagamento será automaticamente debitado do mesmo cartão.

No entanto, caso ocorra uma falha no método de pagamento principal, o aplicativo realizará a cobrança utilizando os métodos de pagamento adicionais, como o saldo disponível na carteira, por exemplo. Por esse motivo, uma vez selecionada, não é possível modificar a forma de pagamento.

Isso está explicado em nossa Central de Ajuda (FAQ), acessível a qualquer momento pelo aplicativo. Basta tocar em “Ajustes” > “Ajuda” e procurar por "Como funciona o pagamento do Seguro Carteira Digital?". Na Central de Ajuda, o demandante também encontrará todos os detalhes sobre o Seguro Carteira.

Ressalta-se que o cliente está segurado a partir do momento em que a confirmação do pagamento é realizada. Portanto, após o pagamento confirmado, não há nenhum período de carência a ser aguardado.

Quando o usuário opta por acionar o seguro, o cliente inicia o que chamamos de solicitação de sinistro. A abertura do sinistro é feita exclusivamente por meio da parceira Kovr, através do link: sinistropicpay.kovr.com.br

Caso haja alguma dúvida sobre a abertura de sinistro ou andamento da solicitação, também é necessário que o usuário entre em contato com a Kovr por e-mail atendimento@kovr.com.br ou pelos telefones (11) 4007 - 1790 - São Paulo (capital); 0800 646 8378 - Demais regiões.

  3.2. DA LEGITIMIDADE DA CONTRATAÇÃO E UTILIZAÇÃO DOS SERVIÇOS

Inicialmente, é importante destacar que o autor possui cadastro legítimo em nossa plataforma, desde 03/12/2020:

[IMAGEM: cadastro do autor na plataforma, desde 03/12/2020]

O autor alega que seu cartão de crédito Pernambucanas foi utilizado de forma indevida e que vem sendo cobrado por um seguro que não contratou.

Ocorre que, após análise, constatou-se que o seguro em questão foi contratado na conta de sua mãe, Sra. Roberta Kelly Silva.

[IMAGEM: comprovante de filiação]

Comprovante de filiação - ID.10360635426

No PicPay, aceitamos qualquer tipo de cartão de crédito (internacionais, virtuais, pré-pagos), desde que eles sejam das bandeiras Visa, American Express (Amex), Hipercard, Elo ou Mastercard.

Vale destacar que, para adicionar um cartão de crédito no aplicativo, é necessário que o usuário possua e informe o nome do titular, a data de vencimento e o CVV corretamente. Caso contrário, retorna uma mensagem de dados inválidos. A solicitação do CVV existe apenas para a segurança do cartão cadastrado.

[IMAGEM: jornada de cadastro de cartão de crédito, telas 1 de 2]

[IMAGEM: jornada de cadastro de cartão de crédito, telas 2 de 2]

Jornada de cadastro de cartão de crédito

Respeitamos todas as normas de segurança e solicitação de dados do PCI (órgão internacional de segurança de dados) e do Banco Central (BACEN). Os dados cadastrados no PicPay são criptografados e armazenados em servidores seguros. Isso quer dizer que ninguém mais tem acesso a eles.

Além disso, salientamos que o autor nos contatou em nosso atendimento via SAC no dia 10/12/2024, protocolo n° 42913108, reclamando sobre o seguro. Nossa equipe avaliou o caso e no dia 16/12/2024 identificou que o cartão estava cadastrado na conta PicPay de Roberta Kelly.

[IMAGEM: protocolo de SAC do autor, 1 de 2]
[IMAGEM: análise da equipe identificando o cartão na conta de Roberta Kelly, 2 de 2]

Diante disso, explicamos ao autor essa situação e informamos que caso conhecesse essa pessoa, era só solicitar que ela excluísse o cartão do cadastro. Contudo, caso não a conhecesse, orientamos a entrar em contato com a instituição emissora do seu cartão e contestar o valor cobrado.

Ficou claro que ele conseguiu contato com sua mãe no mesmo dia 16/12/2024, pois verificou que o seguro foi cancelado manualmente pela Sr.a Roberta:

[IMAGEM: cancelamento manual do seguro pela titular da conta, 1 de 2]
[IMAGEM: cancelamento manual do seguro pela titular da conta, 2 de 2]

Ainda, o cartão também foi excluído da conta da mãe do autor no mesmo dia 16/12/2024, vejamos:

[IMAGEM: exclusão do cartão da conta, 1 de 2]
[IMAGEM: exclusão do cartão da conta, 2 de 2]

Portanto, a contratação e a utilização do seguro foram legítimas. Ademais, o autor possui conhecimento sobre quem realizou a contratação, bem como de que o cartão estava vinculado à conta de sua mãe.

Excelência, cumpre ressaltar que não houve qualquer falha de segurança por parte do PicPay, uma vez que a pessoa que efetuou o cadastro do cartão detinha pleno acesso aos seus dados, os quais são de exclusiva responsabilidade do autor quanto à sua guarda e sigilo.

Assim sendo, verifica-se que o PicPay não fugiu ao cumprimento de suas obrigações institucionais e contratuais, tampouco deixou de prestar a assistência necessária ao Autor, diante do ocorrido, não podendo ser imputada qualquer falha na prestação do serviço ao PicPay.

Pelo exposto, requer que seja julgada IMPROCEDENTE esta demanda judicial.

4.  DO MÉRITO

4.1. IMPOSSIBILIDADE DE INVERSÃO DO ÔNUS DA PROVA

O pedido do Autor para a inversão do ônus da prova deve ser rejeitado, haja vista que o artigo 6º, inciso VIII, do CDC, estabelece que deve haver a comprovação da hipossuficiência do Autor e a verossimilhança de suas alegações, sendo que a produção dessas provas deve ser realizada com base nas regras do CPC, não devendo ser presumidas.

In casu, as alegações do Autor não são minimamente capazes de comprovar qualquer tipo de dano sofrido. Vê-se, assim, que a inversão não terá cabimento, pois diante dos indícios, não houve conduta irregular por parte da ré.

Quanto à hipossuficiência, trata-se de impotência do consumidor, seja de origem econômica ou de outra natureza, para apurar e demonstrar a causa do dano cuja responsabilidade é imputada ao fornecedor. Pressupõe uma situação em que concretamente se estabeleça uma dificuldade muito grande para o consumidor de desincumbir–se de seu natural onus probandi, estando o fornecedor em melhores condições para elucidar o evento danoso. Não estão presentes, no caso em tela, a hipossuficiência que justificaria a medida.

Além disso, a inversão não deve ser automática, ocorrendo somente por decisão do Juiz diante dos requisitos previstos em lei, sendo este o entendimento dos Tribunais:

  AGRAVO INTERNO NO RECURSO ESPECIAL. AÇÃO DECLARATÓRIA DE INEXISTÊNCIA DE DÉBITO C/C REPARAÇÃO POR DANOS MORAIS. ALEGAÇÃO DE OMISSÃO E DEFICIÊNCIA DE FUNDAMENTAÇÃO. NÃO OCORRÊNCIA. INVERSÃO DO ÔNUS DA PROVA. NECESSIDADE DE COMPROVAÇÃO MÍNIMA DAS TESES DEDUZIDAS. AGRAVO DESPROVIDO. (...) A jurisprudência desta Corte Superior se posiciona no sentido de que a inversão do ônus da prova não dispensa a comprovação mínima, pela parte autora, dos fatos constitutivos do seu direito. 3. Assim, antes de ser imputado à ré o ônus de produção da prova em sentido contrário, caberia ao Autor comprovar minimamente o seu direito, por meio da apresentação de documento comprobatório do pedido de cancelamento do terminal telefônico, ônus do qual não desincumbiu.

  (STJ, AgInt no REsp: 1717781/RO Relator: Min. MARCO AURÉLIO BELLIZZE, Julgamento: 05/06/2018, 3º Turma, DJe 15/06/2018)

  Não comprovação dos alegados danos materiais e morais sofridos. - Ao autor, incumbe a prova dos atos constitutivos de seu direito. - Em que pese a indiscutível aplicação da inversão do ônus da prova ao CDC, tal instituto não possui aplicação absoluta. A inversão deve ser aplicada quando, a critério do juiz, for verossímil a alegação ou quando for ele hipossuficiente, segundo as regras ordinárias de experiências. - Entenderam as instâncias ordinárias, após análise das provas dos autos, que o recorrente não comprovou as falhas na prestação dos serviços contratados. Necessidade de revolvimento de todo o conjunto fático-probatório. Óbice da Súmula 7 do STJ. - O recorrente não provou a ocorrência de vícios no serviço que pudessem lhe conferir direito a uma indenização por danos materiais ou morais. Recurso especial não conhecido”.

  (STJ - REsp: 741393/PR Relator: Ministra NANCY ANDRIGHI, 3º Turma, DJe 22/08/2008)

No caso em tela não há que se falar em inversão, tendo em vista que o dano pleiteado deve ser provado pelo Autor, não sendo possível ser produzido prova por parte do PicPay a esse respeito. A concessão da inversão do ônus da prova sem o preenchimento dos requisitos legais afronta ao princípio constitucional da igualdade (Constituição Federal, artigo 5º).

Assim, o Autor não demonstrou de forma incontroversa sua hipossuficiência, bem como não comprovou a verossimilhança de suas alegações, razão pela qual deve ser indeferido o pedido de inversão do ônus da prova. 

4.2. DA NATUREZA DOS SERVIÇOS PRESTADOS PELO REQUERIDO – O QUE É O PICPAY?

Antes de informar/esclarecer os motivos pelos quais o Requerido não possui qualquer pendência e inexiste o dever de indenizar suscitado pelo Requerente, pede-se vênia para explicar resumidamente a sua forma de atuação.

Fundado em julho de 2012, na capital do Estado do Espírito Santo, o PICPAY é uma instituição de pagamento, autorizada pelo Banco Central do Brasil – BACEN, que abraça os mais diversos tipos de público – em especial, aqueles consumidores desbancarizados –, oferecendo aos seus clientes uma vasta gama de produtos e serviços digitais para facilitar o seu dia-a-dia.

Para a melhor compreensão de sua natureza e atividades, pertinente se faz colacionar a definição dada pelo BACEN a uma instituição de pagamento:

  “Instituições de pagamento são pessoas jurídicas não financeiras que executam os serviços de pagamento no âmbito do arranjo de pagamento e que são responsáveis pelo relacionamento com os usuários finais do serviço de pagamento, pagadores e recebedores.
  São exemplos de instituições de pagamento os credenciadores de estabelecimentos comerciais para a aceitação de cartões e as instituições não financeiras que recebem recursos do público que serão utilizados para fazer pagamentos ou transferir fundos, utilizando, por exemplo, moeda eletrônica.”[1]

  As instituições de pagamento possibilitam ao cidadão realizar pagamentos independentemente de relacionamentos com bancos e outras instituições financeiras. Com o recurso financeiro movimentável, por exemplo, por meio de um cartão pré-pago ou de um telefone celular, o usuário pode portar valores e efetuar transações sem estar com moeda em espécie. Graças à interoperabilidade, o usuário pode, ainda, receber e enviar dinheiro para bancos e outras instituições de pagamento.[2]

Neste ponto, considerando que a atuação do PicPay se dá “no âmbito do arranjo de pagamento”, cumpre esclarecer que este “é o conjunto de regras e procedimentos que disciplina a prestação de determinado serviço de pagamento ao público”, objetivando facilitar “as transações financeiras que usam dinheiro eletrônico”[3], ou seja, é a tecnologia que permite que as transações financeiras sejam possíveis, através de cartões (crédito ou débito), boletos ou telefones celulares.

Feita essa breve digressão, de rigor mencionar que, com o PicPay, o consumidor pode efetuar, via aplicativo, pagamentos com cartão de crédito, enviar e receber dinheiro, pagar boletos, emitir cobranças, transferir dinheiro, realizar recarga de celular e de cartões de transporte, utilizar o saldo da carteira virtual em mais de 5 (cinco) milhões de estabelecimentos cadastrados, além de armazenar dinheiro em sua “carteira virtual”:

[IMAGEM: funcionalidades do aplicativo PicPay]

Trata-se, em outras palavras, de um aplicativo de pagamentos – com sistema operacional Android ou IOS -, que funciona como uma “carteira digital”, que, em 2021, atingiu mais de 50 milhões de clientes no Brasil, tornando-se um dos maiores aplicativos de pagamentos do país, facilitando, indene de dúvidas, a vida financeira de seus usuários.

Desta forma, relevante apontar a Vossa Excelência que, nessa função, o PicPay agiu adequadamente conforme a sua função institucional, não havendo o que se falar em responsabilização por quaisquer prejuízos suscitados pela parte adversa.

  4.3. DA CULPA EXCLUSIVA DO AUTOR

Cabe reiterar que não há qualquer irregularidade na conduta do PicPay. Portanto, se de fato o autor não reconhece a contratação do seguro, essa se deu por terceiro em posse de seus dados pessoais, sendo que não há como responsabilizar o PicPay por tal.

Nesta senda, é culpa exclusiva do Autor pois permitiu que terceiro tivesse acesso aos seus dados e realizasse a contratação do seguro reclamado.

Além disso, o artigo 14 do CDC estabelece o rol para configuração na falha de prestação de serviços, in verbis:

  Art. 14. O fornecedor de serviços responde, independentemente da existência de culpa, pela reparação dos danos causados aos consumidores por defeitos relativos à prestação dos serviços, bem como por informações insuficientes ou inadequadas sobre sua fruição e riscos.

  § 1° O serviço é defeituoso quando não fornece a segurança que o consumidor dele pode esperar, levando-se em consideração as circunstâncias relevantes, entre as quais:

  I - o modo de seu fornecimento;

  II - o resultado e os riscos que razoavelmente dele se esperam;

  III - a época em que foi fornecido.

Portanto, resta afastada a responsabilidade do PicPay no caso em tela, nos termos do § 3º do art. 14 do CDC, visto que foi comprovada a culpa exclusiva do autor.

4.4. DO EXERCÍCIO REGULAR DO DIREITO

Conforme narrado anteriormente, houve a contratação do seguro de forma legítima. Sendo assim, não há o que se falar em falhas ou devolução de valores.

Todo aquele que exerce um direito assegurado por lei não pratica ato ilícito. o Autor, ciente dos termos de condições de uso, cedeu os seus dados pessoais, e o PicPay atuou apenas como intermediador da contratação do seguro, o que não configura ato ilícito (art. 186 do Código Civil - CC), vez que consiste no exercício regular do direito.

O Superior Tribunal de Justiça possui o entendimento consolidado em casos análogos, reconhecendo o exercício regular do direito, bem como afastando qualquer condenação em reparação de danos:

  DÉBITO REALIZADO EM EXERCÍCIO REGULAR DE DIREITO. ATO ILÍCITO INEXISTENTE. ENCARGOS SUCUMBENCIAIS.INVERSÃO. [...] Age em exercício regular de direito a instituição financeira que, ao valer-se de autorização prevista em cláusula contratual, debita valores referentes a operação de empréstimo em conta bancária, ainda...Requer, em consequência da declaração de ilegalidade, a devolução dos valores debitados e a condenação no pagamento de danos morais.

  (STJ - AREsp: 1790408 PR 2020/0303611-8, Relator: Ministra MARIA ISABEL GALLOTTI, Data de Publicação: DJ 09/04/2021)

  AGRAVO INTERNO NO AGRAVO EM RECURSO ESPECIAL. RECURSO ESPECIAL NÃO CONHECIDO. RECONSIDERAÇÃO DA DECISÃO AGRAVADA. CONTRATO BANCÁRIO.CONTRATO DE EMPRÉSTIMO. GASTOS EM CARTÃO DE CRÉDITO. DESCONTO DAS PARCELAS EM CONTA CORRENTE EM QUE DEPOSITADO O SALÁRIO. AUSÊNCIA DE ATO ILÍCITO. REPETIÇÃO DO INDÉBITO. DANOS MORAIS. DESCABIMENTO.AGRAVO INTERNO PROVIDO. RECURSO ESPECIAL NÃO PROVIDO. 1. É lícito o desconto em conta corrente bancária comum, ainda que usada para recebimento de salário, das prestações relativas a contratos de empréstimos, financiamentos, cartões de crédito, e outros serviços bancários livremente pactuados entre o correntista e a instituição financeira. Precedentes. 2. Consoante a jurisprudência do Superior Tribunal de Justiça, por se tratar de hipóteses diversas, não é possível aplicar, por analogia, a limitação legal de descontos firmados em contratos de empréstimo consignado aos demais contratos firmados com cláusula de desconto em conta corrente. Incidência da Súmula 83/STJ. 3. Na hipótese, em que pese o Tribunal de origem tenha limitado os descontos realizados na conta corrente da recorrente a 30% do valor dos seus rendimentos, não há que se falar em repetição do indébito ou indenização por danos morais, em razão da licitude dos descontos efetuados pela instituição financeira. 4. Agravo interno provido para, reconsiderando a decisão agravada, negar provimento ao recurso especial.

  (AgInt no AREsp 1527316/DF, Rel. Ministro RAUL ARAÚJO, QUARTA TURMA, DJe 13.2.2020).

Portanto, as cobranças na fatura do cartão de crédito do autor são legítimas e decorrem da contratação do seguro carteira.

Assim, impugna-se as alegações do Autor quanto ao desconto indevido e requer o reconhecimento do exercício regular do direito, pois o repasse só foi realizado em razão da solicitação pelo Autor.

4.5. DA AUSÊNCIA DE DEVER DE INDENIZAR - DA INEXISTÊNCIA DE FALHA NA PRESTAÇÃO DE SERVIÇO

Resta demonstrado que o PicPay cumpriu de forma correta sua prestação de serviço, prestou o devido suporte ao Autor quando comunicado, e também dispõe em seu site todas as soluções de eventuais dúvidas que possam surgir, conforme já demonstrado.

O dever de indenizar encontra-se plasmado no artigo 927 do cc, o qual estabelece o seguinte:

  Art. 927. Aquele que, por ato ilícito (arts. 186 e 187), causar dano a outrem, fica obrigado a repará-lo.

  Parágrafo único. Haverá obrigação de reparar o dano, independentemente de culpa, nos casos especificados em lei, ou quando a atividade normalmente desenvolvida pelo Autor do dano implicar, por sua natureza, risco para os direitos de outrem.

O ato ilícito consiste naquele que por ação, omissão, negligência ou imperícia, causar dano a outrem, nos moldes do artigo 186 do CC, o que não se verifica no caso em tela.

É evidente que o PicPay não cometeu nenhuma ação descrita no artigo legal supra, pois apenas disponibilizou a contratação do seguro na plataforma, e a análise foi realizada exclusivamente pela Seguradora Kovr.

Assim, não se verifica a existência de ato ilícito, vez que competia ao Autor se atentar às condições gerais para utilização e cobertura do seguro em questão.

Além disso, o artigo 14 do CDC estabelece o rol para configuração na falha de prestação de serviços, in verbis:

  Art. 14. O fornecedor de serviços responde, independentemente da existência de culpa, pela reparação dos danos causados aos consumidores por defeitos relativos à prestação dos serviços, bem como por informações insuficientes ou inadequadas sobre sua fruição e riscos.

  § 1° O serviço é defeituoso quando não fornece a segurança que o consumidor dele pode esperar, levando-se em consideração as circunstâncias relevantes, entre as quais:

  I - o modo de seu fornecimento;

  II - o resultado e os riscos que razoavelmente dele se esperam;

  III - a época em que foi fornecido.

Sob nenhum aspecto é possível vislumbrar eventual falha na prestação de serviço não se enquadrando em nenhuma das vertentes do artigo 14 do aludido Codex Consumerista.

Portanto, não se encontram presentes os requisitos caracterizadores do dever de indenizar, vez que não há ato ilícito.

O PicPay cumpriu com todas suas obrigações, razão pela qual impugna-se as alegações autorais e requer o reconhecimento da ausência do dever de indenizar, demonstrando a inexistência de falha na prestação de serviço.

4.5. DA INOCORRÊNCIA DE DANOS MORAIS

O Autor, diante de supostos aborrecimentos a ela causados, requer a condenação dos réus ao pagamento da exorbitante quantia de R$5.000,00 (cinco mil reais), relativos à reparação de danos morais. Porém, seu pedido deve ser, de plano, rejeitado, conforme passa a expor. 

Pela narrativa fática apresentada, é impossível a constatação de responsabilidade do PicPay, em razão de ter apenas disponibilizado o seguro na plataforma, cujo contrato foi firmado entre o Autor e a Seguradora Kovr.

Só seriam cabíveis eventuais danos morais - mera argumentação -, se de fato se estivesse diante da violação de algum direito da personalidade e se comprovado o nexo causal com as alegações do Autor.

Entretanto, o Autor não logrou êxito em comprovar os autos os danos morais que teria sofrido em decorrência dos serviços prestados pela Ré.

Conclui-se, portanto, que não houve desrespeito ao CDC, nem tampouco aos princípios estabelecidos no mesmo diploma legal, posto que o serviço foi prestado com a qualidade esperada.

Deve-se pontuar que o princípio da boa-fé objetiva, plasmado pelo CDC (artigo 4, III) e pelo CC (artigos 422, 113 e 187) constitui uma "estrada de duas mãos", estabelecendo deveres éticos para as duas partes vinculadas por uma relação obrigacional, mesmo nas relações de consumo, em todas as suas fases desde momento anterior à celebração de um negócio jurídico até momento posterior à própria extinção do vínculo negocial.

A boa-fé objetiva constitui verdadeiro modelo de conduta, exigido de todos integrantes da relação obrigacional (devedor e credor), devendo manter uma postura ética na busca do correto adimplemento da obrigação, que é a sua finalidade essencial.

A PicPay não praticou qualquer ato ilícito na execução do seu dever obrigacional tampouco cometeu falhas na prestação dos seus serviços, sendo que não se justifica o pedido de danos morais, sendo este o entendimento jurisprudencial, observa-se:

  APELAÇÃO CÍVEL Nº 0001085-95.2019.8.08.0021 APELANTE: ELIZABETE SALUSTRE DOS SANTOS APELADO: BANCO BRADESCO S/A RELATOR: DES. ANNIBAL DE REZENDE LIMA ACÓRDÃO EMENTA CONSUMIDOR APELAÇÃO CÍVEL AÇÃO DE INDENIZAÇÃO ATENDIMENTO EM AGÊNCIA BANCÁRIA TEMPO DE ESPERA DANO MORAL INEXISTÊNCIA DE CIRCUNSTÂNCIAS PECULIARES MERO DISSABOR RECURSO DESPROVIDO. O mero dissabor ou aborrecimento cotidiano, peculiar às relações comerciais, que não exponha o consumidor a uma situação de perigo, humilhação ou constrangimento, sem causar-lhe abalo à honra e à dignidade, não gera dano moral indenizável. VISTOS, relatados e discutidos os presentes autos de recurso de apelação em que é Apelante ELIZABETE SALUSTRE DOS SANTOS e Apelado BANCO BRADESCO S/A ; A CORDA a Colenda Primeira Câmara Cível, na conformidade da ata e notas taquigráficas da sessão, à unanimidade, conhecer do recurso e lhe negar provimento, nos termos do voto do Relator. Vitória, 02 de março de 2021. PRESIDENTE RELATOR

  (TJ-ES - AC: 00010859520198080021, Relator: ANNIBAL DE REZENDE LIMA, Data de Julgamento: 02/03/2021, PRIMEIRA CÂMARA CÍVEL, Data de Publicação: 16/03/2021)

  APELAÇÃO CÍVEL Nº 0011184-63.2011.8.08.0035 APELANTE: FABIANO MOREIRA LIMA APELADO: BANCO PANAMERICANO S⁄A RELATOR: DES. SUBST. JÚLIO CÉSAR COSTA DE OLIVEIRA ACÓRDÃO EMENTA CIVIL E PROCESSUAL CIVIL - APELAÇÃO CÍVEL - DANOS MORAIS – AUSÊNCIA DE NEGATIVAÇÃO - MERO DISSABOR - INEXISTÊNCIA DE DANO MORAL. Para a caracterização do dano moral, impõe-se seja a parte vítima de uma situação tal que a impinja verdadeira dor e sofrimento, sentimentos esses capazes de lhe incutir transtorno psicológico de grau relevante ou, no mínimo, abalo que exceda a normalidade. O vexame, a humilhação ou a frustração devem interferir de forma intensa no âmago do indivíduo, causando-lhe aflições, angústia e desequilíbrio em seu bem-estar. VISTOS, relatados e discutidos os presentes autos de recurso de apelação cível, em que é Apelante FABIANO MOREIRA LIMA e Apelado BANCO PANAMERICANO S⁄A. ACORDA a Colenda Primeira Câmara Cível, na conformidade da ata e notas taquigráficas da sessão, por unanimidade de votos, conhecer do recurso e lhe negar provimento, nos termos do voto do Relator. Vitória, 15 de setembro de 2015. PRESIDENTE RELATOR

  (TJ-ES - APL: 00111846320118080035, Relator: ANNIBAL DE REZENDE LIMA, Data de Julgamento: 15/09/2015, PRIMEIRA CÂMARA CÍVEL, Data de Publicação: 24/09/2015)

Ora, o que seria o relatado senão um mero aborrecimento? Vale lembrar que o artigo 186 do CC prevê a culpa de outrem como ato ilícito se deste ato houver omissão, negligência ou imprudência.

Os percalços eventualmente sofridos consistem em mero dissabor, não vindo a agredir os direitos de personalidade da consumidora, o Autor não demonstra nenhuma de suas alegações constitutivas do direito, não juntou um documento sequer que comprove o alegado constrangimento que experimentou.

O dano moral atinge a honra, o caráter e aquilo que é mais íntimo do ser, sendo necessária a aferição média comparada entre a situação verídica e o que se espera ou poderia esperar. Excelência, o Autor não comprovou qualquer abalo psicológico, qualquer ponte entre a normalidade do cotidiano e um suposto dano causado pela Ré.

O Superior Tribunal de Justiça possui o entendimento de que os danos extrapatrimoniais devem ser provados pela parte que o alega, como se vê:

  PROCESSUAL CIVIL E ADMINISTRATIVO. OFENSA AO ART. 1.022 DO CPC/2015 NÃO CONFIGURADA. RESPONSABILIDADE CIVIL DO ESTADO. ACIDENTE DE TRÂNSITO. AÇÃO DE INDENIZAÇÃO POR DANOS MATERIAIS E MORAIS. ACÓRDÃO RECORRIDO COM FUNDAMENTO CONSTITUCIONAL. SÚMULA 126/STJ. 1. A solução integral da controvérsia, com fundamento suficiente, não caracteriza ofensa ao art. 1.022 do CPC/2015. 2. No mérito, assim se manifestou a Corte local para reformar a sentença no que diz respeito aos danos emergentes (fl. 747-751, e-STJ): "Cinge-se a controvérsia à responsabilidade do Município de Cabedelo pelos danos percebidos em razão da colisão de veiculo automotor de sua propriedade com o ciclista, em acidente ocorrido na BR-230. O art. 37, §6° da Constituição Federal dispõe que as pessoas jurídicas de direito público e as de direito privado prestadoras de serviços públicos responderão objetivamente pelos danos que seus agentes, nessa qualidade, causarem a terceiros. O dispositivo constitucional institui a responsabilidade objetiva por danos causados pelos agentes do Estado e das prestadoras de serviço público, sem distinguir se se cuida de responsabilidade por ação ou omissão, por ato lícito ou ilícito. Para que surja o dever de indenizar, bastante estejam provados o ato de agente estatal, o dano e o nexo de causalidade entre um e outro, prescindível a prova da conduta culposa ou dolosa. (...) Não há prova de que o Autor tenha pago tal valor, tampouco realizado a cirurgia. Por isso, o pleito deve ser postulado em ação própria e não por via reflexa, em ação de indenização. Por óbvio, deve ser parcialmente reformada a sentença, no sentido de excluir da condenação a imposição constante no item 3 do dispositivo da sentença: '3) na obrigação de arcar com as despesas da cirurgia descrita no pedido de fls. 338'". 3. Ao decidir a questão, o Tribunal de origem se embasou em preceitos constitucionais e infraconstitucionais. Contudo, contra o aresto impugnado foi interposto unicamente o presente Recurso Especial, deixando o agravante de apresentar Recurso Extraordinário ao STF. Permanecem incólumes os fundamentos constitucionais do decisório recorrido, suficientes para mantê-lo. Incide o óbice da Súmula 126/STJ. 4. Agravo conhecido para conhecer parcialmente do Recurso Especial, apenas em relação à preliminar de violação do art. 1.022 do CPC/2015, e, nessa parte, não provido.

  (AREsp n. 1.548.458/PB, relator Ministro Herman Benjamin, Segunda Turma, julgado em 19/9/2019, DJe de 11/10/2019.)

  AGRAVO INTERNO NO AGRAVO EM RECURSO ESPECIAL. AÇÃO DE INDENIZAÇÃO POR DANOS MORAIS. FALHA NA PRESTAÇÃO DO SERVIÇO. AUSÊNCIA DE COMPROVAÇÃO. SAQUE EM CONTA CORRENTE MEDIANTE USO DE CARTÃO MAGNÉTICO E SENHA PESSOAL. ACÓRDÃO ESTADUAL QUE DECIDIU COM BASE NAS PROVAS DOS AUTOS ALINHADO À JURISPRUDÊNCIA DESTA CORTE. INCIDÊNCIA DAS SÚMULAS NºS 7 E 83 DO STJ. AGRAVO INTERNO NÃO PROVIDO. 1. Tribunal local que, com amparo nos elementos de convicção dos autos, entendeu não estar provado o fato constitutivo do direito do Autor, decidindo pela ausência dos requisitos ensejadores da reparação civil. O uso do cartão magnético com sua respectiva senha é exclusivo do correntista e, portanto, eventuais saques irregulares na conta somente geram responsabilidade para o Banco se provado ter agido com negligência, imperícia ou imprudência na entrega do numerário, o que não ocorreu na espécie. 2. Impossibilidade de reexame de fatos e provas. Incidência do óbice da súmula 7/STJ no tocante à tese de reconhecimento da responsabilidade civil. 3. Ademais, é firme a jurisprudência do Superior Tribunal de Justiça no sentido de que a presunção de veracidade dos fatos alegados pelo Autor em razão da ocorrência da revelia é relativa, sendo que para o pedido ser julgado procedente o juiz deve analisar as alegações do Autor e as provas produzidas. 4. Agravo interno não provido.

  (AgInt no AREsp n. 1.399.771/MG, relator Ministro Luis Felipe Salomão, Quarta Turma, julgado em 2/4/2019, DJe de 8/4/2019.)

Novamente, o Autor não comprova nos autos nenhum ato da contestante que enseje a reparação de danos morais, não cumprindo o ônus existente no artigo 373 do CPC e o entendimento unânime dos Tribunais, ressaltando que não houve conduta ilícita da Contestante PicPay.

A postura da Ré não se enquadra em qualquer sistemática do artigo 186 do CC ou qualquer signatário que decorra em prejuízo causado sob o manto da irresponsabilidade.

Portanto, requer que seja afastado o pedido de condenação em danos morais e materiais em qualquer patamar. 

4.5.1. DO PEDIDO SUBSIDIÁRIO - DA REDUÇÃO DOS DANOS MORAIS PLEITEADOS

Espera a Ré, serenamente, que o pedido de reparação de danos morais seja julgado totalmente improcedente. Malgrado, apenas por amor ao debate, requer, subsidiariamente, na remota hipótese de ser reconhecido o dano, o que não se acredita, que a condenação seja arbitrada em valor moderado, ficando desde já impugnado o valor pretendido pelo Autor, sendo totalmente incabível uma condenação na quantia requerida.

Inacreditavelmente o Autor pleiteia uma indenização por danos morais de R$5.000,00 (cinco mil reais), montante que se mostra demasiadamente elevado, quando sequer há responsabilidade imputável à PicPay.

Frisa-se que não houve falha na prestação de serviços, sendo que o PicPay apenas disponibilizou a contratação do seguro na plataforma, e a análise foi realizada exclusivamente pela Seguradora Kovr.

O dano moral deve ser aferido sob dois binômios, a realidade fatídica e o prejuízo causado. Assim, deve ser levado em consideração o prejuízo efetivamente causado ao Autor. No caso em tela não houve qualquer conduta ilícita por parte do PicPay, como se observa da realidade fática já relatada.

O Prof. Carlos Roberto Gonçalves já tratou do tema com excelência:

  Por outro lado, deve o juiz, ‘ao fixar o valor, e à falta de critérios objetivos, agir com prudência, atendendo em cada caso, Às suas peculiaridades e à repercussão econômica da indenização, de modo que o valor da mesma não deve ser nem tão grande que se converta em fonte de enriquecimento, nem tão pequeno que se torne inexpressivo. (GONÇALVES, Carlos Roberto. Direito Civil Brasileiro: Responsabilidade Civil. p. 407, 2016).

Em que pese estar demonstrado que não houve ato ilícito ou sofrimento de dano moral de acordo com o cenário apresentado, à luz do princípio da eventualidade, cabe à Ré destacar que, caso esse MM. Juízo entende pela procedência do pedido, o valor da indenização deve ser baseado nos critérios de proporcionalidade e razoabilidade, de forma a evitar enriquecimento sem causa. Ademais, os Tribunais vêm decidindo que a fixação do quantum indenizatório por dano moral deve ser feita com critérios e moderação com o intuito de não banalizar o instituto. Assim, deve ser respeitada a proporcionalidade entre a extensão do dano e o montante a ser arbitrado para indenização dos danos morais.

Destaca-se que não houve falha na prestação de serviços por parte do PicPay, não cabendo imputação de responsabilidade sobre quaisquer transações, enquanto a indenização pretendida é de R$5.000,00 (cinco mil reais), sendo evidente o enriquecimento sem causa do Autor, nos moldes do artigos 884 e 994 do CC.

O E. Tribunal de Justiça do Espírito Santo inclusive, entende que eventual condenação em danos morais, o valor deve ser minorado, respeitando a razoabilidade e proporcionalidade, observa-se:

  CONSUMIDOR E PROCESSUAL CIVIL. APELAÇÃO CÍVEL. AÇÃO OBRIGACIONAL C/C INDENIZAÇÃO POR DANOS MORAIS. FORNECIMENTO INSUFICIENTE DE ENERGIA ELÉTRICA. NECESSIDADE DE INSTALAÇÃO DE TRANSFORMADOR. DANOS MORAIS CONFIGURADOS. RAZOABILIDADE E PROPORCIONALIDADE. REDUÇÃO DO MONTANTE. RECURSO PARCIALMENTE PROVIDO. 1) Nos termos do art. 40 da Resolução nº 414/2010 da ANEEL, cabe à concessionária promover a instalação gratuita de transformador ou extensão de rede em propriedade com consumo inferior a 50 kW. 2) Comprovada a insuficiência na prestação do serviço de fornecimento de energia elétrica e os transtornos gerados ao consumidor, que se encontra privado do uso de eletrodomésticos básicos, afigura-se adequada a condenação ao pagamento de indenização por danos morais. 3) Em atenção aos postulados da razoabilidade e proporcionalidade e considerando a ausência de prova de perda econômica direta decorrente do fato em exame, revela-se necessária a redução do montante para R$ 4.000,00, o que, aliás, está em consonância com outros precedentes deste Sodalício em causas similares. 4) Recurso parcialmente provido. ACORDA a Egrégia Segunda Câmara Cível, em conformidade da ata e notas taquigráficas da sessão, que integram este julgado, à unanimidade, dar parcial provimento ao apelo.

  (TJES - APL 0000219-98.2018.8.08.0061 Órgão Julgador SEGUNDA C MARA CÍVEL Publicação 30/10/2019 Julgamento 22 de Outubro de 2019 Relator JOSÉ PAULO CALMON NOGUEIRA DA GAMA)

Ou seja, o valor pleiteado pelo Autor mostra-se absolutamente desproporcional ao suposto prejuízo por ela sofrido, tendo em vista que não houve responsabilidade da ré, razão pela qual impugna-se o valor ora pleiteado.

Desta forma, caso o pedido não seja julgado improcedente, na eventual condenação de indenização de danos morais, requer que estes sejam reduzidos ao patamar adequado, considerando os princípios da razoabilidade e proporcionalidade.

  5. DOS REQUERIMENTOS FINAIS

Por todas razões expostas, requer a Vossa Excelência:

  (i) Seja acolhida a preliminar arguida de ilegitimidade passiva do PicPay, julgado extinto o feito sem resolução do mérito;

  (ii) Seja negada a aplicação da inversão do ônus da prova, uma vez que absolutamente descabida no caso em epígrafe, pois não apresenta seus requisitos de implementação: verossimilhança do quanto alegado pelo Autor e a hipossuficiência

  (iii) Caso Vossa Excelência não entenda desta forma, requer que a presente ação seja julgada totalmente IMPROCEDENTE, , bem como a ausência no dever de indenizar por danos morais, vez que o Autor não comprovou a experimentação de qualquer constrangimento aos seus direitos da personalidade, tampouco demonstrou conduta ilícita da Ré, afastando tais pedidos autorais. De forma subsidiária, que o valor pleiteado a título de danos morais seja reduzido nos moldes dos princípios da razoabilidade e proporcionalidade;

  Protesta por todos os meios de prova em direito admitidos, ainda que não especificamente pleiteados.

Por fim, requer-se ainda que as publicações ocorridas nestes autos sejam feitas em nome de MARIO THADEU LEME DE BARROS FILHO (OAB/MG nº 230.285 - S), sob pena de nulidade.

Termos em que pede deferimento.

São Paulo/SP, 29 de Maio de 2025

MARIO THADEU LEME DE BARROS FILHO

OAB/MG nº 230.285 - S

[1] https://www.bcb.gov.br/acessoinformacao/glossario

[2] https://www.bcb.gov.br/pre/composicao/instpagamento.asp?frame=1#:~:text=Institui%C3%A7%C3%A3o%20de%20pagamento%20(IP)%20%C3%A9,e%20financiamentos%20a%20seus%20clientes.

[3] https://www.bcb.gov.br/estabilidadefinanceira/arranjospagamento
```

## Passo 4: Peça completa em .docx com provas embutidas (quando pedido)

Quando o usuário pedir a peça pronta para protocolo com as provas anexadas,
não só o texto:

1. **Numere os documentos pela ordem em que aparecem no texto** (Doc. 01,
   Doc. 02, ...), não pela ordem em que foram recebidos. Ao inserir ou remover
   um documento depois de já ter numerado, renumere tudo o que vier depois e
   confira, com uma busca por `Doc\. [0-9]+` no arquivo inteiro, que a
   sequência ficou contínua e sem repetição, tanto no corpo do texto quanto na
   lista final de documentos.
2. **Prepare as imagens de cada prova**: renderize páginas de PDF com
   PyMuPDF (`page.get_pixmap(dpi=200)` é uma resolução boa para tela e
   impressão) e recorte com PIL o que interessa de cada print (remova cabeçalho
   de ticket, nome de sistema interno, colunas irrelevantes, nome de
   atendente ou de time interno), deixando a evidência limpa e enquadrada.
   Remova também qualquer nota, rodapé ou aviso de manuseio interno (ex.:
   "dados sensíveis, apresentação nos autos mediante autorização judicial"):
   esses avisos nunca podem aparecer no recorte final, mesmo quando a
   informação em si (biometria, documento, dado do sistema) é mantida e
   embutida normalmente (ver nota sobre isso no Passo 1). Depois de cada
   corte, releia a imagem resultante para conferir tanto que não sobrou nome
   de área interna ou aviso de manuseio quanto que o corte não cortou texto
   ou conteúdo relevante ao meio.
   **Uma tela-fonte com vários fatos gera vários recortes, nunca um só:**
   quando um mesmo print ou página reúne mais de um dado que a peça vai
   afirmar separadamente (ex.: dois ou três dispositivos vinculados numa
   mesma tabela, ou um dispositivo e um evento de redefinição de senha na
   mesma tela), recorte cada dado em uma imagem própria, mesmo que isso
   signifique cortar a mesma tela-fonte em fatias diferentes (uma por linha
   de dispositivo, por exemplo). Nunca use um único recorte amplo, com vários
   dispositivos ou eventos visíveis ao mesmo tempo, para ilustrar mais de um
   parágrafo/item da peça: cada parágrafo ou item numerado tem sua própria
   imagem dedicada ao fato que ele afirma (ver também a abertura obrigatória
   do 5.2, que exige um item por dispositivo e por evento de segurança).
3. **Gere o .docx** com a biblioteca `docx` (Node/docx-js): `ImageRun` para
   cada prova, com largura uniforme para todas as imagens, centralizada, e
   uma legenda curta em itálico logo abaixo ("Doc. NN — descrição").
   **Níveis de título:** use `##` para as seções de primeiro nível do
   esqueleto (1, 2, 3, 4, 5, 6 — ex. `## 5. Mérito`), `###` para o segundo
   nível decimal (X.Y — ex. `### 5.3. Do direito`) e `####` para o terceiro
   nível decimal, quando o caso pedir essa granularidade (X.Y.Z — ex.
   `#### 5.3.1. Culpa exclusiva do consumidor e terceiros`). Ao montar o
   script que gera o `.docx`, mapeie os três níveis markdown para três estilos
   de título decrescentes (ex.: Heading 1, Heading 2, Heading 3 do Word, com
   tamanho de fonte decrescente entre eles); não pare no segundo nível só
   porque nem todo caso usa granularidade de terceiro nível.
   **Posicionamento das imagens, regra obrigatória:** cole cada imagem logo
   após o parágrafo em que o documento correspondente é mencionado pela
   primeira vez de forma completa (quando o mesmo documento é citado em duas
   frases seguidas, como "(Doc. 01 e Doc. 03)" repetido em dois fatos
   consecutivos, cole a imagem depois da segunda menção, a mais completa).
   Nunca escreva todos os parágrafos de uma seção primeiro e só depois
   acumule as imagens correspondentes num bloco só ao final dela: a imagem
   entra no fluxo do texto, no ponto em que o fato ou a cláusula que ela
   comprova acabou de ser afirmado. **Nenhum tópico ou subtópico pode
   terminar em imagem.** Depois da última imagem inserida dentro de um item
   (um fato da cronologia, uma subseção do mérito), sempre deve vir ainda um
   parágrafo de texto antes do próximo título ou item: se a seção já tinha um
   parágrafo de fechamento ("Em suma...", "Nesse cenário...", frase de
   transição para o próximo tópico), posicione a imagem antes desse parágrafo
   de fechamento, não depois dele. Se a seção não tinha um parágrafo de
   fechamento previsto, escreva um breve parágrafo de transição só para essa
   finalidade, em vez de deixar a imagem como último elemento visual antes do
   próximo título. Mantenha o mesmo texto do corpo em um `.md` paralelo (sem
   imagens, só o texto), para o usuário poder copiar e ajustar. Ao alterar a
   peça depois de gerada, edite os dois arquivos (`.md` e o script que gera o
   `.docx`) e regenere.
4. **Verifique visualmente antes de entregar**: converta o .docx para PDF
   (`soffice --headless --convert-to pdf`) e depois para JPEG por página
   (`pdftoppm -jpeg`), e releia página a página com a ferramenta de leitura
   de imagem, sobretudo as páginas com prova embutida (enquadramento,
   legenda, corte limpo, ausência de aviso de manuseio interno, imagem
   posicionada logo após a menção e nunca isolada como fechamento de tópico),
   as páginas com jurisprudência transcrita (recuo de bloco, negrito nas
   partes grifadas, itálico em *ratio decidendi*, sem corte no meio de
   frase) e a página final de documentos. Apague os arquivos temporários de
   verificação (PDF, JPEGs) depois de conferir.
5. **Feche com uma tabela de correlação Doc. → ponto da peça**, ao final do
   `.docx` (como tabela nativa do Word) e do `.md` (como tabela markdown),
   indicando para cada documento qual preliminar/item do mérito ele sustenta,
   já na numeração X.Y (ou X.Y.Z) do esqueleto. Essa tabela é parte da entrega
   padrão sempre que a peça for entregue em arquivo com provas, não apenas
   quando pedida explicitamente.
6. Entregue os dois arquivos (`.docx` e `.md`) com `SendUserFile`.

## Estilo e tom

Para a prosa narrativa (fatos, transições, análise própria do caso), a regra
de ouro está em `references/estilo-autentico.md`; leia esse arquivo. Os pontos
centrais:

- **Sem travessão na prosa narrativa.** Não use o sinal longo nos parágrafos
  que você escreve do zero. Onde a tentação aparecer, encerre a frase com
  ponto, use parênteses para o aparte ou dois-pontos para a explicação.
  Vírgula resolve a pausa interna. Exceções: as legendas curtas das imagens
  embutidas no Passo 4, como rótulo; os blocos reaproveitáveis do Modelo de
  referência ampliado (citados verbatim, inclusive o título "X – O QUE É O
  PICPAY"); e a contestação transcrita em "Modelo de contestação completa:
  Seguro Carteira Digital (Kovr)".
- **Vicios de IA na prosa narrativa.** Corte palavras-muleta ("crucial",
  "cristalino", "inegável", "robusto") e conectivo repetido ("Ademais",
  "Outrossim", "Nesse sentido", "Vale ressaltar") nos trechos que você
  escreve. Essa regra também não se aplica aos blocos reaproveitáveis nem à
  peça transcrita do Seguro Carteira Digital, que mantêm a linguagem original
  do escritório mesmo quando repetem expressões como "compulsando os autos" ou
  "frisa-se".
- **Ritmo variado** na prosa narrativa. Não escreva todas as frases do mesmo
  tamanho. Alterne períodos longos de fundamentação com frases curtas e secas.
- **Ancorada no fato.** Cada afirmação jurídica grudada num dado dos autos
  (número, data, hora, valor, CNPJ, ID, protocolo de atendimento).
- **Linguagem formal em prosa corrida**, sem latinismo decorativo (use só os
  consagrados e funcionais). Sem bullets dentro da peça, salvo a enumeração
  usada no modelo (parágrafos curtos numerados na síntese da demanda, no
  bloco de abertura obrigatório do item 5.2 com a lista (i), (ii), (iii)... e
  imagem colada a cada item, ver 5.2 no "Modelo de referência ampliado", e nos
  requerimentos finais em algarismos romanos), que é parte do padrão. Não
  estenda essa forma numerada a mais nenhum outro ponto da peça.
- **Terceira pessoa:** "o PicPay", "a Parte Autora"/"o Autor", "este Réu",
  "a Requerente"/"o Requerente", conforme o gênero da parte no caso concreto.
- **Ajuste ao caso concreto.** Gênero, nomes e fatos vêm dos autos. Os dados
  dos modelos e blocos reaproveitáveis são referência de linguagem e
  fundamentação, nunca copie os números de processo ou valores do exemplo.
- **Calibre pelo rito.** No JEC, a preliminar de incompetência por
  chamamento de terceiro costuma caber; na Justiça Comum, prefira pedir a
  inclusão do terceiro no polo passivo. Considere prejudiciais
  (prescrição/decadência) e impugnação à gratuidade quando houver elementos
  documentais.
- **Imagens nunca fecham um tópico sozinhas** (ver regra de posicionamento
  no Passo 4, item 3): elas entram coladas na menção e sempre são seguidas
  de texto antes do próximo título.

## Checklist final antes de entregar

Confira que: **a numeração segue o padrão de `references/modelo.md`** (1, 2,
3.x, 4 apenas quando houver prejudicial, 5.1 a 5.4 com casas decimais extras
só quando o caso pedir granularidade, 6), sem pular nem duplicar número
dentro de um mesmo item, e sem ter revertido para algarismos romanos ou
outro esquema (a numeração da peça-fonte do Seguro Carteira Digital é
anterior ao padrão e deve ser remapeada pela tabela de correspondência);
se o item 4 foi omitido por não haver prejudicial, isso está
correto e não precisa ser "consertado"; a prosa narrativa (fora dos blocos
reaproveitáveis) não tem travessão nem hífen usado como pausa; não há
palavra-muleta ou conectivo de IA repetido fora dos blocos reaproveitáveis; o
ritmo das frases varia; todos os valores, datas, horários, CNPJs, IDs,
protocolos e contratos batem com os documentos; beneficiários e instituições
recebedoras estão nominados; cláusulas do Termo de Uso citadas existem e o
número confere com `references/termos-de-uso.md`; artigos de lei corretos;
nenhuma jurisprudência foi inventada (as citadas são as dos blocos
reaproveitáveis, as fornecidas pelo usuário, ou as localizadas nesta sessão
pela skill de jurisprudência do tribunal do caso, nunca por conhecimento
geral; as ementas da peça-fonte do Seguro Carteira Digital só entram depois de
conferidas na fonte do tribunal, conforme as conferências listadas naquela
seção); quando houver pedido de dano moral, o item 5.4.2 e o pedido
correspondente em "6. Dos pedidos" trazem OS DOIS encargos (correção
monetária pela Súmula 362/STJ e juros de mora pelo art. 405 do CC), não só
um deles; em peça do tema Seguro Carteira Digital, não há pedido de
acolhimento de preliminar sem que a preliminar tenha sido arguida no corpo;
a peça segue a ordem e a profundidade do "Modelo de referência
ampliado" (endereçamento com tempestividade embutida, síntese, preliminares
cabíveis ou omitidas com justificativa, prejudiciais quando houver, mérito
com as subseções aplicáveis ao caso, pedidos em cascata); **o item 5.2 abre
com o bloco fixo obrigatório (os quatro parágrafos de abertura, a lista
numerada (i), (ii), (iii)... com imagem colada a cada item, e o parágrafo de
fechamento citando a admissão da parte autora na inicial/BO quando ela
existir nos autos) antes de qualquer cronologia detalhada**, e essa forma
numerada não foi usada em nenhum outro ponto do mérito; e nenhum dado foi
inventado. Quando a entrega for em arquivo com provas (Passo 4), confira
também: a numeração dos documentos é contínua e sem lacunas do texto até a
lista final; cada imagem embutida renderiza corretamente, centralizada, com
legenda, sem nome de área interna ou de sistema visível e sem nenhum aviso ou
nota de manuseio interno (ex.: exigência de autorização judicial) visível no
recorte; **cada imagem está posicionada logo após o parágrafo que a
menciona, nunca todas empilhadas ao final da seção; nenhum tópico ou
subtópico termina em imagem, havendo sempre um parágrafo de texto depois da
última imagem inserida e antes do próximo título**; os três níveis de título
(`##`, `###`, `####`) renderizam com estilos de Word visivelmente distintos e
decrescentes; a tabela Doc. → ponto da peça cobre todos os documentos, já na
numeração X.Y/X.Y.Z do esqueleto; e, se havia registro de biometria facial
com prova de vida no material recebido, ele foi usado como exhibit próprio,
com a(s) foto(s) efetivamente embutida(s) (biometria facial e documento,
frente e verso, quando existirem) e discutido no texto, não só citado de
passagem, e não omitido por causa de aviso de manuseio interno no documento
fonte; **o inventário de segurança está completo**, ou seja, todos os
dispositivos vinculados à conta constam da peça (um item/parágrafo e uma
imagem por dispositivo, nunca agrupados) e todo o histórico de
recuperação/redefinição de senha disponível nos autos foi extraído e usado
(cada ocorrência, ou a ausência explícita, como fato próprio), e nenhuma
tela-fonte que reunia vários desses dados foi usada como um recorte único
para ilustrar mais de um parágrafo. Relate ao usuário, de forma explícita, o
resultado dessa conferência antes de encerrar.