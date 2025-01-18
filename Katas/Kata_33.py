# 33 Crea una funcion lambda que sume elementos correspondientes de dos listas dadas

sumar_listas = lambda x, y: x + y # Definimos la función lambda que suma dos valores


lista1 = [3, 5, 7, 9]
lista2 = [10, 20, 30, 40]


resultado = list(map(sumar_listas, lista1, lista2))  #map para iterar sobre cada elemento y list para transformar a lista

# Mostramos el resultado
print(resultado)  # Salida: [13, 25, 37, 49]
