import pandas as pd

dados = pd.read_csv('/storage/emulated/0/Documents/athlete_events.csv')

dados.drop('ID', axis=1)#axis é pra dizer se é linha ou coluna, se axis = 1 então é coluna, mas se axis = 0 então é linha.

dados.drop('Season', axis=1)

dados.drop('NOC', axis=1)