# Crea una función lambda que sume 3 a cada número de una lista dada.

# Lista de entrada
lista_dada = [2, 4, 3, 7, 5]  # Esta es la lista de números sobre la cual vamos a trabajar.

# Usamos map() para aplicar la función lambda a cada elemento de la lista.
# La función lambda toma cada número de la lista y le suma 3.
lista_por_3 = map(lambda x: x + 3, lista_dada)  # La función lambda toma x y devuelve x+3 para cada elemento.

# Imprimimos el resultado como una lista.
# Como map() devuelve un objeto 'map', lo convertimos en una lista para imprimir los valores.
print(list(lista_por_3))  # Convertimos el resultado de map() en una lista y lo imprimimos.
