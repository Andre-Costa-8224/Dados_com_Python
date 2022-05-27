kmh = [30,40,60,80,100,120]#cria a lista a ser usada

"OBSERVE QUE PARA USAR A FUNÇÃO MAP É NECESSARIO UTILIZAR UMA FUNÇÃO E DEPOIS INDICAR QUAIS DADOS SERÃO UTILIZADOS NESSA FUNCÃO."

mph1 = list(map(lambda x: x/1.61,kmh))

#OBS: A FUNCÃO DE DENTRO NÃO PRECISA SER LAMBDA, PODE USAR UMA FUNCAO DEF

def func(x):
	y = x/1.61
	return y
	

#ou

"""
def func(x):
	return x/1.61
"""

mph2 = list(map(func, kmh))#cria a nova lista usando a função map utilizando dentro dela uma função lambda

print(mph1,'\n\n',mph2)