# eSAJ / CJSG do TJSP — referência técnica dos campos

Consulta de Jurisprudência de Segundo Grau (CJSG) do TJSP, host `https://esaj.tjsp.jus.br`. Este arquivo existe para dar precisão ao Passo 3 da SKILL.md: como o formulário funciona por baixo, quais os nomes exatos dos campos, como paginar, como abrir o inteiro teor e quais as armadilhas. Na prática cotidiana, prefira operar o formulário visível pelo Claude in Chrome; recorra a este detalhamento quando precisar montar uma URL, entender por que uma busca voltou vazia ou eventualmente automatizar por requisição direta.

## Índice
1. Endpoints
2. Campos de busca (corpo do POST)
3. Origem: Câmaras vs Colégios/Turmas Recursais
4. Paginação
5. Leitura dos resultados e link do inteiro teor
6. Armadilhas (codificação, sessão, bloqueio)

## 1. Endpoints

| Função | Método | URL |
|---|---|---|
| Formulário de busca (abre a sessão/cookies) | GET | `https://esaj.tjsp.jus.br/cjsg/consultaCompleta.do` |
| Submeter a busca | POST | `https://esaj.tjsp.jus.br/cjsg/resultadoCompleta.do` |
| Página N de resultados (inclusive a 1ª) | GET | `https://esaj.tjsp.jus.br/cjsg/trocaDePagina.do?tipoDeDecisao=A&pagina=N` |
| Inteiro teor do acórdão (PDF) | GET | `https://esaj.tjsp.jus.br/cjsg/getArquivo.do?cdAcordao=XXXX&cdForo=0` |
| Árvore de códigos de classe | GET | `https://esaj.tjsp.jus.br/cjsg/classesTreeSelect.do?campoId=classes` |
| Árvore de códigos de assunto | GET | `https://esaj.tjsp.jus.br/cjsg/assuntosTreeSelect.do?campoId=assuntos` |
| Árvore de órgãos julgadores (seções) | GET | `https://esaj.tjsp.jus.br/cjsg/secaoTreeSelect.do?campoId=secoes` |

Sutileza importante do fluxo: a busca é **POST**, mas o corpo da resposta ao `resultadoCompleta.do` é só um "ack" do envio do formulário — o HTML com os resultados vem do **GET seguinte** a `trocaDePagina.do?tipoDeDecisao=A&pagina=1`. Ou seja, tanto a página 1 quanto as demais saem de `trocaDePagina.do`.

## 2. Campos de busca (corpo do POST para `resultadoCompleta.do`)

Nomes verbatim (idênticos entre os raspadores de referência — courtsbr/esaj, jjesusfilho/tjsp, jtrecenti/juscraper):

Texto / consulta principal
- `dados.buscaInteiroTeor` — Pesquisa Livre / inteiro teor (busca ementa + texto integral). **Limite de 120 caracteres** imposto pelo TJSP.
- `dados.buscaEmenta` — busca apenas na ementa (padrão `""`).
- `dados.pesquisarComSinonimos` — sinônimos. Valores `"S"` (com) / `"N"` (sem).

Números
- `dados.nuProcOrigem` — número do processo/recurso de origem.
- `dados.nuRegistro` — número de registro.

Relator / magistrado
- `agenteSelectedEntitiesList`, `contadoragente` (`"0"`), `contadorMaioragente` (`"0"`), `nmAgente` (nome do relator).
- `codigoCr` (Colégio Recursal), `codigoTr` (Turma Recursal) — quando o relator é de órgão recursal.

Classe / Assunto / Comarca / Órgão
- `classesTreeSelection.values` — código(s) de classe, separados por vírgula; `classesTreeSelection.text` vazio.
- `assuntosTreeSelection.values` — código(s) de assunto; `assuntosTreeSelection.text` vazio.
- `cdComarca` — código da comarca (valor único); acompanha `comarcaSelectedEntitiesList`, `contadorcomarca`, `contadorMaiorcomarca`, `nmComarca`.
- `secoesTreeSelection.values` — código(s) do órgão julgador / seção / câmara, separados por vírgula; `secoesTreeSelection.text` vazio.

Datas (formato `dd/mm/aaaa`)
- `dados.dtJulgamentoInicio` / `dados.dtJulgamentoFim` — data de julgamento.
- `dados.dtRegistroInicio` / `dados.dtRegistroFim` — data de registro.
- Observação: o formulário do TJSP filtra por **julgamento/registro**, não por publicação — não conte com `dtPublicacao*`.

Origem / tipo / ordenação
- `dados.origensSelecionadas` — `"T"` = 2º grau (Câmaras); `"R"` = Colégios Recursais. Ver seção 3.
- `tipoDecisaoSelecionados` — `"A"` = Acórdãos; `"D"` = Decisões Monocráticas.
- `dados.ordenacao` — `"dtPublicacao"` para ordenar por data (mais recente primeiro).
- `conversationId` — vai vazio no POST inicial; o valor real é lido do HTML da resposta e reusado na paginação.

