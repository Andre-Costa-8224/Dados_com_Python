#compressao de lista é usar o for em uma so linha dentro da lista

kmh = [30,40,60,80,100,120]#cria a variavel do tipo lista

"OBSERVE QUE PARA CRIAR A LIST COMPREHENSION PRECISA FAZER O FOR DE TRÁS PRA FRENTE, OU SEJA, COLOCAR O QUE VAI SER FEITO ANTES E O FOR EM SÍ DEPOIS"

mph = [x/1.61 for x in kmh]#cria a nova lista

print(mph)