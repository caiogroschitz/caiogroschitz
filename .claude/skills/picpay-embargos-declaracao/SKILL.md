---
name: picpay-embargos-declaracao
description: >-
  Analisa a íntegra dos autos e redige, direto no chat, EMBARGOS DE DECLARAÇÃO
  (CPC, arts. 1.022 a 1.026) na perspectiva do RÉU/Embargante — tipicamente o
  PicPay (PicPay Bank, Banco Original) e demais réus do mesmo escritório. Antes
  de redigir, faz DIAGNÓSTICO técnico e
  não-superficial das hipóteses — omissão (inclusive art. 489, §1º, e tese de
  repetitivo/IAC), contradição, obscuridade, erro material e prequestionamento
  (art. 1.025) — separando vício real de mero inconformismo, para não opor ED
  protelatório (multa do art. 1.026, §2º). Use SEMPRE que apresentarem os autos
  (sentença, acórdão de Turma Recursal, decisão interlocutória, contestação) e
  pedirem para "fazer os embargos de declaração", "opor embargos", "embargar a
  sentença/acórdão", "fazer os ED", "tem omissão nessa sentença?", "cabe
  embargos?", "prequestionar para o recurso especial" ou "vê se cabe embargos";
  ou colarem a decisão pedindo para apontar omissão/contradição/obscuridade. NÃO
  use para contestação, recurso inominado ou cumprimento de liminar.
---

# Embargos de Declaração — perspectiva do Embargante (PicPay e demais réus do escritório)

Esta skill faz duas coisas, nesta ordem: primeiro **diagnostica com rigor** se há vício de embargabilidade na decisão (e qual), depois **escreve a peça inteira, pronta para copiar no chat**, no estilo do escritório. O Embargante padrão é o **PicPay Instituição de Pagamento S.A.** (ou PicPay Bank / Banco Original), mas o escritório também embarga por outros réus. **Adote sempre como Embargante a pessoa jurídica efetivamente ré nos autos** — confira na decisão, nunca presuma que é o PicPay.

Embargos de declaração não servem para rediscutir o mérito nem para manifestar inconformismo: servem para **integrar, esclarecer ou corrigir** a decisão quando ela for omissa, contraditória, obscura ou contiver erro material (CPC, art. 1.022). Opor ED sem vício real desgasta a credibilidade do escritório perante o juízo e expõe o cliente à **multa do art. 1.026, §2º** (até 2%, e até 10% na reiteração, condicionando recursos futuros ao depósito). Por isso o diagnóstico honesto vem antes da redação — e às vezes a resposta correta é "aqui não cabe ED; o caminho é o recurso inominado".

## Princípio central: a peça nasce da íntegra dos autos e do texto exato da decisão

A força desta peça está na **ultra-fidelidade ao que a decisão embargada efetivamente diz** (e ao que ela deixou de dizer). Cada omissão apontada precisa ser ancorada em um **ponto concreto que foi suscitado e não enfrentado**; cada contradição, em **duas passagens do próprio julgado que não se conciliam**; cada obscuridade, no **trecho ininteligível**; cada erro material, no **equívoco objetivo** (nome, data, valor, número de processo). Apontar omissão sobre questão que a decisão de fato enfrentou é o erro mais comum e mais fatal — vira munição para a multa de protelação.

Por isso, **antes de escrever, leia toda a íntegra fornecida de forma minuciosa** e reconstrua (a) o que o Embargante alegou na contestação/manifestação e (b) o que a decisão respondeu, ponto por ponto. Só então confronte os dois para localizar o que ficou sem resposta.

### Passo 1 — Ultra-análise dos autos e da decisão embargada

Leia cada peça e documento e extraia, em rascunho:

- **Endereçamento e processo:** órgão prolator (juízo de 1º grau, Turma Recursal, relator), comarca/UF, número do processo, partes com a qualificação institucional do réu, e **a natureza da decisão embargada** (sentença, acórdão, decisão interlocutória).
- **O que o Embargante suscitou:** liste as preliminares e teses de mérito efetivamente deduzidas na contestação/manifestação, com o **acervo documental** invocado (cadastro, biometria/selfie, Device ID, IDs/E2E de transação, beneficiários + CNPJ, Reason Code, protocolos, cláusulas, CCB, telas de atendimento, MED, comprovação de cumprimento de liminar).
- **O que a decisão decidiu e fundamentou:** transcreva mentalmente (ou em rascunho) os trechos-chave do dispositivo e da fundamentação — cada condenação, valor, multa, prazo, juros, correção — e **como** o juízo fundamentou cada um.
- **Dados de fidelidade:** datas (sobretudo a da intimação/publicação, para a tempestividade), valores, IDs, CNPJs, beneficiários, cláusulas, protocolos, número exato do processo e dos IDs de documento.

