---
name: recorte-provas-peticao
description: >-
  Recorta trechos de documentos (autos de processo, contestacao, contratos,
  extratos, prints, comprovantes) em imagens PNG individuais, uma por item,
  para o usuario colar na peticao como prova. Use SEMPRE que o usuario pedir
  para "recortar", "recorte onde esta X", "me traz os recortes", "print do
  documento", "destacar o trecho", "preciso colar essa prova na peticao",
  "separa cada documento em uma imagem", "extrai a parte onde aparece o
  cadastro / a biometria / o aparelho / a assinatura / o comprovante", ou
  enviar PDFs de um processo pedindo as provas recortadas. Tambem aciona
  quando, depois de redigir contestacao/peca, o usuario quer transformar
  cada documento citado no merito/preliminar em uma imagem separada para
  anexar. NAO use para redigir a peca em si (use redator-juridico-br) nem
  para juntar varios comprovantes numa imagem so quando o pedido for o
  contrario (separar em imagens individuais e o caso desta skill).
---

# Recorte de provas para peticao

Esta skill pega documentos em PDF e devolve **uma imagem PNG por item**, cada
uma com o trecho exato que sustenta um ponto da peca, recortada e limpa, pronta
para o advogado colar na petição. Nasceu do fluxo real: depois de redigir a
contestação, o cliente precisa colar, ao lado de cada argumento, o print do
documento que o prova (o cadastro, a biometria, o aparelho autorizado, a
assinatura do contrato, o comprovante, o extrato).

A regra de ouro: **cada item citado na peca vira uma imagem separada**, com
nome descritivo, fiel ao documento, sem inventar nada.

## Passo 0: Levantar a lista de itens

Antes de recortar, monte a lista do que precisa virar imagem. Duas situacoes:

1. O usuario ja redigiu a peca (preliminar/merito). Releia cada ponto e extraia
   todo documento citado como prova. Cada citacao documental e um recorte.
2. O usuario so descreve ("recorta o cadastro, a biometria, o aparelho, a
   assinatura, o comprovante"). Liste esses itens diretamente.

Se um item citado **nao tiver documento correspondente** nos arquivos enviados
(exemplo classico: a peca menciona o MED, mas nao ha tela de MED nos autos),
**avise o usuario e nao fabrique**. Pergunte se ele tem o documento ou se o
item deve sair da lista.

## Passo 1: Localizar cada item no PDF certo, na pagina certa

Para cada item, identifique o arquivo e a pagina onde o trecho aparece. Leia os
PDFs (Read em PDF, ou pdftotext) para confirmar pagina e conteudo. Nunca chute a
pagina: confirme que o texto-alvo esta ali.

## Passo 2: Calibrar o recorte (renderizar, olhar, cortar)

O recorte e por faixa vertical da pagina. O metodo confiavel:

1. Renderize a pagina inteira a 200 DPI e olhe (gere uma "folha de contato" com
   varias miniaturas quando houver muitas paginas, para enxergar o layout de uma
   vez). A4 a 200 DPI tem cerca de 1654x2339 px.
2. Escolha a faixa vertical do trecho: rect no formato `LARGURAxALTURA+0+TOPO`.
   Use a largura cheia da pagina e ajuste TOPO e ALTURA. O `-trim` do script
   remove a margem branca sobrando, entao pode ser generoso.
3. Gere o recorte e **veja o resultado**. Se cortou demais ou de menos, ajuste
   TOPO/ALTURA e refaca. Esse loop de conferencia e o que garante a precisao.

Para um trecho que ocupa a pagina toda (um extrato, um documento de identidade),
nao passe `rect`: o script usa a pagina inteira e so apara a margem.

## Passo 3: Gerar os recortes (use o script, de preferencia em lote)

O script `scripts/crop_doc.py` faz render + recorte + trim + borda branca, e
legenda opcional. Rode em lote para fazer todos de uma vez. Monte um `jobs.json`:

```json
[
  {"pdf":"dados_cadastrais.pdf","page":1,"rect":"1654x880+0+0","out":"01-cadastro-conta.png"},
  {"pdf":"prevencao.pdf","page":2,"rect":"1653x820+0+930","out":"04-dispositivo.png"},
  {"pdf":"ccb.pdf","page":5,"rect":"1653x680+0+110","out":"09-ccb-assinatura.png"},
  {"pdf":"autos.pdf","page":18,"out":"10-extrato.png"}
]
```

E execute (saida na pasta de entregaveis do usuario):

```bash
python scripts/crop_doc.py --batch jobs.json --outdir /caminho/para/outputs
```

Opcoes uteis por item: `"label":"Doc. 04 - dispositivo autorizado em 09/05/2026"`
escreve uma legenda no topo do recorte (bom para numerar como Doc. 01, Doc. 02);
`"dpi":300` para mais nitidez; `"rect"` ausente recorta a pagina inteira.

Nomeie os arquivos com numero + descricao curta (`04-dispositivo-autorizado.png`),
para o usuario saber na hora qual prova e qual.

## Passo 4: Conferir e entregar

Gere uma folha de contato com todos os recortes finais e confira que cada um
pegou o trecho certo. Refaca os que sairam tortos. Entregue ao usuario:

1. As imagens individuais (uma por item), via present_files.
2. Uma **tabela de mapeamento**: numero do recorte, o que mostra, documento de
   origem, e o ponto da peca (preliminar/merito) que ele sustenta. E essa tabela
   que permite ao advogado colar cada imagem ao lado do argumento certo.

## Privacidade e fidelidade

- Dados de terceiros (CPF, dados de colaboradores, contas recebedoras) devem ser
  mantidos **exatamente como aparecem no documento**, inclusive ja mascarados.
  Nao reconstrua um CPF de terceiro juntando partes de telas diferentes. Se a
  analise interna pedir tarja, tarje (cubra a regiao com um retangulo) antes de
  entregar.
- O rosto e o documento do proprio cliente podem ir aos autos, mas confirme com
  o usuario se quer manter ou tarjar.
- Nunca edite o conteudo do documento. Recorte e tarja de terceiros sao as unicas
  intervencoes. O valor probatorio depende da fidelidade ao original.

## Saidas comuns desta skill (mapa rapido de onde achar cada prova)

Em casos bancarios/PicPay e similares, os trechos mais pedidos costumam estar em:
cadastro e data de abertura da conta; historico de senha; identidade/biometria
facial; dispositivo/aparelho autorizado e a data da autorizacao; prova de vida;
conta recebedora do beneficiario; tela de negativacao (ou de ausencia dela);
dados do contrato/CCB na primeira folha; autenticacao da assinatura eletronica;
extrato das operacoes contestadas; e-mails e prints juntados pela parte; e os
comprovantes de transacao. Use isso so como guia de onde procurar, nunca como
substituto da leitura do documento real.
