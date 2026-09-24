---
name: "picpay-requisicao-cumprimento-of"
description: "Redige a requisição sistêmica de cumprimento de OF/liminar/sentença ao PicPay (Projuris) a partir do PDF dos autos, em formato enxuto, e calcula o prazo fatal."
---

# Requisição de cumprimento de OF / liminar / sentença (PicPay, BFAP)

Use quando o Caio anexar o PDF dos autos e pedir "requisição de cumprimento", "solicitar cumprimento da OBF", "mensagem sistêmica ao cliente" ou algo parecido. A entrega é um texto para colar no módulo de Requisições do Projuris. As regras gerais de requisição estão na skill `picpay-requisicoes-projuris`.

## 1. Leitura dos autos (rápida)

PDFs do PJe/eProc costumam ter mais de 100 páginas. Não leia página por página:

1. Extraia o texto: `pdftotext -layout arquivo.pdf saida.txt`.
2. Leia a capa (número, órgão, partes, lista de documentos com datas e IDs).
3. Localize a decisão ou sentença com grep: `DEFIRO|JULGO|condenar|abstenha|multa|dias úteis|Súmula 410`.
4. Leia o dispositivo e as linhas de expedição/intimação (eProc: blocos "Evento", "Prazo", "Data Inicial/Final", "Status").
5. Se o pedido se refere à "última manifestação" da parte, leia os últimos eventos até o fim do arquivo.
6. Pegue: nome e CPF/CNPJ do autor, número do contrato/conta, valores, prazo e multa (valor, periodicidade, teto).

## 2. Formato da requisição (ENXUTO)

O Caio quer só a solicitação de cumprimento, sem parecer nem análise na mensagem. Estrutura fixa:

**Tipo de Requisição:** Cumprimento de Liminar - PicPay (liminar/tutela) ou Cumprimento de Obrigação de Fazer - PicPay (sentença/OF)
**Título:** PRAZO DD/MM/AAAA - CUMPRIMENTO DE OF - NOME DA PARTE - Nº DO PROCESSO
**Exigíveis:** decisão ou sentença (com ID/evento) e petição inicial; se o pedido nasce de manifestação da parte, incluir essa petição.

**Detalhes:**
> Processo nº, juízo/comarca. Autor(a): nome, CPF/CNPJ (conta/contrato nº, se houver).
>
> Uma ou duas frases com o que a decisão determinou, prazo e multa.
>
> (Se for reiteração: uma frase descrevendo o problema relatado pela parte, ex.: "informa CPF e senha no app PicPay Empresas e recebe 'Não é possível acessar a conta'".)
>
> Solicitamos:
>
> 1. Ação concreta 1.
> 2. Ação concreta 2.
>
> Solicitamos o envio dos prints que comprovem o cumprimento.

No máximo 2 ou 3 itens de ação, cada um executável pela equipe de dossiês. Nada de contexto processual extra, teses ou divergências dentro da requisição.

## 3. Regras de conteúdo

- Decisão não definitiva (liminar ou sentença sem trânsito) que declara inexigibilidade: pedir apenas SUSPENSÃO da cobrança e do contrato, nunca "declarar inexigível" ou "baixar". Baixa definitiva só com esgotamento das vias recursais e "de acordo" do Jurídico Interno. Se a sentença mandar baixar já na tutela, redigir como suspensão e avisar o Caio fora da requisição.
- Negativação: "não incluir o nome nos órgãos de proteção ao crédito; se já houver inscrição, retirá-la".
- Reativação de conta ou limite: pedir a correção objetiva e prints de conta ativa + histórico de login bem-sucedido depois da correção.
- Prazo de cumprimento na requisição: 2 a 5 dias úteis. Com 2 dias, incluir **Justificativa:** (multa já fixada, prazo processual correndo).

## 4. Prazo fatal

- Obrigação de fazer/não fazer exige intimação pessoal do devedor (Súmula 410 do STJ). A contagem parte da intimação pessoal (AR/eCarta entregue, domicílio eletrônico), não da publicação ao advogado.
- Se os autos não mostram a intimação pessoal da PicPay, diga isso e calcule de forma conservadora a partir da juntada da sentença/decisão. Mostre também como o fatal muda se a intimação vier depois.
- JEC: prazos em dias úteis. Calcule com script, excluindo fins de semana e feriados nacionais (ex.: 12/10, 02/11, 15/11, 20/11, 25/12). Avise que suspensões locais do tribunal estendem o prazo.
- O prazo interno do título fica bem antes do fatal (folga para o cliente).
- Recurso inominado: 10 dias úteis da ciência. Aponte quando isso pesar na decisão entre suspender e baixar.

## 5. Fora da requisição (resposta ao Caio)

Depois do texto da requisição, no máximo 2 ou 3 pontos curtos:
- divergências (ex.: polo cadastrado como "PicPay Serviços S.A." x inicial com PicPay Instituição de Pagamento, CNPJ 22.896.431/0001-10), sempre explícitas;
- prazo processual vencendo (ex.: manifestação que fecha hoje; sugerir petição de dilação);
- incidência de multa já em curso.
Separe sempre o dado dos autos da inferência.

## 6. Peças correlatas no mesmo fluxo

Pedido de dilação de prazo (quando a verificação técnica não fica pronta a tempo): petição curta no chat, com endereçamento, qualificação ("já qualificada nos autos"), síntese do último relato da parte, providências anteriores já comprovadas (eventos), art. 139, VI, do CPC transcrito em itálico com recuo, pedido de prazo adicional (em regra 5 dias) sem multa no período, pedido de publicações em nome do advogado constituído e fecho com data e OAB. Não nomear áreas internas do cliente (usar "análise técnica específica") e não expor fragilidades do processo interno.

## 7. Estilo

- Português jurídico, sem travessões (—), sem fórmulas batidas, sem intensificadores.
- Entregar direto no chat (texto curto, pronto para colar).
- Ao final, sugerir o título da conversa: "PicPay x [Parte] — [Cumprimento de Liminar/OF/Sentença] [nº CNJ curto] ([Tribunal])".