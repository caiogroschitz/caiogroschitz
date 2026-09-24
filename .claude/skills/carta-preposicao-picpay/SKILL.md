---
name: carta-preposicao-picpay
description: >-
  Preenche automaticamente a CARTA DE PREPOSIÇÃO do PicPay (PicPay Instituição
  de Pagamento S.A.) a partir dos dados do preposto/correspondente e da
  audiência, devolvendo a carta pronta no chat. Use SEMPRE que o usuário pedir
  para "fazer/preencher/gerar a carta de preposição", "carta de preposto",
  "nomear preposto", "preposto para a audiência", ou simplesmente enviar os
  dados de um correspondente (nome + CPF) junto de um processo/audiência do
  PicPay para protocolar. Também aciona quando o usuário cola apenas "nome,
  CPF, processo, data e hora da audiência" no contexto PicPay e espera a carta
  formatada. NÃO use para procuração ad judicia, substabelecimento, contestação
  ou outras peças (cada uma tem fluxo próprio).
---

# Carta de Preposição PicPay

Esta skill gera a carta de preposição do PicPay no formato fixo do escritório,
preenchendo apenas os campos variáveis. A outorgante (PicPay) e os poderes são
fixos; o que muda a cada caso é o preposto, o processo, a audiência e o local
do fecho. A saída é texto no chat, pronto para copiar.

## O que é fixo (nunca alterar)

- **Outorgante:** PICPAY INSTITUIÇÃO DE PAGAMENTO S.A, empresa regularmente
  inscrita no CNPJ/ME sob o nº 22.896.431/0001-10, com sede na Avenida Manuel
  Bandeira, nº 291, Vila Leopoldina, na cidade de São Paulo - SP, CEP
  05317-020.
- **Poderes:** "podendo praticar os atos que se fizerem necessário,
  especialmente prestar depoimento pessoal, apresentar documentos, transigir,
  assinar recibos, receber e dar quitação."

## Campos variáveis (o usuário fornece)

| Campo | Exemplo | Observação |
|---|---|---|
| Nome do preposto | ANTONIO JULIO COSTA | Em maiúsculas, como no modelo |
| CPF do preposto | 391.020.256-04 | Formato 000.000.000-00 |
| Nº do processo | 5000273-70.2026.8.13.0477 | |
| Data da audiência | 25/03/2026 | Numérico DD/MM/AAAA |
| Hora da audiência | 13:00 | HH:MM |
| Cidade/UF do fecho | São Paulo/SP | Variável (costuma ser a cidade da comarca) |

## Regras de preenchimento

1. **Data da carta = data da audiência, por extenso.** A linha de fecho usa a
   mesma data da audiência, escrita por extenso e com o mês em minúsculas. Ex.:
   audiência em 25/03/2026 vira "25 de março de 2026". Converta sempre o mês
   numérico para o nome por extenso.
2. **Local do fecho é variável.** Use a cidade/UF que o usuário informar. Se
   ele não informar, use a cidade da comarca do processo (se já estiver no
   contexto da conversa) e, na dúvida, pergunte antes de fechar.
3. **Concorde o gênero do preposto.** Se o preposto for mulher, ajuste
   "inscrito" para "inscrita" e "como PREPOSTO" para "como PREPOSTA". Se houver
   dúvida de gênero pelo nome, mantenha o masculino do modelo, mas é melhor
   confirmar.
4. **Não invente dados.** CPF, número de processo, data e hora têm que vir
   exatamente do que o usuário mandou ou do que já consta nos autos juntados na
   conversa. Se faltar algum campo essencial (nome, CPF, processo, data ou hora
   da audiência), pergunte de forma agrupada e objetiva antes de gerar. Nunca
   preencha por suposição.
5. **Reaproveite o contexto.** Se o processo, a data e a hora da audiência já
   aparecem na conversa (por exemplo, numa intimação ou nos autos já lidos),
   use-os direto e peça ao usuário só o que falta, normalmente nome e CPF do
   preposto.
6. **Vários de uma vez.** Se o usuário mandar dados de mais de um preposto ou
   de mais de um processo, gere uma carta separada para cada, na mesma ordem em
   que foram enviados.
7. **Normalize a pontuação do CNPJ.** Escreva "nº 22.896.431/0001-10" com
   espaço após "nº" (o modelo às vezes vem sem espaço).

## Formato de saída (exato)

Reproduza este texto, substituindo apenas o que está entre colchetes. Mantenha
o parágrafo único corrido, sem travessão e sem alterar a redação fixa.

```
CARTA DE PREPOSIÇÃO

PICPAY INSTITUIÇÃO DE PAGAMENTO S.A, empresa regularmente inscrita no CNPJ/ME sob o nº 22.896.431/0001-10, com sede na Avenida Manuel Bandeira, nº 291, Vila Leopoldina, na cidade de São Paulo - SP, CEP 05317-020, [NOME DO PREPOSTO], inscrito no CPF/MF sob o nº [CPF], como PREPOSTO para a audiência a ser realizada no dia [DD/MM/AAAA] às [HH:MM], referente ao processo n° [Nº DO PROCESSO], podendo praticar os atos que se fizerem necessário, especialmente prestar depoimento pessoal, apresentar documentos, transigir, assinar recibos, receber e dar quitação.

[CIDADE]/[UF], [DIA] de [mês por extenso] de [ANO]
```

## Exemplo

Entrada do usuário: "preposto: Antonio Julio Costa, CPF 391.020.256-04,
processo 5000273-70.2026.8.13.0477, audiência 25/03/2026 às 13:00, comarca
Sete Lagoas/MG"

Saída:

```
CARTA DE PREPOSIÇÃO

PICPAY INSTITUIÇÃO DE PAGAMENTO S.A, empresa regularmente inscrita no CNPJ/ME sob o nº 22.896.431/0001-10, com sede na Avenida Manuel Bandeira, nº 291, Vila Leopoldina, na cidade de São Paulo - SP, CEP 05317-020, ANTONIO JULIO COSTA, inscrito no CPF/MF sob o nº 391.020.256-04, como PREPOSTO para a audiência a ser realizada no dia 25/03/2026 às 13:00, referente ao processo n° 5000273-70.2026.8.13.0477, podendo praticar os atos que se fizerem necessário, especialmente prestar depoimento pessoal, apresentar documentos, transigir, assinar recibos, receber e dar quitação.

Sete Lagoas/MG, 25 de março de 2026
```
