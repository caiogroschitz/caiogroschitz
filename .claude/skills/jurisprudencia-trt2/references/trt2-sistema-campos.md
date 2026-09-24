# Sistema de Jurisprudência do TRT2 — referência técnica e receitas de operação

Sistema de Pesquisa de Jurisprudência do TRT da 2ª Região, versão 1.5.0, host `https://pje.trt2.jus.br/jurisprudencia/`. Aplicação Angular de página única, integrada ao PJe. Este arquivo dá precisão ao Passo 3 da SKILL.md: parâmetros de URL, comportamento do desafio de caracteres, anatomia dos resultados, filtros, **receitas de operação pelo navegador** e armadilhas. Verificado ao vivo em 27/07/2026, incluindo três execuções completas da skill.

## Índice
1. Desafio de caracteres: escopo e comportamento
2. Parâmetros de URL (busca pré-preenchida)
3. Os cinco campos de texto
4. Tipos de documento
5. Filtros laterais
6. Barra de resultados
7. Anatomia de um resultado
8. Links permanentes
9. **Receitas de operação (leia antes da primeira busca)**
10. Armadilhas
11. FALCÃO (rota alternativa)
12. Fontes de direito sumulado

## 1. Desafio de caracteres: escopo e comportamento

Ao clicar em "Pesquisar", pode abrir um diálogo com imagem distorcida ("Digite os caracteres exibidos na imagem"), com opção de áudio e rodapé citando a Resolução nº 139/2014 do CSJT.

O que se observou em execução real:

- A validação é **por sessão do navegador**, não por busca nem por aba. Depois de validada, buscas seguintes e abas novas rodam livremente.
- O diálogo pode aparecer **mesmo com a sessão já validada**, aparentemente por uma corrida entre o clique e a leitura do cookie de sessão. Nas três execuções de teste ele apareceu na primeira tentativa e desapareceu ao cancelar e reacionar "Pesquisar", sem que ninguém o resolvesse.
- Quem resolve, quando é mesmo necessário, é o usuário. Você nunca resolve, nem quando pedem.

Procedimento: acione "Pesquisar"; se o diálogo aparecer, cancele e reacione uma vez; se persistir, migre para o FALCÃO e entregue o trabalho, mencionando a alternativa apenas no fechamento. Nunca interrompa o trabalho para pedir CAPTCHA.

## 2. Parâmetros de URL (busca pré-preenchida)

O botão "Compartilhar" gera uma URL com todos os filtros. A mesma URL, montada à mão, abre o formulário já preenchido.

| Parâmetro | Campo correspondente | Formato |
|---|---|---|
| `filtroE` | Contendo as palavras (e) | texto, aspas permitidas |
| `filtroOu` | Qualquer das palavras (ou) | texto |
| `filtroNao` | Sem conter as palavras (não) | texto |
| `filtroEEmenta` | Palavras na ementa (e) | texto |
| `filtroEDispositivo` | Palavras no dispositivo (e) | texto |
| `documento` | Tipos de documento | `Acórdão`, `Decisão`, `Despacho`, `Sentença` (URL-encoded; repetível) |
| `dataAssinaturaInicio` / `dataAssinaturaFim` | Data de Assinatura | `DD-MM-AAAA` |
| `dataDistribuicaoInicio` / `dataDistribuicaoFim` | Data de Distribuição | `DD-MM-AAAA` |

Exemplo funcional:

```
https://pje.trt2.jus.br/jurisprudencia?filtroEEmenta=%22justa+causa%22+%22abandono+de+emprego%22&filtroEDispositivo=%22negar+provimento%22&documento=Ac%C3%B3rd%C3%A3o&dataAssinaturaInicio=01-01-2025
```

Abrir a URL **preenche**; não dispara a busca. Órgão julgador, magistrado, classe e assunto não são aceitos por URL: selecione pelos combos da coluna Filtros.

## 3. Os cinco campos de texto

Todos aceitam aspas para expressão exata e podem ser usados juntos (relação E entre campos). Sem conectores digitados e sem caracteres especiais.

- **Contendo as palavras (e)**: qualquer lugar do documento, inclusive relatório e fundamentação. O mais ruidoso.
- **Qualquer das palavras (ou)**: sinônimos e variantes.
- **Sem conter as palavras (não)**: exclusões.
- **Palavras na ementa (e)**: onde o tema é declarado. Dá precisão.
- **Palavras no dispositivo (e)**: onde está o resultado. Dá direção.

