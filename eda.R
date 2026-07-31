# ----------------------------------------------------------------------
# Semana 4: EDA Rápida em R (dplyr + ggplot2)
# Projeto: Analytics E-Commerce Olist
# ----------------------------------------------------------------------

install.packages("tidyverse", "lubridate")

# 1. Carregar Pacotes
library(tidyverse)
library(lubridate)

# 2. Carregar os Dados
orders <- read_csv("olist_orders_dataset.csv")
items  <- read_csv("olist_order_items_dataset.csv")

# 3. Tratamento Inicial e Join (Estilo dplyr)
df_sales <- orders %>%
  filter(order_status == "delivered") %>%
  inner_join(items, by = "order_id") %>%
  mutate(
    order_purchase_timestamp = ymd_hms(order_purchase_timestamp),
    year_month = floor_date(order_purchase_timestamp, "month")
  )

# ----------------------------------------------------------------------
# Análise 1: Evolução Mensal do Faturamento (Série Temporal)
# ----------------------------------------------------------------------
sales_monthly <- df_sales %>%
  group_by(year_month) %>%
  summarise(
    total_revenue = sum(price, na_rm = TRUE),
    total_orders  = n_distinct(order_id)
  ) %>%
  filter(year_month >= "2017-01-01" & year_month <= "2018-08-31")

# Gráfico 1: Evolução das Vendas Mensais
ggplot(sales_monthly, aes(x = year_month, y = total_revenue / 1e3)) +
  geom_line(color = "#2b5c8f", size = 1.2) +
  geom_point(color = "#2b5c8f", size = 2) +
  scale_y_continuous(labels = scales::dollar_format(prefix = "R$ ", suffix = "k")) +
  scale_x_date(date_labels = "%b/%Y", date_breaks = "2 months") +
  labs(
    title = "Evolução do Faturamento Mensal (Olist)",
    subtitle = "Período de Jan/2017 a Ago/2018",
    x = "Mês",
    y = "Faturamento (em R$ Milhares)",
    caption = "Fonte: Olist Dataset"
  ) +
  theme_minimal() +
  theme(plot.title = element_text(face = "bold", size = 14))

# ----------------------------------------------------------------------
# Análise 2: Top 10 Categorias por Receita
# ----------------------------------------------------------------------
products <- read_csv("olist_products_dataset.csv")

top_categories <- df_sales %>%
  inner_join(products, by = "product_id") %>%
  group_by(product_category_name) %>%
  summarise(total_revenue = sum(price, na_rm = TRUE)) %>%
  drop_na(product_category_name) %>%
  slice_max(order_by = total_revenue, n = 10)

# Gráfico 2: Top 10 Categorias
ggplot(top_categories, aes(x = reorder(product_category_name, total_revenue), y = total_revenue / 1e3)) +
  geom_col(fill = "#4682b4") +
  coord_flip() +
  scale_y_continuous(labels = scales::dollar_format(prefix = "R$ ", suffix = "k")) +
  labs(
    title = "Top 10 Categorias por Receita Total",
    x = "Categoria",
    y = "Receita (R$ Milhares)"
  ) +
  theme_minimal()

