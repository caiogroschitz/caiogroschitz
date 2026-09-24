---
name: picpay-recurso-inominado
description: >-
  Redige, na íntegra e direto no chat, RECURSO INOMINADO (Lei 9.099/95) na
  perspectiva do RÉU/Recorrente — tipicamente o PicPay, mas também outros réus
  do mesmo escritório (GFG/Dafiti, Banco Original etc.) — contra sentença de
  Juizado Especial Cível que o condenou. Use SEMPRE que o usuário apresentar a
  íntegra (ou peças) dos autos — inicial, contestação, sentença, comprovantes,
  extratos, contratos, logs de biometria, telas de chargeback — e pedir para
  "fazer o recurso inominado", "recorrer da sentença", "fazer minhas razões
  recursais", "reformar a sentença", "elaborar o recurso", "redigir o recurso
  do PicPay" ou "analisa os autos e faz o recurso". Também aciona quando o
  usuário cola o teor da sentença pedindo a peça de insurgência. Faz
  ultra-análise dos autos e reproduz a estrutura, a narrativa e a construção
  argumentativa dos modelos do escritório. NÃO use para contestação (use
  picpay-contestacao), réplica, apelação cível ou petição inicial.
---

# Recurso Inominado — perspectiva do Recorrente (PicPay e demais réus do escritório)

Esta skill escreve, **inteira e pronta para copiar no chat**, a peça de RECURSO INOMINADO interposto pelo **réu condenado** (o Recorrente) contra a sentença do Juizado Especial Cível, no estilo do escritório. O objetivo é a **reforma integral** da sentença (improcedência da ação) e, subsidiariamente, a minoração das condenações.

O Recorrente padrão é o **PicPay Instituição de Pagamento S.A.**, mas o escritório também recorre por outros réus (GFG/Dafiti, Banco Original, sellers etc.). **Sempre adote como Recorrente a pessoa jurídica efetivamente ré e condenada nos autos** — nunca presuma que é o PicPay se os autos disserem outra coisa.

## Princípio central: a peça nasce da íntegra dos autos

A força desta peça está na **ultra-fidelidade ao que está nos autos**. Cada data, horário, valor, ID/E2E de transação, CNPJ, beneficiário, número de contrato/pedido, Device ID, Reason Code, número de protocolo, cláusula contratual, número de ID de documento e o **teor exato de cada item da sentença** precisam espelhar o que consta no processo. Um dado inventado destrói a credibilidade da peça e pode configurar litigância de má-fé.

Por isso, **antes de redigir, leia toda a íntegra fornecida de forma minuciosa** e reconstrua o caso. Não comece a escrever enquanto não dominar os fatos.

### Passo 1 — Ultra-análise dos autos

Leia cada peça e documento (inicial, contestação, sentença, comprovantes, extratos, contratos, telas, prints) e extraia, em nota mental ou rascunho:

- **Endereçamento e processo:** juízo/vara/juizado, comarca/UF, número do processo, partes (nome completo do autor e do réu, com qualificação institucional do réu).
- **Da inicial:** o que a parte autora alega, que pedidos formulou (declaração de inexistência, obrigação de fazer, danos morais e materiais e respectivos valores), e qual a tese fática dela (golpe Pix, desconhecimento de transação, empréstimo fraudulento, negativação indevida, cobrança a maior, produto não entregue etc.).
- **Da contestação:** preliminares e teses de mérito já deduzidas, e — crucialmente — **o acervo documental** que o réu juntou (cadastro, biometria/selfie, Device ID, IDs de transação, beneficiários, Reason Code, protocolos, cláusulas contratuais, contratos de empréstimo/CCB, telas de atendimento).
- **Da sentença (o alvo do recurso):** data da intimação/publicação; o que o juízo decidiu **item por item** (cada condenação, valor, multa, prazo, juros, correção); e, sobretudo, **quais erros a sentença cometeu** — por exemplo: aplicou responsabilidade objetiva de forma automática sem demonstrar defeito do serviço; inverteu o ônus da prova como fundamento autônomo; impôs prova diabólica; aplicou súmula a hipótese fática estranha (479, 548, 385); confundiu fatos geradores; desconsiderou o acervo documental ("telas unilaterais"); deixou de enfrentar provas (CPC, art. 489, §1º, IV).
- **Dados de fidelidade:** liste todos os números, datas, IDs, valores, nomes de beneficiários, CNPJs, cláusulas e protocolos que vão ancorar a narrativa.

### Passo 2 — Confirmar o que falta ANTES de escrever

Se faltar dado essencial (data da intimação para a tempestividade, valor exato de uma condenação, ID de uma transação, número de uma cláusula, OAB/UF do subscritor), **pergunte ao usuário de forma agrupada e objetiva** antes de redigir. Nunca preencha com presunção nem invente. Se o usuário autorizar seguir sem um dado, **omita o trecho correspondente** — não o fabrique.

### Passo 3 — Selecionar as teses aplicáveis

Com base nos erros da sentença e nos fatos, escolha quais teses de mérito entram na peça. O catálogo completo, com quando usar e o esqueleto de cada uma, está em **`references/teses.md`** — leia antes de montar o mérito. As mais comuns: regularidade/legitimidade da operação; ausência de defeito + culpa exclusiva do consumidor ou de terceiro (art. 14, §3º, I e II, CDC); inversão indevida do ônus / prova diabólica (art. 373 CPC; art. 6º, VIII, CDC); aplicação equivocada de súmula (479/548/385 STJ); afastamento do dano moral (mero aborrecimento); pedido subsidiário de minoração; ausência de danos materiais.

### Passo 4 — Montar a peça na estrutura e no estilo do escritório

Siga a estrutura fixa, a numeração, a voz e a arquitetura argumentativa descritas em **`references/estrutura-e-estilo.md`** — leia esse arquivo antes de redigir. Para ver peças completas como referência viva de tom e construção, consulte **`references/modelos.md`**.

Para a **craft da prosa** — escrita densa de parecerista sênior que não soa a IA (ritmo de frase variado, sem conectores previsíveis empilhados, latim contido, posição firme) somada à **disciplina de defesa da instituição e fidelidade documental** —, leia **`references/estilo-de-escrita.md`**. Esse arquivo funde o estilo das skills `advogado-civel-br` e `picpay-contestacao` e explica o que herdar de cada uma sem desfigurar o padrão forense dos modelos.

**Saída padrão: texto no chat, pronto para copiar.** Só gere arquivo (.docx) se o usuário pedir.

### Passo 5 — Conferência final

Antes de entregar, confira o checklist em `references/estrutura-e-estilo.md`: todos os dados batem com os autos; cada tese ataca um erro concreto da sentença; cada citação de jurisprudência tem a "ponte" de aplicação ao caso; a ordem das seções está correta; nada foi inventado; e a peça pede a reforma integral (e, subsidiariamente, a minoração).

## Cuidados que definem a qualidade

- **Ataque a sentença, não o autor em abstrato.** A peça é recursal: cada tese começa identificando o **erro específico do julgado** ("A r. sentença recorrida...") e termina pedindo a reforma daquele ponto ("Dessa forma... impõe-se a reforma da r. sentença para...").
- **Ancoragem documental obsessiva.** Sempre que afirmar um fato, amarre-o ao dado dos autos (ID, data, valor, beneficiário, cláusula, protocolo). É isso que diferencia esta peça de uma defesa genérica.
- **Jurisprudência sempre com ponte.** Não basta colar a ementa: depois de transcrevê-la, explique por que ela se aplica ao caso ("O precedente aplica-se à hipótese dos autos porque...").
- **Prosa que não soa a