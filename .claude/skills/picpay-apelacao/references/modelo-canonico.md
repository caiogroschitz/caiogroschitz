# Modelo canônico — esqueleto completo do Recurso de Apelação (Apelante)

Este é o **molde de saída**: mostra como a peça aparece, na ordem e com o visual do modelo do escritório (autos 0811684-11.2022.8.19.0066, TJRJ). O conteúdo entre `[ ]` é variável; os blocos longos vêm de `blocos-fixos.md`; o mérito vem de `teses-apelacao.md`.

> **Numeração:** o modelo original tem numeração inconsistente. Corrija: numere as seções das razões em sequência limpa (I, II, III, IV, V...). Seções marcadas *(condicional)* entram só quando o caso pedir.

---

## PARTE 1 — PETIÇÃO DE INTERPOSIÇÃO (endereçada ao juízo *a quo*)

Curta e protocolar. Não argumente aqui: toda a tese vai nas razões.

```
^ **EXCELENTÍSSIMO(A) SENHOR(A) DOUTOR(A) JUIZ(A) DE DIREITO DA [nª] VARA CÍVEL DA COMARCA DE [CIDADE] - [UF]**

**Autos: [número do processo]**

[Bloco fixo nº 1 - parágrafo de interposição, art. 1.009.]

[Bloco fixo nº 2 - preparo, art. 1.007.]

[Bloco fixo nº 3 - recebimento, contrarrazões em 15 dias e remessa ao Tribunal, art. 1.010, §1º.]

^ Termos em que pede deferimento.

^ São Paulo, [data por extenso].

^ **[NOME DO ADVOGADO]**

^ **OAB/[UF] nº [número]**

---
```

A linha `---` marca a quebra de página. Da página seguinte em diante, quem lê é o Tribunal.

---

## PARTE 2 — RAZÕES DE APELAÇÃO (endereçadas ao Tribunal *ad quem*)

```
^ **EGRÉGIO TRIBUNAL DE JUSTIÇA DO ESTADO [DE/DO] [ESTADO]**

# RAZÕES DE APELAÇÃO

[[QUADRO]]
APELANTE: [razão social do réu condenado]
APELADO: [nome do autor]
PROCESSO: [número dos autos]
ORIGEM: [nª Vara Cível da Comarca de [cidade] - [UF]]
[[/QUADRO]]

Ínclitos Desembargadores,

Colenda [nª] Câmara Cível do Eg. Tribunal de Justiça do Estado [de/do] [estado].
```

### I - DO JUÍZO DE ADMISSIBILIDADE PELO TRIBUNAL AD QUEM
Bloco fixo nº 4. Pede o recebimento nos efeitos devolutivo e suspensivo (arts. 1.010, §3º, 1.012 e 1.013) e antecipa, em uma frase, que a sentença não merece prosperar.

### II - DA TEMPESTIVIDADE
Bloco fixo nº 5. Indica a data da publicação da sentença — **ou da decisão dos embargos de declaração, quando houver, porque é dela que o prazo reabre** —, conta os 15 dias úteis (art. 1.003, §5º, com a contagem do art. 219) e conclui pela tempestividade.

### III - DA SÍNTESE DA DEMANDA
Narra em terceira pessoa, sem argumentar ainda:

1. Que ação é, ajuizada por quem contra quem.
2. A tese fática do autor, em dois ou três períodos.
3. Os pedidos da inicial, enumerados em `(i)`, `(ii)`, `(iii)`.
4. Que o Apelante contestou, mencionando o acervo documental juntado.
5. **O dispositivo da sentença transcrito literalmente**, em bloco de citação (`>`), item por item, com valores, prazos, multas, juros, correção e sucumbência.
6. *(condicional)* Os embargos de declaração opostos e o teor da rejeição, também transcrito.
7. A transição para o mérito: `Com máxima vênia ao entendimento do Nobre Magistrado, a r. sentença combatida merece reforma, haja vista que não houve o deslinde adequado do feito, conforme razões abaixo expostas.`

### IV - DAS RAZÕES DE APELAÇÃO — [título que descreve o erro atacado]
O coração da peça. Uma subseção por tese, cada uma com título próprio em caixa alta que **nomeia o erro do julgado**, não o tema genérico. Ver `teses-apelacao.md` para o catálogo e `estilo-de-escrita.md` para a arquitetura de seis movimentos.

Aqui entra a **narrativa probatória**: afirma o fato → espaço de prova → afirma o próximo fato → espaço de prova. Exemplo do tema de redução de limite (o do modelo):

```
O apelado possui cadastro legítimo junto ao PicPay desde [data], como se vê:

[[PROVA 1 | print da tela de cadastro do apelado, conta ativa desde [data]]]

O apelado realizou o envio da documentação para contratação do PicPay Card, como se vê:

[[PROVA 2 | print do envio de documentação para contratação do cartão]]

O cartão foi aprovado, com limite pré-aprovado no valor de [valor], como se vê:

[[PROVA 3 | print da aprovação do cartão com o limite de [valor]]]

Por sua vez, o apelado foi notificado sobre a desabilitação da função crédito via PUSH no dia [data] às [hora]:

[[PROVA 4 | print da notificação PUSH enviada em [data], às [hora]]]
```

