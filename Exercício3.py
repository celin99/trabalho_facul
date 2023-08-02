import pandas as pd
import matplotlib.pyplot as plt

# Carregando o arquivo CSV e renomeando as colunas
df = pd.read_csv("Stores.csv")
df.rename(columns={
    "Items_Available": "Itens Disponíveis",
    "Daily_Customer_Count": "Visitantes Diários",
    "Store_Sales": "Vendas da Loja"
}, inplace=True)

# Obtendo os valores mínimo, máximo, médio e desvio padrão para as colunas específicas
min_items_available = df["Itens Disponíveis"].min()
max_items_available = df["Itens Disponíveis"].max()
mean_items_available = df["Itens Disponíveis"].mean()
std_items_available = df["Itens Disponíveis"].std()

min_daily_customer_count = df["Visitantes Diários"].min()
max_daily_customer_count = df["Visitantes Diários"].max()
mean_daily_customer_count = df["Visitantes Diários"].mean()
std_daily_customer_count = df["Visitantes Diários"].std()

min_store_sales = df["Vendas da Loja"].min()
max_store_sales = df["Vendas da Loja"].max()
mean_store_sales = df["Vendas da Loja"].mean()
std_store_sales = df["Vendas da Loja"].std()

# Criando os gráficos de dispersão
plt.figure(figsize=(10, 5))
plt.scatter(df.index, df["Itens Disponíveis"], c='blue', label='Itens Disponíveis')
plt.scatter(df.index, df["Visitantes Diários"], c='red', label='Visitantes Diários')
plt.scatter(df.index, df["Vendas da Loja"], c='green', label='Vendas da Loja')
plt.xlabel('Lojas')
plt.ylabel('Valores')
plt.title('Desempenho das Lojas')
plt.legend()
plt.show()

# Exibindo os valores mínimo, máximo, médio e desvio padrão
print("Itens Disponíveis:")
print("Mínimo:", min_items_available)
print("Máximo:", max_items_available)
print("Média:", mean_items_available)
print("Desvio Padrão:", std_items_available)
print()

print("Visitantes Diários:")
print("Mínimo:", min_daily_customer_count)
print("Máximo:", max_daily_customer_count)
print("Média:", mean_daily_customer_count)
print("Desvio Padrão:", std_daily_customer_count)
print()

print("Vendas da Loja:")
print("Mínimo:", min_store_sales)
print("Máximo:", max_store_sales)
print("Média:", mean_store_sales)
print("Desvio Padrão:", std_store_sales)
