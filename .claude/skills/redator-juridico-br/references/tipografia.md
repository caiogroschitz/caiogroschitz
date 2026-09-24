# Tipografia Jurídica — Negrito e Itálico sem Poluir a Peça

Formatação é comunicação. Bem usada, ela conduz o olhar do juiz aos pontos
nodais e aumenta a chance de êxito. Mal usada, polui, cansa e denuncia amadorismo
(empilhar negrito, itálico, caixa-alta e sublinhado é "crime tipográfico"). A
regra-mãe é a moderação estratégica: destaque pouco, para que o pouco destacado
realmente salte aos olhos. Se tudo está em negrito, nada está em negrito.

## Negrito (uso cirúrgico)

O negrito é o recurso mais forte e o que mais rápido se esgota. Reserve-o para:

- a palavra-chave da tese principal de cada capítulo (uma ou duas por capítulo,
  não a frase inteira);
- o ponto nodal dos fatos que o juiz precisa enxergar de imediato (uma data
  decisiva, um valor crítico, a conduta determinante);
- dentro de ementa transcrita, as expressões que sustentam a tese (com
  `(grifou-se)` logo após), dirigindo o olhar ao trecho que interessa;
- o núcleo de cada pedido, quando ajudar a leitura rápida do rol.

Não negrite frases inteiras, parágrafos, nem o capítulo todo. Negrito em bloco
longo perde função e vira ruído. Em regra, no máximo um a dois destaques por
parágrafo, e muitos parágrafos sem nenhum.

## Itálico (uso natural)

O itálico é sóbrio e quase invisível, ideal para o que não deve gritar, apenas
sinalizar. Use itálico para:

- termos em latim (*in casu*, *data venia*, *fumus boni iuris*, *periculum in
  mora*, *ratio decidendi*, *inaudita altera parte*, *a posteriori*);
- citações diretas curtas, de até três linhas, mantidas no corpo do texto entre
  aspas e em itálico (as transcrições longas vão para bloco recuado, sem itálico,
  com fonte menor);
- estrangeirismos eventualmente necessários;
- títulos de obras doutrinárias citadas, quando houver.

Itálico e negrito raramente convivem na mesma expressão. Escolha um.

## Sublinhado e caixa-alta

Evite sublinhado ao máximo. É poluente, herança da máquina de escrever e hoje
sinal de documento datado. Onde pensar em sublinhar, use negrito. A caixa-alta
serve ao endereçamento, ao nome da ação e aos títulos de capítulo; no corpo do
texto, palavra em caixa-alta para "gritar" é deselegante e cansativa, troque por
negrito pontual.

## Não empilhar destaques

Nunca combine negrito + itálico + caixa-alta + sublinhado no mesmo trecho. Um
único nível de destaque por vez. O acúmulo anula o efeito e suja a página.

## Respiro e legibilidade (o que o script já entrega)

Fonte serifada (Times New Roman) ou Arial, corpo 12; espaçamento entre linhas
1,5; espaço a mais entre parágrafos para criar respiros visuais; texto
justificado; recuo de primeira linha. Ementas longas em bloco recuado, fonte
menor e espaçamento simples. O `scripts/gerar_docx.py` já aplica esse padrão; a
formatação de destaque vem do seu uso de `**negrito**` e `*itálico*` no Markdown.

## Como marcar no Markdown desta skill

- `**palavra**` vira negrito no .docx. Use com parcimônia, conforme acima.
- `*termo*` vira itálico. Aplique em todos os latinismos e nas citações curtas
  no corpo.
- Dentro de bloco de ementa (`>`), use `**negrito**` apenas nas expressões-chave
  e feche o bloco com `(grifou-se)`.
- Não use sublinhado (o script não o aplica de propósito).

## Microteste tipográfico (silencioso, antes de fechar)

A página tem áreas de respiro, sem manchas pretas de negrito; cada capítulo tem
no máximo um ou dois negritos; os latinismos estão em itálico; não há sublinhado;
nenhum trecho acumula dois tipos de destaque; as ementas longas estão recuadas e
menores, com o grifo sinalizado. Se algo falhar, reduza destaque antes de
entregar. Na dúvida, destaque menos.


## Nomes próprios e partes (convenção forense)

Nomes próprios das partes recebem destaque, mas com disciplina. Na qualificação e
na primeira menção, o nome de cada parte vai em negrito e caixa-alta (autor, réu,
exequente, executado): é o que permite localizar as partes num relance. Depois da
primeira menção, refira-se pela posição processual (Excipiente, Autora, Ré,
Reclamado) em texto normal, sem repetir o negrito a cada linha, sob pena de poluir.

Também recebem destaque, uma única vez:

- o nome da ação ou da peça (ex.: EXCEÇÃO DE PRÉ-EXECUTIVIDADE), em negrito e
  caixa-alta, no anúncio da peça;
- o juízo, no endereçamento, em caixa-alta;
- os nomes dos advogados subscritores no fecho, em negrito e caixa-alta, com a
  OAB logo abaixo.

Não negrite o nome da parte toda vez que ele aparecer no corpo. O destaque vale na
apresentação; no desenvolvimento, a posição processual basta. O `gerar_docx.py`
já coloca em negrito qualquer linha inteiramente em caixa-alta (endereçamento,
nome da peça, fecho); para destacar um nome próprio dentro de um parágrafo
corrido (a qualificação), marque-o com `**...**` no Markdown.


## Cabeçalho da peça (convenções que o script aplica)

O `gerar_docx.py` reconhece e formata o cabeçalho automaticamente, desde que a
marcação esteja certa no Markdown:

- Endereçamento: escreva a linha inteira em CAIXA-ALTA (ex.: EXCELENTÍSSIMO ...).
  O script alinha à esquerda, em negrito, sem recuo.
- Número do processo: marque a linha inteira em negrito, `**Processo nº ...**`.
  Sai à esquerda, em negrito, sem recuo.
- Nome da peça: use `# NOME DA PEÇA POR EXTENSO`. Sai centralizado, em negrito e
  caixa-alta. Não use o nome da peça como linha solta de prosa.
- Fecho: nomes dos advogados em linhas de CAIXA-ALTA (saem em negrito), com a
  OAB logo abaixo em linha normal.

Não passe `--titulo` ao gerar peça real: ele cria um título solto acima do
endereçamento, o que está errado. O nome da peça deve vir no corpo, com `#`, no
lugar correto (após a qualificação).
