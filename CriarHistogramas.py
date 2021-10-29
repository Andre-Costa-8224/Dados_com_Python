import pandas as pd
import matplotlib.pyplot as plt


dados = pd.read_csv('/storage/emulated/0/Documents/athlete_events.csv')


print(dados.hist(column='Weight', bins=100))

#da pra usar arrays do numpy para criar histogramas, a sintaxe é:  plt.hist(nome_da_variavel,bins=100)

plt.show()