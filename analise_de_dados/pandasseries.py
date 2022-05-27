import pandas as pd
import numpy as np

lista = [1,2,3,'olá',6.5,np.nan,8]
tupla = (1,2,'aba')
dicionario = {'telefone':94159469,'email':'amdre8224@gmail.com','nome':'André'}

dados1 = [1,2,3,4]

dados2 = [3,2,4,1]

s1 = pd.Series(lista)

s2 = pd.Series(tupla)

s3 = pd.Series(dicionario)

indices1 = ['Brasil','Argentina','Japão','USA']

indices2 = ['USA','Brasil','Argentina','Japão']

s4 = pd.Series(data=dados1, index=indices1)

s5 = pd.Series(data=dados2,index=indices2)

print(s1,'\n\n')
print(s2,'\n\n')
print(s3,'\n\n')
print(s4,'\n\n')
print(s5,'\n\n')
print(s4+s5)