import os
from google.cloud import bigquery
from graficos import gerar_grafico_sazonalidade, gerar_grafico_correlation, gerar_grafico_ticket


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/mnt/c/Users/lucas/OneDrive/Desktop/Lucas/estudos 2026/projeto ecommerce/projeto-olist-analytics-b00a9d7606ef.json"
client = bigquery.Client(project="projeto-olist-analytics")

print("Iniciando a extração de dados do BigQuery...")
df_pedidos = client.query("SELECT * FROM `analytics_olist.pedidos`").to_dataframe()
df_pagamentos = client.query("SELECT * FROM `analytics_olist.pagamentos`").to_dataframe()
df_itens = client.query("SELECT * FROM `analytics_olist.itens`").to_dataframe()
df_clientes = client.query("SELECT * FROM `analytics_olist.clientes`").to_dataframe()
print("Dados carregados com sucesso!")

gerar_grafico_sazonalidade(df_pedidos, df_pagamentos)
gerar_grafico_ticket(df_pedidos, df_itens, df_clientes)
gerar_grafico_correlation(df_itens)

print("Todos os gráficos foram gerados e salvos com sucesso na pasta!")
