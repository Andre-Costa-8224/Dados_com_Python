#criar uma relacao do peso e altura dos atletas masculinos
import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('/storage/emulated/0/Documents/athlete_events.csv')

dadosmasc = dados.loc[dados['Sex']=='M']

plt.scatter(dadosmasc['Height'],dadosmasc['Weight'])
plt.show()
