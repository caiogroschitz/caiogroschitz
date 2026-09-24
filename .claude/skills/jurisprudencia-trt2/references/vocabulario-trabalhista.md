# Vocabulário de busca por família de tese trabalhista

Este arquivo existe para transformar a tese da peça em expressões que realmente aparecem nas ementas do TRT2, e para lembrar qual enunciado consolidado governa o tema. Ementa é onde o desembargador declara o assunto; dispositivo é onde ele diz quem ganhou. As duas colunas abaixo alimentam, respectivamente, os campos `filtroEEmenta` e `filtroEDispositivo`.

**Os números de súmula, OJ e tema listados aqui são roteiro de verificação, não citação.** Confira o enunciado e sua vigência na fonte oficial antes de citar: TRT2 em `https://ww2.trt2.jus.br/jurisprudencia/jurisprudencia/trt2-jurisprudencia-consolidada` e TST em `https://www.tst.jus.br/livro-de-jurisprudencia-indice`. Há enunciados cancelados, convertidos e alterados pela Lei 13.467/2017, e citar um deles como vigente é erro que o juiz percebe.

## Como escolher os marcadores de dispositivo

O campo de dispositivo não diz de quem era o recurso, apenas o que o colegiado fez com ele. Por isso, combine sempre com um marcador de sentido na ementa e confirme lendo.

| Situação | Dispositivo | Confirmação na ementa |
|---|---|---|
| Reclamada quer manter improcedência ou derrubar recurso do reclamante | `"negar provimento"`, `"nego provimento"`, `"não provido"` | `"mantida a improcedência"`, `"recurso do reclamante"`, `"sentença mantida"` |
| Reclamada recorreu e quer reforma | `"dar provimento"`, `"reformar a sentença"` | `"recurso da reclamada"`, `"reforma da sentença"`, `"afastada a condenação"` |
| Reclamante quer reforma da improcedência | `"dar provimento"`, `"reformar a sentença"` | `"recurso do reclamante"`, `"condenação"`, `"deferido o pedido"` |
| Reclamante quer manter procedência | `"negar provimento"` | `"recurso da reclamada"`, `"sentença mantida"` |

Cuidado com acórdãos de provimento parcial: o dispositivo traz "dar provimento parcial" e a tese pode ter sido vencida no ponto que interessa. Quando o resultado for parcial, leia o item da ementa correspondente à sua tese, não o resultado global.

## 1. Vínculo de emprego

**Ementa**: `"vínculo de emprego"`, `"vínculo empregatício"`, `"relação de emprego"`, `"subordinação jurídica"`, `"subordinação estrutural"`, `"pessoalidade"`, `"onerosidade"`, `"não eventualidade"`, `"trabalho autônomo"`.
**Recortes**: `"motorista de aplicativo"`, `"entregador de aplicativo"`, `"plataforma digital"`, `"pejotização"`, `"representante comercial"`, `"contrato de parceria"`, `"cooperativa"`, `"salão-parceiro"`, `"corretor de imóveis"`.
**Base**: arts. 2º e 3º da CLT; art. 9º da CLT (fraude); Lei 6.019/1974.
**Enunciados e temas a verificar**: Tema 1291 do STF (RE 1.446.336), sobre vínculo entre motorista e plataforma, com repercussão geral reconhecida; ADC 48 (transportadores autônomos); Súmula 331 do TST para intermediação; IACs de regionais sobre trabalho por aplicativo.
**Exclusões úteis** (`filtroNao`): quando o caso for de motorista, exclua `"entregador"`; quando for de entregador, exclua `"motorista"`.
**Este é o exemplo clássico de tema fraturado.** O campo de dispositivo rende pouco aqui: em execução de teste, `"dar provimento"` devolveu três resultados e nenhum aproveitável. O que separa as correntes é o marcador doutrinário na ementa. Pró-vínculo: `"subordinação algorítmica"`, `"subordinação por algoritmo"`, `"controle por avaliação"`, `"gerenciamento algorítmico"`, `"trabalhador avulso digital"` (tese sucessiva usada na 4ª Turma). Contra o vínculo: `"ausência de subordinação"`, `"autonomia na prestação"`, `"livre adesão"`, `"parceria"`. Em julho de 2026, a corrente majoritária do TRT2 nega o vínculo (numa amostra dos 20 acórdãos mais recentes, 18 negavam), e há acórdãos reconhecendo em Turmas específicas. Diga isso ao usuário antes de entregar as ementas.

