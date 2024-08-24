import pandas as pd

file_path = 'arquivos tratados/produtos_corrigidos.csv'
df = pd.read_csv(file_path)

# 1. Verificar IDs duplicados
duplicated_ids = df[df.duplicated('ID_Produto', keep=False)]
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

# 3. Verificar inconsistências nas associações entre Nome_Produto, Categoria_Produto, e Preco_Base
inconsistent_produtos = df.groupby('Nome_Produto').nunique()
inconsistent_produtos = inconsistent_produtos[(inconsistent_produtos['Categoria_Produto'] > 1) | (inconsistent_produtos['Preco_Base'] > 1)]
if not inconsistent_produtos.empty:
    print("\nInconsistências encontradas:")
    print(inconsistent_produtos)
else:
    print("\nNenhuma inconsistência encontrada.")

# 4. Converter as colunas categóricas para valores numéricos
df_numeric = df.copy()
df_numeric['Categoria_Produto'] = df_numeric['Categoria_Produto'].astype('category').cat.codes
df_numeric['Nome_Produto'] = df_numeric['Nome_Produto'].str.extract('(\d+)').astype(int)

# 5. Calcular a correlação de Pearson
correlation_matrix = df_numeric.corr(method='pearson')

# Exibir a matriz de correlação
print("\nMatriz de Correlação de Pearson:")
print(correlation_matrix.round(3))
