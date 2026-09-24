---
name: pje-calc-liquidacao-trabalhista
description: >-
  Lê a íntegra dos autos de um processo trabalhista (especialmente do TRT2) e
  produz um ROTEIRO DE PREENCHIMENTO do PJe-Calc, tela por tela, com cada valor,
  período e índice localizado no processo e a fonte (ID/página) citada, para o
  advogado da parte autora lançar a liquidação sem errar. Use SEMPRE que o usuário
  enviar PDF(s) de processo trabalhista e pedir para "fazer/calcular a liquidação",
  "preencher o PJe-Calc", "montar os cálculos de liquidação de sentença", "extrair
  os parâmetros do cálculo", "me ajuda a lançar no PJe-Calc", "quais valores uso no
  PJe-Calc", "roteiro do PJe-Calc", "liquidar a sentença trabalhista" ou "analisa
  os autos e prepara o cálculo". Também aciona quando o usuário cola o teor da
  sentença/acórdão trabalhista pedindo os dados para liquidar. NÃO é a calculadora
  final: organiza e fundamenta os parâmetros para lançamento no PJe-Calc (engine
  oficial), com máxima precisão. NÃO use para cálculo cível/DrCalc nem para redigir
  contestação, recurso ou réplica.
---

# Roteiro de preenchimento do PJe-Calc (liquidação trabalhista — parte autora)

## O que esta skill faz e por que existe

Em liquidação trabalhista, errar custa caro: uma verba esquecida, um marco de
correção trocado ou um período mal lançado refaz toda a planilha e pode ser
impugnado. O PJe-Calc é a engine oficial da Justiça do Trabalho e produz o
arquivo `.pjc` exigido para juntada (no TRT2 a planilha em PDF sozinha não basta).
O gargalo humano não é a aritmética — é **ler corretamente os autos e transcrever
cada parâmetro para o campo certo do PJe-Calc**. É exatamente esse gargalo que
esta skill elimina.

A skill **não inventa números nem índices** e **não substitui o PJe-Calc**. Ela:

1. Lê a íntegra do processo (sentença, acórdão, contrato, CTPS, holerites, TRCT,
   ficha financeira, petições).
2. Extrai cada parâmetro da liquidação **com a fonte citada** (ID/página do
   documento de onde saiu).
3. Sinaliza ambiguidades, conflitos e lacunas em vez de "chutar".
4. Entrega um **roteiro de preenchimento em `.docx`**, organizado na mesma ordem
   das telas/módulos do PJe-Calc, para o usuário transcrever com segurança.

O princípio que governa tudo: **a fonte da verdade é o título executivo (o
dispositivo da sentença/acórdão transitado em julgado, lido em conjunto com a
fundamentação), os documentos dos autos e as tabelas oficiais do próprio
PJe-Calc.** Quando a skill não tem base documental para um campo, ela diz isso
abertamente — nunca preenche por suposição.

## Fluxo de trabalho

### Passo 1 — Inventariar os autos
Leia todos os PDFs fornecidos. Antes de extrair, monte um índice rápido do que
existe e do que falta. Os documentos típicos e o que cada um fornece estão em
`references/extracao-autos.md` — **leia esse arquivo agora**, pois ele define a
ordem de leitura, a hierarquia de fontes (o que prevalece em caso de conflito) e
como tratar documentos ilegíveis ou ausentes.

Se faltar algo essencial para liquidar (ex.: não há a sentença, ou não há
evolução salarial e o cálculo depende dela), **pare e avise o usuário** listando
o que falta, antes de gerar o roteiro.

### Passo 2 — Identificar o comando da sentença (o coração da precisão)
A liquidação reproduz **exatamente** o que o título mandou pagar — nada além,
nada aquém. Extraia, do dispositivo somado à fundamentação e ao trânsito em
julgado:

