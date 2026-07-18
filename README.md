# Olist E-commerce Analytics 🚀

Este projeto foi desenvolvido com o objetivo de analisar o comportamento de compra, faturamento, logística e retenção de clientes da **Olist** (maior integradora de marketplaces do Brasil), utilizando dados reais disponíveis no Kaggle. 

O foco principal do projeto foi integrar uma infraestrutura moderna de dados em nuvem com análises locais robustas utilizando boas práticas de engenharia de software (código modularizado).

## 🛠️ Tecnologias e Infraestrutura
*   **Google Cloud Platform (GCP):** Hospedagem e armazenamento dos dados.
*   **BigQuery:** Criação do Data Lakehouse, saneamento e consultas analíticas complexas via SQL.
*   **Python + Pandas:** Conexão direta com a nuvem (via chaves de Conta de Serviço/IAM do Google), manipulação de dados e engenharia de features.
*   **Matplotlib & Seaborn:** Geração de inteligência visual (EDA) para tomada de decisão.
*   **WSL 2 (Ubuntu no Windows):** Ambiente de desenvolvimento ágil simulando servidores de produção Linux.

---

## 📈 Principais Insights de Negócio Gerados

1.  **Sazonalidade e Histórico:** Identificação de anomalias no histórico de dados (como o início incompleto da operação no fim de 2016 e quedas pontuais em meados de 2017) contrapostas a uma clara tendência de crescimento no faturamento mensal global.
2.  **Volume vs. Valor:** A categoria *Cama, Mesa e Banho* lidera disparada em volume físico de pedidos, porém a categoria *Beleza e Saúde* é o verdadeiro motor de faturamento da empresa devido ao maior ticket médio dos produtos.
3.  **Geomarketing & Logística:** Estados fora do eixo Sudeste (como a Paraíba) possuem os maiores tickets médios por pedido. Isso indica que consumidores do Norte/Nordeste tendem a inflar seus carrinhos para diluir o custo e a espera do frete de longa distância.
4.  **Concentração de Mercado:** Utilizando *Window Functions* no SQL, foi mapeado que o estado de São Paulo concentra sozinho **37%** do faturamento da empresa, e a região SP-RJ-MG domina mais de **50%** de todo o e-commerce, escancarando uma forte dependência geográfica.
5.  **Retenção Crítica (Churn):** Análise avançada com a função `LAG()` revelou que a Olist opera no modelo *one-time buyer* (apenas ~3.000 recompras em um universo de 100k pedidos). Quem recompra demora, em média, **79 dias**, indicando uma necessidade urgente de estratégias de CRM/fidelização.

---

## 📂 Estrutura do Projeto Modular
Para garantir manutenibilidade e clean code, a extração de dados e a geração de gráficos foram separadas em scripts independentes coordenados por um arquivo mestre:

*   `main.py`: Conecta no BigQuery, baixa os DataFrames e orquestra a execução.
*   `grafico_sazonalidade.py`: Gera a análise temporal de faturamento.
*   `grafico_ticket.py`: Plota o comportamento do ticket médio por UF.
*   `grafico_correlation.py`: Avalia o impacto do preço do produto no frete cobrado.
