import pandas as pd
import csv
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns

years = range(2019, 2025)
months = ['01', '02', '03']
sumsByYear = {}

# Loop sobre os anos
for year in years:
    # Inicializar a soma do ano
    yearSum = 0
    # Loop sobre os meses do primeiro trimestre
    for month in months:
        # Construir o caminho do arquivo
        file = f'./docs/{year}/{year}{month}_Transferencias.csv'
        # Verificar se o arquivo existe
        if os.path.exists(file):
            print(f'🔍 Lendo o arquivo: {file} ')
            # Carregar o DataFrame
            data = pd.read_csv(file, sep=';', quoting=csv.QUOTE_NONE, encoding='latin-1', on_bad_lines='skip')
            # Limpar a coluna "VALOR TRANSFERIDO"
            data['"VALOR TRANSFERIDO"'] = data['"VALOR TRANSFERIDO"'].str.strip('"').str.replace(',', '.').astype(float)
            # Filtrar os dados para a UF de SP e a função de educação
            data = data[(data['"UF"'] == '"SP"') & (data['"NOME FUNÇÃO"'] == '"Educação"')]
            # Adicionar a soma do mês à soma do ano
            yearSum += data['"VALOR TRANSFERIDO"'].sum()
    # Armazenar a soma do ano no dicionário de somas por ano
    sumsByYear[year] = np.round(yearSum)

# Imprimir as somas por ano
for year, soma in sumsByYear.items():
    print(f'✅ A soma das transferencias realizadas pelo governo para educação em São Paulo no primeiro trimestre de {year} foi: {soma} 🪙')

# Criar uma figura e um eixo (subplot)
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plotar a soma dos valores no primeiro eixo
ax1.plot(sumsByYear.keys(), sumsByYear.values(), marker='o', color='skyblue', linestyle='-', label='Soma das Transferências')
ax1.set_xlabel('Ano')
ax1.set_ylabel('Soma das Transferências')
ax1.ticklabel_format(style='plain', axis='y', useOffset=False)
ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: '{:,.0f}M'.format(x / 1e6)))
ax1.grid(True)

# Adicionar valores percentuais de aumento/diminuição acima de cada ponto do gráfico azul
for year, value in sumsByYear.items():
    if year != min(sumsByYear.keys()):
        difference_percent = ((value - sumsByYear[year - 1]) / sumsByYear[year - 1]) * 100
        ax1.text(year, value, f'{difference_percent:.2f}%', ha='center', va='bottom', fontsize=8)

# Título geral para o gráfico
plt.title('Soma de valor das transferências e Variação Percentual para educação em SP no 1 trimestre anualmente')

# Salvar o gráfico como um arquivo PNG
plt.savefig('soma_e_variacao_percentual.png')


print('📊 Gráfico combinado foi salvo como soma_e_variacao_percentual.png ✅')