## 2. Jornada, horas extras e compensação

**Ementa**: `"horas extras"`, `"jornada de trabalho"`, `"controle de jornada"`, `"cartões de ponto"`, `"jornada britânica"`, `"banco de horas"`, `"acordo de compensação"`, `"regime 12x36"`, `"turnos ininterruptos de revezamento"`, `"tempo à disposição"`, `"minutos residuais"`, `"horas in itinere"`, `"sobreaviso"`, `"prontidão"`, `"teletrabalho"`, `"cargo de confiança"`.
**Base**: arts. 4º, 58, 58-A, 59, 59-A, 59-B, 62, III, 71 e 74, § 2º, da CLT; art. 7º, XIII e XIV, da CF.
**Enunciados a verificar**: Súmula 338 (cartões inválidos e ônus da prova), Súmula 85 (compensação), Súmula 366 (minutos residuais), Súmula 428 (sobreaviso), Súmula 90 (in itinere, contratos anteriores à reforma), Súmula 291 (supressão de horas extras), Súmula 340 e OJ 397 da SDI-1 (comissionistas), OJ 275 da SDI-1 (turnos).
**Nota temporal**: horas in itinere e a redação anterior do art. 71, § 4º, só valem para contratos e períodos anteriores a 11/11/2017. Restrinja o período da busca quando a tese depender do regime aplicável.

## 3. Intervalos

**Ementa**: `"intervalo intrajornada"`, `"intervalo interjornada"`, `"intervalo do artigo 384"`, `"supressão do intervalo"`, `"natureza indenizatória"`, `"pagamento apenas do período suprimido"`.
**Base**: art. 71, § 4º, da CLT (redação da Lei 13.467/2017: só o tempo suprimido, natureza indenizatória); art. 66 da CLT.
**Enunciados a verificar**: **Súmula 437 do TST está CANCELADA** — Res. 225/2025, DEJT de 30.06 e 01 e 02.07.2025, por perda de eficácia a partir de 11.11.2017, pela Lei 13.467/2017 (verificado no consultor de verbetes do TST em 27/07/2026). Era o enunciado que sustentava a tese contrária, então o cancelamento vai no topo da resposta quando se defende a limitação. Ver também Súmula 118 e OJ 342 da SDI-1. No âmbito do TRT2, a **Súmula 29** ainda fala em remunerar o período integral como extraordinário, e a **Tese Jurídica Prevalecente nº 16** trata da impossibilidade de redução do intervalo por norma coletiva: as duas são anteriores à reforma e contrárias na letra, e precisam ser enfrentadas com distinção em vez de ignoradas.
**Uso típico pela reclamada**: `filtroEEmenta` com `"intervalo intrajornada" "natureza indenizatória"` e dispositivo `"dar provimento"` para limitar condenação pós-reforma. Lembre que praticamente todo acórdão do tema é de provimento parcial: leia o item da ementa relativo à sua tese.

## 4. Adicionais de insalubridade, periculosidade e transferência

**Ementa**: `"adicional de insalubridade"`, `"adicional de periculosidade"`, `"adicional de transferência"`, `"laudo pericial"`, `"perícia técnica"`, `"agente insalubre"`, `"fornecimento de EPI"`, `"neutralização"`, `"eliminação do agente"`, `"base de cálculo"`, `"energia elétrica"`, `"inflamáveis"`, `"motocicleta"`, `"vigilante"`.
**Base**: arts. 189 a 195 e 193 da CLT (§ 4º para motociclista); NR-15 e NR-16; art. 469, § 3º, da CLT.
**Enunciados a verificar**: Súmula 80 (EPI eficaz elimina), Súmula 448 (enquadramento na NR-15), Súmula 364 (periculosidade e exposição intermitente), Súmula Vinculante 4 e Súmula 228 do TST (base de cálculo da insalubridade), OJ 385 da SDI-1 (rede elétrica).

## 5. Justa causa e modalidades de rescisão

