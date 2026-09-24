---
name: picpay-diretrizes-recursais
description: >-
  Diretrizes Recursais oficiais do PicPay (massificado civel) para a BFAP decidir RECORRER ou DISPENSAR
  recurso. Use SEMPRE que precisar analisar interesse recursal, decidir se cabe apelacao/agravo/recurso,
  aplicar a regra de ouro (custas 70%+), consultar a tabela de dano moral por UF (27 UFs, JEC e Vara Civel),
  avaliar hipoteses obrigatorias/dispensa, decidir REsp/RE, Embargos de Declaracao, memoriais/sustentacao
  oral, abrir requisicao de analise recursal, ou redigir o parecer/comunicacao recursal no formato padrao
  (Objeto, Resumo da Inicial, Pedidos, Dossie, Sentenca, Condenacao, Prazos, Parecer Recursal). Aciona com
  "cabe recurso nesse caso", "tenho que recorrer", "isso e dispensa recursal", "passou da media de dano moral
  da UF", "custas acima de 70%", "cabe REsp", "redige o parecer recursal". Faz a analise CONJUNTA dos itens
  obrigatorios e de dispensa (errata 06/06/2025). NAO use para teses/contestacao (skill picpay-teses-defesa)
  nem para o passo a passo das requisicoes.
---

# Diretrizes Recursais PicPay (BFAP)

As Diretrizes Recursais oficiais (vigentes desde 19/05/2025, com errata de 06/06/2025) regem a
interposicao de recursos no **massificado civel** -- JEC, Varas Civeis da Justica Comum e Justica Federal.
Casos estrategicos/especiais tem analise individualizada do advogado interno PicPay.

**Objetivos:** reduzir o ticket medio de condenacao, aumentar encerramentos favoraveis sem onus,
uniformizar jurisprudencia favoravel, reduzir a entrada de processos e aumentar acordos pre/pos-sentenca.

## REGRA CENTRAL -- analise CONJUNTA (errata 06/06/2025)

Os itens **obrigatorios (1.2)** e de **dispensa (1.3)** sao analisados **em conjunto**. Mesmo com hipotese
obrigatoria, o recurso pode estar dispensado por outra razao -- e vice-versa.

> Exemplo: ha provas favoraveis (obrigatorio 1.2.1), mas as custas recursais sao >= 70% da condenacao
> (dispensa 1.3.1) -> **nao recorrer**.

**Fluxo de decisao sugerido:** (1) verifique se cai em hipotese **obrigatoria**; (2) verifique se cai em
hipotese de **dispensa**; (3) se houver tensao, a dispensa por custas/economicidade tende a prevalecer,
mas registre o racional; (4) na duvida ou em padrao regional anomalo, **abra requisicao de analise recursal**.

## Hipoteses de interposicao OBRIGATORIA

**Tutelas de urgencia (liminar / antecipada):**
- Obrigacao impossivel de cumprimento.
- Multa diaria sem limitacao.
- Multa diaria > R$ 300,00.

**Merito (sentenca) -- qualquer um dos 6 gatilhos:**
1. Provas favoraveis ao PicPay (subsidios favoraveis).
2. Vicios processuais.
3. Jurisprudencia favoravel nos Tribunais.
4. Obrigacao de fazer impossivel de cumprimento.
5. Dano moral **acima da media da regiao** (ver tabela em `references/tabela-dano-moral.md`).
6. Advogado agressor com indicios de irregularidade/fraude processual.

> Observacao -- OBF cumprida no prazo: se a OBF foi cumprida no prazo, **sem astreintes**, o recurso esta
> DISPENSADO, priorizando o encerramento rapido.

## Hipoteses de DISPENSA

- **Regra de Ouro - 70%**: custas recursais **>= 70%** do valor total da condenacao (danos morais + materiais).
- **Fraude com baixo dano**: fraude constatada **e** dano moral nao superior a media da regiao/orgao (tabela),
  desde que **nao haja devolucao em dobro** ou que **o dobro do dano material nao supere R$ 1.000,00**.
