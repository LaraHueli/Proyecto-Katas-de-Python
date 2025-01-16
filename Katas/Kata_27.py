# 27  Crea una funcion que calcule el promedio de una lista de numeros

lista_numeros =[2,7,5,3,8,12]

promedio = lambda numeros: sum(numeros)/len(numeros)

resultado = round((promedio(lista_numeros)),2)

print(f"El promedio de la lista: {lista_numeros} es :{resultado}")