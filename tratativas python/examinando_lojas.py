import pandas as pd

file_path = 'arquivos tratados/lojas_corrigidas.csv'
df = pd.read_csv(file_path)

# 1. Verificar IDs duplicados
duplicated_ids = df[df.duplicated('ID_Loja', keep=False)]
if not duplicated_ids.empty:
    print("IDs duplicados encontrados:")
    print(duplicated_ids)
else:
    print("Nenhum ID duplicado encontrado.")

# 2. Verificar campos vazios
missing_values = df.isnull().sum()
if missing_values.any():
    print("\nCampos com valores ausentes:")
    print(missing_values[missing_values > 0])
else:
    print("\nNenhum campo vazio encontrado.")

# 3. Verificar inconsistências nas associações entre Nome_Loja, Cidade, e Pais
inconsistent_lojas = df.groupby('Nome_Loja').nunique()
inconsistent_lojas = inconsistent_lojas[(inconsistent_lojas['Cidade'] > 1) | (inconsistent_lojas['Pais'] > 1)]
if not inconsistent_lojas.empty:
    print("\nInconsistências encontradas:")
    print(inconsistent_lojas)
else:
    print("\nNenhuma inconsistência encontrada.")

# 4. Converter as colunas categóricas para valores numéricos
df_numeric = df.copy()
df_numeric['Cidade'] = df_numeric['Cidade'].astype('category').cat.codes
df_numeric['Pais'] = df_numeric['Pais'].astype('category').cat.codes
df_numeric['Nome_Loja'] = df_numeric['Nome_Loja'].str.extract('(\d+)').astype(int)

# 5. Calcular a correlação de Pearson
correlation_matrix = df_numeric.corr(method='pearson')

# Exibir a matriz de correlação
print("\nMatriz de Correlação de Pearson:")
print(correlation_matrix.round(3))
