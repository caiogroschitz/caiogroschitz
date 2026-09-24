---
name: picpay-apelacao
description: >-
  Redige o RECURSO DE APELAÇÃO (art. 1.009 do CPC) na ótica do RÉU/APELANTE,
  padrão PicPay (PicPay Instituição de Pagamento, PicPay Bank, Banco Original)
  e demais clientes do escritório BFAP, contra sentença de Vara Cível que o
  condenou. Entrega a peça inteira no chat com ESPAÇOS MARCADOS para colar os
  prints do dossiê e gera o .docx já timbrado no padrão do escritório. Use
  SEMPRE que o usuário enviar autos ou peças de processo da Justiça Comum
  (sentença, inicial, contestação, dossiê, decisão de embargos) e pedir para
  "fazer a apelação", "apelar da sentença", "recorrer da sentença da vara
  cível", "elaborar o recurso de apelação", "fazer as razões de apelação" ou
  "analisa os autos e faz a apelação"; também aciona ao colar sentença de Vara
  Cível pedindo a peça de insurgência. NÃO use para recurso inominado do JEC
  (picpay-recurso-inominado), contrarrazões de apelação
  (picpay-contrarrazoes-apelacao), contestação, embargos de declaração,
  réplica ou parecer de recorribilidade (picpay-diretrizes-recursais).
---

# Recurso de Apelação — perspectiva do Apelante (PicPay e clientes BFAP)

Esta skill escreve, inteira e pronta para protocolar, a **apelação interposta pelo réu condenado** contra sentença de Vara Cível. O objetivo é a **reforma integral** (improcedência da ação) e, subsidiariamente, a minoração das condenações.

É a **irmã de segunda instância** da skill `picpay-recurso-inominado`: mesma ótica (réu inconformado), mesma arquitetura argumentativa, mesma obsessão documental. O que muda é o **rito** — Apelação do CPC na Justiça Comum, não Recurso Inominado no Juizado. As diferenças estão na tabela abaixo e valem para cada fórmula da peça.

O Apelante padrão é o **PICPAY INSTITUIÇÃO DE PAGAMENTO S.A.**, mas o escritório também apela por outros réus (PicPay Bank, Banco Original, GFG/Dafiti, sellers). **Adote como Apelante a pessoa jurídica efetivamente ré e condenada nos autos** — nunca presuma que é o PicPay se os autos disserem outra coisa.

## O que muda em relação ao recurso inominado

| Item | Inominado (JEC) | **Apelação (Justiça Comum)** |
|---|---|---|
| Endereçamento da interposição | Juizado Especial Cível | **Juiz(a) de Direito da [nª] Vara Cível da Comarca de [x] - [UF]** (juízo *a quo*) |
| Fundamento da interposição | art. 41 da Lei 9.099/95 | **art. 1.009 e ss. do CPC** |
| Prazo | 10 dias úteis (art. 42) | **15 dias úteis (art. 1.003, §5º, CPC)** |
| Preparo | art. 42, §1º, Lei 9.099/95 | **art. 1.007 do CPC** |
| Efeitos | devolutivo, salvo dano irreparável (art. 43) | **devolutivo e suspensivo como regra (arts. 1.012 e 1.013)** |
| Juízo de admissibilidade | Turma Recursal | **Tribunal *ad quem* (art. 1.010, §3º)** |
| Contrarrazões da parte adversa | 10 dias | **15 dias (art. 1.010, §1º)** |
| Vocativo das razões | Colenda Turma Recursal | **Ínclitos Desembargadores / Colenda Câmara Cível** |
| Como chamar as partes | Recorrente / Recorrido | **Apelante / Apelado (Apelada)** |
| Sucumbência | inexiste em 1º grau | **existe: custas e honorários também são atacáveis** |

## Princípio central: a peça nasce da íntegra dos autos

A força desta peça está na **fidelidade ao que está no processo**. Cada data, horário, valor, ID/E2E de transação, CNPJ, beneficiário, número de contrato, Device ID, cláusula contratual, ID de documento e o **teor exato de cada item da sentença** precisam espelhar os autos. Um dado inventado destrói a credibilidade da peça e pode configurar litigância de má-fé — em segundo grau, onde o relator lê a sentença lado a lado com o recurso, o descompasso é ainda mais visível.

Por isso, **leia toda a íntegra fornecida antes de redigir**. Não comece a escrever enquanto não dominar os fatos.

## Fluxo de trabalho

### Passo 1 — Ultra-análise dos autos

Leia cada peça e documento (inicial, contestação, dossiê, sentença, decisão dos embargos, comprovantes, extratos, contratos, telas) e extraia:

