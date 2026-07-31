<<<<<<< HEAD
import os
import pandas as pd
from scipy import stats
from google.cloud import bigquery


#Conexão e carregamento dos dados
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/mnt/c/Users/lucas/OneDrive/Desktop/Lucas/estudos 2026/projeto ecommerce/projeto-olist-analytics-b00a9d7606ef.json"
client = bigquery.Client(project="projeto-olist-analytics")

query = """
SELECT 
    i.price,
    p.product_category_name
FROM `analytics_olist.itens` i
JOIN `analytics_olist.produtos` p ON i.product_id = p.product_id
WHERE p.product_category_name IN ('cama_mesa_banho', 'beleza_saude')
"""

print("Baixando dados para o teste estatístico...")
df = client.query(query).to_dataframe()

#Separando duas amostras
cama_mesa = df[df['product_category_name'] == 'cama_mesa_banho']['price']
beleza_saude = df[df['product_category_name'] == 'beleza_saude']['price']

#Métricas descritivas
print(f"\nResumo Amostral")
print(f"Cama, Mesa e Banho -> Média: R$ {cama_mesa.mean():.2f} | Total Itens: {len(cama_mesa)}")
print(f"Beleza e Saúde     -> Média: R$ {beleza_saude.mean():.2f} | Total Itens: {len(beleza_saude)}")

#Aplicação do Teste T de Welch (equal_var=False para não presumir variâncias iguais)
stat, p_valor = stats.ttest_ind(cama_mesa, beleza_saude, equal_var=False)

print(f"\nResultado do Teste T")
print(f"Estatística T: {stat:.4f}")
print(f"p-valor: {p_valor}")

print("Hipótese nula (H0): A diferença estatística entre os tickets médios das categorias sugere acaso amostral (> 5%)")
print("Hipótese alternativa (H1): A diferença estatística entre os tickets médios das categorias segue o padrão de mercado (≤ 5%)")

#Conclusão
if p_valor < 0.05:
    print("\nRejeitamos H0 - Hipótese alternativa aceita")
    print("Existe uma diferença estatisticamente significativa no ticket médio das duas categorias.")
else:
    print("\nRejeitamos H1 - Hipótese nula aceita")
=======
import os
import pandas as pd
from scipy import stats
from google.cloud import bigquery


#Conexão e carregamento dos dados
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/mnt/c/Users/lucas/OneDrive/Desktop/Lucas/estudos 2026/projeto ecommerce/projeto-olist-analytics-b00a9d7606ef.json"
client = bigquery.Client(project="projeto-olist-analytics")

query = """
SELECT 
    i.price,
    p.product_category_name
FROM `analytics_olist.itens` i
JOIN `analytics_olist.produtos` p ON i.product_id = p.product_id
WHERE p.product_category_name IN ('cama_mesa_banho', 'beleza_saude')
"""

print("Baixando dados para o teste estatístico...")
df = client.query(query).to_dataframe()

#Separando duas amostras
cama_mesa = df[df['product_category_name'] == 'cama_mesa_banho']['price']
beleza_saude = df[df['product_category_name'] == 'beleza_saude']['price']

#Métricas descritivas
print(f"\nResumo Amostral")
print(f"Cama, Mesa e Banho -> Média: R$ {cama_mesa.mean():.2f} | Total Itens: {len(cama_mesa)}")
print(f"Beleza e Saúde     -> Média: R$ {beleza_saude.mean():.2f} | Total Itens: {len(beleza_saude)}")

#Aplicação do Teste T de Welch (equal_var=False para não presumir variâncias iguais)
stat, p_valor = stats.ttest_ind(cama_mesa, beleza_saude, equal_var=False)

print(f"\nResultado do Teste T")
print(f"Estatística T: {stat:.4f}")
print(f"p-valor: {p_valor}")

print("Hipótese nula (H0): A diferença estatística entre os tickets médios das categorias sugere acaso amostral (> 5%)")
print("Hipótese alternativa (H1): A diferença estatística entre os tickets médios das categorias segue o padrão de mercado (≤ 5%)")

#Conclusão
if p_valor < 0.05:
    print("\nRejeitamos H0 - Hipótese alternativa aceita")
    print("Existe uma diferença estatisticamente significativa no ticket médio das duas categorias.")
else:
    print("\nRejeitamos H1 - Hipótese nula aceita")
>>>>>>> 6070dae4c48dada854a8569c1569a7de1c89f499
    print("A diferença observada pode ser apenas fruto do acaso na amostragem.")