Depois da narrativa, transcreva a cláusula contratual que autoriza a conduta (`>`), o dispositivo legal aplicável e a jurisprudência com a ponte de aplicação.

### V - DA AUSÊNCIA DE CABIMENTO DE INDENIZAÇÃO POR DANOS MORAIS
Bloco fixo nº 6, adaptado ao caso: retoma a legitimidade da conduta, invoca arts. 186 e 927 do CC e art. 14 do CDC, sustenta o mero aborrecimento, cobra o ônus do art. 373 do CPC, transcreve a jurisprudência do STJ sobre necessidade de prova do dano e, à luz da eventualidade, pede a minoração do *quantum* com o valor concreto arbitrado na sentença.

### VI - *(condicional)* DA AUSÊNCIA DE CABIMENTO DE INDENIZAÇÃO POR DANOS MATERIAIS
Quando houver condenação a restituição ou ressarcimento. Ver tese G em `teses-apelacao.md`.

### VII - *(condicional)* DA REVISÃO DA SUCUMBÊNCIA
Quando o percentual de honorários for desproporcional, incidir sobre base equivocada (art. 85, §2º) ou quando a reforma implicar inversão. Peça a redistribuição.

### VIII - *(condicional)* DO PREQUESTIONAMENTO
Uma passagem curta listando os dispositivos que se pretende ver expressamente enfrentados (art. 14, §3º, do CDC; art. 373, I, do CPC; arts. 186 e 927 do CC; art. 926 do CPC), para viabilizar eventual REsp/RE. Inclua quando o caso tiver porte para recurso aos tribunais superiores, conforme as `picpay-diretrizes-recursais`; omita nos casos de baixo valor.

### IX - CONCLUSÃO E REQUERIMENTOS
Bloco fixo nº 7. Pede **TOTAL PROVIMENTO**, discrimina o que se pretende reformar item por item, inclui o pedido subsidiário de minoração, a inversão da sucumbência e o requerimento de publicações exclusivas em nome do patrono.

```
^ Termos em que pede deferimento.

^ São Paulo, [data por extenso].

^ **[NOME DO ADVOGADO]**

^ **OAB/[UF] nº [número]**
```

---

## Fidelidade ao modelo

- O réu fala sempre em terceira pessoa: "o Apelante", "o PicPay". O autor é "o apelado" / "a parte apelada".
- A sentença é **citada textualmente** em bloco de citação, com trechos reais dos autos.
- A força está na narrativa probatória do tópico IV: afirmar, comprovar, afirmar, comprovar.
- Prosa corrida, sem bullets no corpo da peça. A única enumeração admitida é a romana `(i)`, `(ii)`, `(iii)` ao listar pedidos, elementos ou incisos.

## Checklist final antes de entregar

- [ ] Petição de interposição endereçada à **Vara Cível** (juízo *a quo*) e razões endereçadas ao **Tribunal** — as duas partes separadas por quebra de página.
- [ ] Apelante = pessoa jurídica efetivamente ré e condenada (confira se é PicPay, PicPay Bank, Banco Original ou outro).
- [ ] Fundamento da interposição: art. 1.009 do CPC. Preparo: art. 1.007. Contrarrazões: art. 1.010, §1º.
- [ ] Tempestividade com a data real de publicação e contagem de **15 dias úteis** — a partir da decisão dos ED, se houve.
- [ ] Síntese narra os pedidos da inicial e transcreve **cada item** do dispositivo.
- [ ] Toda data, valor, ID, CNPJ, beneficiário, cláusula e protocolo batem com os autos. Nada inventado.
- [ ] Cada tese ataca um **erro concreto** da sentença e termina pedindo a reforma daquele ponto.
- [ ] Cada ementa transcrita tem a frase-ponte de aplicação ao caso; nenhum acórdão inventado.
- [ ] Toda súmula de tribunal local ou enunciado de jornada foi conferido como em vigor (a Súmula 75 do TJRJ está cancelada desde 2018).
- [ ] Nenhum número calculado por dedução aparece como se fosse dado extraído dos autos.
- [ ] Um espaço de prova para cada print do dossiê, numerado em sequência e com etiqueta do que colar.
- [ ] Nenhum travessão (—) nem traço médio (–) no texto.
- [ ] Pedido final: provimento total + subsidiário de minoração + inversão da sucumbência + publicações exclusivas.
- [ ] Fecho com cidade, data, advogado e OAB/UF compatível.
- [ ] Nenhum dado do modelo-exemplo (Carlos Henrique, Volta Redonda, R$ 3.500,00, 06/10/2022) vazou para a peça real.
