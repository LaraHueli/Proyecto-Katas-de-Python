# 2.- Dada una lista de numeros, obten una nueva lista con el doble de cada valor. Usa la funcion map()

# Usando un bucle for

numeros = [1,3,5,7,9,2,4,6,8,10]
dobles =[] # lista vacía dobles
for n in numeros: #buvle for para añadir el doble
    dobles.append(n*2)
print(dobles)    


# map(función, iterable). usando lambda que es como la funcion comodin
numeros = [1,3,5,7,9,2,4,6,8,10]
dobles = map(lambda n: n * 2, numeros) # map aplica la función lambda a cada elemento de la lista
print(list (dobles) ) #  mostrar el resultado como lista, hay que convertir  map a list()



# map(función, iterable).  Definiendo una función normal
numeros = [1,3,5,7,9,2,4,6,8,10]
def valor_doble(n): # Definimos una función que multiplica un número por 2
    return n * 2
dobles = map(valor_doble, numeros) # map aplica la función "valor_doble" a cada elemento de la lista
print(list(dobles))