from prophet import Prophet
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, mean_absolute_error

#Carregar dados
orders = pd.read_csv("olist_orders_dataset.csv")
items = pd.read_csv("olist_order_items_dataset.csv")

#Filtrar pedidos entregues e fazer join
df = orders[orders['order_status'] == 'delivered'].merge(items, on='order_id')
df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])

#Agrupar faturamento por DIA
df_daily = df.groupby(df['order_purchase_timestamp'].dt.date)['price'].sum().reset_index()
df_daily.columns = ['date', 'revenue']
df_daily['date'] = pd.to_datetime(df_daily['date'])

#Filtrar intervalo com dados consistentes (janeiro 2017 a agosto 2018)
df_daily = df_daily[(df_daily['date'] >= '2017-01-01') & (df_daily['date'] <= '2018-08-31')].sort_values('date')

#Preencher dias faltantes com 0 caso haja lacunas
df_daily = df_daily.set_index('date').asfreq('D', fill_value=0).reset_index()

print(f"Período final: {df_daily['date'].min()} até {df_daily['date'].max()}")
print(f"Total de dias: {len(df_daily)}")


#================PASSO 2: Feature Engineering para Scikit-Learn
def create_features(df):
    data = df.copy()
    
    # Recursos de calendário
    data['dayofweek'] = data['date'].dt.dayofweek
    data['day'] = data['date'].dt.day
    data['month'] = data['date'].dt.month
    
    # Lags (dias anteriores)
    data['lag_1'] = data['revenue'].shift(1)
    data['lag_7'] = data['revenue'].shift(7)
    data['lag_14'] = data['revenue'].shift(14)
    
    # Médias móveis
    data['rolling_mean_7'] = data['revenue'].shift(1).rolling(window=7).mean()
    data['rolling_mean_14'] = data['revenue'].shift(1).rolling(window=14).mean()
    
    return data.dropna()

df_features = create_features(df_daily)


#===========PASSO 3: DIVISÃO TEMPORAL (TRAIN/TEST SPLIT)
# Usaremos os últimos 60 dias para TESTE
test_days = 60

train = df_features.iloc[:-test_days]
test = df_features.iloc[-test_days:]

X_cols = ['dayofweek', 'day', 'month', 'lag_1', 'lag_7', 'lag_14', 'rolling_mean_7', 'rolling_mean_14']
y_col = 'revenue'

X_train, y_train = train[X_cols], train[y_col]
X_test, y_test = test[X_cols], test[y_col]

#=========PASSO 4: Treinamento e Avaliação no Scikit-Learn
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error

# --- Modelo 1: Regressão Linear ---
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)
lr_preds = lr_model.predict(X_test)

# --- Modelo 2: Random Forest ---
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
rf_preds = rf_model.predict(X_test)

# Métricas de Avaliação
def eval_metrics(y_true, y_pred, model_name):
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    mae = mean_absolute_error(y_true, y_pred)
    print(f"--- {model_name} ---")
    print(f"MAE  (Erro Médio Absoluto): R$ {mae:.2f}")
    print(f"RMSE (Raiz do Erro Quadrático): R$ {rmse:.2f}\n")

eval_metrics(y_test, lr_preds, "Regressão Linear")
eval_metrics(y_test, rf_preds, "Random Forest Regressor")

#=========PASSO 5: PROPHET

# O Prophet precisa de colunas chamadas 'ds' (data) e 'y' (valor a prever)
df_prophet = df_daily.rename(columns={'date': 'ds', 'revenue': 'y'})

# Mantemos a mesma divisão temporal: treinar no passado e testar nos últimos 60 dias
test_days = 60
train_prophet = df_prophet.iloc[:-test_days]
test_prophet  = df_prophet.iloc[-test_days:]


# Inicialização e Treinamento do Modelo
# Desativamos a sazonalidade diária pois os dados já são agregados por dia
model_prophet = Prophet(
    yearly_seasonality=True,   # Captura picos ao longo do ano
    weekly_seasonality=True,   # Captura padrões de dias da semana (ex: fim de semana)
    daily_seasonality=False,
    interval_width=0.95        # Intervalo de confiança de 95%
)

# Adicionar feriados do Brasil melhora consideravelmente as previsões do e-commerce
model_prophet.add_country_holidays(country_name='BR')

# Treinamento
model_prophet.fit(train_prophet)


# Gerando previsões para o período de teste
# Criamos um dataframe com os dias do futuro que queremos prever (60 dias)
future = model_prophet.make_future_dataframe(periods=test_days, freq='D')
forecast = model_prophet.predict(future)

#Filtramos as previsões apenas para o período de teste
forecast_test = forecast.tail(test_days)
prophet_preds = forecast_test['yhat'].values  # 'yhat' é a previsão central do Prophet


#Métricas de avaliação
mae_prophet  = mean_absolute_error(test_prophet['y'], prophet_preds)
rmse_prophet = np.sqrt(mean_squared_error(test_prophet['y'], prophet_preds))

print("--- Prophet (Meta) ---")
print(f"MAE  (Erro Médio Absoluto): R$ {mae_prophet:.2f}")
print(f"RMSE (Raiz do Erro Quadrático): R$ {rmse_prophet:.2f}\n")


# Visualização Comparativa dos 60 Dias de Teste
plt.figure(figsize=(14, 6))

# Vendas Reais
plt.plot(test['date'], y_test, label='Vendas Reais', color='black', linewidth=2)

# Previsões com os valores calculados
plt.plot(test['date'], lr_preds, label='Regressão Linear (MAE: R$ 5.164)', color='#2b5c8f', linestyle='--')
plt.plot(test['date'], rf_preds, label='Random Forest (MAE: R$ 5.207)', color='#e67e22', linestyle='--')
plt.plot(test['date'], prophet_preds, label='Prophet (MAE: R$ 8.743)', color='#27ae60', linestyle=':')

plt.title('Comparativo de Modelos: Previsão de Faturamento Diário (Últimos 60 Dias)', fontsize=14, fontweight='bold')
plt.xlabel('Data')
plt.ylabel('Receita Diária (R$)')
plt.legend(loc='upper left')
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Salvar gráfico
plt.savefig('comparativo_modelos.png', dpi=300)
plt.show()