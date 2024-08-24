import pandas as pd

# Carregar o arquivo CSV
df = pd.read_csv('arquivos não tratados/vendas_atualizado.csv')

# 1. Remover milissegundos da coluna 'Data_Venda'
df['Data_Venda'] = pd.to_datetime(df['Data_Venda']).dt.strftime('%Y-%m-%d %H:%M:%S')

# 2. Arredondar valores das colunas para duas casas decimais
colunas_para_arredondar = ['Preco_Unitario', 'Desconto']
for coluna in colunas_para_arredondar:
    if coluna in df.columns:
        df[coluna] = df[coluna].round(2)

# 3. Substituir 'False' por 'F' e 'True' por 'T'
df.replace({False: 'F', True: 'T'}, inplace=True)

# Exibir as primeiras linhas após as modificações
print("Primeiras linhas após as modificações:")
print(df.head())

# Salvar o DataFrame modificado em um novo arquivo CSV
df.to_csv('vendas_tratadas.csv', index=False)
print("Arquivo CSV modificado salvo como 'vendas_tratadas.csv'")
