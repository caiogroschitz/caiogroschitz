---
name: jurisprudencia-trt2
description: Busca jurisprudência trabalhista do TRT da 2ª Região a partir da última peça da conversa (contestação, recurso ordinário, contrarrazões, agravo de petição) ou de um tema informado. Identifica a favor de quem a peça argumenta e procura acórdãos REAIS e favoráveis no FALCÃO (jurisprudencia.jt.jus.br, sem CAPTCHA) e, quando pedido, no sistema nativo do TRT2, complementando com Súmulas, Teses Jurídicas Prevalecentes, IRDR e IAC do TRT2 e com Súmulas e OJs do TST. Devolve cada julgado com citação no padrão CNJ, ementa transcrita ipsis litteris e link do inteiro teor, prontos para colar na peça. Use SEMPRE que o usuário pedir "busca jurisprudência no TRT2", "julgados trabalhistas de São Paulo", "precedentes do TRT da 2ª Região", "acórdãos das Turmas do TRT2", "jurisprudência pra essa reclamação trabalhista", "súmula do TRT2 sobre isso" ou, depois de redigir ou colar uma peça trabalhista, "agora busca jurisprudência". NÃO use para redigir a peça em si, para cálculo de liquidação nem para jurisprudência cível.
---

# Jurisprudência TRT2 favorável à tese da peça

## Objetivo

A partir da última peça trabalhista da conversa (ou de um tema que o usuário indicar), encontrar acórdãos reais do TRT da 2ª Região que sustentem as teses da peça e entregá-los prontos para citação: identificação completa no padrão CNJ, ementa transcrita literalmente e link do inteiro teor. Depois, reforçar com o direito sumulado, que pesa mais que acórdão isolado: Súmulas, Teses Jurídicas Prevalecentes, IRDR e IAC do próprio TRT2, e Súmulas e OJs do TST.

A ideia que organiza toda a busca é simples: **o tema mora na ementa, o resultado mora no dispositivo**. Julgado útil é o que decide a favor, não o que menciona o assunto, e é a leitura do resultado que separa um do outro. O sistema nativo do TRT2 tem um campo dedicado ao dispositivo, o que quase nenhum buscador de tribunal oferece; o FALCÃO não tem, mas roda sem CAPTCHA e cobre TRT2 e TST. A escolha entre os dois está na seção seguinte.

## REGRA DE OURO — integridade

Isto é inegociável, porque uma citação inventada destrói a peça e a credibilidade de quem assina:

- Só cite acórdãos que você efetivamente localizou e abriu NESTA sessão. **Nunca invente, complete de memória ou "reconstrua" número de processo, relator, turma, data ou texto de ementa.** Números CNJ têm dígito verificador; um número plausível é quase sempre um número errado.
- A ementa citada é transcrição literal. Cortes são permitidos e sinalizados com "(...)"; alterações, não. Atenção à armadilha silenciosa: **a lista de resultados do TRT2 exibe toda ementa em caixa alta por CSS**. A caixa fiel está na janela "Ementa" e no inteiro teor. Transcrever da lista deturpa o texto.
- Confirme a direção do julgado antes de citar. Não basta o dispositivo: `"dar provimento"` casa também com "dar provimento parcial", e em temas como intervalo intrajornada quase todo acórdão é parcial. Leia o item da ementa correspondente à **sua** tese, não o resultado global. Do mesmo modo, um acórdão cujo resultado favorece a reclamada mas cuja ementa é redigida em tom pró-empregado não serve para colar na peça: o texto citado trabalha contra quem cita.
- Súmula, OJ e tese prevalecente se conferem na fonte oficial, com número e texto em vigor. Há enunciados cancelados e convertidos (a Súmula 437 do TST, sobre intervalo intrajornada, foi cancelada pela Res. 225/2025 por perda de eficácia desde 11.11.2017). Citar enunciado revogado como vigente é erro grave.
- Se a busca falhar de verdade (site fora do ar em ambas as rotas, navegador não conectado, zero resultados reais), diga isso ao usuário e pare. Não preencha o buraco com "jurisprudência de conhecimento geral".

