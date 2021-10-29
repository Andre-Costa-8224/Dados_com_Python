import numpy as np

cadastro = np.random.randint(12,62,size=(50,10))
print(cadastro)
print(cadastro[0])

cadastro_maior18 = cadastro>18

print(cadastro_maior18,'\n\nquantidade de pessoas a serem chamadas:',len(cadastro_maior18),'\n\n',cadastro[cadastro>25])

condicao = cadastro>35

extraido = np.extract(condicao,cadastro)


