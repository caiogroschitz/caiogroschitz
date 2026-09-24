# Estrutura, voz e arquitetura argumentativa

## 1. Estrutura fixa da peça

Reproduza esta ordem. Itens marcados *(condicional)* entram só quando o caso pedir.

1. **Endereçamento** — em caixa alta, ao juízo prolator (é ele quem recebe o recurso): `EXCELENTÍSSIMO(A) SENHOR(A) DOUTOR(A) JUIZ(A) DE DIREITO DO [Nº] JUIZADO ESPECIAL CÍVEL DA COMARCA DE [CIDADE] - [UF]`.
2. **Número do processo** — `Processo nº [...]` ou `Autos nº [...]`.
3. **Parágrafo de interposição** — `[RÉU], já qualificada, nos autos da [tipo de ação] movida por [AUTOR], parte também já qualificada, vem, por seus advogados, respeitosamente, à presença de Vossa Excelência, com fundamento no artigo 41 da Lei 9.099/95, interpor RECURSO INOMINADO, nos termos que seguem.`
4. **Preparo** — `Requer a juntada da respectiva guia de preparo, nos termos do artigo 42, §1º da Lei n° 9.099/95.`
5. *(condicional)* **Efeitos** — quando se pedir efeito suspensivo: `requer-se o processamento do referido recurso em ambos os efeitos, DEVOLUTIVO e SUSPENSIVO, conforme prevê o artigo 43 da Lei 9.099/95.`
6. *(condicional)* **Folha de rosto das razões** — alguns modelos abrem nova página com `RAZÕES DE RECURSO INOMINADO` e o vocativo `Nobres Julgadores,` / `Colenda Turma Recursal,` (porque as razões serão julgadas pela Turma). Pode-se usar ou ir direto à tempestividade.
7. **DA TEMPESTIVIDADE** — abre com `Ab initio, cumpre destacar a tempestividade do referido recurso.` Indica a data da intimação/publicação, conta os **10 dias úteis** (art. 42), e conclui `Desta forma, inegável a TEMPESTIVIDADE do presente recurso.` (ou `requer seja certificada a tempestividade`).
8. **SÍNTESE DA DEMANDA** (ou **SÍNTESE DOS FATOS**) — narra, em terceira pessoa: o que a parte autora ajuizou e pediu; o que o réu sustentou em contestação (com o acervo documental); e o que a sentença decidiu, **item por item**. Fecha com a transição padrão: `Conforme se verifica, muito embora o r. Juízo a quo profira suas decisões habitualmente com acerto, deixou de observar fatos relevantes delineados no processo, [...], de modo que se requer a reforma da sentença, pelas razões a seguir expostas.`
9. **DO MÉRITO** — uma ou mais subseções de tese (ver `teses.md` e item 3 abaixo). Cada subseção tem título próprio em caixa alta descrevendo o erro atacado.
10. **DA AUSÊNCIA DE CABIMENTO DE INDENIZAÇÃO POR DANOS MORAIS** (e/ou MATERIAIS) — tese de afastamento do dano.
11. *(condicional)* **DO PEDIDO SUBSIDIÁRIO - DA REDUÇÃO DOS DANOS MORAIS PLEITEADOS** — minoração, caso mantida a condenação.
12. *(condicional)* **DA AUSÊNCIA DE CABIMENTO DE INDENIZAÇÃO POR DANOS MATERIAIS** — quando houver condenação material a atacar.
13. **DOS PEDIDOS** — `Pelo acima descrito, requer seja o presente RECURSO aceito e julgado PROCEDENTE, para reforma da r. Sentença, julgando improcedente a ação [...]`. Inclui o pedido subsidiário de minoração quando houver, e, se for o caso, o pedido de que as publicações saiam em nome do patrono.
14. **Fecho** — `Termos em que, pede deferimento.` + `[Cidade]/[UF], [data por extenso].` + nome do advogado + `OAB/[UF] nº [...]`.

A numeração das seções pode ser arábica (`3. DO MÉRITO`, `3.1.`, `4.2`) ou apenas títulos em caixa alta — ambos os padrões aparecem nos modelos; escolha um e mantenha a consistência.

