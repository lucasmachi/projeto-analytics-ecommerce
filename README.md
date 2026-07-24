# Olist E-commerce Analytics

Este projeto foi desenvolvido com o objetivo de analisar o comportamento de compra, faturamento, logística, retenção de clientes e eficiência operacional da **Olist** (maior integradora de marketplaces do Brasil), utilizando dados reais disponíveis no Kaggle. 

O foco do projeto abrange desde a infraestrutura de dados em nuvem até a validação estatística formal de hipóteses de negócio, utilizando boas práticas de engenharia de software (código modularizado).

---

##  Tecnologias e Infraestrutura
*   **Google Cloud Platform (GCP):** Hospedagem e armazenamento do Data Lakehouse.
*   **BigQuery:** Manipulação, saneamento e consultas analíticas complexas via SQL.
*   **Python + Pandas:** Conexão direta com a nuvem (via IAM Service Account do GCP), manipulação de dados e engenharia de features.
*   **SciPy & Statsmodels:** Aplicação de testes estatísticos paramétricos para validação formal de hipóteses.
*   **Matplotlib & Seaborn:** Geração de inteligência visual (EDA) modularizada.
*   **WSL 2 (Ubuntu no Windows):** Ambiente de desenvolvimento focado em padrão de produção Linux.

---

## Principais Insights de Negócio Gerados

1.  **Sazonalidade e Histórico:** Identificação de anomalias no histórico de dados contrapostas a uma clara tendência de crescimento no faturamento mensal global.
2.  **Volume vs. Valor:** A categoria *Cama, Mesa e Banho* lidera disparada em volume físico de pedidos, porém a categoria *Beleza e Saúde* é o verdadeiro motor de faturamento devido ao maior ticket médio.
3.  **Geomarketing & Logística:** Consumidores do Norte/Nordeste (ex: Paraíba) possuem os maiores tickets médios por pedido, indicando propensão a inflar carrinhos para otimizar o frete.
4.  **Concentração de Mercado:** Através de *Window Functions* no SQL, identificou-se que o estado de SP concentra sozinho **37%** do faturamento total, com a região Sudeste representando mais de 50% de todas as transações.
5.  **Retenção Crítica (Churn):** Análise via função `LAG()` revelou um modelo predominantemente *one-time buyer* (apenas ~3.000 recompras em 100k pedidos), com janela média de recomposição de **79 dias**.

---

## 🔬 Validação Estatística de Hipóteses (A/B & Inferência)

Para além da análise descritiva, o projeto aplica testes estatísticos formais para garantir decisões baseadas em evidências:

*   **Diferença de Ticket Médio por Categoria (Teste T de Welch):**
    *   *Hipótese:* Avaliar se a diferença de gasto médio entre *Beleza e Saúde* e *Cama, Mesa e Banho* é estatisticamente significante.
    *   *Resultado:* Confirmado com 95% de confiança que a categoria *Beleza e Saúde* gera maior valor financeiro por pedido transacionado.
*   **Gargalo Logístico Regional (Teste Z de Proporções):**
    *   *Hipótese:* Comparar a proporção de entregas com atraso entre os dois maiores mercados (SP vs. RJ).
    *   *Resultado:* O Rio de Janeiro apresenta uma taxa de atraso de **13,47%** contra apenas **5,89%** de São Paulo, provando uma falha logística estrutural no estado do RJ.

---

## 📂 Estrutura do Projeto Modular

```text
├── main.py                     # Script orquestrador da carga GCP e execução dos plots
├── graficos.py                 # Funções modularizadas para visualização de dados
├── teste_hipotese.py           # Aplicação do Teste T de Welch (Ticket Médio)
├── teste_ab_logistica.py       # Aplicação do Teste Z de Proporções (Atrasos SP vs RJ)
├── sazonalidade_faturamento.png #Gráficos
├── ticket_medio_por_estado.png
├── correlacao_preco_frete.png
└── .gitignore                  # Proteção de credenciais GCP e datasets pesados
