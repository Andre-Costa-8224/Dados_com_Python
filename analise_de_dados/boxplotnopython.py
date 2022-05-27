import pandas as pd
import matplotlib.pyplot as plt


dados = pd.read_csv('/storage/emulated/0/Documents/athlete_events.csv')


dados.boxplot(column=['Age','Weight','Height'])
plt.show()