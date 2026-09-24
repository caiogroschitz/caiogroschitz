---
name: drcalc-automacao
description: "Skill descontinuada: redireciona para calculo-condenacao-drcalc, que agora cobre também a automação pura do formulário do DrCalc quando os parâmetros já estão prontos."
---

# Skill descontinuada -- use calculo-condenacao-drcalc

Esta skill foi **unificada** na skill `calculo-condenacao-drcalc`, que agora
cobre o fluxo inteiro: extracao do PDF, validacao com o usuario, o gate de
verificacao de datas e de juros, o preenchimento do formulario do DrCalc
(`juridico.asp`) e a planilha final em PDF.

**Nao repita aqui o mapa de campos do formulario** -- ele mudou e vive so na
skill unificada, com as correcoes sobre datas nunca estimadas e sobre juros
com mais de uma data de inicio por condenacao (grupos de `jmdata`).

Invoque `calculo-condenacao-drcalc` sempre, inclusive quando o usuario ja
trouxer os parametros prontos sem PDF: nesse caso, dentro daquela skill, pule
direto para o "Gate de Verificacao" e a "Fase 3 -- Calculo no DrCalc", sem
refazer a extracao do PDF.