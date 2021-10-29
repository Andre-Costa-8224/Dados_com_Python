import pandas as pd

def line():
	return print('–'*56)

dic = {'nome':['fulano','ciclano','bulano','sulano'],'nota':[4,6,5.5,8.5],'situação':['reprovado','aprovado','recuperação','aprovado']}

df = pd.DataFrame(data=dic)

print(df)

line()

print(df['nome'])#coluna

line()

print(df.loc[[0]],f'\n{"–"*56}\n',df.loc[[2,0,3]],f'\n{"–"*56}\n',df.loc[0:2])#filtra linha

line()

print(df.loc[df['nome']=='ciclano'])
