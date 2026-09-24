# Causa Raiz (CR1 -> CR2 -> CR3 -> CR4)

A Causa Raiz identifica o motivo fatico do litigio. Rol taxativo, hierarquia de ate 4 niveis.
Base atual PicPay: 262 combinacoes, 11 BUs, 13 Centros de Custo (VCs), ~50 produtos, 127 CR1 e 28 CR2.

- **CR1 sempre obrigatoria.**
- **CR2 apenas quando aplicavel** (35 das 262 combinacoes), tipicamente para fraude, golpe, cashback, instabilidade sistemica e analogos.
- Arvore completa oficial: arquivo "SANEAMENTO CAUSA RAIZ - VERSAO FINAL", mantido pela coordenacao.
- Se nenhuma combinacao refletir o caso, **NAO inventar** -- sinalizar a coordenacao BFAP.

## Panorama por Business Unit (BU)

### BU EMPRESTIMOS
Produtos: Consignado, Credito Pessoal, Credito Trabalhador, FGTS - Saque Aniversario, Clube do Emprestimo, Cartao Consignado.
CR1 frequentes: Cancelamento, Cobranca Indevida, Condicoes Contratuais, Contrato Nao Reconhecido, Credito Nao Disponibilizado, Desconto Indevido, Divida Prescrita, Duplicidade de Desconto, Exibicao de Documentos, Fraude (CR2 "Contrato Nao Reconhecido"), Inadimplencia do Tomador, Instabilidade Sistemica, Limitacao de Descontos, Negativacao Indevida, Portabilidade Negada/Cancelada, Refinanciamento Nao Reconhecido, Registro SCR, Revisional, Superendividamento, Tarifas.

### BU WALLET
Produtos: Conta, Pix, Boleto, CDB Banking, Cofrinho.
CR1 frequentes: Bloqueio de Conta, Boleto Cobrado em Duplicidade, Boleto Recusado/Devolvido, Cashback (CR2: Publicidade Enganosa, Credito Expirado, Nao Recebido, Atraso na Disponibilizacao), Chargeback - Boletos, Chave (CR2: Transacao para Chave Incorreta, Alerta de Suspeita de Fraude), Compensacao/Falha no Repasse do Boleto, Debito Automatico, Debito Veiculares, Divergencia em Calculo de Rendimento, Encerramento de Conta, Exibicao de Documentos, Falha na Solicitacao de Abertura de Conta, Fraude (CR2: Conta Nao Reconhecida, Conta Pre-Existente, Pagamento por Aproximacao), Golpe (CR2: Falso Produto, Falso Investimento, Boa Noite Cinderela, Invasao de Conta, Engenharia Social, Falso Advogado, Falsa Central, Boleto Adulterado, Troca de Cartao, Maquininha), Instabilidade Sistemica (CR2 "Falhas nas Transacoes"), Nao Concorda com Rentabilidade, Nao Consegue Resgatar, Nome Social (CR2 "Impacto Reputacional"), OpenFinance (CR2 "Falha na Prestacao de Servicos"), Saque Digital (CR2 "QR Code"), Superendividamento, Tarifas, Tarifas de Boleto.

### BU CARDS
Produtos: PicPay Card, Cartao, Limite Garantido.
CR1 frequentes: vinculadas a dinamica do cartao (negativacao, cobranca indevida, transacao negada, ajuste de limite, etc.). Consultar a arvore completa.

### BU SEGUROS
Produtos: Seguro Residencial, Seguro Prestamista (Consignado CDT / Credito Pessoal), Assistencia Saude, Assistencia Residencial, Auxilio Medicamento, Seguro Renda Protegida - FGTS, Seguro Emprestimo Pessoal, Seguro Fatura Protegida, Seguro Vida, Seguro Protecao Celular.
CR1 frequentes: contratacao, cobranca, cobertura e cancelamento.

### BU PESSOA JURIDICA
Produtos: Maquininha, Link de Pagamento, QR Code Fisico, E-commerce, Marketplace, 1-Click, Antecipacao, Aluguel, Cadastro PJ e outros da aceitacao PJ.
**Maior volume: 77 linhas cadastradas.**

### Demais BUs
- COBRANCA - Recuperacao de Clientes (10 combinacoes).
- STORE - Shop AE (10 combinacoes).
- BENEFICIOS - Beneficios PJ / Cartao Beneficio (7 combinacoes).
- INVEST - Invest PF / Investimento (5 combinacoes).
- CRYPTO - Criptomoedas e Digital Goods (3 combinacoes).
- JURIDICO - Juridico Corporativo (1) e OpenFinance (1).

## Combinacoes com CR2 obrigatoria (as 35)
- **Fraude** -> "Contrato Nao Reconhecido", "Conta Nao Reconhecida", "Conta Pre-Existente", "Pagamento por Aproximacao".
- **Golpe** -> tipologia especifica (Falso Produto, Falso Investimento, Boa Noite Cinderela, Invasao de Conta, Engenharia Social, Falso Advogado, Falsa Central, Boleto Adulterado, Troca de Cartao, Maquininha).
- **Cashback** -> "Publicidade Enganosa", "Credito Expirado", "Nao Recebido", "Atraso na Disponibilizacao".
- **Chave Pix** -> "Transacao para Chave Incorreta" ou "Alerta de Suspeita de Fraude".
- **Instabilidade Sistemica** -> "Falha nas Transacoes".
- **Nome Social** -> "Impacto Reputacional".
- **Saque Digital** -> "QR Code".
- **OpenFinance** -> "Falha na Prestacao de Servicos".
