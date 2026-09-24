# Citação de Lei e Jurisprudência — Padrão Forense + ABNT

Citar bem é metade da força da peça. Citação imprecisa, inventada ou apenas
colada (sem trabalho) enfraquece a tese e, no limite, configura má-fé. Este guia
é de aplicação OBRIGATÓRIA sempre que a peça invocar jurisprudência.

## REGRA DE OURO: precedente não se cola, se trabalha

O erro mais comum e mais fatal é colar uma ementa e seguir adiante, como se o
julgado falasse por si. Não fala. O art. 489, § 1º, V e VI, do CPC considera NÃO
FUNDAMENTADA a decisão que apenas invoca precedente sem identificar seus
fundamentos determinantes nem demonstrar que o caso se ajusta a eles. O que vale
para o juiz vale, por simetria, para o advogado que quer convencê-lo. Toda
jurisprudência citada deve vir cercada de três movimentos:

1. **Antes:** uma frase que anuncia a tese que o precedente vai sustentar.
2. **A citação:** a ementa ou o trecho do voto, identificado e destacado.
3. **Depois (o mais importante):** a explicitação da *ratio decidendi* (o
   fundamento determinante do julgado) e a demonstração de que o caso concreto se
   ajusta a esse fundamento. É aqui que o precedente vira argumento.

Sem o terceiro movimento, a citação é decorativa e o juiz a ignora.

## Como transcrever uma ementa (forma correta)

- **Prefira ementas curtas e objetivas.** Um julgado certeiro vale mais que dez
  empilhados. Não faça "colcha de retalhos" de ementas.
- **Aspas obrigatórias** na transcrição direta. É reprodução literal, marque como
  tal.
- **Recuo à esquerda, fonte menor e espaçamento simples** para trechos com mais
  de três linhas (o script `gerar_docx.py` formata assim os blocos iniciados por
  `>`).
- **Sinalize cortes** com reticências entre parênteses ou colchetes: `(...)` ou
  `[...]`. Cortar é legítimo; esconder o corte, não.
- **Dirija o olhar do juiz:** destaque em negrito as palavras-chave que sustentam
  a tese e informe o destaque com `(grifou-se)` ou `(grifo nosso)`. Se o destaque
  já vinha no original, escreva `(grifos no original)`. Em `gerar_docx.py`, use
  `**negrito**` dentro do bloco `>` para grifar.
- **Identificação completa e verdadeira logo abaixo da transcrição:** tribunal,
  classe e número do processo, relator, órgão julgador, data de julgamento e data
  de publicação (DJe). Sem isso, a citação não tem força e parece inventada.

Modelo (bloco recuado seguido da linha de identificação):

> "RESPONSABILIDADE CIVIL. INSTITUIÇÃO FINANCEIRA. FRAUDE DE TERCEIRO. FORTUITO
> INTERNO. **RESPONSABILIDADE OBJETIVA.** (...) O risco do empreendimento
> bancário atrai a responsabilização independentemente de culpa. (grifou-se)"
>
> (STJ, REsp nº [número verificado], Rel. Min. [nome], [Órgão], j. [dd/mm/aaaa],
> DJe [dd/mm/aaaa])

Depois do bloco, EXPLIQUE: "A ratio do julgado é a de que [fundamento
determinante]. Transposta ao caso, [demonstração do ajuste fático]." Só então a
citação cumpriu sua função.

## Hierarquia: precedente x jurisprudência (use a palavra certa)

O CPC, nos arts. 926 e 927, estrutura um sistema de precedentes de observância
qualificada. Saiba o que está invocando, porque o peso retórico muda:

- **Precedentes vinculantes / de observância obrigatória (art. 927):** súmulas
  vinculantes do STF; teses de repercussão geral (STF) e de recursos repetitivos
  (STJ); acórdãos em IAC e IRDR; enunciados de súmula do STF em matéria
  constitucional e do STJ em infraconstitucional. Ao invocá-los, frise o dever de
  observância e o risco de improcedência liminar (art. 332) ou de reforma se o
  juízo destoar. Tese fixada deve ser transcrita literalmente, com o número do
  Tema.
