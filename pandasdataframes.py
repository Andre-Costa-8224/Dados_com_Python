import pandas as pd
import numpy as np

#criacao de dataframes a partir de arrays

arr = np.random.randint(10,55,size=(4,4))

print(arr)

df1 = pd.DataFrame(data=arr,index=['a','b','c','d'],columns=['w','x','y','z'])

print(df1)

#criacao de dataframes a partir de listas

lista = [[10,20,30],[40,50,60],[70,80,90],[100,110,120]]

df2 = pd.DataFrame(data=lista,index=['linha1','linha2','linha3','linha4'],columns=['coluna1','coluna2','coluna3'])

print(df2)

#criacao de dataframes a partir de listas

dados = {'Produtos':['Xbox','PS5','Mouse','Monitor','Teclado','PC'],'Preços':[2269.99,3655,32.50,230,56,2468.99]}

df3 = pd.DataFrame(data=dados)

df3['Custo'] = [1720,2999,27.99,189,44,1918.99]

df3['Lucro'] = df3['Preços']-df3['Custo']

print(df3)