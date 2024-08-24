import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Ler o arquivo CSV
file_path = 'dados significativos/tabelas/visao_geral.csv'
df = pd.read_csv(file_path)

# Configurar o estilo do gráfico
sns.set(style="whitegrid")

# Ajustar o tamanho da figura
plt.figure(figsize=(15, 10))

# Gráfico 1: Quantidade total de produtos vendidos por categoria
plt.subplot(2, 2, 1)
sns.barplot(x='Total_Produtos_Vendidos', y='Categoria_Produto', data=df, errorbar=None)
plt.title('Total de Produtos Vendidos por Categoria')
plt.xlabel('Total de Produtos Vendidos')
plt.ylabel('Categoria')

# Gráfico 2: Lucro total por categoria
plt.subplot(2, 2, 2)
sns.barplot(x='Lucro_Total', y='Categoria_Produto', data=df, errorbar=None)
plt.title('Lucro Total por Categoria')
plt.xlabel('Lucro Total')
plt.ylabel('Categoria')

# Gráfico 3: Quantidade total de produtos vendidos por produto
plt.subplot(2, 2, 3)
sns.barplot(x='Total_Produtos_Vendidos', y='Nome_Produto', data=df, errorbar=None)
plt.title('Total de Produtos Vendidos por Produto')
plt.xlabel('Total de Produtos Vendidos')
plt.ylabel('Produto')

# Ajustar layout
plt.tight_layout()

# Salvar o dashboard como uma imagem
output_path = 'dashboard_visao_geral.png'
plt.savefig(output_path)

print(f"Dashboard salvo em: {output_path}")
