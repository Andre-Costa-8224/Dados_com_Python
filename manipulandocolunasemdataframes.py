import pandas as pd

dados = pd.read_csv('/storage/emulated/0/Documents/athlete_events.csv')

print(dados.head())

dados.rename(columns={'Name':'Nome','Sex':'sexo','Age':'Idade'},inplace=True)#inplace serve pra não mostrar o resultado

print()

print(dados['ID'], type(dados['ID']))

print()

print(dados['Medal'].value_counts())

print()

print(dados['City'].value_counts())

print()

print(dados.describe())