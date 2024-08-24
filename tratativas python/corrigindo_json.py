#importando bibliotecas e lendo o dataframe (tabela)
import pandas as pd
import numpy as np

dataframe = pd.read_json('arquivos não tratados/vendas_online.json')

#encontrando a linha onde começa a separação
for i in range(len(dataframe)):
  if np.isnan(dataframe["idVenda"][i]):
    separador =  i
    print(i)
    break

#printando as colunas
print(dataframe.columns)

#subtituir as colunas da tabela
for i in range(0, separador):
  dataframe.loc[i, 'ID_Venda'] = dataframe['idVenda'][i]
  dataframe.loc[i, 'ID_Produto'] = dataframe['idProduto'][i]
  dataframe.loc[i, 'ID_Loja'] = dataframe['idLoja'][i]
  dataframe.loc[i, 'Quantidade'] = dataframe['qtd'][i]
  dataframe.loc[i, "Data_Venda"] = dataframe['dataVenda'][i]
  dataframe.loc[i, "Preco_Unitario"] = dataframe['precoUnit'][i]
  dataframe.loc[i, "ID_Cliente"] = dataframe['idCliente'][i]
  dataframe.loc[i, "Desconto"] = dataframe['desconto'][i]
  dataframe.loc[i, "Promocao"] = dataframe['promocao'][i]
  dataframe.loc[i, "Estoque_Inicial"] = dataframe['estoqueInicial'][i]
  dataframe.loc[i, "Estoque_Final"] = dataframe['estoqueFinal'][i]
  dataframe.loc[i, "Devolucao"] = dataframe['devolucao'][i]
  dataframe.loc[i, "Canal_Venda"] = dataframe['canalVenda'][i]

#criando uma cópia do dataframe

final_dataframe = dataframe.iloc[:, 13:]

#salvando arquivos

final_dataframe.to_json('vendas_online_corrigida.json', orient='records')