## 2. Voz e registro

- Linguagem jurídica formal, assertiva e técnica, em **prosa corrida** (sem bullets dentro da peça; a única enumeração admitida é a romana `(i)`, `(ii)`, `(iii)` ao listar elementos ou os incisos legais transcritos).
- Terceira pessoa. O réu é `o PicPay` / `a Recorrente` / `este Réu`; o autor é `o Recorrido` / `a Recorrida` / `a parte autora`. Ajuste o gênero ao caso.
- Vocativos e conectores do escritório: `Ab initio`, `Prima facie`, `Data venia` / `Data maxima venia`, `Nobres Julgadores`, `Colenda Turma Recursal`, `Excelência`, `Vejamos`, `Pois bem`, `com a devida vênia`, `Dessa forma`, `Destarte`, `Ante o exposto`.
- Tom: respeitoso com o juízo a quo (`muito embora profira suas decisões habitualmente com acerto`), mas firme ao apontar o erro. Nunca agressivo ou irônico com o magistrado.
- Fundamentos recorrentes: CDC art. 6º e 14 (e §3º, I e II); CPC art. 373, art. 489 §1º IV; CC arts. 186, 187, 188 I, 422; súmulas 479, 548, 385 do STJ; boa-fé objetiva; vedação ao *venire contra factum proprium* e à *reformatio in pejus*.

## 3. Arquitetura de cada tese de mérito (a "ultra-análise" em ação)

Esta é a assinatura do escritório. **Cada subseção de mérito segue, em prosa, esta progressão de seis movimentos:**

1. **Identifica o erro da sentença.** Abre com `A r. sentença recorrida [...]` descrevendo, com precisão, o equívoco do julgado (aplicou X automaticamente, confundiu Y, ignorou Z).
2. **Enuncia a tese da Recorrente.** `A tese ora defendida é [...]` / `A tese da Recorrente é simples e juridicamente sólida: [...]` — em uma ou duas frases límpidas.
3. **Aplica ao caso concreto, ancorada nos autos.** `No caso concreto, [...]` desfia os dados do processo (IDs, datas, valores, beneficiários, biometria, cláusulas, protocolos, Reason Code) demonstrando a tese. É aqui que mora a força: fatos amarrados a documentos.
4. **Transcreve o dispositivo legal/sumular.** Reproduz literalmente o artigo do CDC/CPC/CC ou a súmula, recuado, e explica seu pressuposto.
5. **Transcreve jurisprudência com ponte de aplicação.** Cola a ementa (STJ ou Tribunal pertinente) e, logo após, faz a ponte: `O precedente aplica-se à hipótese dos autos porque [...]`. Nunca deixe uma ementa solta.
6. **Fecha pedindo a reforma daquele ponto.** `Dessa forma, [...], impõe-se a reforma da r. sentença para [...]`.

Nem toda tese precisa dos seis movimentos completos, mas o **1 → 2 → 3 → 6** é obrigatório. A jurisprudência e a transcrição legal entram quando reforçam a tese.

## 4. Checklist final antes de entregar

- [ ] Endereçamento ao juízo prolator, com comarca/UF corretos.
- [ ] Recorrente = pessoa jurídica efetivamente ré e condenada (confira se é PicPay ou outro).
- [ ] Tempestividade com a data real de intimação e contagem em dias úteis.
- [ ] Síntese narra os pedidos da inicial e **cada item** da sentença recorrida.
- [ ] Toda data, valor, ID, CNPJ, beneficiário, cláusula e protocolo batem com os autos — nada inventado.
- [ ] Cada tese de mérito ataca um **erro concreto** da sentença e termina pedindo a reforma do ponto.
- [ ] Cada ementa transcrita tem a frase-ponte de aplicação ao caso.
- [ ] Ordem das seções correta; dano moral antes do subsidiário de minoração.
- [ ] Pedido final: reforma integral + (subsidiário) minoração.
- [ ] Fecho com cidade, data, advogado e OAB/UF compatível.
- [ ] Nenhum dado dos modelos-exemplo (nomes, IDs, Reason Codes) vazou para a peça real.