- **Ausencia de provas**: condenacao fundada na ausencia de producao de provas (ausencia de subsidios fornecidos pelo PicPay).
- **Jurisprudencia consolidada**: decisao fundada em IRDR, Repetitivos, Sumulas dos Tribunais Superiores ou do Tribunal local.
- **Contratacao irregular com boa-fe do cliente**: sentenca reconhece irregularidade pautada na boa-fe
  (intencao de devolucao do credito declarada na inicial), DESDE QUE: (a) ajuizamento em ate **180 dias**
  apos a contratacao; (b) deferida a compensacao do credito com a condenacao OU a condenacao por danos
  materiais **nao** fixada em dobro.
- **Advogados agressores sem indicios**: sem indicios de irregularidade/fraude e dano moral **abaixo** da media da regiao/orgao.

## Tabela de Dano Moral por UF (gatilho de recurso)

Recurso por dano moral acima da media e obrigatorio quando a condenacao **supera a coluna "recorrer quando
superar"** (= media da UF + R$ 1.000,00). A tabela oficial (Anexo II Final) cobre **todas as 27 UFs**, em
duas colunas conforme o orgao -- **JEC** ou **Vara Civel**. Consulte a UF e o orgao corretos em
`references/tabela-dano-moral.md`.

Atalho para as UFs da BFAP (recorrer quando superar): JEC -- MG R$ 4.139 / ES R$ 3.815 / DF R$ 3.689.
Vara Civel -- MG R$ 7.563 / ES R$ 4.247 / DF R$ 5.809. Para qualquer outra UF, use a tabela completa.

## Embargos de Declaracao

**NAO opor ED como meio procrastinatorio** (risco de nao conhecimento e multa por recurso protelatorio).
ED **apenas** com erro material, omissao, contradicao interna ou obscuridade da decisao.

## REsp e RE

- **Regra: NAO interpor** REsp/RE, salvo violacao expressa a legislacao federal ou a Constituicao.
- **Excecao**: reducao de limite + condenacoes **> R$ 50 mil** -> abrir requisicao de analise recursal de REsp/RE.
- Caso excepcional fora dessas hipoteses -> abrir requisicao de analise recursal no Projuris.
- Demais hipoteses pos-acordao -> abrir **diretamente** a requisicao de pagamento da condenacao, sinalizando
  "esgotamento da via recursal" (sem requisicao de analise recursal de REsp/RE).

## Atuacao estrategica (memoriais e sustentacao oral)

Ao recorrer, providenciar memoriais, despacho e/ou sustentacao oral perante o colegiado em todos os casos com:
- Dano moral **> R$ 10.000,00**;
- Advogado agressor com indicios de irregularidade/fraude processual (sem analise das provas);
- Clube do emprestimo.
Alem de atuacao ostensiva em teses de maior relevancia/impacto financeiro (alinhado ao Juridico Interno).

## Risco reputacional / imagem

Decisao com risco reputacional/imagem -> **abrir requisicao de analise recursal** no Projuris **e** acionar
o advogado interno responsavel pela carteira.

## Casos automatizados x excecao

A maior parte dos casos e automatizada (andamentos "Dispensa Recursal Automatica" / "Recurso Automatico").
Para qualquer **excecao** a regra automatizada, padrao regional de condenacoes elevadas, ou caso com
**responsabilidade de parceiros**, abrir requisicao de analise recursal (o passo a passo da requisicao
esta na skill `picpay-requisicoes-projuris`). O rol exemplificativo das Diretrizes (prova favoravel,
vicios processuais, jurisprudencia consolidada, OBF impossivel) esta em `references/rol-recursos.md`.

## Formato da comunicacao / parecer recursal (quando NAO for automatico)

Quando o caso **nao** for resolvido pela regra automatizada e exigir comunicacao (interesse recursal a
submeter, requisicao de analise recursal, ou parecer ao Juridico Interno), a saida deve seguir **exatamente**
este template, preenchendo cada campo com base nos autos e na analise CONJUNTA das Diretrizes. O **PARECER
RECURSAL** e a conclusao fundamentada (recorrer x dispensar) e deve explicitar o racional -- inclusive a
tensao entre hipotese obrigatoria e de dispensa quando houver.

