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
            # Adicionar a soma do mês à soma do ano
            yearSum += data['"VALOR TRANSFERIDO"'].sum()
    # Armazenar a soma do ano no dicionário de somas por ano
    sumsByYear[year] = np.round(yearSum)

# Imprimir as somas por ano
for year, soma in sumsByYear.items():
    print(f'✅ A soma das transferencias realizadas pelo governo no primeiro trimestre de {year} foi: {soma} 🪙')

# Plotar o gráfico de soma
plt.figure(figsize=(10, 6))
plt.bar(sumsByYear.keys(), sumsByYear.values(), color='skyblue')
plt.title('Soma de valor das transferencias no 1 trimestre anualmente')
plt.xlabel('Ano')
plt.ylabel('Soma das Transferências')
plt.grid(True)

# Salvar o gráfico como um arquivo PNG
plt.savefig('soma_dos_valores_dos_trimestres.png')

print('📊 Gráfico de soma foi salvo como soma_dos_valores_dos_trimestres.png ✅')

# Calcular a diferença percentual entre os valores de sumsByYear
differences = {}
previous_value = None
for year, value in sumsByYear.items():
    if previous_value is not None:
        difference_percent = ((value - previous_value) / previous_value) * 100
        differences[year] = difference_percent
    previous_value = value

# Plotar o gráfico
plt.figure(figsize=(10, 6))
sns.barplot(x=list(differences.keys()), y=list(differences.values()), palette='coolwarm')
plt.title('Diferença Percentual nas Soma Anual das Transferências')
plt.xlabel('Ano')
plt.ylabel('Diferença Percentual (%)')
plt.grid(True)

# Salvar o gráfico como um arquivo PNG
plt.savefig('diferenca_percentual.png')

print('📊 Gráfico de percentual foi salvo como diferenca_percentual.png ✅')

