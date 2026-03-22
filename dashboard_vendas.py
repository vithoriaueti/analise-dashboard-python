import pandas as pd
import matplotlib.pyplot as plt

dados = {
    'produto': ['Camiseta', 'Calça', 'Tênis', 'Camiseta', 'Calça', 'Tênis'],
    'regiao': ['Sudeste', 'Sul', 'Nordeste', 'Sudeste', 'Sul', 'Nordeste'],
    'valor': [50, 120, 200, 70, 150, 220]
}

df = pd.DataFrame(dados)

total = df['valor'].sum()
print("Total de vendas:", total)

vendas_produto = df.groupby('produto')['valor'].sum()
vendas_regiao = df.groupby('regiao')['valor'].sum()

plt.figure()
vendas_produto.plot(kind='bar')
plt.title('Vendas por Produto')
plt.xlabel('Produto')
plt.ylabel('Valor')
plt.show()

plt.figure()
vendas_regiao.plot(kind='bar')
plt.title('Vendas por Região')
plt.xlabel('Região')
plt.ylabel('Valor')
plt.show()