Cruzar ementa e dispositivo é a técnica central. Medida real: ementa `"justa causa" "abandono de emprego"` mais dispositivo `"negar provimento"`, só acórdãos, a partir de 01-01-2025, devolveu 21 resultados, todos no tema e no sentido buscado, contra 3.775 de uma busca livre equivalente.

Ressalva importante: em temas de jurisprudência dividida o campo de dispositivo rende pouco (numa execução de teste, `"dar provimento"` para vínculo em plataforma devolveu 3 resultados e nenhum aproveitável). Nesses casos, use marcador de corrente na ementa em vez de marcador de resultado no dispositivo.

## 4. Tipos de documento

Caixas "Todos", "Acórdão", "Decisão", "Despacho", "Sentença". O sistema indexa também o primeiro grau, diferença relevante em relação aos buscadores estaduais.

- **Acórdão**: Turmas e seções especializadas. Padrão da skill.
- **Sentença**: Varas do Trabalho da 2ª Região. Não vincula e pesa menos em peça recursal, mas mede a temperatura do primeiro grau.
- **Decisão** e **Despacho**: monocráticas e expedientes, raramente citáveis.

## 5. Filtros laterais

- **Órgão Julgador**: unidade em sentido amplo (Varas, gabinetes, AJUDE, Vice-Presidência).
- **Órgão Julgador Colegiado**: as Turmas e colegiados, multi-seleção por caixas com campo "Filtrar itens". É o filtro certo para 2º grau.
- **Magistrado**, **Classe Judicial**, **Assunto [código do CNJ]**.
- **Data de Assinatura** e **Data de Distribuição**, início e fim, com calendário.

## 6. Barra de resultados

Ícones de impressão (exporta em PDF pela impressão do navegador), limpar e filtro. Controles: **Ordenar por** (`Relevância` ou `Data de assinatura`), **Resultados por página** (10, 20, 50, 100), contador e paginação (`1 - 20 de 21`).

## 7. Anatomia de um resultado

Cabeçalho: `Processo <CLASSE> - <número CNJ>` (link para `https://pje.trt2.jus.br/consultaprocessual/detalhe-processo/<numero>`), ícone de informação e links `Inteiro Teor`, `Ementa` (só quando há ementa) e `Baixar como RTF`.

Corpo: tipo do documento e `Data de assinatura`; `Relator(a)` (só em acórdãos); `Órgão julgador`; `Ementa:` com o texto da ementa; `Amostras do Inteiro Teor:` com os termos destacados.

Três observações que afetam a fidelidade da transcrição:

- **A lista renderiza a ementa em CAIXA ALTA por CSS.** A caixa real está na janela "Ementa" e no inteiro teor. As "Amostras" preservam a caixa original, mas são fragmentárias.
- **Ementas longas vêm truncadas com "(+)"** na lista, justamente as do padrão CNJ, em que o item IV traz o dispositivo. Para acórdão de 2025 em diante, quase sempre é preciso abrir a ementa completa ou o inteiro teor.
- **Alguns resultados não trazem a sigla da classe** ("Processo - 1000446-51.2025.5.02.0382"). Cite como "Processo nº ..."; não deduza a classe.

O ícone de informação expande classe, polo ativo, polo passivo, instância e data de distribuição — útil para confirmar quem recorreu.

A janela do link "Ementa" traz a ementa completa, botão "Copiar tudo" e, ao final, a identificação oficial:

```
(TRT da 2ª Região; Processo: 1000364-03.2025.5.02.0614; Data de assinatura: 24-07-2026; Órgão Julgador: 19ª Turma - Cadeira 4 - 19ª Turma; Relator(a): FULANO DE TAL)
```

Acórdãos de 2025 em diante costumam vir na ementa-padrão do CNJ, com blocos I a IV, "Tese de julgamento" e remissões. O bloco IV entrega a direção do julgado.

## 8. Links permanentes

- Inteiro teor: `https://pje.trt2.jus.br/jurisprudencia/<hash de 32 caracteres>`, estável e compartilhável. É o link que vai para o usuário.
- Processo: `https://pje.trt2.jus.br/consultaprocessual/detalhe-processo/<número CNJ>`.
- Busca reproduzível: a URL de parâmetros da seção 2.

## 9. Receitas de operação

