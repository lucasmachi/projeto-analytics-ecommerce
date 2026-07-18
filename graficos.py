import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def gerar_grafico_sazonalidade(df_pedidos, df_pagamentos):
    print("Gerando Gráfico 1: Sazonalidade...")
    df_vendas = pd.merge(df_pedidos, df_pagamentos, on="order_id", how="inner")
    df_entregues = df_vendas[df_vendas["order_status"] == "delivered"].copy()
    
    df_entregues["order_purchase_timestamp"] = pd.to_datetime(df_entregues["order_purchase_timestamp"])
    df_entregues["ano_mes"] = df_entregues["order_purchase_timestamp"].dt.to_period("M").astype(str)
    
    faturamento_mensal = df_entregues.groupby("ano_mes")["payment_value"].sum().reset_index().sort_values("ano_mes")
    
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=faturamento_mensal, x="ano_mes", y="payment_value", marker="o", color="darkblue", linewidth=2.5)
    plt.title("Evolução Mensal do Faturamento - Olist", fontsize=14, fontweight="bold")
    plt.xticks(rotation=45)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.savefig("sazonalidade_faturamento.png")
    plt.close() # Fecha a figura para liberar memória

def gerar_grafico_ticket(df_pedidos, df_itens, df_clientes):
    print("Gerando Gráfico 2: Ticket Médio...")
    valor_por_pedido = df_itens.groupby("order_id")["price"].sum().reset_index()
    df_geo = pd.merge(df_pedidos, df_clientes, on="customer_id", how="inner")
    df_geo = pd.merge(df_geo, valor_por_pedido, on="order_id", how="inner")
    
    df_geo_entregues = df_geo[df_geo["order_status"] == "delivered"]
    ticket_por_estado = df_geo_entregues.groupby("customer_state")["price"].mean().reset_index()
    ticket_por_estado = ticket_por_estado.sort_values(by="price", ascending=False).head(10)
    
    plt.figure(figsize=(12, 6))
    sns.barplot(data=ticket_por_estado, x="customer_state", y="price", palette="Blues_r")
    plt.title("Top 10 Estados por Ticket Médio - Olist", fontsize=14, fontweight="bold")
    plt.grid(axis="y", linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.savefig("ticket_medio_por_estado.png")
    plt.close()

def gerar_grafico_correlation(df_itens):
    print("Gerando Gráfico 3: Correlação Preço vs Frete...")
    df_amostra = df_itens.sample(n=5000, random_state=42)
    
    plt.figure(figsize=(10, 6))
    sns.regplot(data=df_amostra, x="price", y="freight_value", 
                scatter_kws={"alpha": 0.4, "color": "teal"}, line_kws={"color": "red", "linewidth": 2})
    plt.title("Correlação: Preço do Produto vs Valor do Frete", fontsize=14, fontweight="bold")
    plt.xlim(0, 1000)
    plt.ylim(0, 200)
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.savefig("correlacao_preco_frete.png")
    plt.close()