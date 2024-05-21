import pandas as pd
import csv
import numpy as np
import os
import matplotlib.pyplot as plt

def plot_transferencias_por_regiao(estados_regiao, regiao, color, funcao):
    sumsByYear = {}

    years = range(2019, 2025)
    months = ['01', '02', '03']

    # Loop sobre os anos
    for year in years:
        yearSum = 0
        # Loop sobre os meses do primeiro trimestre
        for month in months:
            # Construir o caminho do arquivo
            file = f'./docs/{year}/{year}{month}_Transferencias.csv'
            # Verificar se o arquivo existe
            if os.path.exists(file):
                # Carregar o DataFrame
                data = pd.read_csv(file, sep=';', quoting=csv.QUOTE_NONE, encoding='latin-1', on_bad_lines='skip')
                # Limpar a coluna "VALOR TRANSFERIDO"
                data['"VALOR TRANSFERIDO"'] = data['"VALOR TRANSFERIDO"'].str.strip('"').str.replace(',', '.').astype(float)
                # Filtrar os dados para a UF da região e a função especificada
                data = data[(data['"UF"'].str.strip('"').isin(estados_regiao)) & (data['"NOME FUNÇÃO"'] == f'"{funcao}"')]
                # Adicionar a soma do mês à soma do ano
                yearSum += data['"VALOR TRANSFERIDO"'].sum()
        # Armazenar a soma do ano no dicionário de somas por ano
        sumsByYear[year] = np.round(yearSum)

    # Imprimir as somas por ano
    for year, soma in sumsByYear.items():
        print(f'✅ A soma das transferências realizadas pelo governo para {funcao} na {regiao} no primeiro trimestre de {year} foi: {soma} 🪙')

    # Plotar a soma dos valores para a região com a cor específica
    plt.plot(sumsByYear.keys(), sumsByYear.values(), marker='o', linestyle='-', color=color, label=regiao)

# Lista de estados por região
estados_norte = ['AC', 'AP', 'AM', 'PA', 'RO', 'RR', 'TO']
estados_nordeste = ['AL', 'BA', 'CE', 'MA', 'PB', 'PE', 'PI', 'RN', 'SE']
estados_centro_oeste = ['GO', 'MT', 'MS', 'DF']
estados_sudeste = ['ES', 'MG', 'RJ', 'SP']
estados_sul = ['PR', 'RS', 'SC']

# Configurar cores para cada região
cores = ['blue', 'orange', 'green', 'red', 'purple']

# Gerar gráfico para Educação
plt.figure(figsize=(10, 6))

plot_transferencias_por_regiao(estados_norte, 'Região Norte', cores[0], 'Educação')
plot_transferencias_por_regiao(estados_nordeste, 'Região Nordeste', cores[1], 'Educação')
plot_transferencias_por_regiao(estados_centro_oeste, 'Região Centro-Oeste', cores[2], 'Educação')
plot_transferencias_por_regiao(estados_sudeste, 'Região Sudeste', cores[3], 'Educação')
plot_transferencias_por_regiao(estados_sul, 'Região Sul', cores[4], 'Educação')

plt.legend()
plt.title('Soma de valor das transferências para educação por região no 1º trimestre anualmente')
plt.xlabel('Ano')
plt.ylabel('Soma das Transferências (em Milhões de Reais)')
plt.savefig('soma_transferencias_educacao_por_regiao.png')
print('📊 Gráfico de Educação foi salvo como soma_transferencias_educacao_por_regiao.png ✅')
plt.show()

# Gerar gráfico para Ciência e Tecnologia
plt.figure(figsize=(10, 6))

plot_transferencias_por_regiao(estados_norte, 'Região Norte', cores[0], 'Ciência e Tecnologia')
plot_transferencias_por_regiao(estados_nordeste, 'Região Nordeste', cores[1], 'Ciência e Tecnologia')
plot_transferencias_por_regiao(estados_centro_oeste, 'Região Centro-Oeste', cores[2], 'Ciência e Tecnologia')
plot_transferencias_por_regiao(estados_sudeste, 'Região Sudeste', cores[3], 'Ciência e Tecnologia')
plot_transferencias_por_regiao(estados_sul, 'Região Sul', cores[4], 'Ciência e Tecnologia')

plt.legend()
plt.title('Soma de valor das transferências para ciência e tecnologia por região no 1º trimestre anualmente')
plt.xlabel('Ano')
plt.ylabel('Soma das Transferências (em Milhões de Reais)')
plt.savefig('soma_transferencias_ciencia_tecnologia_por_regiao.png')
print('📊 Gráfico de Ciência e Tecnologia foi salvo como soma_transferencias_ciencia_tecnologia_por_regiao.png ✅')
plt.show()
