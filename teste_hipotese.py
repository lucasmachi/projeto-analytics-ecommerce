import os
import pandas as pd
from scipy import stats
from google.cloud import bigquery

# Conexão e carregamento dos dados
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

# Garantir preços numéricos e remover valores ausentes
df['price'] = pd.to_numeric(df['price'], errors='coerce')
df = df.dropna(subset=['price'])

# Separando duas amostras de preços por item
cama_mesa = df.loc[
    df['product_category_name'] == 'cama_mesa_banho',
    'price'
]

beleza_saude = df.loc[
    df['product_category_name'] == 'beleza_saude',
    'price'
]

if len(cama_mesa) < 2 or len(beleza_saude) < 2:
    raise ValueError(
        "Cada categoria precisa ter pelo menos dois itens com preços válidos."
    )

# Métricas descritivas
print("\nResumo amostral — preço por item")
print(
    f"Cama, Mesa e Banho -> Média: R$ {cama_mesa.mean():.2f}"
    f" | Total de itens: {len(cama_mesa)}"
)
print(
    f"Beleza e Saúde -> Média: R$ {beleza_saude.mean():.2f}"
    f" | Total de itens: {len(beleza_saude)}"
)

# Hipóteses do teste bilateral
print("\nH0: as médias populacionais de preço por item são iguais.")
print("H1: as médias populacionais de preço por item são diferentes.")

# Teste t de Welch, sem assumir variâncias iguais
stat, p_valor = stats.ttest_ind(
    cama_mesa,
    beleza_saude,
    equal_var=False,
    alternative='two-sided'
)

print("\nResultado do teste t de Welch")
print(f"Estatística t: {stat:.4f}")
print(f"p-valor: {p_valor:.6g}")

# Conclusão com nível de significância de 5%
alpha = 0.05

if pd.isna(p_valor):
    print(
        "\nNão foi possível obter um resultado válido. "
        "Verifique a variabilidade e os valores das amostras."
    )
elif p_valor < alpha:
    print("\nRejeitamos H0 ao nível de significância de 5%.")
    print(
        "O teste indica uma diferença estatisticamente significativa "
        "no preço médio por item entre as categorias."
    )

    if beleza_saude.mean() > cama_mesa.mean():
        print("Na amostra, Beleza e Saúde apresenta a maior média.")
    else:
        print("Na amostra, Cama, Mesa e Banho apresenta a maior média.")
else:
    print("\nNão rejeitamos H0 ao nível de significância de 5%.")
    print(
        "Não há evidência estatística suficiente para concluir "
        "que os preços médios por item diferem entre as categorias."
    )

# Limites da interpretação
print(
    "\nObservação: esta análise compara preços por item, "
    "não o valor total de cada pedido."
)
print(
    "O teste pressupõe observações independentes. Itens do mesmo pedido "
    "ou anúncios repetidos podem apresentar dependência."
)
