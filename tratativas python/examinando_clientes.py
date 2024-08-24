import pandas as pd
import numpy as np

# Ler o arquivo CSV
df = pd.read_csv('arquivos tratados/clientes.csv')

# Exibir informações básicas sobre o dataframe
print("Informações básicas do dataframe:")
print(df.info())

# Mostrar as primeiras linhas do dataframe
print("\nPrimeiras linhas do dataframe:")
print(df.head())

# Verificar se há valores ausentes
print("\nAnálise de valores ausentes:")
missing_values = df.isnull().sum()
missing_percentage = (missing_values / len(df)) * 100
missing_data = pd.DataFrame({'Valores Ausentes': missing_values, 'Porcentagem': missing_percentage})
print(missing_data[missing_data['Valores Ausentes'] > 0])

# Verificar linhas duplicadas
duplicates = df.duplicated().sum()
print(f"\nNúmero de linhas duplicadas: {duplicates}")

# Remover linhas duplicadas, se houver
if duplicates > 0:
    df = df.drop_duplicates()
    print(f"{duplicates} linhas duplicadas foram removidas.")
else:
    print("Nenhuma linha duplicada encontrada.")

# Verificar tipos de dados e valores únicos para cada coluna
print("\nAnálise das colunas:")
for column in df.columns:
    print(f"\nColuna: {column}")
    print(f"Tipo de dado: {df[column].dtype}")
    print(f"Valores únicos: {df[column].nunique()}")
    print(f"Exemplos de valores: {df[column].unique()[:5]}")  # Mostrar até 5 valores únicos como exemplo

    # Verificação adicional para colunas de tipo object (strings)
    if df[column].dtype == 'object':
        print(f"Número de valores únicos com espaços ou case variations: {df[column].str.strip().str.lower().nunique()}")

# Resumo estatístico das colunas numéricas
print("\nResumo estatístico das colunas numéricas:")
print(df.describe().round(2))

# Verificar se há colunas categóricas
categorical_columns = df.select_dtypes(include=['object'])
if not categorical_columns.empty:
    print("\nResumo das colunas categóricas:")
    print(categorical_columns.describe())
else:
    print("\nNão há colunas categóricas para resumo.")

# Análise de correlação de Pearson
print("\nAnálise de correlação de Pearson:")

# Filtrar colunas numéricas
df_numeric = df.select_dtypes(include=[np.number])

# Verificar se há colunas numéricas após filtragem
if df_numeric.empty:
    print("Não há colunas numéricas para análise de correlação.")
else:
    correlation_matrix = df_numeric.corr(method='pearson').round(3)
    print(correlation_matrix)

    # Identificar correlações fortes (acima de 0.5 ou abaixo de -0.5)
    strong_corr = correlation_matrix[(correlation_matrix > 0.5) | (correlation_matrix < -0.5)]
    print("\nCorrelação forte (acima de 0.5 ou abaixo de -0.5):")
    print(strong_corr.dropna(how='all', axis=0).dropna(how='all', axis=1).round(3))
