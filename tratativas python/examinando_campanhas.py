import pandas as pd

# Carregar o dataset
df = pd.read_csv('arquivos tratados/campanhas_marketing.csv', encoding='utf-8')

# Converter colunas de data para datetime
df['Data_Inicio'] = pd.to_datetime(df['Data_Inicio'])
df['Data_Fim'] = pd.to_datetime(df['Data_Fim'])

# Converter datas para números (dias desde uma data de referência)
df['Dias_Desde_Inicio'] = (df['Data_Inicio'] - df['Data_Inicio'].min()).dt.days
df['Dias_Desde_Fim'] = (df['Data_Fim'] - df['Data_Inicio'].min()).dt.days

# Verificar valores ausentes
missing_values = df.isnull().sum()
missing_percentage = (df.isnull().sum() / len(df)) * 100
print("Valores ausentes:\n", missing_values)
print("Porcentagem de valores ausentes:\n", missing_percentage)

# Verificar linhas duplicadas
duplicate_rows = df.duplicated().sum()
print("Linhas duplicadas:", duplicate_rows)

if duplicate_rows > 0:
    print("Exemplos de linhas duplicadas:\n", df[df.duplicated()].head())

# Verificar tipos de dados
data_types = df.dtypes
print("Tipos de dados:\n", data_types)

# Verificar valores únicos por coluna
unique_values = df.nunique()
print("Valores únicos por coluna:\n", unique_values)

# Verificar quaisquer inconsistências óbvias nos dados
summary_stats = df.describe(include='all')
print("Estatísticas sumárias:\n", summary_stats)

# Filtrar apenas colunas numéricas para calcular a correlação
numeric_df = df.select_dtypes(include=['float64', 'int64'])

# Incluir as colunas convertidas de datas
numeric_df['Dias_Desde_Inicio'] = df['Dias_Desde_Inicio']
numeric_df['Dias_Desde_Fim'] = df['Dias_Desde_Fim']

print("\nCorrelação forte (acima de 0.5 ou abaixo de -0.5):")
# Análise de correlações entre variáveis numéricas
correlation_matrix = numeric_df.corr()
print("Matriz de correlação:\n", correlation_matrix.round(3))