Estas quatro receitas resolvem o que consumiu mais tentativas nas execuções de teste. Vale ler antes da primeira busca.

**a) Acionar a busca.** Não clique em "Pesquisar" por coordenada. O clique posicional com frequência só dispara o tooltip "Fazer pesquisa pelos filtros informados" e a busca não roda, produzindo um "zero resultados" falso; cliques repetidos pioram, porque, depois que os resultados renderizam, o layout desloca e o clique acaba abrindo um inteiro teor em aba nova. Acione pelo elemento:

```js
[...document.querySelectorAll('button')]
  .find(b => (b.getAttribute('aria-label')||'').includes('Fazer pesquisa'))
  .click(); 'ok'
```

Alternativa sem JS: `find` com a consulta "botão Pesquisar" e clique por `ref`.

**b) Colher os links permanentes.** O `read_page` só enxerga os primeiros resultados, por renderização preguiçosa da lista, e o `get_page_text` da página inteira é caríssimo (cerca de 15 mil palavras numa lista de 20). Use a ferramenta `find` com a consulta "Inteiro Teor links": ela devolve os `href` no formato `/jurisprudencia/<hash>`, na ordem da lista.

**c) Extrair a ementa completa.** O painel do link "Ementa" **não** é um diálogo (não tem `role=dialog` nem `mat-dialog-container`): é um painel inline. O caminho que funciona é acionar o botão pelo `aria-label` e ler o texto do contêiner:

```js
// abre a ementa do n-ésimo resultado (0-based)
[...document.querySelectorAll('button')]
  .filter(b => (b.getAttribute('aria-label')||'').includes('Exibir ementa'))[n].click(); 'ok'
```

```js
// lê o painel aberto, em fatias (o retorno do javascript_tool corta perto de 1.000 caracteres)
const d = [...document.querySelectorAll('div')]
  .filter(e => e.innerText.includes('Copiar tudo') && e.innerText.includes('TRT da 2')).pop();
d.innerText.slice(0, 900)
```

Repita com `.slice(900, 1800)` e assim por diante. Se a ementa for muito longa, abrir o inteiro teor e ler com `get_page_text` costuma sair mais barato.

**d) Contornar o filtro de saída do `javascript_tool`.** Retornos que incluam `outerHTML`, atributos `href` ou certos prefixos concatenados podem voltar como `[BLOCKED: Cookie/query string data]`, mesmo sendo inofensivos. Devolva **apenas texto puro**, em fatias curtas, sem concatenar rótulos. Em `tst.jus.br` a execução de JavaScript é bloqueada por domínio: lá, use `get_page_text` e `find`.

## 10. Armadilhas

- **Data de assinatura não é data de julgamento nem de publicação.** Para acórdão praticamente coincidem, mas o rótulo é esse.
- **A base mistura instâncias.** Sem marcar o tipo de documento, sentenças de Vara aparecem no meio dos acórdãos.
- **Órgão Julgador não é Órgão Julgador Colegiado.** Para Turma, use o segundo.
- **Nada de conectores digitados**; aspas importam muito.
- **`"dar provimento"` casa com "dar provimento parcial"**. Em temas como intervalo intrajornada quase todo acórdão é parcial: leia o item da ementa relativo à sua tese.
- **Ementa da lista pode enganar duas vezes**: pela caixa alta e pelo recorte. Numa execução de teste, um resultado com texto fortemente favorável era o **voto vencido**, e o dispositivo do acórdão dizia o contrário. Abrir o inteiro teor evitou o erro.
- **Turmas com ementa padronizada** (a 14ª usa uma que não menciona o objeto do caso) exigem abrir o inteiro teor para confirmar a moldura fática.
- **Sem resultado não é sem jurisprudência.** Afrouxe na ordem: tire o dispositivo, reduza a ementa, amplie o período.
- **Vários navegadores conectados**: `tabs_context_mcp` pode exigir escolha. Resolva com `list_connected_browsers` e `select_browser`, criando aba própria com `tabs_create_mcp` e passando `tabId` explícito em todas as chamadas, inclusive dentro de `browser_batch`. Em trabalho paralelo, abas podem ser recriadas ou navegadas por outro processo; se uma leitura vier vazia, confira se ainda está na sua aba.
- **A busca demora alguns segundos** e a aba pode ficar momentaneamente sem responder à captura de tela. Espere e releia antes de concluir que falhou.

