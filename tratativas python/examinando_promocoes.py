import pandas as pd
import numpy as np
from scipy.stats import pearsonr

# Carregar o arquivo CSV
file_path = 'arquivos tratados/promocoes.csv'
df = pd.read_csv(file_path)

# Exibir as primeiras linhas do dataframe
print("Primeiras linhas do dataframe:")
print(df.head())

# Resumo estatístico inicial
print("\nResumo estatístico inicial:")
print(df.describe(include='all'))

# Tratamento de valores ausentes
# Preenchendo valores ausentes com a média para colunas numéricas
numeric_columns = df.select_dtypes(include=['number']).columns
df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())

# Para colunas categóricas, preenchendo valores ausentes com a moda (valor mais frequente)
for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].fillna(df[col].mode()[0])

# Verificando e tratando inconsistências nos tipos de dados
# Tentando converter colunas numéricas que podem estar como string
for col in df.columns:
    try:
        df[col] = pd.to_numeric(df[col])
    except ValueError:
        pass

# Verificando valores duplicados e removendo-os
df.drop_duplicates(inplace=True)

# Verificar tipos de dados após o tratamento
print("\nTipos de dados após o tratamento:")
print(df.dtypes)

# Exibir resumo estatístico após o tratamento
print("\nResumo estatístico após o tratamento:")
print(df.describe(include='all'))

# Análise de Correlação de Pearson
# Vamos calcular a correlação de Pearson entre todas as variáveis numéricas
numerical_cols = df.select_dtypes(include=[np.number]).columns
correlation_matrix = df[numerical_cols].corr(method='pearson')

print("\nMatriz de Correlação de Pearson:")
print(correlation_matrix.round(3))
