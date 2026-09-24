# Consulta de Jurisprudência do TJES: referência técnica

Sistema publicado em 31/10/2025 em `https://sistemas.tjes.jus.br/consulta-jurisprudencia/` (versão observada: V2.11.73). Substituiu as consultas anteriores e integra, numa interface única, as bases do PJe (1º e 2º graus), as decisões monocráticas, o acervo de processos físicos e as Turmas Recursais do Projudi.

Este arquivo existe para dar precisão ao Passo 3 da SKILL.md: como o sistema funciona por baixo, quais os nomes exatos dos parâmetros, o que cada base devolve e onde estão as armadilhas. Todos os números e nomes abaixo foram verificados ao vivo em agosto de 2026.

## Índice
1. Endpoint e forma de acesso
2. Parâmetros da busca
3. As cinco bases (cores) e seus campos
4. Sintaxe de consulta
5. Filtros disponíveis e seus valores
6. Ler os resultados e abrir o inteiro teor
7. Armadilhas

## 1. Endpoint e forma de acesso

| Função | Método | URL |
|---|---|---|
| Interface de busca | GET | `https://sistemas.tjes.jus.br/consulta-jurisprudencia/` |
| API de busca (JSON) | GET | `https://sistemas.tjes.jus.br/consulta-jurisprudencia/api/search` |

A interface é uma SPA que consome a própria API. Não há login, não há captcha e não há cookie de sessão a preservar, o que torna a operação bem mais simples que a do TJMG.

**A API só responde de dentro do navegador.** Requisição vinda de fora (WebFetch, curl, requests, qualquer cliente HTTP) recebe **403**; há um WAF filtrando por origem e user-agent. O caminho que funciona é executar o fetch no contexto da própria página já carregada, com `javascript_tool`:

```js
const r = await fetch('/consulta-jurisprudencia/api/search?core=pje2g&q='
  + encodeURIComponent('ementa:("culpa exclusiva da vítima" AND pix)')
  + '&jurisdicao=' + encodeURIComponent('Turma Recursal')
  + '&dataIni=2024-01-01&sort=' + encodeURIComponent('dt_juntada desc')
  + '&page=1&per_page=50').then(x => x.json());
r.total; r.docs.map(d => [d.nr_processo, d.orgao_julgador, d.magistrado, d.dt_juntada]);
```

Cuidado ao imprimir o resultado: devolver JSON bruto grande costuma ser truncado ou bloqueado. Extraia só os campos que interessam (número, órgão, magistrado, data, ementa) e recorte a ementa com `.slice()` quando for só para triagem.

## 2. Parâmetros da busca

Todos vão na query string do `GET /api/search`. Nomes verbatim:

| Parâmetro | Conteúdo | Observação |
|---|---|---|
| `core` | base pesquisada | obrigatório. Valores na seção 3 |
| `q` | consulta | aceita sintaxe Solr (seção 4) |
| `page` | página, 1-based | |
| `per_page` | itens por página | a interface oferece 10/20/50/100; a API aceita 200 sem reclamar |
| `sort` | ordenação | ex.: `dt_juntada desc`, `dt_juntada asc`, `nr_processo asc`, `nr_processo desc`. Omitir = relevância |
| `dataIni` | data inicial | formato `AAAA-MM-DD` |
| `dataFim` | data final | formato `AAAA-MM-DD` |
| `jurisdicao` | jurisdição | `Tribunal de Justiça` ou `Turma Recursal` (só nas bases PJe de 2º grau) |
| `orgao_julgador` | órgão julgador | valor literal, ex.: `3ª Câmara Cível`, `Turma Recursal - 5ª Turma` |
| `magistrado` | relator | nome completo em caixa alta, como no cadastro |
| `classe_judicial` | classe | ex.: `APELAÇÃO CÍVEL`, `RECURSO INOMINADO CÍVEL` |
| `lista_assunto` | assunto | ex.: `Indenização por Dano Moral` |

A resposta traz `core_used`, `docs`, `facets`, `page`, `per_page`, `total`, `total_pages`. As facetas (`facets.facet_fields`) listam os valores disponíveis de `classe_judicial`, `jurisdicao`, `lista_assunto`, `magistrado` e `orgao_julgador` para aquela consulta, com contagem.

Na interface, a caixa **"Busca Exata"** não é um parâmetro próprio: ela simplesmente envolve todo o conteúdo digitado em aspas antes de mandar para `q`. Ou seja, marcar essa caixa com uma consulta que já usa `AND` ou prefixo de campo destrói a consulta.

## 3. As cinco bases (cores) e seus campos

