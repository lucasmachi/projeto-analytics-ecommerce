# Olist E-commerce Analytics | Predictive Modeling

[Leia em Português (Brasil)](./LEIAME.md)

This project explores revenue, purchasing behavior, logistics, customer retention, and sales forecasting using publicly available Olist e-commerce data from Kaggle.

The workflow combines cloud-based data processing, SQL analysis, statistical hypothesis testing, and predictive modeling in Python and R. Its goal is to turn historical transaction data into insights that support commercial and operational decisions.

---

## Technologies and Infrastructure

- **Google Cloud Platform (GCP):** cloud data storage and infrastructure.
- **BigQuery and SQL:** data cleaning, analytical queries, aggregations, and window functions.
- **Python and Pandas:** GCP integration through an IAM service account, data manipulation, and feature engineering.
- **R and Tidyverse (`dplyr` and `ggplot2`):** exploratory data analysis and visualization.
- **lubridate:** date handling and time-based aggregation in R.
- **scikit-learn:** Linear Regression and Random Forest models.
- **Prophet:** time series modeling, trend analysis, and seasonality decomposition.
- **SciPy and Statsmodels:** statistical hypothesis testing.
- **Matplotlib and Seaborn:** modular data visualization.
- **WSL 2 with Ubuntu:** Linux development environment on Windows.

## Key Business Insights

1. **Revenue trends:** the analysis identified growth in monthly revenue alongside unusual patterns in the historical data that require attention to data coverage and quality.
2. **Volume versus value:** Bed, Bath & Table leads in order volume, while Health & Beauty leads in revenue in the reported analysis, with a higher average order value.
3. **Geography and purchasing behavior:** states in the North and Northeast, such as Paraíba, show high average order values. Larger baskets as a way to offset shipping costs are a possible explanation to investigate, rather than a demonstrated customer motivation.
4. **Market concentration:** SQL window functions showed that São Paulo accounts for approximately **37% of total revenue**, while the Southeast represents more than **50% of transactions**.
5. **Repeat purchases:** analysis using `LAG()` identified approximately **3,000 repeat purchases across 100,000 orders**, with an average interval of **79 days** between repeat purchases. This suggests limited repeat purchasing within the observed period; it is not, by itself, a churn rate.

## Statistical Hypothesis Testing

The project goes beyond descriptive analysis by comparing groups within historical transaction data. These are observational comparisons, not randomized A/B experiments.

### Average Order Value by Category — Welch's t-test

- **Question:** does average spending per order differ between Health & Beauty and Bed, Bath & Table?
- **Method:** Welch's t-test for comparing means.
- **Reported result:** a statistically significant difference at the 5% significance level, with higher average spending in Health & Beauty.

### Delivery Delays by State — Two-proportion z-test

- **Question:** do late-delivery rates differ between São Paulo and Rio de Janeiro?
- **Method:** a z-test comparing two proportions.
- **Observed rates:** **13.47% in Rio de Janeiro** versus **5.89% in São Paulo**, a difference of **7.58 percentage points**.
- **Interpretation:** the observed difference highlights an opportunity to investigate logistics in Rio de Janeiro. This comparison alone does not establish the causes of delays or prove a structural logistics failure.

## Exploratory Data Analysis in R

Selected analyses were replicated in R to explore the same business questions across the Python and R ecosystems:

- Data transformation and aggregation with `dplyr` and the pipe operator (`%>%`).
- Date handling and time series aggregation with `lubridate`.
- Customized monthly revenue and top-category charts with `ggplot2`.

## Machine Learning and Revenue Forecasting

The project compares predictive models for daily e-commerce revenue using historical sales and time-based features.

### Feature Engineering and Validation

- **Daily frequency:** the time series is organized with `asfreq('D')`. Missing dates become explicit; handling missing values requires considering the dataset's coverage.
- **Lag features:** revenue values from 1, 7, and 14 days earlier.
- **Rolling averages:** 7-day and 14-day windows shifted with `shift(1)` to prevent the target day's revenue from entering its own predictors.
- **Temporal split:** evaluation on the final **60 days** of the historical dataset, preserving chronological order without random shuffling.

### Model Performance

The following metrics measure prediction errors for daily revenue during the 60-day test period. Both are expressed in Brazilian reais (BRL); lower values indicate smaller errors.

| Model | Approach | MAE (BRL) | RMSE (BRL) | Evaluation result |
| --- | --- | ---: | ---: | --- |
| **Linear Regression** | Tabular baseline | **5,163.81** | **6,476.80** | Lowest errors among the evaluated models. |
| **Random Forest** | Tree ensemble | 5,206.60 | 6,796.30 | Performance close to Linear Regression. |
| **Prophet** | Time series model | 8,743.44 | 11,183.64 | Higher errors over the evaluated period. |

- **MAE (Mean Absolute Error):** the average absolute difference between predicted and actual daily revenue. For Linear Regression, predictions differed from actual revenue by BRL 5,163.81 per day on average during the test period.
- **RMSE (Root Mean Squared Error):** a measure of error that gives greater weight to large deviations. It remains in the same unit as revenue.

These metrics measure the size of errors, not whether the models consistently overpredict or underpredict. They are not percentage errors or the total error accumulated over 60 days.

### Modeling Insights

1. Linear Regression with lag-based features achieved the lowest MAE and RMSE in the evaluated period, demonstrating the value of a simple baseline.
2. Random Forest produced similar results but did not outperform Linear Regression on either reported metric.
3. Prophet provides interpretable trend and seasonality components. The reported analysis identified weekly peaks on Mondays and Tuesdays, but the results above do not establish superior performance for annual forecasts.
4. A 60-day test period is not necessarily a 60-day-ahead forecast. Performance at specific horizons, such as 7, 15, or 365 days, requires a corresponding evaluation that accounts for which lag values would be available when each prediction is made.

## Project Structure

```text
├── README.md                    # Main documentation in English
├── LEIAME.md                    # Documentation in Brazilian Portuguese
├── main.py                      # GCP integration and Python chart orchestration
├── eda.R                        # Exploratory analysis in R
├── ml_sales_prediction.py       # Predictive models and performance evaluation
├── graficos.py                  # Modular visualization functions
├── teste_hipotese.py             # Welch's t-test for average order value
├── teste_ab_logistica.py         # Two-proportion z-test for SP vs. RJ delays
├── comparativo_modelos.png       # Model comparison chart
├── sazonalidade_faturamento.png
├── ticket_medio_por_estado.png
├── correlacao_preco_frete.png
└── .gitignore                   # Excludes credentials and local data files
```

## Scope and Limitations

The findings describe the historical dataset and the period analyzed, rather than Olist's current operations.

Differences across states and categories may reflect factors such as order composition, delivery distance, and seller profiles. Statistical comparisons can help assess differences between groups but do not establish causality on their own.

Using the forecasts for inventory or cash-flow planning requires validation at the intended forecast horizon and ongoing monitoring of prediction errors.