## Qual motor usar, e por que o CAPTCHA não entra no fluxo

**O motor padrão é o FALCÃO** (`https://jurisprudencia.jt.jus.br`, busca nacional da Justiça do Trabalho, mantida pelo CSJT), que indexa os acórdãos do TRT2 com filtro por tribunal e por Turma, mais as súmulas e precedentes qualificados de todos os regionais e do TST. Sem CAPTCHA, sem login. Comece por ele, sempre, sem passar pelo sistema nativo antes.

O sistema nativo do TRT2 é mais preciso (é o único que pesquisa no dispositivo), mas exige um desafio de caracteres da Resolução CSJT 139/2014, e **você não resolve CAPTCHA, em nenhuma hipótese, nem quando o usuário pede**. Em medição real de julho de 2026, o desafio apareceu em todas as tentativas, inclusive depois de cancelar e reacionar. Insistir nele queima tempo e tokens para chegar ao mesmo lugar.

Portanto, a regra é econômica e sem laço:

- Use o sistema nativo **apenas** quando o usuário pedir a passada de precisão, ou quando o FALCÃO tiver falhado em entregar material suficiente e o usuário estiver presente para destravar.
- Nesse caso, **uma tentativa, só**. Se o desafio aparecer, cancele, registre e volte ao FALCÃO. Não reacione, não abra outra aba, não troque de navegador, não fique tentando.
- Nunca pare o trabalho para pedir CAPTCHA ao usuário. Se a passada de precisão fizer diferença para o caso, mencione isso em uma linha no fechamento, como oferta, depois de já ter entregue o resultado.

Quando a sessão do navegador estiver validada (porque o usuário resolveu o desafio por conta própria em algum momento), a validação vale para toda a sessão, inclusive abas novas, e o sistema nativo roda livremente. Aproveite se for o caso, mas não conte com isso.

## Passo 1 — A favor de quem, e quais teses

1. **A favor de quem eu busco?**
   - Há peça na conversa: deduza dela e declare em uma linha de que lado entendeu que está buscando, para o usuário poder corrigir de imediato. Não pergunte.
   - Só há tema, mas o enunciado da tese já é unidirecional (quem invoca o art. 71, § 4º pós-reforma quer reduzir condenação; quem pede reconhecimento de vínculo é o reclamante): declare a hipótese com todas as letras e siga. Uma frase de confirmação basta.
   - Só há tema e ele serve genuinamente aos dois polos ("horas extras", "justa causa", "dano moral"): aí sim pergunte antes de buscar, porque busca feita para o lado errado é trabalho inteiro perdido.
2. **Quais teses precisam de reforço?** Extraia de 2 a 4 teses centrais. Cada tese vira uma ou duas buscas próprias; não busque a peça inteira de uma vez. O vocabulário de cada família de tese, com enunciados e temas correspondentes, está em `references/vocabulario-trabalhista.md`. Leia esse arquivo antes de montar os termos: é ele que evita busca genérica.

## Passo 2 — Traduzir a tese em termos de busca

A lógica é a mesma nos dois motores: **o tema mora na ementa, o resultado mora no dispositivo**. O que muda é o instrumento. No FALCÃO existe uma caixa única com conectores escritos e um botão para restringir à ementa; no sistema nativo do TRT2 existem cinco campos separados, um deles dedicado ao dispositivo.