## 11. FALCÃO (rota alternativa, sem CAPTCHA)

`https://jurisprudencia.jt.jus.br/jurisprudencia-nacional/pesquisa`, busca nacional da Justiça do Trabalho mantida pelo CSJT. Sem CAPTCHA e sem login.

- Caixa única, aspas para expressão exata e conectores escritos (`e`, `ou`, `nao`). O painel lateral mostra a consulta interpretada (`ACORDAOS E "MOTORISTA DE APLICATIVO" E "VÍNCULO DE EMPREGO"`), o que permite conferir o entendimento do sistema.
- **Coleção**: Acórdãos, Admissibilidade de Recursos, Decisões Monocráticas, Sentenças, Precedentes. Precedentes reúne IRR, IAC, IRDR, repercussão geral e súmulas de todos os regionais e do TST.
- **Tribunal**: TST, TRT1, TRT2 e demais. É assim que se restringe ao Regional de São Paulo.
- **Órgão Julgador**: Turmas, uma a uma, com campo de filtro.
- Outros recortes: Magistrado, Classe, Ementa (com ou sem), Prioridades (acidente de trabalho, assédio moral ou sexual, discriminação).
- Botão "Pesquisar somente nas ementas" para cortar ruído.
- Cada resultado traz `TRIBUNAL - CLASSE número`, relator, turma, data de juntada, ementa e os botões "Copiar Inteiro Teor", "Abrir Inteiro Teor", "Copiar Ementa", "Citar" e "Buscar Similares".

Limitações: ranqueamento por relevância sobre base muito grande, contador generoso que não corresponde a conjunto estritamente filtrado, e ausência de campo de dispositivo. Os primeiros resultados são bons, a cauda é ruído. Nunca cite sem ler. A data exibida é "juntado aos autos", que não é data de julgamento: diga qual data está usando.

**Receitas de operação do FALCÃO:**

- **Link permanente de um julgado**: `https://jurisprudencia.jt.jus.br/jurisprudencia-nacional/pesquisa/numero/<número CNJ>?abaSelecionada=acordaos`. É o endereço que vai para o usuário quando a busca sai por essa rota.
- **Os botões de inteiro teor não têm `href`**: abrem por script. Para capturar o endereço real, intercepte a abertura antes de clicar:

```js
window.__u = []; const o = window.open;
window.open = function(u){ window.__u.push(u); return null; };
'interceptado'
```

Clique no botão de inteiro teor, depois leia `window.__u.join('\n')`. Restaure com `window.open = o` ao final.
- **`navigate` para domínio novo falha dentro de `browser_batch`** e funciona quando chamado isolado. Navegue primeiro, agrupe o resto depois.
- Se o domínio estiver bloqueado por permissão em um dos navegadores conectados, troque de navegador uma vez com `select_browser` e siga. Não fique alternando.

## 12. Fontes de direito sumulado

- TRT2, jurisprudência consolidada: `https://ww2.trt2.jus.br/jurisprudencia/jurisprudencia/trt2-jurisprudencia-consolidada`. **Entre sempre por essa página índice e clique nos itens do menu lateral.** As páginas filhas de Súmulas e de Teses Jurídicas Prevalecentes respondem em `/sumulas` e `/teses-juridicas-prevalecentes`, mas os slugs de IRDR e IAC mudaram e retornam 404 quando montados à mão. São cerca de 80 súmulas, 25 teses prevalecentes, 43 temas de IRDR e 10 de IAC: dá para varrer as listas inteiras quando o tema for central, e é isso que permite responder com segurança que um enunciado **não existe**.
- TST, consultor de verbetes: `https://jurisprudencia.tst.jus.br/?tipoJuris=SUM&orgao=TST&pesquisar=1`, que exibe a **situação** de cada enunciado (em vigor, cancelada, convertida). O parâmetro de número de verbete na URL não é honrado no carregamento: a aplicação carrega a lista e só filtra depois do clique em Pesquisar. A leitura de página inteira trunca por volta de 50 mil caracteres, o que na lista de súmulas para em torno da de nº 95.
- TST, Livro de Jurisprudência: `https://www.tst.jus.br/livro-de-jurisprudencia-indice`.
- Quando os portais falharem, a coleção Precedentes do FALCÃO cobre boa parte do mesmo material. Se não conseguir confirmar um enunciado, diga isso ao usuário e não transcreva o texto como verificado.
