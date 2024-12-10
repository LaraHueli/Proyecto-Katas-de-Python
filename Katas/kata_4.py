# 4.-Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()."



lista1 = [7,8,9,10]
lista2 = [1,5,7,8]
diferencia = map(lambda x, y: x - y, lista1, lista2)
print (list(diferencia))                



lista1 = [7,8,9,10]
lista2 = [1,5,7,8]
def resta (x,y):
    return x-y
diferencia = map(resta, lista1, lista2)
print(list(diferencia))





