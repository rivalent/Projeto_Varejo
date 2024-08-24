import pandas as pd

# Carregar o arquivo CSV
df = pd.read_csv('arquivos tratados/vendas_tratadas.csv')

# Converter a coluna 'Data_Venda' para o tipo datetime
df['Data_Venda'] = pd.to_datetime(df['Data_Venda'])

# Verificar se há linhas duplicadas
duplicated_rows = df.duplicated().sum()

# Verificar valores únicos em 'Promocao' e 'Devolucao'
unique_promocao = df['Promocao'].unique()
unique_devolucao = df['Devolucao'].unique()

# Selecionar apenas as colunas numéricas
numeric_df = df.select_dtypes(include=['number'])

# Calcular a correlação de Pearson entre as variáveis numéricas
correlation_matrix = numeric_df.corr()

print(f"Linhas Duplicadas: {duplicated_rows}")
print(f"Valores únicos em 'Promocao': {unique_promocao}")
print(f"Valores únicos em 'Devolucao': {unique_devolucao}")
print("Matriz de Correlação de Pearson:")
print(correlation_matrix.round(3))