**Ementa**: `"justa causa"`, `"dispensa por justa causa"`, `"abandono de emprego"`, `"desídia"`, `"improbidade"`, `"ato de indisciplina"`, `"insubordinação"`, `"mau procedimento"`, `"gradação de penalidades"`, `"imediatidade"`, `"proporcionalidade da pena"`, `"rescisão indireta"`, `"pedido de demissão"`, `"rescisão por acordo"`, `"culpa recíproca"`.
**Base**: arts. 482, 483, 484 e 484-A da CLT.
**Enunciados a verificar**: Súmula 32 do TST (presunção de abandono após 30 dias do fim do benefício previdenciário, reafirmada no IRR nº 226, Tribunal Pleno, 02/09/2025 — atenção, a redação é previdenciária, de modo que a aplicação ao abandono comum é analógica e convém dizer isso na peça), Súmula 73 (justa causa e aviso prévio), Súmula 212 (ônus da prova do término do contrato, costuma ser invocada pelo lado do empregado). No TRT2, verifique o Tema 62 de IRDR sobre dano moral na reversão de justa causa por imputação de improbidade, que é ponto contrário típico nesse cenário.
**Ônus da prova**: da reclamada, quanto ao fato justificador. Uma busca de defesa combina `"justa causa"` na ementa com `"negar provimento"` no dispositivo e, no campo livre, `"prova robusta"` ou `"ônus da prova"`.

## 6. Dano moral, assédio e acidente do trabalho

**Ementa**: `"dano moral"`, `"dano existencial"`, `"assédio moral"`, `"assédio sexual"`, `"revista íntima"`, `"revista pessoal"`, `"mero aborrecimento"`, `"dano extrapatrimonial"`, `"quantum indenizatório"`, `"doença ocupacional"`, `"nexo de causalidade"`, `"nexo concausal"`, `"acidente de trabalho"`, `"culpa do empregador"`, `"responsabilidade objetiva"`, `"atividade de risco"`, `"estabilidade acidentária"`, `"limbo previdenciário"`.
**Base**: arts. 223-A a 223-G da CLT; art. 927, parágrafo único, do CC; art. 118 da Lei 8.213/1991.
**Enunciados a verificar**: Súmula 378 (estabilidade acidentária), Súmula 443 (dispensa discriminatória e doença grave), Súmula 392 (competência), OJ 359 da SDI-1.
**Defesa típica**: `"mero aborrecimento"` ou `"ausência de nexo"` na ementa, dispositivo `"negar provimento"` ou `"dar provimento"` conforme quem recorreu.

## 7. Terceirização, grupo econômico e responsabilidade

**Ementa**: `"responsabilidade subsidiária"`, `"responsabilidade solidária"`, `"terceirização"`, `"tomador de serviços"`, `"culpa in vigilando"`, `"culpa in eligendo"`, `"dono da obra"`, `"grupo econômico"`, `"sucessão de empregadores"`, `"ente público"`, `"administração pública"`, `"fiscalização do contrato"`.
**Base**: arts. 2º, §§ 2º e 3º, 10, 448 e 455 da CLT; Lei 6.019/1974, arts. 4º-A e 5º-A; art. 71, § 1º, da Lei 8.666/1993 e correspondente na Lei 14.133/2021.
**Enunciados e temas a verificar**: Súmula 331 do TST, itens IV, V e VI (atenção: o item I foi cancelado pela Res. 225/2025, então transcreva da fonte e não de memória), OJ 191 da SDI-1 (dono da obra), Tema 725 do STF e ADPF 324 (licitude da terceirização de atividade-fim), Tema 246 do STF, RE 760.931 (a responsabilidade do ente público não é automática) e Tema 1118 do STF, RE 1.298.647 (ônus da prova da falha de fiscalização, com trânsito em julgado em 2025). O par Tema 246 mais Tema 1118 é o eixo da defesa do tomador público, e o recorte por autarquia costuma render mais que a busca genérica por "administração pública".
**Panorama observado no TRT2 em julho de 2026**: numa amostra de 25 acórdãos lidos, 21 mantinham a responsabilidade subsidiária do ente público e 4 a afastavam. A defesa ganha terreno justamente no recorte de fiscalização documentada e na distribuição do ônus da prova. Diga isso ao usuário.

## 8. Salário, equiparação e função

**Ementa**: `"equiparação salarial"`, `"paradigma"`, `"identidade de funções"`, `"desvio de função"`, `"acúmulo de função"`, `"plano de cargos e salários"`, `"gratificação de função"`, `"incorporação"`, `"alteração contratual lesiva"`, `"redução salarial"`, `"comissões"`, `"prêmios"`, `"gorjetas"`, `"salário in natura"`, `"natureza jurídica da parcela"`.
**Base**: arts. 457, 458, 461, 468 e 71 da CLT.
**Enunciados a verificar**: Súmula 6 (equiparação), Súmula 372 (gratificação de função e incorporação), Súmula 51 (norma regulamentar), OJ 125 da SDI-1 (desvio de função).

