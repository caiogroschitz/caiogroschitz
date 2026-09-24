# Modelo canônico - peça montada (com espaços para colar provas)

Este é o **molde de saída**: mostra como a peça final aparece no chat, já com os blocos fixos no lugar e os **espaços para colar provas** intercalados no mérito. Siga esta ordem e este visual. O conteúdo entre `[ ]` é variável (preenchido a partir dos autos); os blocos longos vêm de `blocos-fixos.md`; o mérito vem de `teses-merito.md`.

> **Numeração:** os modelos originais do escritório têm numeração romana inconsistente (saltam de IV para VI e depois para VIII). **Corrija isso**: numere os tópicos em sequência limpa (I, II, III, IV, V, VI...). É um detalhe que o leitor agradece.

---

## CONVENÇÃO DO ESPAÇO PARA PROVA

Cada prova é antecedida por uma **frase de chamada** (que apresenta o que o print demonstra, terminando em dois-pontos) e, logo abaixo, um **espaço marcado**, numerado, dizendo exatamente o que colar. O advogado localiza o marcador (Ctrl+F por "COLE A PROVA") ao transferir para o Word e cola o screenshot por cima.

Formato do espaço:

```
> 📎 **[ PROVA 1 - COLE A PROVA AQUI ]**
> ▸ O que colar: print da tela de cadastro do Recorrente (conta ativa desde 13/06/2022).
```

Sempre: **frase de chamada terminando em ":" → espaço da prova**. Numere as provas em sequência (PROVA 1, PROVA 2, ...).

---

## ESQUELETO COMPLETO (preencher e entregar no chat)

---

**[ENDEREÇAMENTO]** - ex.: EXCELENTÍSSIMO SENHOR DOUTOR JUIZ DE DIREITO DA [vara/juizado] DE [comarca] - [UF]

**Processo autos nº [número]**

[Petição de encaminhamento - bloco fixo nº 1 de `blocos-fixos.md`: qualificação do PicPay + tempestividade + intimação exclusiva + "Termos em que, pede deferimento" + local/data + advogado/OAB.]

---

## CONTRARRAZÕES AO RECURSO INOMINADO

| | |
|---|---|
| **RECORRENTE:** | [nome do autor] |
| **RECORRIDO:** | PICPAY INSTITUIÇÃO DE PAGAMENTO S.A |
| **PROCESSO DE ORIGEM Nº:** | [número] |
| **ORIGEM:** | [vara/juizado e comarca - UF] |

Colenda Turma Recursal,

[2 parágrafos de abertura - bloco fixo nº 3.]

### I - DA TEMPESTIVIDADE
[bloco fixo nº 4, com a data da intimação.]

### II - DA SÍNTESE DA DEMANDA
Trata-se de [tipo de ação] em desfavor do PicPay. Pleiteia [pedidos do autor: danos morais de R$ X, obrigação de fazer etc.].

Em contestação, foi demonstrada [teses da defesa: ilegitimidade/incompetência se houve, regularidade da conduta, inocorrência de danos].

A sentença julgou improcedentes os pedidos, sob o fundamento de que [fundamento central da sentença - citar].

Conforme se verifica, a r. Sentença analisou as questões objeto do recurso com a propriedade devida, com base nas provas produzidas nos autos e na legislação vigente, devendo ser mantida por seus próprios fundamentos.

### III - DA INÉPCIA RECURSAL
[bloco fixo nº 5 - dialeticidade + ementas. Incluir só se o recurso apenas reproduz a inicial.]

### IV - DA AUSÊNCIA DE FALHA NA PRESTAÇÃO DOS SERVIÇOS DO RECORRIDO
No caso em tela, cabe salientar que a sentença deve ser mantida em sua integralidade.

Vejamos o trecho da decisão proferida, essencial para o deslinde do presente recurso:

> "[transcrever trecho real da sentença]"

[Aqui entra a NARRATIVA PROBATÓRIA - a espinha dorsal do caso. Cada fato é afirmado e imediatamente comprovado por um print. Exemplo (caso de bloqueio de conta):]

O Recorrente é usuário legítimo do PicPay desde [data], possuindo cadastro ativo até o presente momento:

> 📎 **[ PROVA 1 - COLE A PROVA AQUI ]**
> ▸ O que colar: print da tela de cadastro do Recorrente (conta ativa desde [data]).

A parte Recorrente teve sua biometria validada na mesma data:

> 📎 **[ PROVA 2 - COLE A PROVA AQUI ]**
> ▸ O que colar: print da validação de biometria.

Ocorre que foi verificada uma violação a Políticas e Termos de Uso na conta da parte Recorrente, razão pela qual sua conta foi limitada em [data] de forma cautelar:

> 📎 **[ PROVA 3 - COLE A PROVA AQUI ]**
> ▸ O que colar: print do registro de limitação/violação dos Termos de Uso.

[... continue intercalando frase de chamada + espaço de prova para cada print do dossiê: modificação da restrição/saques liberados, transferência do saldo via PIX para conta de mesma titularidade, cláusulas dos Termos de Uso (itens 3 e 4), resgate do saldo etc.]

Diante da violação aos termos de uso, o usuário teve sua conta limitada. O bloqueio da conta de qualquer usuário é uma prerrogativa do próprio PicPay, devidamente prevista no contrato de adesão pactuado entre as partes:

> 📎 **[ PROVA N - COLE A PROVA AQUI ]**
> ▸ O que colar: print do item dos Termos de Uso que prevê o bloqueio cautelar.

Assim sendo, o bloqueio cautelar da sua conta junto ao Recorrido não configura ato ilícito (art. 186 do Código Civil), vez que consiste no exercício regular do direito por parte do PicPay.

Portanto, a sentença deve ser mantida em todos os seus termos.

### V - DA MANUTENÇÃO DA DECISÃO - DO NÃO CABIMENTO DE INDENIZAÇÃO POR DANOS MORAIS
[bloco fixo nº 6 - não cabimento + eventual minoração + ementa de redução do quantum.]

### VI - DOS REQUERIMENTOS FINAIS
[bloco fixo nº 7.]

---

## Observações de fidelidade aos modelos
- O réu/recorrido fala sempre em 3ª pessoa ("o Recorrido", "o PicPay") e trata o autor como "o Recorrente".
- O tom é assertivo e respeitoso com o juízo ("a brilhante decisão", "r. Sentença", "Colenda Turma").
- A sentença é **citada textualmente** em blocos de citação - use trechos reais dos autos, não invente.
- A força da peça está na **narrativa probatória** do tópico de mérito (IV): afirmar → comprovar com print → afirmar → comprovar. Cada print tem o seu espaço.
- Não gere .docx. A peça sai inteira no chat, em Markdown, pronta para o advogado copiar para o modelo Word do escritório (com timbre BFAP) e colar os prints nos espaços.
