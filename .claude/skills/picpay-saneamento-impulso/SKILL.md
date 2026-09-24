---
name: picpay-saneamento-impulso
description: "Gera minutas de petição de impulso/prosseguimento (e correlatas) a partir de uma planilha de saneamento de processos parados (Astrea x Projuris), filtrada por responsável, buscando os dados que faltam (parte autora, litisconsortes, vara oficial) direto no Astrea e nos documentos já existentes na pasta do processo no Drive."
---

# Saneamento de processos parados (Astrea x Projuris) — minutas de impulso

Esta skill cobre o fluxo de força-tarefa de saneamento: o usuário sobe uma
planilha "Saneamento_Processos_Parados_Astrea_x_Projuris.xlsx" (ou equivalente)
e pede para gerar as petições de impulso dos processos sob a responsabilidade
dele. A saída é um lote de minutas em .docx (uma por processo) mais uma
planilha de controle. **Não é a skill para peças robustas** (contestação,
recurso, cumprimento de liminar) — só para as manifestações curtas de
impulsionamento/prosseguimento do feito parado. Para peças de resposta a um
despacho específico com a íntegra dos autos colada no chat, use
`picpay-peticao-simples`.

A planilha de saneamento é só o ponto de partida: ela é uma FOTO tirada na
"Data-base do cálculo" (célula C2) e não traz nome da parte autora, eventuais
corréus nem o nome oficial completo da vara — dados indispensáveis para a
qualificação no modelo real do escritório (Passo 4). O usuário mostrou, em uma
gravação de tela, que o fluxo manual dele busca isso direto no Astrea e na
pasta do processo no Google Drive — reproduza esse fluxo com automação de
navegador em vez de pedir tudo por placeholder.

## Passo 0 — Verificar acesso

Antes de começar, confirme que há um navegador disponível na sessão (Claude in
Chrome ou o navegador embutido) e que ele está autenticado em:

- `astrea.net.br` (sistema de gestão processual do escritório)
- Google Drive/Docs da conta do escritório (pasta compartilhada "PROCESSOS",
  organizada em subpastas por número de processo)

Se nenhum navegador estiver disponível, ou as sessões não estiverem logadas,
avise o usuário e caia para o modo com placeholders (Passo 4a) em vez de travar
o lote inteiro.

## Passo 1 — Ler a planilha

A aba relevante costuma se chamar "Saneamento", com cabeçalho na linha 3
(linhas 1-2 são título/legenda). Colunas-chave observadas:

- `Nº do Processo`, `Cliente`, `Responsável (Astrea)`, `Vara`, `Foro`, `Inst.`
- `Dias parado`, `Data últ. histórico`, `Último histórico (Astrea)`
- `Providência sugerida`, `Detalhamento / pedido a ser formulado`
- `Status (Projuris)`, `Motivo encerramento (Projuris)` — usados para detectar
  divergência de bases (ver Passo 3)

Extraia com openpyxl (`data_only=True`) e filtre por
`Responsável (Astrea)` = nome informado pelo usuário. Se o nome não bater
exatamente com nenhum valor da coluna, liste os responsáveis disponíveis e
pergunte, em vez de adivinhar por aproximação.

## Passo 2 — Categorias de Providência sugerida e base legal

Cada linha tem uma `Providência sugerida`. Mapeamento de categoria -> tipo de
petição -> fundamento (validado contra modelo real do escritório):

| Providência sugerida | Gera petição? | Fundamento legal |
|---|---|---|
| Impulso oficial – requerer prosseguimento | Sim | Art. 5º, LXXVIII, da CF (razoável duração do processo) + art. 4º do CPC (celeridade) |
| Análise + impulso oficial | Sim (mesmo modelo do impulso oficial) | idem |
| Conclusão para sentença | Sim | Arts. 226 e 227 do CPC (reiteração de pedido de prolação de sentença) — **não confundir com o fundamento do impulso oficial genérico** |
| Recursal – impulso do julgamento | Sim | Pedido de informação sobre distribuição/inclusão em pauta; subsidiariamente, se já julgado, baixa dos autos e certidão de trânsito em julgado |
| Habilitação/cadastro nos autos | Sim | Petição de juntada de procuração/substabelecimento + pedido de cadastro dos patronos |
| Cumprimento – comprovar pagamento | Minuta parcial | Art. 924, II, do CPC (extinção pelo adimplemento) — **só finalize e libere para protocolo depois que o usuário anexar o comprovante de pagamento**; nunca afirme quitação sem o documento. Verifique também se já existe uma minuta de "petição de juntada" pronta na pasta do processo no Drive (ver Passo 4) — é comum já haver uma iniciada |
| Baixa – encerrar no Astrea | Verificar no Astrea antes de decidir | A planilha pode estar desatualizada: no caso observado, a planilha dizia "Arquivado/Baixa", mas o Astrea ao vivo mostrava status "Ativo 1º Grau" com uma tarefa aberta ("Analisar possibilidade de encerramento") e a tag "Aguarda comprovante de pgto". Não assuma que é só ação interna sem confirmar no Astrea |
| Sem histórico – conferir cadastro | Não (a princípio) | Ação interna (conferir andamento real e se habilitar) — mas, como acima, confirme no Astrea antes de descartar a petição |