| Aba na interface | `core` | Volume | Cobertura | Campo de texto |
|---|---|---|---|---|
| 1º Grau PJe | `pje1g` | ~1.513.000 | sentenças de 1º grau, inclusive Juizados Especiais | `inteiro_teor`, `inteiro_teor_html` |
| 2º Grau PJe | `pje2g` | ~219.900 | acórdãos colegiados: 141.378 do Tribunal de Justiça (desde 2020) e 78.488 de Turma Recursal (desde 2018) | `ementa`, `ementa_html`, `acordao`, `acordao_html` |
| 2º Grau Monocrático PJe | `pje2g_mono` | ~97.200 | decisões monocráticas de desembargador e de relator de Turma Recursal | `inteiro_teor`, `inteiro_teor_html` |
| 2º Grau - Físicos | `legado` | ~38.500 (amostra por termo) | acórdãos de processos físicos, julgados de 1997 a agosto/2023 | `conteudo_decisao_html`, `conteudo_decisao_completa_html`, `conteudo_dispositivo_decisao_html` |
| Turmas Recursais - Projudi | `turma_recursal_legado` | ~45.300 (amostra por termo) | Turmas Recursais no Projudi, de 2011 a agosto/2023 | `cont_ementa` |

Campos de identificação por base:

- `pje2g` e `pje2g_mono`: `nr_processo`, `classe_judicial`, `classe_judicial_sigla`, `magistrado`, `cargo_julgador`, `orgao_julgador`, `jurisdicao`, `competencia`, `localizacao`, `assunto_principal`, `lista_assunto`, `dt_juntada`, `id`, `id_bin`.
- `pje1g`: igual, trocando `jurisdicao` por `comarca`.
- `legado`: `numero_processo_legado`, `nome_desembargador`, `orgao_julgador`, `orgao_origem`, `data_julgamento`, `data_publicacao`, `codigo_recurso`, `codigo_sessao`.
- `turma_recursal_legado`: `num_processo`, `classe_processo`, `nome_juiz`, `orgao_julgador`, `data_julgamento`, `cont_ementa`, `tipo_arquivo`.

**Sobre datas.** As bases PJe expõem apenas `dt_juntada` (data de juntada do documento aos autos, em ISO 8601 com fuso). A interface rotula essa coluna como "Julg.", mas não é necessariamente a data da sessão de julgamento. Só as bases legadas têm `data_julgamento` e `data_publicacao` de verdade. Ao citar acórdão das bases PJe, procure a data da sessão no corpo do documento; se não constar, cite a data do sistema identificando-a como data de juntada.

Nas bases legadas, `jurisdicao`, `orgao_julgador`, `classe_judicial`, `lista_assunto` e `sort=dt_juntada` não se aplicam: o esquema é outro, e a interface esconde esses filtros quando essas abas estão ativas. Ordenação nelas usa `data_julgamento asc|desc`. Consultas com `q=*:*` também não funcionam nessas duas bases.

## 4. Sintaxe de consulta

O `q` é repassado ao motor de busca (Solr) praticamente sem tratamento, o que dá muito controle. Verificado na base `pje2g`:

| Consulta | Resultados | Leitura |
|---|---|---|
| `golpe pix` | 7.547 | termos soltos = OU |
| `golpe AND pix` | 1.394 | conjunção explícita |
| `+golpe +pix` | 1.394 | equivalente |
| `"golpe pix"` | 11 | frase literal |
| `culpa exclusiva da vítima` | 73.110 | OU entre quatro palavras |
| `"culpa exclusiva da vítima"` | 3.882 | frase, em qualquer parte do documento |
| `ementa:"culpa exclusiva da vítima"` | 943 | frase, só na ementa |
| `ementa:("culpa exclusiva da vítima" AND pix)` | 111 | agrupamento por campo |
| `ementa:"engenharia social"` | 128 | contra 684 no texto integral |
| `nr_processo:"5012965-16.2025.8.08.0012"` | 1 | localiza um documento específico |

Também funcionam `OR`, parênteses, `NOT` e curinga `*` (`consign*`). As próprias dicas da interface confirmam aspas, `AND`/`OR` e `*`.

Prefixo de campo só vale se o campo existir naquela base: `ementa:` na base `pje2g_mono` não filtra nada (lá o texto está em `inteiro_teor`) e devolve dezenas de milhares de resultados, dando falsa impressão de busca ampla.

Consultas que rendem em causa bancária e de consumo, para adaptar:

```
ementa:("engenharia social" AND ("culpa exclusiva" OR "fortuito externo"))
ementa:("golpe do falso funcionário" AND pix)
ementa:("instituição de pagamento" AND ilegitimidade)
ementa:("empréstimo consignado" AND ("biometria" OR "dispositivo previamente habilitado"))
ementa:("bloqueio" AND ("prevenção à fraude" OR "exercício regular de direito"))
ementa:("mero aborrecimento" AND "dano moral")
ementa:("repetição de indébito" AND "engano justificável")
```

## 5. Filtros disponíveis e seus valores

Valores lidos das facetas da base 2º Grau PJe (a contagem oscila conforme a base atualiza):

- **Jurisdição**: `Tribunal de Justiça`, `Turma Recursal`.
- **Órgão julgador (Tribunal)**: 1ª e 2ª Câmara Criminal; 1ª, 2ª, 3ª e 4ª Câmara Cível; Câmaras Criminais Reunidas; Câmaras Cíveis Reunidas; Reunidas 1º Grupo Criminal; Reunidas 1º e 2º Grupo Cível; Tribunal Pleno.
- **Órgão julgador (Juizados)**: `Turma Recursal - 1ª Turma` a `Turma Recursal - 5ª Turma`; `Plenário do Colégio Recursal`; `Turma de Uniformização de Lei`.
- **Classe judicial** (as mais usadas): `APELAÇÃO CÍVEL`, `RECURSO INOMINADO CÍVEL` (também aparece como `Recurso Inominado Cível`), `AGRAVO DE INSTRUMENTO`, `REMESSA NECESSÁRIA CÍVEL`, `MANDADO DE SEGURANÇA CÍVEL`, `PEDIDO DE UNIFORMIZAÇÃO DE INTERPRETAÇÃO DE LEI CÍVEL`, `TUTELA CAUTELAR ANTECEDENTE`, `PROCEDIMENTO COMUM CÍVEL`.
- **Lista de assuntos** (bancário e consumo): `Indenização por Dano Moral`, `Indenização por Dano Material`, `Contratos Bancários`, `Bancários`, `Empréstimo consignado`, `Cartão de Crédito`, `Práticas Abusivas`, `Repetição de indébito`, `Inclusão Indevida em Cadastro de Inadimplentes`, `Cédula de Crédito Bancário`, `Interpretação / Revisão de Contrato`.

A duplicidade de classes em caixa alta e caixa mista vem de cadastros distintos (PJe antigo e novo) e o filtro é literal: escolher só uma das grafias descarta metade do acervo. Em caso de dúvida, deixe a classe em "Todos" e restrinja pela consulta.

## 6. Ler os resultados e abrir o inteiro teor

Na interface, cada linha da tabela traz Processo, Classe Judicial, Magistrado, Órgão Julgador, Data e a coluna "Ações". O botão de olho abre um modal com o documento renderizado e dois botões, "Baixar PDF" e "Baixar DOCX", gerados no próprio navegador.

**Não existe link permanente por acórdão.** Não há âncora com URL para o documento, nem rota de deep link na SPA: o estado da busca vive só na memória da página. Para reencontrar um julgado, busque pelo número: `nr_processo:"5012965-16.2025.8.08.0012"` (bases PJe). Nas bases legadas os campos são `numero_processo_legado` e `num_processo`.

O texto devolvido pela API vem com muitos espaços e quebras de linha excedentes, principalmente nas ementas em padrão CNJ. Normalize espaçamento ao transcrever, sem alterar palavras. Os rótulos iniciais variam ("Ementa:", "EMENTA:", "Ementa."); remova o rótulo e transcreva o corpo.

## 7. Armadilhas

- **Aba padrão errada.** A interface abre com "2º Grau Monocrático PJe" selecionada. Quem digita a consulta e clica em Buscar sem olhar acaba pesquisando decisões monocráticas achando que está em acórdãos.
- **Trocar de aba limpa os filtros.** Escolha a base primeiro, depois preencha jurisdição, classe, datas e ordenação.
- **"Busca Exata" quebra consulta estruturada**, porque envolve tudo em aspas.
- **Termos sem operador viram OU** e devolvem resultado inflado que parece rico e não é.
- **`ementa:` só existe na base 2º Grau PJe.**
- **403 fora do navegador.** Não perca tempo com WebFetch ou curl.
- **Câmaras e Turmas Recursais moram na mesma base.** Sem filtrar `jurisdicao`, um resultado "do TJES" pode ser de Juizado, e a citação sai com a unidade errada. Duas passadas resolvem.
- **Data exibida é de juntada**, não necessariamente de julgamento, nas bases PJe.
- **Bases legadas param em agosto de 2023.** Para tese atual elas não servem; para tese antiga ou histórico de entendimento, servem e trazem data de julgamento e de publicação reais.
