import pandas as pd
import pandas_ods_reader as pdr

dados = pd.read_excel('/storage/emulated/0/Documents/arquivo1.xlsx', engine='openpyxl')

dados2 = pd.read_csv('/storage/emulated/0/Documents/athlete_events.csv')

dados3 = pdr.read_ods('/storage/emulated/0/Documents/arquivo1.ods',1)

print(dados2.head(5))