# 22 Dada una lista numerica, obten el producto total de los valores de dicha lista usando la funcion reduce()

from functools import reduce #primero importaciones necesarias


numeros = [1, 3, 5, 7, 9] # lista dada

# Utilizamos reduce(función, iterable)
# - lambda x, y: x * y 
producto = reduce(lambda x, y: x * y, numeros)

print(producto) # Imprimimos el resultado