- Cada **verba deferida** e sua redação literal (ex.: "horas extras além da 8ª
  diária e 44ª semanal, com adicional de 50%, e reflexos em DSR, férias + 1/3,
  13º, FGTS + 40% e aviso prévio").
- Os **reflexos/repercussões** determinados para cada verba.
- **Parâmetros fixados** pela sentença: divisor, adicional, base de cálculo,
  jornada reconhecida, limitação temporal, evolução salarial a considerar.
- O que foi **expressamente indeferido** ou excluído (para não lançar).
- **Honorários** (sucumbenciais/assistenciais — percentual e base), **justiça
  gratuita**, **dedução de valores já pagos**.
- Definição de **correção monetária e juros** se a sentença/acórdão fixou regime
  específico; caso contrário, aplicar o regime vigente conforme
  `references/correcao-juros.md`.

Transcreva o comando verba a verba **citando o ID/página**. Onde a sentença for
ambígua ou comportar interpretações, registre a ambiguidade explicitamente em vez
de escolher silenciosamente.

### Passo 3 — Mapear cada parâmetro para os campos do PJe-Calc
Use `references/pje-calc-campos.md` — **leia esse arquivo** — para saber, módulo a
módulo (Dados do Processo, Parâmetros do Cálculo, Histórico Salarial, Faltas e
Férias, Parcelas Principais e Reflexas, Correção/Juros/Multa, Incidências
FGTS/INSS/IRPF), qual campo recebe qual dado e de onde no processo esse dado vem.
Para o regime de atualização (índices, marcos, ADC 58, Lei 14.905/2024), use
`references/correcao-juros.md`.

Para **cada verba**, defina e registre: período de incidência (início/fim), base
de cálculo, adicional/divisor, reflexos marcados, **natureza** (salarial ou
indenizatória) e **incidências** (FGTS, INSS/Contribuição Social, IRPF, Previdência
Privada, Pensão). Erro de natureza/incidência é uma das maiores fontes de
impugnação — trate com cuidado e fundamente cada escolha na verba e na lei.

### Passo 4 — Gerar o roteiro `.docx`
Monte o conteúdo do roteiro como um JSON estruturado e renderize com o script
incluído:

```bash
python3 scripts/build_roteiro_docx.py <caminho-do-json> <caminho-de-saida.docx>
```

O esquema do JSON e um exemplo mínimo estão documentados no topo do próprio
script (`scripts/build_roteiro_docx.py`). O roteiro segue a ordem das telas do
PJe-Calc, e cada lançamento traz: **o valor a digitar, o campo exato do PJe-Calc,
e a fonte (ID/página)**. Toda incerteza vira um item destacado de "⚠ Conferir".

Salve o `.docx` na pasta de saída e entregue ao usuário com `present_files`.

### Passo 5 — Resumo honesto ao usuário
Ao final, em poucas linhas: o que foi extraído com segurança, o que ficou como
"⚠ Conferir" (e por quê), e o lembrete de que os índices/tabelas do PJe-Calc
devem estar atualizados (atualização on-line no próprio sistema) e que o cálculo
final deve ser conferido pelo usuário antes da juntada.

## Regras de ouro (precisão)

- **Nunca invente valor, data, índice ou alíquota.** Sem base documental, marque
  "⚠ Conferir" e diga o que precisa ser confirmado.
- **Cite a fonte de cada dado** (ID/página). Um parâmetro sem fonte é suspeito por
  definição.
- **Reproduza o título, não o reinterprete.** A liquidação não amplia nem reduz a
  coisa julgada. Excesso de execução e liquidação a menor são, ambos, erros.
- **Conflito entre documentos** (ex.: salário do holerite ≠ da CTPS) → não escolha
  sozinho: aplique a hierarquia de `references/extracao-autos.md` e sinalize.
- **Índices de correção mudam por lei e por decisão** (ADC 58/STF, Lei
  14.905/2024). Não fie-se em memória: siga o que o título fixou e o que as
  tabelas oficiais do PJe-Calc trazem. Veja `references/correcao-juros.md`.
- **A engine é o PJe-Calc.** Esta skill prepara o preenchimento; ela não é a
  autoridade aritmética final.

## Arquivos da skill

- `references/extracao-autos.md` — ordem de leitura dos autos, o que extrair de
  cada documento, hierarquia de fontes e tratamento de conflitos/lacunas.
- `references/pje-calc-campos.md` — mapa módulo-a-módulo dos campos do PJe-Calc e
  a origem de cada dado nos autos.
- `references/correcao-juros.md` — regime de correção monetária e juros (deferindo
  ao título e às tabelas oficiais), com a árvore de decisão pós-ADC 58 e Lei
  14.905/2024.
- `scripts/build_roteiro_docx.py` — gerador do roteiro `.docx` a partir do JSON
  estruturado (esquema documentado no cabeçalho do script).
- `assets/exemplo_roteiro.json` — exemplo de JSON de entrada do gerador.
                                                                                                          