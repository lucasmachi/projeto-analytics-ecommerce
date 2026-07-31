<<<<<<< HEAD
import os
import pandas as pd
from statsmodels.stats.proportion import proportions_ztest
from google.cloud import bigquery

#Conexão e carregamento dos dados
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/mnt/c/Users/lucas/OneDrive/Desktop/Lucas/estudos 2026/projeto ecommerce/projeto-olist-analytics-b00a9d7606ef.json"
client = bigquery.Client(project="projeto-olist-analytics")

query = """
SELECT 
    c.customer_state,
    p.order_delivered_customer_date,
    p.order_estimated_delivery_date
FROM `analytics_olist.pedidos` p
JOIN `analytics_olist.clientes` c ON p.customer_id = c.customer_id
WHERE p.order_status = 'delivered'
  AND c.customer_state IN ('SP', 'RJ')
"""

print("Baixando dados do BigQuery...")
df = client.query(query).to_dataframe()

# Criando a flag de atraso (1 se entregou depois da data estimada, 0 se entregou no prazo)
df['order_delivered_customer_date'] = pd.to_datetime(df['order_delivered_customer_date'])
df['order_estimated_delivery_date'] = pd.to_datetime(df['order_estimated_delivery_date'])

df['atrasado'] = (df['order_delivered_customer_date'] > df['order_estimated_delivery_date']).astype(int)

# Agrupando os dados por estado
resumo = df.groupby('customer_state')['atrasado'].agg(['sum', 'count']).reset_index()
resumo['taxa_atraso_%'] = (resumo['sum'] / resumo['count']) * 100

print("\nResumo de Logística por Estado")
print(resumo)

# Preparando dados para o Teste Z 
atrasos = resumo['sum'].values # Número de atrasos
totais = resumo['count'].values # Tamanho total das amostras

stat, p_valor = proportions_ztest(count=atrasos, nobs=totais)

print(f"\nResultado do Teste Z de Proporções")
print(f"Estatística Z: {stat:.4f}")
print(f"p-valor: {p_valor}")

if p_valor < 0.05:
    print("\nExiste uma diferença estatisticamente significante nas taxas de atraso entre SP e RJ (p-value < 0.05)")
else:
=======
import os
import pandas as pd
from statsmodels.stats.proportion import proportions_ztest
from google.cloud import bigquery

#Conexão e carregamento dos dados
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/mnt/c/Users/lucas/OneDrive/Desktop/Lucas/estudos 2026/projeto ecommerce/projeto-olist-analytics-b00a9d7606ef.json"
client = bigquery.Client(project="projeto-olist-analytics")

query = """
SELECT 
    c.customer_state,
    p.order_delivered_customer_date,
    p.order_estimated_delivery_date
FROM `analytics_olist.pedidos` p
JOIN `analytics_olist.clientes` c ON p.customer_id = c.customer_id
WHERE p.order_status = 'delivered'
  AND c.customer_state IN ('SP', 'RJ')
"""

print("Baixando dados do BigQuery...")
df = client.query(query).to_dataframe()

# Criando a flag de atraso (1 se entregou depois da data estimada, 0 se entregou no prazo)
df['order_delivered_customer_date'] = pd.to_datetime(df['order_delivered_customer_date'])
df['order_estimated_delivery_date'] = pd.to_datetime(df['order_estimated_delivery_date'])

df['atrasado'] = (df['order_delivered_customer_date'] > df['order_estimated_delivery_date']).astype(int)

# Agrupando os dados por estado
resumo = df.groupby('customer_state')['atrasado'].agg(['sum', 'count']).reset_index()
resumo['taxa_atraso_%'] = (resumo['sum'] / resumo['count']) * 100

print("\nResumo de Logística por Estado")
print(resumo)

# Preparando dados para o Teste Z 
atrasos = resumo['sum'].values # Número de atrasos
totais = resumo['count'].values # Tamanho total das amostras

stat, p_valor = proportions_ztest(count=atrasos, nobs=totais)

print(f"\nResultado do Teste Z de Proporções")
print(f"Estatística Z: {stat:.4f}")
print(f"p-valor: {p_valor}")

if p_valor < 0.05:
    print("\nExiste uma diferença estatisticamente significante nas taxas de atraso entre SP e RJ (p-value < 0.05)")
else:
>>>>>>> 6070dae4c48dada854a8569c1569a7de1c89f499
    print("\nA diferença observada nas taxas de atraso não é estatisticamente significante (p-value > 0.05)")