- **Tema.** Uma ou duas expressões entre aspas, no vocabulário que um desembargador usa no cabeçalho da ementa: `"intervalo intrajornada"`, `"justa causa" "abandono de emprego"`, `"responsabilidade subsidiária"`, `"adicional de insalubridade"`.
- **Resultado.** `"negar provimento"`, `"nego provimento"`, `"não provido"` quando se quer manter improcedência ou derrubar o recurso adversário; `"dar provimento"`, `"reformar a sentença"` quando se quer reformar.
- **Quando o tribunal está dividido, o marcador de corrente rende mais que o de resultado.** Em temas fraturados (vínculo em plataforma digital, limitação aos valores da inicial), buscar por `"dar provimento"` traz pouco e mal: numa execução de teste devolveu três resultados e nenhum aproveitável. O que separa as correntes é a expressão doutrinária que cada uma usa (`"subordinação algorítmica"`, `"subordinação estrutural"` de um lado; `"autonomia na prestação"`, `"ausência de subordinação"` do outro). Nesses casos, largue o marcador de resultado e trabalhe pelo vocabulário da corrente.
- **Exclusões** limpam o ruído clássico: buscando motorista de plataforma, exclua `"entregador"`, e vice-versa.
- Três a cinco expressões no total. Mais que isso zera; menos traz milhares e nada específico.

Se a primeira passada vier vazia, afrouxe na ordem inversa: tire o marcador de resultado, reduza o tema a uma expressão, amplie o período. Se vier volumosa demais, aperte pelo resultado e pela Turma antes de mexer no tema.

## Passo 3 — Motor padrão: FALCÃO

`https://jurisprudencia.jt.jus.br/jurisprudencia-nacional/pesquisa`. Precisa do Chrome conectado (Claude in Chrome). Se houver mais de um navegador conectado, escolha com `select_browser`, crie sua própria aba e passe `tabId` explícito; não trave por isso. Navegação para domínio novo pode falhar dentro de `browser_batch`: faça o `navigate` isolado.

1. Digite a consulta na caixa única, com aspas para expressão exata e os conectores escritos entre os termos: `"intervalo intrajornada" e "natureza indenizatória"`. Confira no painel lateral a consulta interpretada, que o próprio sistema exibe no formato `ACORDAOS E "INTERVALO INTRAJORNADA" E "NATUREZA INDENIZATÓRIA"`. É a forma barata de descobrir que ele entendeu outra coisa.
2. Na coluna de filtros, selecione **Coleção → Acórdãos** e **Tribunal → TRT2**. Sem o filtro de tribunal você recebe a Justiça do Trabalho inteira. Para súmulas e precedentes qualificados, use **Coleção → Precedentes** com o mesmo filtro de tribunal.
3. Ligue **"Pesquisar somente nas ementas"**. É o que mais melhora a precisão, porque corta os acórdãos que só citam o tema de passagem.
4. Refine, se precisar, por **Órgão Julgador** (as Turmas do TRT2, uma a uma, com campo de filtro), Classe, Magistrado ou Ementa (com ou sem).

Cada resultado traz `TRT2 - CLASSE número`, relator, Turma, data de juntada, a ementa e os botões "Copiar Ementa", "Abrir Inteiro Teor", "Citar" e "Buscar Similares". Dois detalhes operacionais que economizam tentativas: o link permanente de um julgado segue o padrão `https://jurisprudencia.jt.jus.br/jurisprudencia-nacional/pesquisa/numero/<número CNJ>?abaSelecionada=acordaos`, e os botões de inteiro teor não têm `href` (abrem por script), de modo que capturar o endereço exige interceptar `window.open`. A receita está em `references/trt2-sistema-campos.md`.

Cuidados próprios do FALCÃO, que não são pequenos:

- **O ranqueamento é por relevância sobre base enorme e o contador é generoso.** Os primeiros resultados são bons, a cauda é ruído. O número exibido não é o tamanho de um conjunto estritamente filtrado, então não o repasse ao usuário como se fosse.
- **Não há campo de dispositivo.** A direção do julgado se confirma lendo a ementa inteira e, na dúvida, o inteiro teor.
- **A data exibida é "juntado aos autos"**, que não é data de julgamento. Cite pelo que o documento disser, e diga qual data está usando.

