import matplotlib.pyplot as plt
import numpy as np

l1 = [1,2,3,4,5,6,7,8,9]

l2= [2,4,6,8,10,12,14,16,18]

x = np.arange(-100,100,1)

#plt.scatter(l1,l2)#metedo para graficos simples

plt.plot(x, x**5)#metodo para graficos com funcoes

plt.show()