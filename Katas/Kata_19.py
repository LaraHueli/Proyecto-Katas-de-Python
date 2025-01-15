# Crea una funcion lambda que filtre los numeros impares de una lista dada

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #lista dada

numeros_impares = list(filter(lambda n: n %2 != 0, numeros))

print(numeros_impares)