Use o texto da coluna `Detalhamento / pedido a ser formulado` como apoio, mas
ele é um resumo interno gerado pelo próprio escritório, não os autos — trate
como indício da providência, não como fonte primária do que está no processo.
A fonte primária é o Astrea ao vivo (Passo 3).

## Passo 3 — Verificar cada processo no Astrea antes de finalizar

Para cada processo do lote, com o navegador:

1. Acesse `astrea.net.br`, cole o número do processo na busca e abra o caso.
2. O título do caso vem no formato `[Cliente] X [Nome da parte autora]` —
   é a fonte mais confiável para o **nome da parte autora**, que a planilha
   não traz.
3. Confira `Status` (ex.: "Ativo 1º Grau"), as tags (ex.: "Aguarda
   comprovante de pgto", "Resultado: Sentença Procedente em Parte") e as
   tarefas abertas na aba Atividades. Se isso contradisser a
   `Providência sugerida` da planilha (como no caso do Passo 2 acima),
   **use o que está no Astrea ao vivo**, e registre a divergência na
   planilha de controle em vez de ignorar.
4. Nunca assuma nome de correu (ex.: Banco Original) que não apareça no
   próprio Astrea/Projuris para aquele processo específico.

Se o navegador não conseguir acessar o Astrea (não logado, bloqueado, fora do
ar), avise o usuário para aquele processo específico e use o modo placeholder
(Passo 4a) só para ele, sem travar o restante do lote.

## Passo 4 — Reaproveitar petição já existente na pasta do processo (Drive)

O escritório mantém uma pasta compartilhada "PROCESSOS" no Google Drive, com
uma subpasta por número de processo. Antes de montar o endereçamento e a
qualificação do zero:

1. Procure no Drive uma pasta com o número do processo.
2. Se houver uma petição anterior (Google Doc ou PDF) naquela pasta, abra-a:
   ela já traz o endereçamento oficial validado da vara, a qualificação
   completa (parte ré + corréus + parte autora) e o advogado/OAB usados da
   última vez. **Reaproveite esses dados exatamente como estão** em vez de
   tentar recriá-los — são a referência mais confiável disponível.
3. Adapte só o corpo da nova petição (a providência atual) e a data,
   mantendo endereçamento, qualificação e rodapé de OAB da peça anterior.
4. Se não houver nenhuma petição anterior na pasta, use o nome da parte
   autora obtido no Astrea (Passo 3) e monte o endereçamento com o nome da
   vara que a planilha traz, avisando o usuário que esse endereçamento não
   foi validado contra uma peça anterior.

### Passo 4a — Modo placeholder (só quando Astrea/Drive não estiverem disponíveis)

Se não houver navegador, ou o navegador não conseguir acessar Astrea/Drive
para um processo, gere a minuta com marcadores explícitos em vez de inventar:

- Nome da parte autora -> `[NOME DA PARTE AUTORA]`
- Eventuais corréus além do PicPay/Banco Original -> `[DEMAIS RÉUS, SE
  HOUVER]`
- Nome/OAB do advogado subscritor -> `[NOME DO ADVOGADO] — OAB/[UF] nº
  [XXXXX]`

Nunca adivinhe esses três dados. Deixe explícito, na planilha de controle,
quais processos caíram no modo placeholder e por quê (sem acesso ao
Astrea/Drive naquele momento), para o usuário saber quais minutas ainda
precisam de complementação manual.

## Passo 5 — Modelo real de petição (estrutura)

Estrutura confirmada a partir de protocolos reais do escritório
(ex.: 5017157-26.2024.8.08.0012, TJES):

```
EXCELENTÍSSIMO SENHOR DOUTOR JUÍZ DE DIREITO DA [NOME OFICIAL COMPLETO DA
VARA] DA COMARCA DE [COMARCA] – [UF]


Autos nº: [número CNJ]

[PICPAY INSTITUIÇÃO DE PAGAMENTO S.A / PICPAY BANK — BANCO MÚLTIPLO S.A]
[e demais corréus, se houver — ex.: e BANCO ORIGINAL S.A], devidamente
qualificado(s) nos autos em epígrafe [movido(s) por | movidos por] [NOME DA
PARTE AUTORA], vem, respeitosamente, à presença de Vossa Exceência, por
seu(s) procurador(es) que esta(s) subscreve(m), requerer [pedido central,
ver Passo 2 — ex.: "o regular ANDAMENTO DO FEITO" ou "a juntada do
comprovante de pagamento da condenação"], conforme exposto adiante.

[corpo específico da categoria — ver Passo 2; no caso de impulso oficial:
"Ocorre que os autos encontram-se paralisados desde [mês/ano ou data] sem
que houvesse qualquer movimentação processual, despacho ou sentença.
Portanto, em observância ao princípio constitucional da razoável duração do
processo (art. 5º, LXXVIII, da CF) e visando a celeridade processual (art.
4º do CPC), requer-se o prosseguimento do feito com o seu regular
andamento."]

Por fim, requer-se ainda que as publicações ocorridas nestes autos sejam
feitas em nome de [NOME DO ADVOGADO] (OAB/[UF] nº [XXXXX]), sob pena de
nulidade.

Termos em que pede deferimento.
[Cidade, por padrão “São Paulo”], [dia] de [mês por extenso] de [ano].

[NOME DO ADVOGADO]
OAB/[UF] nº [XXXXX]
```

Observações de formatação vistas nos originais: não usa "(A)"/"(O)" de
linguagem neutra (é sempre "EXCELENTÍSSIMO SENHOR DOUTOR JUÍZ", não
"EXCELENTÍSSIMO(A)..."); a data do fecho é por extenso ("17 de Maio de
2026"), não numérica; o rótulo é sempre "Autos nº", nunca "Processo nº"; não
há título de peça centralizado (o pedido central já vem em CAIXA-ALTA dentro
do próprio parágrafo de qualificação).

## Passo 6 — Geração dos arquivos

- Um .docx por processo, fonte Times New Roman 12, espaçamento 1,5,
  justificado, recuo de primeira linha 2 cm nos parágrafos de prosa (padrão
  forense). Pode ser feito com `python-docx` diretamente.
- Nome do arquivo, seguindo a convenção real do escritório observada no
  Drive: `{Nº do processo} - {tipo curto da peça}.docx` (ex.:
  `5023593-28.2025.8.08.0024 - petição de juntada.docx`,
  `5014564-77.2025.8.13.0035 - petição de impulso.docx`).
- Empacote todas as minutas de um lote em um único .zip.
- Gere também uma planilha de controle (.xlsx), uma linha por processo, com:
  Nº do processo, Categoria, Nome da parte autora (e de onde veio: Astrea /
  Drive / placeholder), Status ("Minuta pronta para revisão e protocolo" /
  "Minuta pronta — EXIGE VALIDAÇÃO antes de protocolar" / "Minuta incompleta
  — aguarda comprovante de pagamento" / "Minuta com placeholder — sem
  acesso a Astrea/Drive" / "Sem petição — ação interna"), Observação (texto
  do alerta, se houver) e nome do arquivo da minuta. Use cor de fundo por
  status para leitura rápida.

## Passo 7 — Entrega

Envie o .zip das minutas e a planilha de controle como arquivos (não cole
dezenas de petições no chat). No resumo em texto, separe claramente: quantas
minutas estão prontas com dado real (Astrea/Drive), quantas caíram em modo
placeholder por falta de acesso, quantas exigem validação por divergência de
bases, quantas estão incompletas por falta de insumo, e quantos processos
não geraram petição. Avise sempre que o endereçamento e a qualificação
precisam de conferência final antes do protocolo, mesmo quando vieram do
Astrea/Drive.