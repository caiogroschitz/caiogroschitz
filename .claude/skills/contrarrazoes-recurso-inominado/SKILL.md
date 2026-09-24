---
name: contrarrazoes-recurso-inominado
description: "Redige CONTRARRAZÕES AO RECURSO INOMINADO na ótica do RÉU/RECORRIDO (padrão PicPay - PicPay Instituição de Pagamento, PicPay Bank, Banco Original - e demais clientes do escritório BFAP), DIRETO NO CHAT em Markdown, sem gerar .docx, e com ESPAÇOS MARCADOS para o usuário colar as provas (prints de cadastro, biometria, termos de uso, extratos, telas do app). Use SEMPRE que o usuário enviar os autos (sentença de improcedência, recurso inominado do autor, contestação, dossiê de provas) e pedir 'fazer as contrarrazões', 'contrarrazoar o recurso', 'responder ao recurso inominado', 'contrarrazões ao recurso inominado', 'rebater o recurso do autor' ou 'analisa os autos e faz as contrarrazões'. Reproduz os blocos fixos do escritório: tempestividade, inépcia recursal/dialeticidade, síntese da demanda, danos morais e requerimentos finais. NÃO use para contestação, recurso inominado do próprio réu, embargos de declaração, réplica ou cumprimento de liminar."
---

# Contrarrazões ao Recurso Inominado (réu/recorrido)

## O que esta skill faz

Monta, **inteira no chat e em Markdown**, a peça de **contrarrazões ao recurso inominado** na ótica do **réu/recorrido** (padrão: PicPay e demais clientes do escritório BFAP), pedindo o não conhecimento e/ou o não provimento do recurso e a manutenção da sentença de improcedência. A peça já vem com **espaços marcados para o advogado colar as provas** (os prints do dossiê) ao transferir para o modelo Word do escritório.

## Regras inegociáveis

1. **Saída só no chat, nunca .docx.** Entregue a peça completa no corpo da resposta, em Markdown. O advogado copia e cola no modelo Word timbrado (BFAP) e cola os prints nos espaços. Não gere arquivo, não use a skill `docx`, não chame `present_files` com a peça.
2. **Espaços para colar provas.** Para cada prova do dossiê, deixe um espaço marcado e etiquetado (ver convenção abaixo). É o coração do pedido do usuário.
3. **PROIBIDO travessão.** Não use travessão (o traço longo, caractere Unicode U+2014) nem o traço médio (U+2013) em NENHUMA hipótese no corpo da peça. Travessão é a marca registrada de texto de IA e o escritório rejeita. Ver "Proibição absoluta de travessões" abaixo. Antes de enviar, releia a peça inteira e troque qualquer travessão por vírgula, ponto, dois-pontos, parênteses ou reescreva a frase.
4. **Peça robusta e longa, nunca um esqueleto.** O usuário não quer um resumo nem tópicos curtos: quer a peça inteira, densa e argumentada como a de um advogado sênior, no mesmo nível de profundidade e extensão dos modelos do escritório. Ver "Robustez e profundidade" abaixo. Escrever pouco é o erro mais grave desta skill.

## Proibição absoluta de travessões

O único traço permitido é o **hífen simples** (`-`), e mesmo assim só em usos legítimos como "Salvador - BA" ou "Colenda 2ª Turma Recursal". Estão **proibidos** o travessão longo (U+2014) e o traço médio (U+2013), sob qualquer pretexto. Não é preferência estética, é regra rígida: esses traços denunciam texto de IA e o escritório não aceita.

Onde a tentação aparece e como resolver, sempre com pontuação comum:

- Aposto ou explicação intercalada: em vez de cortar a frase com dois travessões, use vírgulas ou parênteses. Ex.: "o PicPay, na qualidade de intermediador de pagamentos, repassou o valor".
- Ênfase ou pausa: use vírgula, ponto e vírgula ou ponto final. Prefira duas frases curtas a uma frase quebrada por travessão.
- Enumeração ou detalhamento: use dois-pontos, ponto e vírgula ou parênteses.

Faça uma varredura final antes de entregar: procure no texto qualquer traço que não seja o hífen simples e elimine todos. Se sobrar um único travessão, a peça está errada e precisa ser corrigida.

## Robustez e profundidade (o mais importante)

O padrão de qualidade são os **modelos do escritório**: uma peça longa, que desenvolve cada argumento em vários parágrafos, transcreve as cláusulas contratuais e os artigos de lei aplicáveis, encadeia a jurisprudência e fecha cada tópico com conclusão. Não entregue um rascunho enxuto.

Como garantir densidade:

- **Não sumarize os blocos fixos: reproduza-os por inteiro, verbatim, de `references/blocos-fixos.md`.** Eles já são longos de propósito. O tópico de danos morais, por exemplo, transcreve o art. 927 e o parágrafo único, o art. 186, o art. 14 do CDC com o §1º e incisos, a jurisprudência aplicável, o ônus da prova do art. 373 do CPC, o argumento do mero aborrecimento e, à luz da eventualidade, a minoração do quantum com ementa. Tudo isso deve aparecer.
- **No mérito (tópico IV), desenvolva a narrativa probatória em profundidade.** Para cada fato relevante: (a) afirme o fato, (b) explique por que ele é juridicamente relevante, (c) transcreva a cláusula do contrato ou o artigo que o sustenta, (d) insira o espaço de prova, (e) conclua. Não basta "o usuário tem cadastro: [prova]". Explique o encadeamento completo do tema (cadastro, biometria, senha, dispositivo, cláusulas dos Termos de Uso, e a conclusão de que não há falha do serviço, art. 14 §3º do CDC, nem ato ilícito, art. 186 do CC).
- **Enfrente as teses concretas do recurso do autor.** Se o recurso inominado ataca a sentença ponto a ponto (e não apenas repete a inicial), responda a cada argumento dele diretamente no tópico de mérito, em vez de recorrer ao tópico de inépcia/dialeticidade. O tópico de inépcia só entra quando o recurso de fato apenas reproduz a petição inicial; forçá-lo contra um recurso bem fundamentado enfraquece a peça.
- **Transcreva de verdade** as cláusulas dos Termos de Uso e os artigos de lei em blocos de citação, como fazem os modelos. Não os mencione apenas por número.
- **Cite a sentença textualmente** em bloco de citação quando o trecho existir nos autos.
- **Extensão de referência:** as contrarrazões do escritório costumam ter várias páginas densas. Se a sua peça está com poucos parágrafos, ela está incompleta; volte e desenvolva cada tópico.

> Regra prática: prefira sempre desenvolver a mais do que a menos. Uma contrarrazão robusta que o advogado corta é útil; um esqueleto que ele precisa reescrever, não.

## Fluxo de trabalho

1. **Leia os autos** que o usuário enviar (