- **Endereçamento e processo:** vara cível, comarca/UF, número dos autos, nome completo do autor e razão social do réu condenado, tribunal competente (TJ do estado).
- **Da inicial:** o que o autor alegou, quais pedidos formulou e com que valores, e qual a tese fática dele (golpe Pix, transação desconhecida, empréstimo fraudulento, bloqueio de conta, redução de limite, negativação, cobrança indevida).
- **Da contestação:** preliminares e teses já deduzidas e, sobretudo, **o acervo documental** juntado (cadastro, biometria, Device ID, IDs de transação, beneficiários, Reason Code, protocolos, cláusulas dos Termos de Uso, CCB).
- **Da sentença (o alvo do recurso):** data da publicação/intimação; **cada item do dispositivo** com valor, prazo, multa, juros, correção e verba sucumbencial; e, principalmente, **quais erros o julgado cometeu** — aplicou responsabilidade objetiva de forma automática sem demonstrar defeito; inverteu o ônus da prova como fundamento autônomo; exigiu prova diabólica; aplicou súmula a hipótese estranha (479, 548, 385); desconsiderou o dossiê como "telas unilaterais"; deixou de enfrentar prova relevante (art. 489, §1º, IV, CPC); julgou *extra*, *ultra* ou *infra petita*; ignorou precedente vinculante ou jurisprudência consolidada (art. 926).
- **Dos embargos de declaração, se houve:** data, vícios suscitados e teor da rejeição. Isso muda a contagem da tempestividade (o prazo da apelação reabre da intimação da decisão dos ED) e rende o argumento de omissão não sanada.
- **Do dossiê:** liste cada print disponível — é o que vai virar espaço de prova na peça.

### Passo 2 — Confirmar o que falta ANTES de escrever

Se faltar dado essencial (data da publicação da sentença ou da decisão dos ED, valor exato de uma condenação, ID de transação, número de cláusula, OAB/UF do subscritor, câmara/tribunal), **pergunte ao usuário de forma agrupada e objetiva**. Nunca preencha por presunção. Se o usuário mandar seguir sem o dado, marque `[CONFERIR]` no ponto exato — uma lacuna sinalizada é corrigível em trinta segundos; um dado inventado passa despercebido até o acórdão.

### Passo 3 — Selecionar as teses

Escolha as teses a partir dos **erros da sentença** e do **tema do caso**. O catálogo, com quando usar, eixo argumentativo e as provas de cada tema, está em **`references/teses-apelacao.md`** — leia antes de montar o mérito.

### Passo 4 — Montar a peça

Siga o esqueleto de **`references/modelo-canonico.md`**, reaproveitando verbatim os blocos de **`references/blocos-fixos.md`** e adaptando o mérito ao caso. Para a craft da prosa (ritmo de frase, vocabulário, latim contido, firmeza sem agressividade), leia **`references/estilo-de-escrita.md`**.

A peça tem **duas partes distintas**, separadas por quebra de página:

1. **Petição de interposição**, endereçada ao **juízo *a quo*** (a Vara Cível), curta: qualificação, interposição com fulcro no art. 1.009, preparo do art. 1.007, pedido de intimação da apelada para contrarrazões em 15 dias e remessa ao Tribunal.
2. **Razões de apelação**, endereçadas ao **Tribunal**, onde mora toda a argumentação.

Confundir as duas é o erro estrutural mais comum: quem escreve as razões direto ao juiz de primeiro grau entrega uma peça que o relator lê como amadora.

### Passo 5 — Entregar

**Entregue a peça inteira no chat, em Markdown, e gere o .docx.** Nesta ordem: primeiro o texto no chat (o advogado revisa e ajusta ali mesmo), depois o arquivo.

Para o .docx, escreva a peça em um arquivo `.md` com a marcação aceita pelo script e rode:

```bash
python3 scripts/montar_docx.py --in peca.md --out "Apelacao - <nº dos autos>.docx"
```

O script despeja o texto dentro de `assets/modelo-bfap.docx`, que já carrega o timbre BFAP, o rodapé com as três unidades, as margens de 2 cm e a fonte Prompt 12 embutida. O resultado sai idêntico ao modelo do escritório, sem trabalho de formatação. A marcação está documentada no cabeçalho do próprio script; em resumo:

| Marcação | Resultado |
|---|---|
| `^ texto` | parágrafo centralizado (endereçamento, fecho, assinatura) |
| `# TEXTO` | título centralizado, negrito, sublinhado (`RAZÕES DE APELAÇÃO`) |
| `## TEXTO` | título de seção, negrito, justificado (`I - DA TEMPESTIVIDADE`) |
| `> texto` | citação de lei ou da sentença: recuo de 2 cm, 11 pt |
| `>> texto` | ementa de acórdão: recuo de 2 cm, 10 pt |
| `[[PROVA 1 \| o que colar]]` | moldura tracejada onde o advogado cola o print |
| `[[QUADRO]] ... [[/QUADRO]]` | quadro de identificação das partes |
| `---` | quebra de página (separa a interposição das razões) |
| `**negrito**` / `*itálico*` | ênfase dentro do parágrafo |

Depois de gerar, entregue o arquivo ao usuário e liste em uma linha as lacunas `[CONFERIR]` que sobraram.

### Passo 6 — Conferência final

