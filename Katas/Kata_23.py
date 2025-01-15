# 23.-  Concatena una lista de palabras. Usa la funcion reduce()


from functools import reduce #primero importaciones necesarias


lista_palabras = ["Concatena", " ", "una", " ",  "lista", " ", "de", " ",  "palabras"] # lista dada

# Utilizamos reduce(función, iterable)
# - lambda  
palabras_concatenadas = reduce(lambda palabra, contatenar: palabra + contatenar , lista_palabras)

print(palabras_concatenadas) # Imprimimos el resultado

# es similar al ejercicio anterior
