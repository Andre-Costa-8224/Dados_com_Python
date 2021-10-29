import pandas as pd

def line():
	return print('–'*56)

dic = {'nome':['fulano','ciclano','bulano','sulano'],'nota':[4,6,5.5,8.5],'situação':['reprovado','aprovado','recuperação','aprovado']}

df = pd.DataFrame(data=dic)

primeiraslinhas = df.loc[0:2]

line()

print(df.loc[df['nome']=='fulano'])

line()

print(df.loc[df['nota']!=6])

line()

print(primeiraslinhas)

line()

print(df.loc[df['situação']!='reprovado'])