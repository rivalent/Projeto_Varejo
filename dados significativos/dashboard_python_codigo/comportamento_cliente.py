import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv('dados significativos/tabelas/comportamento_do_cliente.csv', encoding='utf-8')

# Create a bar plot for average purchase value by satisfaction segment
plt.figure(figsize=(10, 6))
sns.barplot(x='Segmento_Satisfacao', y='Valor_Medio_Compra', data=data)
plt.title('Average Purchase Value by Customer Satisfaction Segment')
plt.xlabel('Satisfaction Segment')
plt.ylabel('Average Purchase Value')
plt.show()

# Create a pie chart for distribution of satisfaction segments
segment_counts = data['Segmento_Satisfacao'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(segment_counts.values, labels=segment_counts.index, autopct='%1.1f%%')
plt.title('Distribuição dos Segmentos de Satisfação do Cliente')
plt.show()

print("Graphs generated successfully.")