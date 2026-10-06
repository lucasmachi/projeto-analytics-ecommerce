# Olist E-commerce Analytics | Predictive Modeling

Este projeto foi desenvolvido com o objetivo de analisar o comportamento de compra, faturamento, logística, retenção de clientes, eficiência operacional e **previsão de vendas (Machine Learning)** da **Olist** (maior integradora de marketplaces do Brasil), utilizando dados reais disponíveis no Kaggle. 

O foco do projeto abrange desde a infraestrutura de dados em nuvem e validação estatística formal de hipóteses de negócio até a **modelagem preditiva poliglota (Python e R)** utilizando boas práticas de engenharia de software e análise temporal.

---

## Tecnologias e Infraestrutura

*   **Google Cloud Platform (GCP):** Hospedagem e armazenamento do Data Lakehouse.
*   **BigQuery:** Manipulação, saneamento e consultas analíticas via SQL.
*   **Python + Pandas:** Conexão direta com a nuvem (via IAM Service Account do GCP), manipulação de dados e engenharia de features.
*   **R + Tidyverse (`dplyr` & `ggplot2`):** Análise exploratória de dados e visualizações idiomáticas avançadas.
*   **Machine Learning & Séries Temporais:** `scikit-learn` (Linear Regression, Random Forest) e `prophet` (Meta Data Science) para previsão de faturamento e tendências.
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

## Validação Estatística de Hipóteses (A/B e Inferência)

Para além da análise descritiva, o projeto aplica testes estatísticos formais para garantir decisões baseadas em evidências:

### Preço médio por item e categoria — teste t de Welch

- **Pergunta:** o preço médio por item difere entre Beleza e Saúde e Cama, Mesa e Banho?
- **Método:** teste t de Welch bilateral, comparando preços por item sem assumir variâncias populacionais iguais.
- **Resultado relatado anteriormente:** diferença estatisticamente significativa ao nível de 5%, com maior média amostral em Beleza e Saúde.
- **Escopo:** a consulta compara preços individuais dos itens, não valores totais por pedido, e não filtra os pedidos pelo status de entrega.
- **Limitação:** o teste pressupõe observações independentes. Itens do mesmo pedido ou anúncios repetidos podem violar essa condição.

---

## Análise Exploratória de Dados em R (`dplyr` + `ggplot2`)

Como demonstração de versatilidade entre ecossistemas de dados (Python/R), parte da análise exploratória foi replicada em **R**:
*   Utilização do operador pipe (`%>%`) e `lubridate` para tratamento e agregação de séries temporais.
*   Geração de gráficos customizados de faturamento mensal e top categorias de produtos utilizando `ggplot2`.

---

## Machine Learning e Previsão de Tendências

Construção e avaliação de modelos preditivos para estimar o faturamento diário do e-commerce com foco em **curto prazo (operacional)** e **longo prazo (estratégico)**.

### Feature Engineering & Estratégia de Validação
*   **Agregação Diária:** Construção de série temporal diária sem lacunas (`asfreq('D')`).
*   **Engenharia de Lags:** Criação de variáveis temporais ($t-1$, $t-7$, $t-14$) e Médias Móveis (7 e 14 dias) com `shift(1)` rigoroso para prevenção de *Data Leakage*.
*   **Divisão Temporal:** Avaliação nos últimos 60 dias do histórico (respeitando a linha do tempo, sem embaralhamento aleatório).

### Comparativo de Desempenho dos Modelos

| **Regressão Linear** | Tabular / Baseline | **R$ 5.163,81** | **R$ 6.476,80** | **Melhor modelo para curto prazo** (planejamento operacional de estoque/caixa em 7–15 dias). |
| **Random Forest** | Árvores | R$ 5.206,60 | R$ 6.796,30 | Bom desempenho, mas propenso a pequenas oscilações em séries temporais médias. |
| **Prophet (Meta)** | Série Temporal | R$ 8.743,44 | R$ 11.183,64 | **Visão estratégica de longo prazo** (decomposição de tendência, sazonalidade e efeito de feriados). |

### Insights da Modelagem
1.  Modelos lineares baseados em *lags* recentes superaram abordagens mais complexas para a previsão diária imediata.
2.  O Prophet destaca-se pela transparência na decomposição da série, identificando picos semanais (segunda/terça-feira) e sazonais. Melhor utilizado para previsões anuais.

---

## Estrutura do Projeto

```text
├── main.py                     # Script orquestrador da carga GCP e execução dos plots em Python
├── eda.R                       # Script em R (dplyr + ggplot2) replicando análises chave
├── ml_sales_prediction.py      # Pipeline completo de ML (Scikit-Learn + Prophet) e métricas
├── graficos.py                 # Funções modularizadas para visualização de dados
├── teste_hipotese.py           # Aplicação do Teste T de Welch (preços médios por item)
├── teste_ab_logistica.py       # Aplicação do Teste Z de Proporções (Atrasos SP vs RJ)
├── comparativo_modelos.png     # Gráfico comparativo dos 3 modelos de ML
├── sazonalidade_faturamento.png
├── ticket_medio_por_estado.png
├── correlacao_preco_frete.png
└── .gitignore                  # Proteção de credenciais GCP e datasets pesados
