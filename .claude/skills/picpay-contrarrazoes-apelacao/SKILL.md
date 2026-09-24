---
name: picpay-contrarrazoes-apelacao
description: "Redige CONTRARRAZÕES AO RECURSO DE APELAÇÃO na ótica do RÉU/APELADO (padrão PicPay - PicPay Instituição de Pagamento, PicPay Bank, Banco Original - e clientes do escritório BFAP), DIRETO NO CHAT em Markdown, sem gerar .docx, com ESPAÇOS MARCADOS para o usuário colar as provas (cadastro, biometria, senha, dispositivo, termos de uso, comprovantes/chargeback). Use SEMPRE que o usuário enviar os autos de um processo na Justiça Comum (sentença, apelação do autor, contestação, dossiê) e pedir 'fazer as contrarrazões de apelação', 'contrarrazoar a apelação', 'responder ao recurso de apelação' ou 'analisa os autos e faz as contrarrazões da apelação'. Reproduz os blocos fixos do escritório - encaminhamento, tempestividade (art. 1.010 §1º CPC), inépcia/dialeticidade, síntese, ausência de falha no serviço, danos morais e requerimentos. NÃO use para contrarrazões ao RECURSO INOMINADO do JEC (use contrarrazoes-recurso-inominado), contestação, recurso do próprio réu, embargos, réplica ou cumprimento de liminar."
---

# Contrarrazões ao Recurso de Apelação (réu/apelado)

## O que esta skill faz

Monta, **inteira no chat e em Markdown**, a peça de **contrarrazões ao recurso de apelação** na ótica do **réu/apelado** (padrão: PicPay e demais clientes do escritório BFAP), pedindo o não conhecimento e/ou o não provimento do recurso e a manutenção da sentença. A peça já vem com **espaços marcados para o advogado colar as provas** (os prints do dossiê) ao transferir para o modelo Word do escritório.

Esta é a **irmã de segunda instância comum** da skill `contrarrazoes-recurso-inominado`. A lógica e os blocos são os mesmos; o que muda é o **rito**: aqui é **Apelação (CPC)** na **Justiça Comum**, não Recurso Inominado no Juizado. Ver "Diferenças em relação ao inominado" abaixo.

## Regras inegociáveis

1. **Saída só no chat, nunca .docx.** Entregue a peça completa no corpo da resposta, em Markdown. O advogado copia e cola no modelo Word timbrado (BFAP) e cola os prints nos espaços. Não gere arquivo, não use a skill `docx`, não chame `present_files` com a peça.
2. **Espaços para colar provas.** Para cada prova do dossiê, deixe um espaço marcado e etiquetado (ver convenção abaixo). É o coração do pedido do usuário.
3. **PROIBIDO travessão.** Não use travessão (o traço longo, caractere Unicode U+2014) nem o traço médio (U+2013) em NENHUMA hipótese no corpo da peça. Travessão é a marca registrada de texto de IA e o escritório rejeita. Ver "Proibição absoluta de travessões" abaixo. Antes de enviar, releia a peça inteira e troque qualquer travessão por vírgula, ponto, dois-pontos, parênteses ou reescreva a frase.
4. **Peça robusta e longa, nunca um esqueleto.** O usuário não quer um resumo nem tópicos curtos: quer a peça inteira, densa e argumentada como a de um advogado sênior, no mesmo nível de profundidade e extensão do modelo do escritório. Ver "Robustez e profundidade" abaixo. Escrever pouco é o erro mais grave desta skill.

## Proibição absoluta de travessões

O único traço permitido é o **hífen simples** (`-`), e mesmo assim só em usos legítimos como "São Paulo - SP" ou "Colenda 2ª Câmara". Estão **proibidos** o travessão longo (U+2014) e o traço médio (U+2013), sob qualquer pretexto. Não é preferência estética, é regra rígida: esses traços denunciam texto de IA e o escritório não aceita.

Onde a tentação aparece e como resolver, sempre com pontuação comum:

- Aposto ou explicação intercalada: em vez de cortar a frase com dois travessões, use vírgulas ou parênteses. Ex.: "o PicPay, na qualidade de intermediador de pagamentos, repassou o valor".
- Ênfase ou pausa: use vírgula, ponto e vírgula ou ponto final. Prefira duas frases curtas a uma frase quebrada por travessão.
- Enumeração ou detalhamento: use dois-pontos, ponto e vírgula ou parênteses.

Faça uma varredura final antes de entregar: procure no texto qualquer traço que não seja o hífen simples e elimine todos. Se sobrar um único travessão, a peça está errada e precisa ser corrigida.

## Robustez e profundidade (o mais importante)

