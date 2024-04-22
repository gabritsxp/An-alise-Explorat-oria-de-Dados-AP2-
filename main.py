import pandas as pd
import csv
import numpy as np

# Carregando o DataFrame com ponto e vírgula como delimitador
data2024firstMounth = pd.read_csv('./docs/202401_Transferencias.csv', sep=';', quoting=csv.QUOTE_NONE, encoding='latin-1', on_bad_lines='skip')

data2024secondMounth = pd.read_csv('./docs/202402_Transferencias.csv', sep=';', quoting=csv.QUOTE_NONE, encoding='latin-1', on_bad_lines='skip')

data2024tirthMounth= pd.read_csv('./docs/202403_Transferencias.csv', sep=';', quoting=csv.QUOTE_NONE, encoding='latin-1', on_bad_lines='skip')

# Remover as aspas extras da coluna "VALOR TRANSFERIDO" antes de tentar converter para float
data2024firstMounth['"VALOR TRANSFERIDO"'] = data2024firstMounth['"VALOR TRANSFERIDO"'].str.strip('"').str.replace(',', '.').astype(float)

data2024secondMounth['"VALOR TRANSFERIDO"'] = data2024secondMounth['"VALOR TRANSFERIDO"'].str.strip('"').str.replace(',', '.').astype(float)

data2024tirthMounth['"VALOR TRANSFERIDO"'] = data2024tirthMounth['"VALOR TRANSFERIDO"'].str.strip('"').str.replace(',', '.').astype(float)

sumValue = data2024firstMounth['"VALOR TRANSFERIDO"'].sum()
roundedSumValue = np.round(sumValue)

print("Valor das transferencias realizadas pelo governo em 01-2024:" , roundedSumValue)
