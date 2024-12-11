# 7.- "Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()."

lista_tuplas = [(2,4,6), ("dos", "cuatro", "seis")]

lista_strings = list(map(lambda tupla: str(tupla), lista_tuplas))
print (lista_strings)
print (type(lista_strings))