## Passo 4 — Passada de precisão (opcional): sistema nativo do TRT2

Só quando o usuário pedir, ou quando o FALCÃO não tiver entregue material suficiente e o usuário estiver por perto. Uma tentativa apenas, pelas razões já ditas.

Monte a URL com os filtros embutidos e abra direto, em vez de preencher campo a campo. É mais rápido e deixa a busca auditável:

```
https://pje.trt2.jus.br/jurisprudencia?filtroEEmenta=%22justa+causa%22+%22abandono+de+emprego%22&filtroEDispositivo=%22negar+provimento%22&documento=Ac%C3%B3rd%C3%A3o&dataAssinaturaInicio=01-01-2024
```

Os cinco campos de texto (`filtroE`, `filtroOu`, `filtroNao`, `filtroEEmenta`, `filtroEDispositivo`), os tipos de documento e os filtros de data estão detalhados em `references/trt2-sistema-campos.md`. `documento=Acórdão` é o padrão; `&documento=Sentença` acrescenta o primeiro grau, útil quando a peça é de Vara, com a ressalva de que sentença não vincula. As datas vão em `DD-MM-AAAA` e se referem à **assinatura** do documento, não ao julgamento.

Abrir a URL preenche o formulário, mas não dispara a busca. **Não clique em "Pesquisar" por coordenada**: nessa página o clique posicional muitas vezes só exibe o tooltip e a busca não roda, o que se manifesta como um "zero resultados" falso. Acione o botão pelo elemento, pelo `aria-label` "Fazer pesquisa pelos filtros informados". Essa receita, mais as de extrair a ementa integral e os links permanentes, estão na seção "Receitas de operação" do reference.

O que compensa nessa rota: a ementa completa na caixa original (a lista uppercaseia por CSS), a linha de identificação oficial do tribunal ao final da janela "Ementa", e o link permanente `https://pje.trt2.jus.br/jurisprudencia/<hash>`.

Abra o inteiro teor, em qualquer das rotas, sempre que a ementa vier truncada, quando o dispositivo não estiver evidente, quando a Turma usar ementa padronizada genérica (a 14ª Turma faz isso) ou quando os fatos importarem para a analogia. Vale o esforço: numa execução de teste, um acórdão com texto fortemente favorável na lista era, no inteiro teor, o **voto vencido**, e o dispositivo dizia o contrário.

**Critérios de seleção**, nesta ordem:

1. A ementa e o dispositivo efetivamente decidem a favor da tese, no ponto específico dela.
2. Caso análogo de verdade: mesma causa de pedir, mesma moldura fática, mesma categoria quando isso importa.
3. Recente, últimos dois ou três anos, e posterior à Lei 13.467/2017 quando a tese depender da reforma.
4. Pluralidade de Turmas. Dois acórdãos de Turmas diferentes valem mais que três da mesma, porque mostram entendimento do Regional, e no TRT2, com dezoito Turmas, isso importa muito. Tanto o FALCÃO quanto o sistema nativo permitem filtrar Turma a Turma para variar de propósito ou para mirar a Turma do recurso em curso.
5. Dois a três julgados por tese é o ideal. A exceção é quando a tese do usuário é a minoritária no tribunal: aí a reiteração é o argumento, e vale entregar quatro ou cinco, sinalizando quais você conferiu um a um.

## Passo 5 — Reforço normativo: o que pesa mais que acórdão

Em trabalhista o enunciado consolidado costuma decidir a tese sozinho. Depois de escolher os acórdãos, verifique se existe enunciado aplicável e cite-o **antes** deles na peça, conferindo o texto na fonte:

