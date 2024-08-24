import json
import pandas as pd

# Função para carregar o arquivo JSON
def carregar_arquivo_json(caminho_arquivo):
    """Carrega um arquivo JSON e retorna os dados como um dicionário."""
    try:
        with open(caminho_arquivo, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
        return None
    except json.JSONDecodeError:
        print(f"Erro: O arquivo '{caminho_arquivo}' não é um JSON válido.")
        return None

# Função para exibir informações sobre o DataFrame
def exibir_informacoes_dataframe(df):
    """Exibe informações básicas sobre o DataFrame."""
    print("Informações sobre o DataFrame:")
    print(df.info())
    print("\nPrimeiras 5 linhas do DataFrame:")
    print(df.head())

# Função para verificar inconsistências
def verificar_inconsistencias(df):
    """Verifica valores ausentes, duplicados e tipos de dados no DataFrame."""
    print("\nVerificando valores ausentes por coluna:")
    print(df.isnull().sum())

    print("\nNúmero de linhas duplicadas:")
    duplicadas = df.duplicated().sum()
    print(duplicadas)

    if duplicadas > 0:
        print("\nExemplo de linhas duplicadas:")
        print(df[df.duplicated(keep=False)])

    print("\nVerificando tipos de dados e valores únicos por coluna:")
    for column in df.columns:
        print(f"\nColuna: {column}")
        print(f"Tipo de dado: {df[column].dtype}")
        print(f"Número de valores únicos: {df[column].nunique()}")
        print(f"Amostra de valores únicos: {df[column].unique()[:5]}")

    print("\nInspeção de dados completa.")

# Caminho do arquivo JSON
caminho_arquivo = 'arquivos tratados/vendas_online_corrigida.json'

# Carregar e processar o arquivo JSON
data = carregar_arquivo_json(caminho_arquivo)
if data:
    df = pd.DataFrame(data)
    exibir_informacoes_dataframe(df)
    verificar_inconsistencias(df)
