import pandas as pd

dados = pd.read_csv('/storage/emulated/0/Documents/athlete_events.csv')

print(dados.head())

dados2 = dados.dropna()#exclui dados faltantes

print(dados2,'\n',dados2.shape,end='\n')

faltantes = dados.isnull()#mostra em quais posicoes tem dados faltantes e a quantidade

print()
print(faltantes)
print()

faltante_total = dados.isnull().sum()

print()
print(faltante_total)
print()

faltante_percentual = (dados.isnull().sum()/len(dados['ID']))*100

print()
print(faltante_percentual)
print()

print()
print(dados['Medal'].fillna('Não Informado'))#FILLNA preenche os dados faltantes com strings, inteiros etc, ou com medias e medianas
print()

print()
print(dados['Age'].fillna(dados['Age'].mean()))
print()

print()
print(dados['Height'].fillna(dados['Height'].mean()))
print()

print()
print(dados['Weight'].fillna(dados['Weight'].mean()))