O padrão de qualidade é o **modelo do escritório**: uma peça longa, que desenvolve cada argumento em vários parágrafos, transcreve as cláusulas contratuais e os artigos de lei aplicáveis, encadeia a jurisprudência e fecha cada tópico com conclusão. Não entregue um rascunho enxuto.

Como garantir densidade:

- **Não sumarize os blocos fixos: reproduza-os por inteiro, verbatim, de `references/blocos-fixos.md`.** Eles já são longos de propósito. O tópico de danos morais, por exemplo, transcreve o art. 927 e o parágrafo único, o art. 186, o art. 14 do CDC com o §1º e incisos, a jurisprudência do STJ sobre senha pessoal intransferível, o ônus da prova do art. 373 do CPC, o argumento do mero aborrecimento e, à luz da eventualidade, a minoração do quantum com ementa. Tudo isso deve aparecer.
- **No mérito (tópico IV), desenvolva a narrativa probatória em profundidade.** Para cada fato relevante: (a) afirme o fato, (b) explique por que ele é juridicamente relevante, (c) transcreva a cláusula do contrato ou o artigo que o sustenta, (d) insira o espaço de prova, (e) conclua. Não basta "o usuário tem cadastro: [prova]". Explique o encadeamento: cadastro legítimo, transações por senha pessoal e intransferível, dispositivo validado, ausência de alteração de senha, contestação do cartão pela operadora, débito gerado ao PicPay, recuperação de valores prevista em contrato, e a conclusão de que não há falha do serviço (art. 14, §3º, CDC) nem ato ilícito (art. 186 CC).
- **Transcreva de verdade** as cláusulas dos Termos de Uso citadas (itens 3, 6 "c", 7 etc.) e os artigos de lei em blocos de citação, como faz o modelo. Não os mencione apenas por número.
- **Cite a sentença textualmente** em bloco de citação quando o trecho existir nos autos.
- **Extensão de referência:** o modelo de apelação do escritório tem cerca de 6 a 10 páginas. Mire nesse porte. Se a sua peça está com poucos parágrafos, ela está incompleta; volte e desenvolva cada tópico.

> Regra prática: prefira sempre desenvolver a mais do que a menos. Uma contrarrazão robusta que o advogado corta é útil; um esqueleto que ele precisa reescrever, não.

## Diferenças em relação ao inominado (leia antes de montar)

| Item | Recurso Inominado (JEC) | **Recurso de Apelação (Justiça Comum)** |
|---|---|---|
| Endereçamento | Turma Recursal / VSJE | **Juiz(a) de Direito da [nª] Vara Cível da Comarca de [x]** (juízo *a quo*, art. 1.010 CPC) |
| Título da peça | CONTRARRAZÕES AO RECURSO INOMINADO | **CONTRARRAZÕES AO RECURSO DE APELAÇÃO** |
| Como chamar as partes | Recorrente / Recorrido | **Apelante / Apelado (Apelada)** |
| Abertura das razões | "Colenda Turma Recursal," | **"Colendos Julgadores,"** |
| Fundamento da tempestividade | art. 218, §4º, CPC | **art. 1.010, §1º, CPC** |
| Quadro de identificação | RECORRENTE/RECORRIDO | **APELANTE/APELADO** |

Fora isso, os blocos de **inépcia recursal (dialeticidade - art. 1.010, III; Súmula 182/STJ; art. 932, III, CPC)**, **danos morais** e **requerimentos finais** são praticamente idênticos aos do inominado.

## Fluxo de trabalho

1. **Leia os autos** que o usuário enviar (anexos/colados): sentença, recurso de apelação do autor, contestação e o **dossiê de provas**. Se vier só o recurso, siga com o que houver, marcando lacunas com `[CONFERIR]`.
2. **Extraia os dados** (checklist abaixo).
3. **Identifique o tema do mérito** (transação contestada/chargeback, golpe/PIX, empréstimo contestado, bloqueio de conta, cobrança/negativação...) → ver `references/teses-merito.md`.
4. **Monte a peça** seguindo `references/modelo-canonico.md`, reaproveitando os blocos fixos verbatim de `references/blocos-fixos.md` e adaptando o mérito ao caso.
5. **Insira um espaço de prova** para cada print que o dossiê comprova, com a frase de chamada antes e a etiqueta do que colar.
6. **Entregue no chat.** Ao final, liste em uma linha as lacunas `[CONFERIR]` que sobraram.

## O que extrair dos autos (checklist)

- Endereçamento: **vara cível, comarca e UF** (é o juízo de 1º grau que recebe as contrarrazões).
- Número dos autos.
- **Apelante** (nome do autor) e **Apelado** (em regra, PICPAY INSTITUIÇÃO DE 