- **Jurisprudência persuasiva:** acórdãos de TJs e TRTs (e julgados isolados de
  tribunais superiores). Convencem pela qualidade do argumento, não por
  vinculação. Prefira o tribunal do foro (mesmo TJ/TRT) e julgados recentes.

Use os termos com precisão: "tese fixada em recurso repetitivo" e "súmula
vinculante" não são sinônimos de "a jurisprudência tem entendido". O rigor
terminológico sinaliza domínio.

## Distinguishing e overruling (precedente contrário não se ignora)

Havendo precedente qualificado contrário à tese, enfrente-o, nunca o omita
(omitir é dar munição ao adversário e ao juízo). Duas técnicas:

- **Distinguishing (distinção):** demonstre que o caso concreto tem
  particularidade fática ou jurídica que o afasta da hipótese do precedente, de
  modo que a tese não incide. Aponte o elemento distintivo com precisão.
- **Overruling/superação:** sustente que o precedente está superado por mudança
  legislativa, social ou de orientação do próprio tribunal, indicando o vetor de
  superação. Use com parcimônia e só com lastro real.

O art. 489, § 1º, VI, do CPC obriga o juiz a enfrentar a distinção ou a superação
que a parte suscitar. Suscitá-la bem, portanto, vincula a fundamentação da
decisão.

## Transparência e honestidade da citação

Informe a data e os dados de identificação. Não corte a ementa para esconder
ressalva que a enfraquece. Se há divergência, diga, e posicione-se pela corrente
prevalente. **Nunca invente número de súmula, Tema, REsp, RE ou acórdão.** Se a
busca não devolveu o identificador exato, descreva o instituto pelo conceito
("o entendimento consolidado da Corte Especial do STJ sobre a mitigação do art.
833, IV") ou deixe marcador explícito `[completar nº/Rel./data]` para o advogado
preencher do banco de jurisprudência. Citação verdadeira incompleta é melhor que
citação completa falsa.

## Como pesquisar antes de citar

Use a ferramenta de busca (`nimble:search` / `WebSearch`) e CONFIRA no resultado:
súmulas aplicáveis (STF, STJ, TST), teses de repetitivo/repercussão geral/IAC/
IRDR (número do Tema e tese literal), e acórdãos recentes do tribunal do foro
(número, relator, órgão, data). Boas queries: `súmula STJ [tese] enunciado`;
`tema repetitivo STJ [assunto] tese fixada 2024 2025`; `[TJ/TRT do foro]
[assunto] ementa recente`. Confira números e datas antes de citar.

## Citação de artigo de lei no corpo

Do mais específico para o geral: artigo (art.), parágrafo (§ ou parágrafo único),
inciso (romano: I, II, III), alínea (minúscula: a, b, c). Ex.: "art. 5º, X, da
Constituição Federal"; "arts. 932, III, e 933 do Código Civil". Na primeira
menção, diploma por extenso com o número da lei: "Código de Defesa do Consumidor
(Lei nº 8.078/1990)"; depois, sigla.

## Referência ABNT completa (NBR 6023, item 7.11.3; corpo pela NBR 10520)

Quando a peça ou o escritório exigir referência formal: JURISDIÇÃO. Órgão. Tipo
de documento nº [número]. Relator: Nome. Local, data de julgamento. Fonte. Se
eletrônico, "Disponível em: [URL]. Acesso em: [data]." Na peça forense, a forma
de identificação abaixo da ementa (acima) costuma bastar; a referência ABNT
completa é mais comum em pareceres e memoriais.

## Doutrina

Cite nominalmente quando agregar (Tepedino, Schreiber, Cavalieri, Marinoni,
Didier, Nery, Tartuce, Godinho Delgado, Paulsen, Hugo de Brito Machado). Sem
certeza da obra ou da página, atribua a tese ao autor pelo entendimento
consolidado, sem inventar citação literal nem número de página.