```
Objeto: <tema do caso, ex.: fraude / emprestimo contestado / negativacao indevida>
RESUMO DA INICIAL: <o que a parte autora alega, em poucas linhas>
DOS PEDIDOS: <pedidos da inicial: declaratorios, restituicao/valor, dano moral pleiteado>
RESUMO DO DOSSIE: <subsidios/provas do PicPay, em itens (i), (ii), (iii)...; excludentes aplicaveis>
RESUMO DA SENTENCA: <dispositivo da sentenca; o que foi julgado procedente/improcedente; criterios de
correcao e juros>
RESUMO DA CONDENACAO:
- <verba 1, ex.: restituicao de R$ ...>
- <verba 2, ex.: dano moral de R$ ...>
DOS PRAZOS: <especie e data fatal do recurso, ex.: Prazo do Recurso Inominado - DD/MM/AAAA>
Media de preparo: R$ <valor estimado do preparo>
Valor atualizado da Condenacao: R$ <valor total atualizado>
PARECER RECURSAL: <conclusao fundamentada aplicando as Diretrizes: enquadramento em hipotese obrigatoria
e/ou de dispensa, leitura da regra de ouro (custas/preparo x condenacao), comparacao do dano moral com a
tabela da UF/orgao, e recomendacao final de RECORRER ou DISPENSAR com o racional>
```

### Como preencher DOS PRAZOS e os valores (NUNCA devolver "confirmar" para o usuario)

O parecer e um entregavel pronto: deduza tudo dos autos, nao transfira tarefa de volta ao usuario.

- **DOS PRAZOS:** conte o prazo a partir da **intimacao/publicacao da decisao recorrida que constar
  nos autos** (recurso inominado = 10 dias uteis; apelacao = 15 dias uteis; contagem em dias uteis,
  art. 219 CPC). **Se a intimacao/publicacao da decisao recorrida NAO estiver nos autos, isso
  significa que a decisao AINDA NAO FOI PUBLICADA** -- registre expressamente que o prazo recursal
  **ainda nao comecou a correr** e que o fatal sera contado da futura publicacao. NUNCA escreva
  "confirmar a data", "verificar no PJe/Astrea" ou equivalente: ou ha publicacao nos autos (calcule
  o fatal) ou nao ha (logo, nao publicado e sem prazo em curso).
- **Media de preparo:** **sempre estime um valor** (faixa em R$), nunca devolva "confirmar guia".
  Calcule pela tabela de custas do TJ local (no ES, Lei 9.974/2013; VRTE 2026 = R$ 4,9383),
  atentando para a diferenca entre orgaos:
    - **JEC (recurso inominado):** no 1º grau nao ha custas, entao o preparo soma **custas de
      1º grau (~2,5% do valor da causa em 2026; 3% a partir de 2027) + custas do recurso (~0,25%)**,
      com piso de 135 VRTE (~R$ 667) por componente, mais porte. Em causas de ~R$ 40-50 mil fica em
      torno de **R$ 1.800-1.950**.
    - **Vara Civel (apelacao):** as custas iniciais ja foram pagas no ajuizamento; o preparo recursal
      e so **~0,25% sobre o valor do pedido recursal, piso de 135 VRTE (~R$ 667)**.
  Apresente a faixa estimada com a base de calculo; o valor exato sai na guia do sistema.
- **Valor atualizado da Condenacao:** estime pelo objeto economico (condenacao em danos e/ou
  valor dos contratos anulados), nunca devolva "confirmar".

> Exemplo (analise CONJUNTA na pratica): dano moral de R$ 3.000,00 ficou **abaixo** da media do TJMG, o que
> isoladamente indicaria dispensa; porem a sentenca tambem determinou a **restituicao de R$ 3.520,00**
> (prejuizo relevante), ha **subsidios tecnicos** no dossie indicando regularidade das transacoes e o
> **preparo e baixo (~R$ 838,39)** frente a condenacao atualizada (~R$ 7.142,05). Pela leitura conjunta
> -- impacto economico relevante + provas favoraveis + custo recursal reduzido -- o parecer e pela
> **interposicao do recurso inominado**.
