import pandas as pd
import csv
import numpy as np
import os
import matplotlib.pyplot as plt

def calcular_transferencias_por_funcao(estados_regiao, funcao, years):
    sumsByYear = {}
    months = ['01', '02', '03']

    for year in years:
        yearSum = 0
        for month in months:
            file = f'./docs/{year}/{year}{month}_Transferencias.csv'
            if os.path.exists(file):
                data = pd.read_csv(file, sep=';', quoting=csv.QUOTE_NONE, encoding='latin-1', on_bad_lines='skip')
                data['"VALOR TRANSFERIDO"'] = data['"VALOR TRANSFERIDO"'].str.strip('"').str.replace(',', '.').astype(float)
                data = data[(data['"UF"'].str.strip('"').isin(estados_regiao)) & (data['"NOME FUNÇÃO"'] == f'"{funcao}"')]
                yearSum += data['"VALOR TRANSFERIDO"'].sum()
        sumsByYear[year] = np.round(yearSum)

    return sumsByYear

def calcular_soma_total(estados_regiao, funcao, years):
    transferencias = calcular_transferencias_por_funcao(estados_regiao, funcao, years)
    return sum(transferencias.values())

# Lista de estados por região
estados_norte = ['AC', 'AP', 'AM', 'PA', 'RO', 'RR', 'TO']
estados_nordeste = ['AL', 'BA', 'CE', 'MA', 'PB', 'PE', 'PI', 'RN', 'SE']
estados_centro_oeste = ['GO', 'MT', 'MS', 'DF']
estados_sudeste = ['ES', 'MG', 'RJ', 'SP']
estados_sul = ['PR', 'RS', 'SC']

# Todos os estados combinados
estados_todos = estados_norte + estados_nordeste + estados_centro_oeste + estados_sudeste + estados_sul

# Anos de interesse
years = range(2020, 2023)

# Calcular a soma total das transferências para educação e ciência e tecnologia
soma_educacao = calcular_soma_total(estados_todos, 'Educação', years)
soma_ciencia_tecnologia = calcular_soma_total(estados_todos, 'Ciência e Tecnologia', years)

# Calcular a diferença percentual
if soma_educacao > 0:
    diferenca_percentual = ((soma_ciencia_tecnologia - soma_educacao) / soma_educacao) * 100
else:
    diferenca_percentual = 0

# Imprimir as somas e a diferença percentual
print(f'Soma das transferências para Educação (2020-2022): {soma_educacao} 🪙')
print(f'Soma das transferências para Ciência e Tecnologia (2020-2022): {soma_ciencia_tecnologia} 🪙')
print(f'Diferença percentual: {diferenca_percentual:.2f}%')

# Plotar o gráfico de barras
labels = ['Educação', 'Ciência e Tecnologia']
valores = [soma_educacao, soma_ciencia_tecnologia]
colors = ['blue', 'orange']

plt.figure(figsize=(10, 6))
bars = plt.bar(labels, valores, color=colors)

# Adicionar a diferença percentual abaixo das barras, perto do eixo x
plt.text(0.5, -max(valores)*0.1, f'Diferença Percentual: {diferenca_percentual:.2f}%', ha='center', va='top', fontsize=12, color='red')

# Adicionar título e rótulos dos eixos
plt.title('Soma de transferências para Educação e Ciência e Tecnologia (2020-2022)')
plt.ylabel('Soma das Transferências (em Milhões de Reais)')
plt.ylim(0, max(valores) * 1.2)  # Ajuste o limite superior do eixo y para dar espaço ao texto abaixo das barras

# Salvar e exibir o gráfico
plt.savefig('soma_transferencias_educacao_ciencia_tecnologia.png')
print('📊 Gráfico foi salvo como soma_transferencias_educacao_ciencia_tecnologia.png ✅')
plt.show()