Rode o checklist de `references/modelo-canonico.md` antes de entregar.

## Convenção dos espaços de prova

Cada prova é antecedida por uma **frase de chamada** que diz o que o print demonstra e termina em dois-pontos, seguida do **espaço marcado**:

```
O apelado possui cadastro legítimo junto ao PicPay desde 24/08/2017, como se vê:

[[PROVA 1 | print da tela de cadastro do apelado, conta ativa desde 24/08/2017]]
```

No chat, o mesmo espaço aparece como `> 📎 **[ PROVA 1 - COLE A PROVA AQUI ]**` com a etiqueta do que colar, para o advogado localizar por Ctrl+F. Numere em sequência.

A regra que sustenta isso: **fato afirmado é fato provado**. Se um documento não existe no dossiê, não crie o espaço nem afirme o fato — uma alegação sem lastro em segundo grau é convite ao "as telas são unilaterais e não comprovam" que já derrubou a defesa em primeiro grau.

## Cuidados que definem a qualidade

**Ataque a sentença, não o autor em abstrato.** Cada tese abre identificando o **erro concreto do julgado** ("A r. sentença recorrida...") e fecha pedindo a reforma daquele ponto ("Dessa forma, impõe-se a reforma da r. sentença para..."). Uma apelação que apenas repete a contestação é uma contestação com capa nova, e o relator percebe.

**Deferência com firmeza.** O tom com o juízo *a quo* é respeitoso ("muito embora profira suas decisões habitualmente com acerto", "com máxima vênia ao entendimento do Nobre Magistrado"), nunca irônico. A firmeza está no argumento, não no adjetivo.

**Jurisprudência sempre com ponte.** Depois de transcrever a ementa, explique por que ela se aplica: "O precedente aplica-se à hipótese dos autos porque...". Ementa solta é peso morto. **Nunca invente número de acórdão, relator ou data** — use as ementas verbatim de `references/blocos-fixos.md`, as que já estão nos autos, ou acione as skills `jurisprudencia-tjsp` / `jurisprudencia-tjmg-picpay` para buscar julgados reais.

**Súmula citada é súmula conferida.** Antes de apoiar uma tese em súmula de tribunal local ou enunciado de jornada, confirme que continua em vigor — enunciados são cancelados e revistos, e o tribunal enxerga na hora. O caso clássico é a Súmula 75 do TJRJ, sobre mero aborrecimento, **cancelada pelo Órgão Especial em 17/12/2018** e ainda hoje citada em peças recicladas: sustentar a tese central nela entrega ao relator um argumento pronto contra a apelação. Súmulas do STJ e do STF do acervo padrão (479, 548, 385) são seguras; qualquer outra, confirme ou não use.

**Cálculo não é fato provado.** Se você deduzir um número que não está nos autos — total do contrato a partir do valor de uma parcela, saldo devedor projetado, diferença entre valores —, apresente-o como o que é: uma inferência a partir dos elementos existentes, com a premissa explicitada, e marque `[CONFERIR]` para o advogado bater com o demonstrativo original. Afirmar como aritmética incontroversa um número que depende de premissa não documentada é o mesmo risco de inventar dado, com a agravante de parecer mais confiável.

**Proibição de travessão.** O único traço admitido é o hífen simples (`-`), em usos legítimos como "São Paulo - SP". O travessão longo (—) e o traço médio (–) são vetados pelo escritório porque denunciam texto de máquina. Onde a tentação aparece, use vírgula, parênteses, dois-pontos ou duas frases. Faça uma varredura antes de entregar: um travessão sobrevivente já basta para a peça voltar.

**Densidade.** O modelo do escritório tem de 6 a 10 páginas. Cada tese desenvolve o argumento em vários parágrafos, transcreve o dispositivo legal e a cláusula contratual aplicáveis, encadeia jurisprudência e fecha com conclusão. Um esqueleto enxuto obriga o advogado a reescrever tudo — desenvolva a mais, que cortar é fácil.

**Sucumbência.** Diferentemente do JEC, aqui há condenação em custas e honorários. Quando o percentual for desproporcional ou incidir sobre base equivocada, atacá-lo é pedido autônomo e barato. Não esqueça de pedir a inversão da sucumbência no requerimento final.

## Skills irmãs

- `picpay-diretrizes-recursais` — decide **se** cabe recorrer (regra de ouro das custas, tabela de dano moral por UF). Consulte antes quando o usuário estiver em dúvida sobre recorrer.
- `indagacao-recursal-bfap` — o one-pager de recorribilidade enviado ao Jurídico Interno.
- `picpay-recurso-inominado` — mesma ótica, rito do JEC.
- `picpay-contrarrazoes-apelacao` — mesmo rito, ótica invertida (PicPay apelado).
- `picpay-embargos-declaracao` — quando o caminho for sanar vício antes de apelar.
- `jurisprudencia-tjsp`, `jurisprudencia-tjmg-picpay` — buscam acórdãos reais para colar na peça.
