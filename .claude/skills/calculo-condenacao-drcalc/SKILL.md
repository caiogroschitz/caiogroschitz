---
name: calculo-condenacao-drcalc
description: "Fluxo completo (extração de PDF + validação + cálculo no DrCalc + planilha em PDF) de liquidação de condenação judicial brasileira, com gate obrigatório contra datas estimadas e contra juros calculados com uma data única quando as verbas têm datas de início de juros diferentes. Absorve e substitui a skill drcalc-automacao."
---

# Skill: Liquidacao de Condenacao Judicial -- extracao + validacao + DrCalc + planilha

Skill unica que cobre o fluxo inteiro em quatro fases. Nao pare na fase 1: o
usuario que pede "os valores" quase sempre quer a planilha pronta no fim. Se o
usuario ja chegar com os parametros prontos (verbas, datas confirmadas com
Id/Evento, indices, juros), pule as Fases 1 e 2 e va direto para o **Gate de
Verificacao** antes da Fase 3 -- mas nunca pule o gate em si, mesmo com
parametros supostamente prontos.

    FASE 1 Auditoria do PDF   ->  FASE 2 Validacao com o usuario
    GATE  Verificacao de datas e de juros (obrigatorio, sempre)
    FASE 3 Calculo no DrCalc  ->  FASE 4 Planilha em PDF

---

## REGRA DE OURO: a data final e SEMPRE HOJE

O calculo fecha na data de hoje, sem excecao, salvo ordem expressa em contrario
(ex.: "atualiza ate a data do transito", "calcula como estava em 23/07").

**Nunca deduza a data de hoje do contexto, do PDF ou da memoria.** Leia do
sistema, na primeira acao da skill:

```bash
date '+%d/%m/%Y'
```

Esse valor e o `HOJE` usado em todo o resto da skill e impresso na planilha.

---

## Regras criticas de datas

Sao a maior fonte de erro nesse tipo de trabalho. Valem sempre, e a numero 0 e
a que mais falha na pratica -- leia com atencao.

0. **Proibido estimar, chutar ou "parecer certo".** Toda data usada no calculo
   precisa vir de uma citacao literal do PDF, com o Id/Evento apontado. "Acho
   que e essa data", "geralmente e X dias depois da sentenca" ou preencher o
   campo so porque uma data qualquer apareceu perto do trecho certo **nao sao
   aceitaveis**. Se voce nao achou o trecho exato que confirma aquela data,
   volte ao `grep`/`sed` e procure mais -- amplie o termo de busca, leia mais
   contexto ao redor, olhe a lista de documentos da capa de novo. Se mesmo
   assim nao achar (ex.: PJe sem evento de ciencia), isso e uma limitacao real:
   sinalize explicitamente ao usuario qual data voce usou como substituto e
   por que, nunca finja certeza que voce nao tem.