### Passo 2 — Diagnóstico das hipóteses de ED (o coração desta skill)

Confronte "o que foi suscitado" com "o que foi enfrentado" e classifique cada achado em uma das quatro hipóteses do art. 1.022 (ou prequestionamento). **Esse diagnóstico não pode ser superficial** — a profundidade aqui é o que diferencia o trabalho do escritório de uma peça genérica. O método completo, com as perguntas de teste de cada hipótese, as omissões recorrentes nos casos PicPay e os critérios para separar vício real de inconformismo, está em **`references/diagnostico.md`** — **leia esse arquivo antes de decidir embargar**.

Ao final do diagnóstico, conclua com honestidade:
- **Há vício(s) real(is):** identifique qual(is), em que ponto, e siga para a redação.
- **Há dúvida sobre um dado:** pergunte ao usuário antes de redigir (Passo 3).
- **Não há vício, só inconformismo:** diga isso ao usuário com franqueza, explique por que ED não é o caminho ali e aponte o recurso cabível (em regra, o inominado — `picpay-recurso-inominado`). Não force uma peça frágil.

### Passo 3 — Confirmar o que falta ANTES de escrever

Se faltar dado essencial — **data da intimação** (indispensável para a tempestividade dos 5 dias), número do processo, valor de uma condenação, OAB/UF do subscritor, ou o teor exato do trecho que se reputa omisso/contraditório —, **pergunte ao usuário de forma agrupada e objetiva** antes de redigir. Nunca preencha com presunção nem invente. Se o usuário autorizar seguir sem um dado, **omita o trecho correspondente** — não o fabrique.

### Passo 4 — Montar a peça na estrutura e no estilo do escritório

Siga a estrutura fixa, a numeração, a voz e a arquitetura argumentativa descritas em **`references/estrutura-e-estilo.md`** — leia antes de redigir. Para o desenvolvimento de cada vício em prosa (a progressão de movimentos que é a assinatura do escritório) e as frases-âncora por hipótese, consulte **`references/teses.md`**. Para ver peças completas como referência viva de tom e construção, consulte **`references/modelos.md`**.

Para a **craft da prosa** — escrita densa que não soa a IA (ritmo de frase variado, conectores não previsíveis, latim contido, posição firme) somada à **disciplina de defesa da instituição e fidelidade documental** —, leia **`references/estilo-de-escrita.md`**.

**Saída padrão: texto no chat, pronto para copiar.** Só gere arquivo (.docx) se o usuário pedir.

### Passo 5 — Conferência final

Antes de entregar, rode o checklist de `references/estrutura-e-estilo.md`: a decisão embargada está corretamente identificada; a tempestividade usa a data real de intimação e conta os **5 dias** (úteis no CPC comum; ver nota sobre JEC); cada vício apontado existe de fato e está ancorado no texto da decisão e no que foi suscitado; nada foi inventado; e o pedido está correto (sanar o vício e, quando for o caso, atribuir **efeitos infringentes** ou consignar o **prequestionamento** do art. 1.025).

## Cuidados que definem a qualidade

- **Vício real, não rediscussão.** Cada seção começa demonstrando o defeito **do próprio julgado** (o ponto suscitado e silenciado, as duas passagens que se contradizem, o trecho obscuro, o erro objetivo) e termina pedindo a integração/correção daquele ponto. Se o argumento for "a decisão decidiu mal", isso é recurso, não ED — não embarque.
- **Efeitos infringentes só quando a correção do vício altera o resultado.** Peça-os de forma fundamentada e excepcional: sanada a omissão/contradição, a conclusão muda. Não os peça como regra.
- **Prequestionamento com técnica.** Quando o fim for viabilizar recurso especial/extraordinário, prequestione **expressamente os dispositivos** (cite o artigo de lei federal/constitucional) e invoque o art. 1.025 do CPC. Lembre que o STJ exige, depois, que o recurso aponte ofensa ao art. 1.022 — registre isso na estratégia.
- **Ancoragem documental obsessiva.** Todo fato amarrado ao dado dos autos (ID, data, valor, beneficiário, cláusula, protocolo, Device ID). Dado inventado destrói a peça e pode configurar litigância de má-fé.
- **Tom respeitoso e firme com o juízo.** ED apontam falha no julgado sem agredir o magistrado ("muito embora a r. decisão tenha sido proferida com habitual acerto, restou omissa quanto a..."). Nunca ironia, nunca acusação de erro grosseiro.
- **Prosa que não soa a IA.** Frases de tamanho variado, sem conectores empilhados, sem vocabulário-clichê. Ver `references/estilo-de-escrita.md`.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                