Os códigos numéricos de classe, assunto e órgão julgador não são fixos aqui de propósito: obtenha-os em tempo de uso nos endpoints de árvore (seção 1), lendo, em cada `<span id="secoes_tree_*" value="CODIGO">`, o atributo `value` (é exatamente o que se envia em `secoesTreeSelection.values`) e o texto visível (nome da câmara/colégio). Operando pelo formulário no navegador, basta selecionar pelo nome — não precisa dos códigos.

## 3. Origem: Câmaras vs Colégios/Turmas Recursais

O campo "Origem" do formulário oferece "2º grau" e "Colégios Recursais", controlados por `dados.origensSelecionadas`:
- `"T"` → 2º grau (Câmaras de Direito Privado/Público).
- `"R"` → Colégios/Turmas Recursais (recursos de Juizado Especial).

Atenção: todos os raspadores públicos assumem `"T"` por padrão, ou seja, **só trazem 2º grau se você não trocar**. Para pegar as Turmas/Colégios Recursais é preciso setar `"R"` explicitamente. Como a carteira de menor valor (consumo, bancário) costuma tramitar no Juizado, cobrir a origem `"R"` é o que torna esta skill mais completa que uma busca só de Câmaras.

Observação verificada em teste ao vivo (jul/2026): mesmo marcando as duas caixas de Origem no formulário, a aba de resultados visível ("Acórdãos(N)") trouxe apenas o 2º grau; os julgados de Colégio/Turma Recursal só apareceram quando a busca foi refeita com **somente** "Colégios Recursais" marcado (e vieram como classe "Recurso Inominado Cível", órgão "Nª Turma Recursal Cível"). Por isso, o caminho confiável para cobrir as duas instâncias é **duas passadas separadas**, uma por origem, e não confiar na busca combinada.

Filtros recursais adicionais no corpo: `codigoCr`, `codigoTr`, `codigoJuizCr`, `codigoJuizTr`. A árvore de seções (`secaoTreeSelect.do`) também traz nós de Colégio/Turma Recursal (ex.: "Colégio Recursal Central da Capital", "1ª Turma Recursal Cível", "Turma de Uniformização dos Juizados Especiais").

## 4. Paginação

1. POST em `resultadoCompleta.do` (registra a consulta na sua sessão/cookie).
2. GET em `trocaDePagina.do?tipoDeDecisao=A&pagina=1` → é a página 1 e também de onde se lê o total.
3. Para cada página seguinte, GET em `trocaDePagina.do` com: `tipoDeDecisao` (`"A"` ou `"D"` — repare que no GET o parâmetro é `tipoDeDecisao`, diferente do `tipoDecisaoSelecionados` do POST), `pagina` (1-based) e `conversationId` extraído da página 1.

São **20 resultados por página**; não há parâmetro de "linhas por página" no CJSG. Nº de páginas = teto(total / 20). O total aparece nos elementos `#totalResultadoAba-A` / `#totalResultadoAba-D`. Vá devagar: ~1 requisição por segundo.

## 5. Leitura dos resultados e link do inteiro teor

Cada resultado é uma linha `<tr class="fundocinza1">`. Dentro dela:
- Âncora `<a class="esajLinkLogin downloadEmenta">`: o texto é o número CNJ do processo; o atributo `cdacordao` é o id do acórdão e `cdforo` o código do foro.
- Linhas `<tr class="ementaClass2">` com rótulo em `<strong>`: Relator(a), Comarca, Órgão julgador, Data do julgamento, Data de publicação/registro.
- Classe/Assunto no nó `.assuntoClasse`.
- Texto da ementa no nó `.mensagemSemFormatacao` (ou no `<div align="justify">` visível, retirando o "Ementa:" inicial).

Monte o link do inteiro teor com os atributos lidos:
`https://esaj.tjsp.jus.br/cjsg/getArquivo.do?cdAcordao=<cdacordao>&cdForo=<cdforo ou 0>`

## 6. Armadilhas

- **Codificação ISO-8859-1 (latin1).** Decodifique como latin1 ou os acentos viram mojibake.
- **Sessão/cookies obrigatórios.** Um GET "frio" a `trocaDePagina.do` não funciona: o POST a `resultadoCompleta.do` semeia a sessão (JSESSIONID) da qual o GET depende. Carregue os cookies do POST para o GET; use `Referer: https://esaj.tjsp.jus.br/cjsg/resultadoCompleta.do`.
- **`conversationId`** não é fixo: leia-o do HTML da página 1 (`<input name="conversationId">`) e reenvie na paginação.
- **User-Agent de navegador real.** O TJSP costuma exigir UA de Chrome; UA de biblioteca pode ser bloqueado. Este é mais um motivo para operar via Claude in Chrome.
- **Rate limiting / bloqueio de IP são reais.** Mantenha single-thread e ~1s entre requisições; poucas páginas por vez.
- **Sem CAPTCHA no CJSG** (diferente da consulta processual do cposg). Não há desafio de JS; o obstáculo é só a sessão/UA.
- **Limite de 120 caracteres** em `dados.buscaInteiroTeor`.
