import pandas as pd

# Carregar o arquivo CSV
df = pd.read_csv('arquivos não tratados/produtos.csv')

# 1. Verificar valores ausentes
missing_values = df.isnull().sum()
print("Valores ausentes por coluna:")
print(missing_values)

# 2. Verificar linhas duplicadas
duplicate_rows = df.duplicated().sum()
print("Número de linhas duplicadas:")
print(duplicate_rows)

# 3. Arredondar valores da coluna 'Preco_Base' para 2 casas decimais
if 'Preco_Base' in df.columns:
    df['Preco_Base'] = df['Preco_Base'].round(2)

# Exibir as primeiras linhas após arredondar
print("Primeiras linhas após arredondar Preco_Base:")
print(df.head())

# Salvar o DataFrame modificado em um novo arquivo CSV
df.to_csv('produtos_corrigidos.csv', index=False)
print("Arquivo CSV modificado salvo como 'prod_corrigidos.csv'")