- **TRT2**: Súmulas, Teses Jurídicas Prevalecentes, IRDR, IAC, Orientações Jurisprudenciais, Precedentes Normativos e Incidentes de Arguição de Inconstitucionalidade em `https://ww2.trt2.jus.br/jurisprudencia/jurisprudencia/trt2-jurisprudencia-consolidada` (páginas filhas `/sumulas`, `/teses-juridicas-prevalecentes` e assim por diante). Tese prevalecente e IRDR do próprio Regional são o argumento mais forte disponível dentro do TRT2.
- **TST**: Súmulas, OJs da SDI-1, SDI-2, SDI-1 Transitória, Tribunal Pleno e Precedentes Normativos. O consultor de verbetes (`https://jurisprudencia.tst.jus.br/?tipoJuris=SUM&orgao=TST&pesquisar=1`) mostra a **situação** de cada enunciado, inclusive cancelamentos, que é justamente o que se precisa saber. O `javascript_tool` é bloqueado em `tst.jus.br` e a leitura de página inteira trunca; quando não conseguir abrir o verbete, diga ao usuário que não confirmou e não transcreva o texto como se tivesse confirmado.
- Teses vinculantes do STF e IRRs do TST que governem o tema entram aqui quando existirem.

Duas honestidades que fazem a diferença e que o usuário não consegue obter sozinho rapidamente:

- **Enunciado contrário**: se houver súmula, OJ ou tese prevalecente contra a tese da peça, diga com todas as letras e ofereça o caminho de distinção. Descobrir a súmula adversa antes do juiz é serviço.
- **Corrente majoritária contrária**: se a leitura dos resultados mostrar que o entendimento dominante do próprio TRT2 é contrário (por exemplo, 18 dos 20 acórdãos mais recentes negam a tese), registre isso antes das ementas. É informação tão decisiva quanto a súmula adversa, e muda a estratégia recursal.

## Passo 6 — Entregar as ementas no formato correto

Para cada tese, entregue no chat, em Markdown, prosa natural, sem travessão decorativo e sem cara de IA:

**a) Linha de citação no padrão CNJ** (Recomendação 154/2024, art. 3º, § 2º: tribunal, classe, número, relator, unidade julgadora, data):

> TRT da 2ª Região, Recurso Ordinário nº 1000364-03.2025.5.02.0614, Rel. Des. Fulano de Tal, 19ª Turma, j. 24.07.2026.

Quando o resultado não trouxer a sigla da classe, cite como "Processo nº ..." em vez de inventar a classe. Quando a data importar, use a nomenclatura do tribunal ("data de assinatura") ou reproduza a linha de identificação oficial que aparece ao final da janela "Ementa". Para enunciados: `Súmula nº X do TRT da 2ª Região`, `Tese Jurídica Prevalecente nº X do TRT da 2ª Região`, `Súmula nº 331, IV, do TST`, `OJ nº 191 da SDI-1 do TST`.

**b) Ementa transcrita**, bloco literal, na caixa e pontuação do original (da janela "Ementa" ou do inteiro teor, nunca da lista), com cortes sinalizados por "(...)" quando longa. É esse bloco que o usuário cola na peça.

**c) Por que serve**, uma ou duas frases ligando o julgado ao trecho ou à tese específica da peça.

**d) Link** do inteiro teor.

Sinalize sempre o que não foi individualmente conferido, se houver. Ao final, se o usuário pedir a ementa "como tem que ser" para minutar (uma ementa nova, um memorial, uma síntese estruturada), redija-a na estrutura da ementa-padrão do CNJ descrita em `references/ementa-padrao-cnj.md`. Leia esse arquivo antes de redigir. Ao apenas TRANSCREVER a ementa de um acórdão real, mantenha o texto original do tribunal.

## Fechamento

Ofereça, em uma linha, o próximo passo: ampliar a busca (mais teses, outro período, outras Turmas, sentenças de 1º grau, TST) ou inserir os julgados selecionados diretamente na peça. Se você tiver entregue pelo FALCÃO por causa do desafio de caracteres, é aqui que se menciona, em uma linha, a possibilidade da passada de precisão no sistema nativo.