1. **Citacao**: use a data de **confirmacao/ciencia** ("CONFIRMADA A CITACAO
   ELETRONICA ... CIENCIA NO DOMICILIO ELETRONICO"), nunca a de expedicao
   ("EXPEDIDA/CERTIFICADA A CITACAO"). Em PJe sem evento de ciencia, a Carta
   Postal - Citacao e o melhor substituto disponivel -- **sinalize a
   limitacao** (regra 0).

2. **Publicacao da sentenca**: use "PUBLICADO NO DJEN", nao "DISPONIBILIZADO NO
   DJEN" nem a data de assinatura eletronica do magistrado.

3. **Titulo reformado em grau recursal**: quem manda e o **acordao**, nao a
   sentenca. Confira se houve Recurso Inominado/Apelacao provido -- o
   dispositivo do acordao substitui o da sentenca. Procure "Certidao de
   julgamento", "Acordao", "Voto do Magistrado", "dar provimento", "reformando
   a sentenca". Se houve reforma, os valores/datas/indices vem do acordao, nao
   da sentenca -- nunca misture os dois.

4. **Arbitramento de dano moral (Sumula 362/STJ)**: "correcao a partir desta
   data" significa a data do julgado que fixou o valor. Se sessao de julgamento
   e assinatura do acordao divergem, sao duas candidatas -- pergunte (regra 5).

5. **Mais de uma data candidata para qualquer campo**: **nao escolha sozinho.**
   Liste as opcoes com o Id/Evento de cada uma e pergunte ao usuario, via
   AskUserQuestion, antes de rodar o calculo. Isso vale mesmo que uma das
   opcoes "pareca" mais provavel -- decisao sobre qual data usar e do usuario,
   nao sua.

6. **Sempre cite o Id/Evento** de onde saiu cada data, para conferencia rapida
   no PJe/eproc. Isso e o que torna a regra 0 verificavel -- se voce nao
   consegue citar o Id/Evento, a data nao esta confirmada.

---

## Regras criticas de juros

O erro mais comum aqui e forcar um unico `jmdata` (o campo do DrCalc que
define "Calcular juros a partir de") quando, na verdade, **as verbas da
condenacao tem datas de inicio de juros diferentes entre si** -- por exemplo,
danos morais com juros contados do arbitramento (Sumula 362/STJ) e danos
materiais/restituicao com juros contados da citacao. O formulario do DrCalc so
aceita **uma unica data** em `jmdata` por rodada de calculo. Preencher um
valor medio, o mais antigo, "o que for mais comum" ou a data da verba de maior
valor esta errado e distorce o resultado de todas as outras verbas.

1. **Antes de tocar no formulario, monte a Tabela de Grupos de Juros** -- uma
   linha por verba: descricao | valor historico | data de inicio da correcao
   (vai no `dia{n}` de cada item) | data de inicio dos juros | taxa/regra de
   juros (legal `l1`/`l2` ou manual `s`/`c` com percentual). Agrupe as verbas
   pela **data de inicio dos juros junto com a regra/taxa de juros** -- nao
   pela data de correcao, que e outro campo e pode variar item a item mesmo
   dentro do mesmo grupo de juros.

2. **Todas as verbas com a mesma data de inicio de juros e a mesma regra/taxa
   de juros -> uma unica rodada no DrCalc**, com `jmdata` = essa data e
   `dia{n}` de cada item conforme sua propria data de correcao (que pode ser
   diferente do `jmdata` sem problema nenhum -- sao campos independentes).

3. **Mais de um grupo de data/regra de juros -> mais de uma rodada.** Rode o
   DrCalc uma vez por grupo (recarregue `juridico.asp`, troque `jmdata`/regra
   e preencha so os itens daquele grupo), capture o TOTAL GERAL de cada
   rodada e **some os totais na planilha final**, deixando claro na Fase 4
   qual item pertence a qual grupo/regra de juros. Avise o usuario disso
   *antes* de rodar: "essa condenacao tem N regras de juros diferentes, vou
   rodar o DrCalc N vezes e consolidar num total geral".

4. **`valor{n}` e sempre o valor historico (singelo)**, nunca o valor ja com
   juros ou correcao embutidos. Nunca calcule juros "na mao" e jogue o
   resultado dentro de `valor{n}` -- e exatamente para isso que existe o
   DrCalc. Se voce fizer essa conta por fora, o site vai calcular juros em
   cima de um valor que ja tem juros embutido (bis in idem) e a planilha final
   nao vai bater com a formula que o proprio rodape do DrCalc mostra.

5. **Taxa legal (`l1`/`l2`) vs taxa manual (`c`/`s`)**: leia o dispositivo com
   atencao antes de marcar o radio.
   - Titulo com percentual fixo ("1% ao mes", "juros de mora de 1% a.m.") ->
     `s` (simples) ou `c` (composta), com `jmjuro`/`jmperiodojuro` preenchidos.
     **Nunca** use `l1`/`l2` nesse caso.
   - Titulo com "juros legais", "juros de mora" sem percentual, ou remissao a
     SELIC/art. 406 do CC -> `l1` (Lei 14.905/2024 + Tema 1368, padrao a partir
     de 30/08/2024) ou `l2` (12%/6% a.a., regra antiga) conforme o periodo.
   - Titulo omisso ou ambiguo quanto a taxa: isso e ambiguidade, nao decisao
     sua -> pergunte ao usuario (mesma regra 5 das datas), nunca assuma a
     leitura mais comum sem confirmar.
   - **Cuidado com "1% ao mes" flutuando solto no PDF.** Peticoes, CCBs de
     emprestimo anexadas, contestacoes e jurisprudencia citada como precedente
     (de **OUTRO** processo) costumam trazer "1% ao mes" escrito em algum
     lugar do PDF, sem que seja a regra da verba que voce esta calculando.
     Antes de aceitar um percentual como "a regra do titulo", confirme que o
     trecho pertence ao Id/Evento da **propria sentenca/acordao deste
     processo** -- nunca a uma peticao das partes, clausula de contrato
     juntado aos autos, ou acordao/jurisprudencia de outro numero de processo
     citado como precedente. Um `grep` que acha "1%" fora do dispositivo do
     proprio titulo **nao vale** -- volte e procure a taxa realmente fixada no
     dispositivo (ou confirme que ele e omisso, regra do "titulo omisso"
     acima).

6. **Pro rata die ate HOJE** (extensao dos juros quando a taxa e fixa `s`/`c`):
   calcule sempre em bash/python, nunca de cabeca, e confira por dois metodos
   de contagem que devem coincidir (procedimento na Fase 3). Isso vale por
   grupo, se houver mais de um grupo de juros.

---

## GATE DE VERIFICACAO (obrigatorio antes da Fase 3, sem excecao)

Nao preencha o formulario do DrCalc sem antes produzir -- na resposta do chat
ou como rascunho interno auditavel -- estas duas tabelas, com **todas** as
celulas preenchidas (nenhuma com "assumindo", "provavelmente", "parece que",
"geralmente"):

**Tabela de Datas** -- uma linha por data usada no calculo:

| Campo do calculo | Data (DD/MM/AAAA) | Id/Evento no PJe/eproc | Trecho literal |
|---|---|---|---|

**Tabela de Grupos de Juros** -- como descrito na secao anterior:

| Grupo | Verbas incluidas | Data inicio juros (`jmdata`) | Regra/taxa | Itens (`dia{n}`/`valor{n}`) |
|---|---|---|---|---|

Se qualquer celula nao tiver uma citacao literal + Id/Evento, ou se houver mais
de uma data/regra candidata para o mesmo campo, **pare e pergunte ao usuario
via AskUserQuestion antes de continuar**. Isso vale mesmo que o usuario so
tenha pedido "roda o calculo" direto -- rodar com dado ambiguo ou estimado e
pior do que perguntar, porque produz uma peca com numero errado.

---

## FASE 1 -- Auditoria do PDF

PDFs de processo passam de 10 MB e 200 paginas. Nao tente ler tudo: extraia
texto e faca buscas segmentadas.

```bash
pdftotext -layout "/caminho/do/arquivo.pdf" /tmp/proc.txt
wc -l /tmp/proc.txt
head -100 /tmp/proc.txt      # capa do PJe: numero, classe, partes, LISTA DE DOCUMENTOS
```

A lista de documentos da capa e o mapa do processo -- use-a para achar o
documento mais recente que importa (acordao > sentenca).

```bash
# Titulo executivo: sentenca e/ou acordao
grep -n -i "SENTEN\|DISPOSITIVO\|JULGO\|CONDENO\|Ante o exposto\|Pelo exposto\|HOMOLOGO" /tmp/proc.txt
grep -n -i "AC[OO]RD[AA]O\|Turma Recursal\|dar.*provimento\|reformando a senten" /tmp/proc.txt

# Citacao
grep -n -i "cita[cc]\|CIENCIA NO DOMICILIO\|Carta Postal" /tmp/proc.txt

# Publicacao / transito
grep -n -i "PUBLICADO NO DJEN\|DISPONIBILIZADO NO DJEN\|Transito em Julgado" /tmp/proc.txt

# Cumprimento de sentenca (memoria da parte contraria, se houver)
grep -n -i "cumprimento de senten\|art. 523\|mem[oo]ria de c[aa]lculo" /tmp/proc.txt
```

Depois use `sed -n 'INICIO,FIMp' /tmp/proc.txt` para ler cada trecho com
contexto. Se um `grep` voltar vazio ou parecer incompleto, **isso nao e sinal
para desistir e estimar** -- tente variacoes do termo, leia paginas vizinhas na
lista de documentos, ou registre a limitacao explicitamente (regra 0 de
datas).

### O que registrar

**Identificacao** -- numero, juizo/comarca, credor, devedor **condenado no
merito** (exclua reus extintos sem merito), titulo exequendo e data do
transito.

**Cada verba** -- tipo (moral/material/restituicao/multa), valor principal,
modalidade (**simples ou em dobro**), se depende de liquidacao, e a
**transcricao literal** do trecho do dispositivo que fixa indice e juros
daquela verba (guarde essa transcricao -- ela alimenta a Tabela de Grupos de
Juros do Gate). Antes de aceitar qualquer percentual (ex.: "1% ao mes") como
regra de juros de uma verba, confirme que ele esta no dispositivo do
**proprio** titulo executivo (sentenca/acordao deste processo, no Id/Evento
certo) -- nunca em peticao das partes, clausula de contrato juntado aos autos,
ou precedente/jurisprudencia citado de **outro** processo (ver "Regras
criticas de juros" acima).

**Datas-marco** -- desembolso de cada parcela, arbitramento, citacao,
publicacao, com Id/Evento de cada uma.

**Indices e juros** -- o que o titulo diz, verba por verba. Se o titulo for
**omisso**, adote o padrao legal e **declare que adotou**:
- ate 29/08/2024: indice do tribunal/INPC/IPCA-E conforme praxe local + 1% a.m.
- a partir de 30/08/2024 (Lei 14.905/2024): IPCA + taxa legal (SELIC-IPCA).
- **Titulo expresso prevalece sobre lei superveniente** -- coisa julgada. Se o
  acordao disse "IPCA-E e 1% ao mes", e isso que se aplica, mesmo depois de
  30/08/2024.

---

## FASE 2 -- Validacao com o usuario

Antes de rodar qualquer calculo, apresente o resumo estruturado (processo,
verbas, datas, indices, fundamento literal) e **pergunte via AskUserQuestion**
sobre todo ponto ambiguo: datas candidatas concorrentes, indice omisso, regra
de juros omissa/ambigua, multa do art. 523. Essa e a mesma logica do Gate mais
adiante -- aqui e onde as ambiguidades tipicamente aparecem pela primeira vez.

Nao rode o DrCalc com data ou regra de juros ambigua. Um dia de diferenca na
citacao, ou uma data de juros errada numa verba, muda o resultado e compromete
a peca.

---

## FASE 3 -- Calculo no DrCalc

Pre-requisito: navegador conectado. Carregue as ferramentas numa unica
chamada:

```
ToolSearch: select:mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__navigate,mcp__claude-in-chrome__javascript_tool,mcp__claude-in-chrome__get_page_text
```

`tabs_context_mcp{createIfEmpty:true}` -> `navigate` para
`https://drcalc.net/juridico.asp`.

Se o Gate identificou **mais de um grupo de juros**, repita esta Fase 3
inteira uma vez por grupo: recarregue `juridico.asp` a cada rodada (nao
reaproveite o formulario da rodada anterior) para nao misturar itens/estado
entre grupos.

### Mapa de campos do formulario (form `formcalculo`, POST para juridico.asp)

| Campo (name) | O que e | Como preencher |
|---|---|---|
| `descricao` | Descricao do calculo (campo de texto livre, topo do formulario) | Preencher sempre com `<NUMERO_DO_PROCESSO> -- <descricao da verba/grupo>` (ex.: `5012857-78.2026.8.08.0035 -- Danos morais`), pra identificar a planilha ja na tela do DrCalc. Se houver mais de um grupo de juros, use a descricao do grupo desta rodada |
| `mes`, `ano` | "Mes/Ano -- Informe Mes e Ano para atualizacao dos valores" (data final da correcao) | **Sempre o mes/ano CORRENTE -- o de HOJE**, o mesmo `HOJE` lido no inicio da skill (Regra de Ouro), **nunca** o ultimo mes publicado pelo indice escolhido, mesmo que esse indice ainda nao tenha publicado o mes corrente. Ver "Fechamento na data de HOJE" abaixo para o aviso obrigatorio quando isso acontece |
| `indice` | Indice de correcao | `9`=IPCA (IBGE), `15`=INPC, `17`=IPCA-E, `1006`=IPCA-15, `41`=JF-Condenatorias Geral (default), alem de indices de tribunal (TJES/TJMG etc.). O rotulo de cada `option` traz o intervalo publicado -- **leia-o** antes de escolher `mes`/`ano` |
| `flagdefl` | Deflacionar em inflacao negativa | checkbox; deixar desmarcado salvo ordem em contrario |
| `jmjuro` | Taxa dos juros moratorios (%) | So usado com `jmcapitalizacao=c` ou `s`. Deixe `0` com taxa legal (`l1`/`l2`) |
| `jmperiodojuro` | Periodo da taxa | `m`=mensal, `a`=anual, `d`=diario |
| `jmcapitalizacao` | **Tipo dos juros moratorios** (radios) | `l1`=taxa legal art. 406/Lei 14.905/24 + STJ Tema 1368 (SELIC-IPCA), padrao pos-30/08/2024; `l2`=taxa legal 12%/6% a.a. (regra antiga); `c`=composta (taxa manual); `s`=simples (taxa manual, ex. "1% ao mes"). Ver Regras criticas de juros acima para escolher certo. **Clicar via `.click()`** para disparar o onclick |
| `jmdata` | "Calcular juros a partir de" | Data unica de inicio dos juros **do grupo desta rodada** (ex.: citacao, ou arbitramento), DD/MM/AAAA. Sai direto da Tabela de Grupos de Juros do Gate -- nunca uma data "media" ou "a mais comum" quando ha mais de um grupo |
| `jmsobrejc` | Juros de mora sobre juros compensatorios | normalmente desmarcado |
| `jcjuro` e demais `jc*` | Juros compensatorios | normalmente `0`/vazio (nao usar, salvo o titulo determinar) |
| `flagart523` | Multa+honorarios art. 523 par. 1 CPC (radios) | `naoaplicar` (default), `aplicarmulta`, `aplicarmultahonorario`. Fase de conhecimento -> `naoaplicar`. So mudar se o usuario confirmar que o prazo de 15 dias correu in albis (nunca por conta propria) |
| `multa`, `honorario` | Percentual/valor | so preencher se `flagart523` != `naoaplicar` |

### Tabela de itens (parcelas) -- so os itens do grupo desta rodada

- Quantidade de linhas: campo `qt1` (default 10). Defina `qt1=N` (N = numero de
  itens **deste grupo**) e **clique no botao "Ok"** (onclick `qt()`) -- e um
  postback que regenera a tabela. Confirme que existe `dia{N}`.
- Por linha `n` (1..N):
  - `item{n}` = numero do item (auto "1","2"...) -- nao mexer
  - `dia{n}` = **data de correcao** DD/MM/AAAA (desembolso/arbitramento
    daquela verba -- pode diferir do `jmdata` da rodada, isso e normal)
  - `valor{n}` = **valor historico (singelo)**, formato BR com virgula (ex.:
    `129,80`). Em **dobro**, lancar o valor ja dobrado por parcela. Nunca
    embuta juros/correcao aqui (regra 4 de juros)
  - `descri{n}` = descricao livre, referenciando o item do dispositivo
  - `tipoparcela{n}` = `1`=parcela de debito (juros+correcao), `2`=custa,
    `3`=despesa, `4`=desconto. Use `1` para verbas condenatorias
- Botao final: **"Executar o calculo"** (onclick `calculo()`).
- Resultado abre em `planilhacalc.asp` com Valor Singelo / Atualizado / Juros /
  Total e o **TOTAL GERAL** -- este e o total do grupo/rodada, nao
  necessariamente o total da condenacao inteira se houver mais de um grupo.

Setar campos via `javascript_tool` com `dispatchEvent` de `input` e `change`.
Radios com `.click()`. **Confira todas as linhas com um dump JSON antes de
submeter.**

Cuidado: clicar "Ok" navega a pagina. **Nao encadeie `await sleep` depois de um
clique que navega** -- o contexto morre ("Inspected target navigated"). Clique
numa chamada, confira o estado na chamada seguinte.

### Fechamento na data de HOJE (o ponto que mais erra)

**Regra confirmada com o usuario (02/09/2026): o campo "Mes/Ano -- Informe Mes
e Ano para atualizacao dos valores" e SEMPRE preenchido com o mes/ano
CORRENTE -- o de HOJE -- nunca com o ultimo mes publicado pelo indice
escolhido, mesmo quando esse indice ainda nao publicou o mes corrente.** Essa
skill ja tentou a logica inversa (fechar no ultimo mes publicado do indice) e
foi corrigida a pedido explicito do usuario -- nao volte a essa logica antiga.

Procedimento:

**1. Use o `HOJE` ja lido no inicio da skill** (Regra de Ouro, `date
'+%d/%m/%Y'`) -- nao releia de novo nem estime. `mes` = mes de HOJE, `ano` =
ano de HOJE.

**2. Confira, so para fins de aviso, se o indice escolhido ja publicou o mes
corrente.** O rotulo da `option` diz o intervalo publicado:

```js
[...document.forms['formcalculo'].elements['indice'].options]
  .map(o => o.value + '=' + o.text)
// "9=IPCA (IBGE) ...... (jan/1980 a jul/2026)"  -> ultimo publicado: jul/2026
```

Cada indice tem sua propria defasagem de divulgacao (o IPCA (IBGE) "puro"
normalmente sai so por volta do dia 9-11 do mes seguinte; IPCA-15 e IPCA-E,
por serem previas/versoes expandidas, costumam sair mais cedo). Isso e so
para saber se falta aviso ao usuario -- **nunca** para trocar o mes/ano que
voce vai preencher, que continua sendo sempre o corrente.

**3. Preencha `mes`/`ano` = mes/ano de HOJE de qualquer forma.** Se o passo 2
mostrou que o indice escolhido ainda nao publicou o mes corrente, **avise
expressamente o usuario na resposta do chat** (nunca dentro do PDF -- ver Fase
4) que a planilha fechou num mes em que o indice `<nome>` ainda nao tinha dado
publicado (ultimo publicado real: `<mes/ano do option>`), e que o valor da
correcao desse(s) mes(es) final(is) e o que o proprio DrCalc calculou para
esse periodo -- sem confirmacao de que corresponde a dado ja publicado pelo
IBGE/orgao responsavel. Sugira reconferir a planilha apos a publicacao, se o
usuario quiser.

Exemplo real: HOJE = 02/09/2026. `IPCA (IBGE)` mostrava "jan/1980 a jul/2026"
(agosto/setembro ainda nao saiu). Preenche-se `mes`/`ano` = **09/2026** (mes
corrente) mesmo assim, e o aviso acima vai na resposta do chat, citando que o
IPCA so tinha publicado ate julho/2026 no momento do calculo.

**4. Estenda os juros ate HOJE, pro rata die** -- quando a taxa for fixa
(`s`/`c`, ex. 1% a.m.). Calcule em bash, nunca de cabeca:

```bash
python3 -c "
from datetime import date
d0=date(2026,2,23)   # inicio dos juros deste grupo (ex.: citacao)
d1=date(2026,8,14)   # HOJE
dias=(d1-d0).days
taxa=dias/30/100     # 1% a.m. simples, base 30 dias
for base in [1037.05, 4016.40]:   # VALOR ATUALIZADO de cada item deste grupo
    print(base, round(base*taxa,2), round(base*(1+taxa),2))
print('%.4f%%' % (taxa*100))
"
```

Confira pelos dois metodos de contagem -- devem coincidir:
- meses cheios + dias/30 (ex.: 5 meses e 22 dias = 5 + 22/30 = 5,7333%)
- dias corridos / 30 (ex.: 172 / 30 = 5,7333%)

Divergiu? Refaca antes de seguir. Se houver mais de um grupo de juros, repita
esse calculo por grupo -- cada grupo tem sua propria data de inicio e,
possivelmente, sua propria taxa.

**5. Taxa legal (`l1`/`l2`)**: a extensao dos juros ate HOJE e automatica (o
proprio DrCalc aplica a taxa vigente mes a mes, sem pro rata manual). O aviso
do passo 3 continua valendo do mesmo jeito se o mes corrente ainda nao tiver
sido publicado pelo indice de correcao escolhido.

**6. Multa do art. 523, par. 1o** so entra se o usuario confirmar que o prazo
de 15 dias correu in albis. Nunca por conta propria.

---

## FASE 4 -- Planilha em PDF

### Formato e destino
- **PDF**, nome **`<NUMERO_DO_PROCESSO>_CALC.pdf`** -- numero como nos autos,
  com pontos e tracos. Variantes recebem sufixo claro (ex.:
  `..._CALC_50pct.pdf`), mantendo o `_CALC`.
  Ex.: `5001536-45.2026.8.13.0637_CALC.pdf`.
- Destino: **`Area de Trabalho/Calculos DrCalc`**
  (`C:\Users\<user>\Desktop\Calculos DrCalc`). A pasta precisa estar
  conectada: liste com `mcp__remote-devices__device_list_dir`, peca acesso com
  **`mcp__remote-devices__device_request_folder_access`**, entregue no chat
  com `SendUserFile` e grave no disco com
  `mcp__remote-devices__device_commit_files` (usa o `file_uuid` devolvido pelo
  `SendUserFile`). Se o usuario tiver definido outra pasta, usar a dele.
- Confirme ao usuario o caminho final e o nome do arquivo salvo.

### Se houve mais de um grupo de juros (mais de uma rodada no DrCalc)
Consolide numa **unica planilha final**: mesma tabela ITEM/DESCRICAO/DATA/...,
com todos os itens de todos os grupos, e uma linha de cabecalho por grupo
indicando a regra de juros usada naquele bloco de itens (ex.: "Juros a partir
da citacao (09/03/2026) -- taxa legal SELIC-IPCA" acima dos itens desse grupo,
"Juros a partir do arbitramento (15/06/2026) -- 1% a.m. simples" acima do
outro). O **TOTAL GERAL** final e a soma dos TOTAL GERAL de cada rodada --
confira essa soma em bash antes de escrever no PDF.

### Conteudo -- planilha limpa, sem apendices
A folha tem **apenas**: identificacao do processo, cabecalhos, tabela, totais
e a nota de rodape do DrCalc. Nada mais.

1. **Identificacao** -- processo, juizo, credor, devedor, titulo exequendo
   (data, Id, orgao julgador, transito).
2. **Cabecalhos**, no estilo do DrCalc (repetir por grupo se houver mais de
   um):
   - `Data de atualizacao dos valores: <HOJE>`
   - `Indexador utilizado: <indice> -- serie acumulada ate <mes/ano de HOJE
     usado no calculo>`. Se o indice ainda nao tinha publicado esse mes no
     momento do calculo, essa ressalva vai **na resposta do chat**, nunca
     dentro do PDF (ver "Fechamento na data de HOJE" na Fase 3)
   - `Juros moratorios ... a partir de <data> ate <HOJE> = N dias = P%` (ou a
     descricao da taxa legal, se `l1`/`l2`)
   - linhas de multa e honorarios (zeradas quando nao incidem)
3. **Tabela**: ITEM | DESCRICAO | DATA | VALOR SINGELO | VALOR ATUALIZADO |
   JUROS MORATORIOS | TOTAL, com banda cinza alternada e linha TOTAIS (por
   grupo, se houver mais de um).
4. **Subtotal** (por grupo, se aplicavel) e **TOTAL GERAL** com linha
   pontilhada e "R$".
5. Rodape com a ressalva do DrCalc (auxiliar, conferir com profissional).

**NAO incluir na planilha**: quadros de "parametros extraidos do titulo",
"cenarios de fechamento", "observacoes e ressalvas", a Tabela de Datas ou a
Tabela de Grupos de Juros do Gate, nem transcricoes do dispositivo. Essas
informacoes vao **na resposta do chat**, nunca no PDF -- a planilha e peca de
instrucao processual e precisa estar limpa.

### Fidelidade visual (a folha do proprio DrCalc)
O PDF deve REPRODUZIR a folha que o DrCalc gera (`planilhacalc.asp` / "Versao
para Impressao" `planilharesult.asp`), nao um layout proprio. Ordem de
preferencia:
1. Se a sessao do navegador permitir salvar/baixar a planilha do DrCalc
   ("Salvar Planilha" = `calculo('save','')` abre `planilharesult.asp`), obter
   esse HTML e converte-lo em PDF (weasyprint/libreoffice).
2. Quando a extracao do HTML/captura de tela nao for possivel na sessao
   (filtros de conteudo, screenshot indisponivel), REPRODUZIR fielmente o
   layout do DrCalc em HTML e renderizar com weasyprint
   (`pip install weasyprint --break-system-packages`), mantendo:
   - titulo vermelho "PLANILHA DE DEBITOS JUDICIAIS";
   - linhas-cabecalho: "Data de atualizacao dos valores", "Indexador
     utilizado", "Juros Moratorios - ...", multa, honorarios;
   - colunas: ITEM | DESCRICAO | DATA | VALOR SINGELO | VALOR ATUALIZADO |
     JUROS MORATORIOS TAXA LEGAL | TOTAL;
   - banda cinza alternada, linha TOTAIS, e Subtotal / TOTAL GERAL com linha
     pontilhada e "R$".
   Se houver mais de um grupo de juros, repita os blocos de cabecalho/tabela
   um por grupo, dentro do mesmo PDF, antes do TOTAL GERAL consolidado.

**Confira antes de entregar**: `pdftoppm -png -r 90 -f 1 -l 1 arquivo.pdf
preview` e leia o PNG, comparando com a planilha do DrCalc.

---

## Na resposta do chat

Depois de entregar o PDF, escreva em prosa curta: o total, os pontos frageis
do calculo (data de citacao sem evento de ciencia, indice adotado por omissao
do titulo), se houve mais de um grupo de juros e por que, divergencia
relevante em relacao a memoria da parte contraria (se houver), e o efeito da
multa do art. 523 caso ela venha a incidir. Sem repetir a tabela.

## Limites
- O DrCalc e auxiliar; o resultado deve ser conferido por profissional
  habilitado.
- Confirme a data exata da citacao na movimentacao (juros correm dela).
- Condenacao solidaria: valor integral exigivel de qualquer reu; "calculo so
  por um dos reus" = valor cheio, sem rateio.
- Restituicao em dobro: correcao e multiplicativa; dobre por parcela
  (recomendado, mantem o rastro claro item a item) em vez de dobrar o total.