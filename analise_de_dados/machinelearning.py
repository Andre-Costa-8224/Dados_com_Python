import pandas as pd
from sklearn.model_selection import train_test_split#train test split serve para criar o treino e o teste do machine learning
from sklearn.ensemble import ExtraTreesClassifier#serve para executar o treino e o teste de machine learning

dados = pd.read_csv('/storage/emulated/0/Documents/wine_dataset.csv')

dados['style'] = dados['style'].replace('red',0)

dados['style'] = dados['style'].replace('white',1)

print(dados)

y = dados['style']
x = dados.drop('style',axis=1)

x_teste, x_treino, y_teste, y_treino = train_test_split(x, y, test_size=0.3)

#criação do modelo
modelo = ExtraTreesClassifier()
modelo.fit(x_treino,y_treino)

#resultados
resultado = modelo.score(x_teste,y_teste)
print('Acurácia',resultado)

print(x_teste[400:403])
print(y_teste[400:3])

previsoes = modelo.predict(x_teste)
print(previsoes)
