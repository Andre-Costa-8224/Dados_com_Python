import pandas as pd

def line():
	return print('–'*56)



dic = {'nome':['fulano','ciclano','bulano','sulano'],'nota':[4,6,5.5,8.5],'situação':['reprovado','aprovado','recuperação','aprovado']}

df = pd.DataFrame(data=dic)

print(df)


line()

print(df.head())

line()

print(df.shape)

line()

print(df.describe())