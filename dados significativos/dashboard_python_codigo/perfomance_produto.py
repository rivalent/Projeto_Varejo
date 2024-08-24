# Import required libraries
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Read the CSV file
df = pd.read_csv('dados significativos/tabelas/perfomance_por_produto.csv', encoding='utf-8')

# Display the first few rows of the dataframe
print(df.head())

# Create a subplot with 2 rows and 2 columns
fig = make_subplots(rows=2, cols=2, subplot_titles=("Total de produtos vendidos por categoria",
                                                    "Total de vendas da categoria",
                                                    "Lucro total por categoria",
                                                    "Produtos com alertas"))

# Add bar charts to the subplots
fig.add_trace(go.Bar(x=df['Categoria_Produto'], y=df['Total_Produtos_Vendidos'], name='Products Sold'),
              row=1, col=1)

fig.add_trace(go.Bar(x=df['Categoria_Produto'], y=df['Total_Categoria_Vendida'], name='Category Sales'),
              row=1, col=2)

fig.add_trace(go.Bar(x=df['Categoria_Produto'], y=df['Lucro_Total'], name='Total Profit'),
              row=2, col=1)

alert_counts = df['Status_Alerta'].value_counts()
fig.add_trace(go.Bar(x=alert_counts.index, y=alert_counts.values, name='Alert Status'),
              row=2, col=2)

# Update layout
fig.update_layout(height=800, width=1000, title_text="Perfomance por Produto Dashboard")

# Save the plot as an HTML file
fig.write_html("perfomance_por_produto.html")

print("Dashboard has been created and saved as 'product_performance_dashboard.html'")