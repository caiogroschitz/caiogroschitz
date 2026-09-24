# Peticionamento 30 dias

Gera, no timbrado do escritório, as minutas de impulso dos processos parados há mais de 30 dias de um responsável, a partir da planilha de saneamento (Astrea x Projuris). A conferência de cada caso no Astrea e o protocolo continuam sendo feitos por uma pessoa: o script não protocola nada e não altera nada no Astrea.

A planilha, o modelo `.docx` e as minutas geradas contêm dados de clientes e **não vão para o repositório**; quem cuida disso é o `.gitignore`.

## Instalação (uma vez)

```bash
pip install -r requirements.txt
```

## 1. Gerar o lote do responsável

```bash
python lote.py "Saneamento_Processos_Parados_30dias.xlsx" --responsavel "Caio Groschitz dos Santos Cruz"
```

O script lê a aba "Saneamento" e grava o `lote.csv`, com um processo por linha, do mais antigo para o mais recente. Processos que já têm algo na coluna "Peticionado?" ficam de fora. O nome do responsável precisa ser exato: a planilha tem, por exemplo, dois "Caio". Se o nome não bater, o script lista os nomes parecidos.

Ao rodar o script de novo, o que já foi preenchido no `lote.csv` é mantido.

## 2. Conferir no Astrea (uma aba só)

Para cada linha do `lote.csv`, busque o número do processo no Astrea, na mesma aba, e preencha:

| Coluna | O que colocar |
|---|---|
| `autor` | nome da parte autora, como aparece no título do caso (`PicPay X [Autor]`) |
| `enderecamento_astrea` | opcional: endereçamento completo, quando a vara/juizado que a planilha traz estiver incompleto (`[Nª]`, `[VARA/JUIZADO]`) |
| `status_astrea` | status e etiquetas relevantes |
| `obs_astrea` | divergência com a planilha (ex.: já sentenciado, suspenso, acordo) |

Regras para a execução com o navegador (Claude in Chrome ou Claude Code local):
- use uma única aba para todo o lote e feche-a no fim;
- tente cada processo uma vez só; se não abrir, anote "pendente" em `obs_astrea` e passe ao próximo;
- no Astrea, só leitura: nenhuma etiqueta, tarefa ou baixa é alterada;
- salve o `lote.csv` a cada processo, para que ele funcione como checkpoint.

## 3. Gerar as minutas

```bash
# piloto com um processo
python gerar_minutas.py lote.csv "Petição 6.docx" --pasta "G:/Meu Drive/Peticionamento 30 dias" --so 5001248-92.2025.8.08.0016

# lote inteiro
python gerar_minutas.py lote.csv "Petição 6.docx" --pasta "G:/Meu Drive/Peticionamento 30 dias"
```

Com o Google Drive para computador instalado, apontar `--pasta` para a pasta sincronizada salva direto no Drive. Se não estiver instalado, gere numa pasta local e envie as minutas pelo navegador.

- **Arquivo:** `{nº do processo} - petição de impulso.docx`. Uma minuta que já existe na pasta **não é refeita**; para refazer, apague o arquivo antes de rodar.
- **Controle:** `Controle - Peticionamento 30 dias.xlsx`, na mesma pasta, com a situação e as observações de cada processo. As cores indicam: verde, minuta pronta para revisão; amarelo, minuta com marcador a completar; vermelho, processo sem minuta, com pendência.
- **Data do fecho:** a de hoje. Outra data vai em `--data AAAA-MM-DD`.

### Conteúdo da minuta

- **Timbre e formatação:** cabeçalho, rodapé e fonte Prompt vêm do modelo. O corpo segue o padrão das peças do escritório: entrelinha 1,5, texto justificado, recuo de primeira linha e nomes em negrito.
- **Assinaturas:** Fernando de Almeida Prado Sampaio (OAB/SP 235.387) e Mario Thadeu Leme de Barros Filho, com a OAB do estado do processo: ES 39.165-S, MG 230.285-S (inclusive TRF6) e DF 75.486-S. Tribunal fora da tabela não gera minuta; o controle pede a inscrição.
- **Texto por providência:**

| Providência (planilha) | Pedido | Fundamento |
|---|---|---|
| Conclusão para sentença | conclusão para prolação de sentença | arts. 226 e 227 do CPC; art. 5º, LXXVIII, da CF; arts. 4º e 139, II, do CPC |
| Impulso oficial / Análise + impulso oficial | regular prosseguimento do feito | art. 5º, LXXVIII, da CF; arts. 4º e 139, II, do CPC |
| Designação de audiência | audiência ou julgamento antecipado | art. 355, I, do CPC |
| Recursal – impulso do julgamento | informações sobre a distribuição e a pauta; subsidiariamente, trânsito e baixa | art. 1.006 do CPC |
| Habilitação/cadastro nos autos | juntada de mandato e cadastro dos patronos | — |
| Acordo, Cumprimento (pagamento), Aguardar (suspenso/IRDR) | **sem minuta**: pendência no controle | — |

- **Marcadores:** o que não se sabe fica marcado e nada é inventado. São eles `[NOME DA PARTE AUTORA]`, `[Nª]` (vara sem número na planilha), `[VARA/JUIZADO]`, `[COMARCA]` e `[PARTE RÉ – CONFERIR NO ASTREA]`, este quando o cliente na planilha não é uma entidade PicPay.
- **Data de paralisação:** vem do último histórico do Astrea, que está na planilha, e deve ser conferida com a última movimentação nos autos.

## 4. Depois do protocolo

Na planilha do escritório, preencha "Peticionado?", "Data do peticionamento" e "Nº do protocolo" só depois de protocolar. A baixa da tarefa no Astrea também só vem depois do protocolo.