## 9. Estabilidades e garantias de emprego

**Ementa**: `"estabilidade provisória"`, `"garantia de emprego"`, `"gestante"`, `"cipeiro"`, `"membro da CIPA"`, `"dirigente sindical"`, `"acidentado"`, `"auxílio-doença acidentário"`, `"reintegração"`, `"indenização substitutiva"`.
**Base**: art. 10, II, do ADCT; arts. 543, § 3º, e 165 da CLT; art. 118 da Lei 8.213/1991.
**Enunciados a verificar**: Súmula 244 (gestante), Súmula 369 (dirigente sindical), Súmula 378 (acidentado), Súmula 396 (exaurimento do período e indenização).

## 10. Negociado sobre legislado e normas coletivas

**Ementa**: `"norma coletiva"`, `"convenção coletiva"`, `"acordo coletivo"`, `"negociado sobre o legislado"`, `"flexibilização"`, `"cláusula normativa"`, `"ultratividade"`, `"contribuição assistencial"`, `"desconto sindical"`.
**Base**: arts. 611-A e 611-B da CLT; art. 7º, XXVI, da CF.
**Temas a verificar**: Tema 1046 do STF (validade de norma coletiva que restringe direito não assegurado em nível constitucional), Súmula 277 do TST (ultratividade, com histórico de suspensão), Tema 935 do STF (contribuição assistencial).

## 11. Processo do trabalho

**Ementa**: `"prescrição bienal"`, `"prescrição quinquenal"`, `"prescrição intercorrente"`, `"justiça gratuita"`, `"honorários sucumbenciais"`, `"honorários periciais"`, `"litigância de má-fé"`, `"confissão ficta"`, `"revelia"`, `"ônus da prova"`, `"cerceamento de defesa"`, `"nulidade processual"`, `"julgamento extra petita"`, `"limitação aos valores da inicial"`, `"aditamento"`, `"coisa julgada"`, `"correção monetária"`, `"juros de mora"`.
**Base**: art. 7º, XXIX, da CF; arts. 11, 11-A, 790, § 4º, 791-A, 793-A a 793-D, 818, 840, § 1º, e 844 da CLT.
**Enunciados e temas a verificar**: Súmula 463 (justiça gratuita e declaração), ADI 5766 (honorários do beneficiário da gratuidade), Súmula 74 (confissão ficta), Súmula 362 (prescrição do FGTS) com o ARE 709.212, ADCs 58 e 59 e a Lei 14.905/2024 (correção monetária e juros).
**Nota prática sobre a limitação aos valores da inicial**: é uma das teses mais disputadas do TRT2 e o entendimento varia entre Turmas. Verificado em julho de 2026: **o TRT2 não tem súmula, tese prevalecente, IRDR nem IAC sobre o tema** (as quatro coleções foram varridas), de modo que a resposta correta a quem pergunta por enunciado regional é a negativa verificada, não uma aproximação. O que governa a matéria vem de fora: a IN 41/2018 do TST, o art. 840, § 1º, da CLT e a ADI 6.002/DF do STF, que deu interpretação conforme ao dispositivo com modulação de efeitos — confira essa decisão e a data de corte na fonte antes de citar, porque é ela que decide se os valores da inicial são estimativa ou teto. Apresente ao usuário o panorama entre Turmas, não só o julgado que agrada.

## 12. Execução

**Ementa**: `"agravo de petição"`, `"desconsideração da personalidade jurídica"`, `"incidente de desconsideração"`, `"redirecionamento da execução"`, `"sócio retirante"`, `"penhora"`, `"impenhorabilidade"`, `"bem de família"`, `"embargos à execução"`, `"cálculos de liquidação"`, `"excesso de execução"`.
**Base**: arts. 10-A, 855-A, 878 a 884 da CLT; arts. 133 a 137 do CPC; Lei 8.009/1990.
**Enunciados a verificar**: Súmula 417 do TST, OJ 343 da SDI-1, súmulas regionais sobre responsabilidade de sócios.

## Categorias com vocabulário próprio

Quando a reclamação envolver categoria regulamentada, acrescente o termo da categoria à ementa. O TRT2 tem massa relevante em: bancários (art. 224 da CLT, Súmulas 102, 109, 199, 287, 340), motoristas profissionais (Lei 13.103/2015, tempo de espera), aeronautas, professores, vigilantes, portuários, teleoperadores (NR-17 e Súmula 178), profissionais de saúde e trabalhadores em telemarketing.
