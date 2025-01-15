# Crea una funcion que calcule el cubo de un numero dado mediante una funcion lambda

numero = int(input(f"Por favor, introduce un numero: ")) # pedimos al usuario que ingrese un numero

numero_cubo = lambda n: n ** 3 # lambda argumento: expresion

resultado = (numero_cubo(numero)) # metemos el resultado en una variable

print(f"Has introducido el numero: {numero}. Y su cubo es: {resultado}.") #printeamos
 