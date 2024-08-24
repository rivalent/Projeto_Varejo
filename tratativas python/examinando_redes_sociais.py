import pandas as pd

file_path = 'arquivos tratados/engajamento_redes_sociais.csv'
df = pd.read_csv(file_path, encoding='ascii')

# Exibir as primeiras linhas do dataframe
print("Primeiras linhas do dataframe:")
print(df.head())

# Exibir estatísticas sumárias detalhadas
print("\nEstatísticas sumárias detalhadas:")
print(df.describe(include='all').round(2))

# Verificar valores ausentes
print("\nValores ausentes por coluna:")
print(df.isnull().sum())

# Verificar a porcentagem de valores ausentes
print("\nPorcentagem de valores ausentes por coluna:")
missing_percentage = df.isnull().mean() * 100
print(missing_percentage)

# Verificar linhas duplicadas
print("\nNúmero de linhas duplicadas:")
print(df.duplicated().sum())

# Verificar tipos de dados e possíveis incoerências
print("\nTipos de dados por coluna:")
print(df.dtypes)

# Exibir as colunas com dados numéricos e verificar a dispersão
print("\nDispersão dos dados numéricos:")
for column in df.select_dtypes(include=['float64', 'int64']).columns:
    print(f'{column}:')
    print(df[column].describe().round(2))
    print()

# Verificar valores únicos nas colunas categóricas
print("\nValores únicos nas colunas categóricas:")
for column in df.select_dtypes(include=['object']).columns:
    print(f'{column}: {df[column].unique()}')

# Verificar a consistência das datas
print("\nAnálise das datas de engajamento:")
df['Data_Engajamento'] = pd.to_datetime(df['Data_Engajamento'], errors='coerce')

# Verificar se há datas não convertidas
invalid_dates = df['Data_Engajamento'].isnull().sum()
print(f"Número de datas inválidas: {invalid_dates}")

# Exibir o intervalo de datas
print(f"Período do engajamento: {df['Data_Engajamento'].min()} até {df['Data_Engajamento'].max()}")

# Verificar se as datas estão ordenadas (opcional)
if df['Data_Engajamento'].is_monotonic_increasing:
    print("As datas estão ordenadas cronologicamente.")
else:
    print("As datas NÃO estão ordenadas cronologicamente.")
