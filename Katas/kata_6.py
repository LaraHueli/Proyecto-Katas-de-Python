# 6.- "Escribe una función que calcule el factorial de un número de manera recursiva."


# Solicitar al usuario que introduzca un número
numero = int(input("Por favor, introduce un número: "))

# Función recursiva para calcular el factorial
def factorial(n):
    if n == 0:  # Caso base: el factorial de 0 es 1
        return 1
    else:  # Caso recursivo: n * factorial(n-1)
        return n * factorial(n - 1)

# Llamar a la función y mostrar el resultado
resultado = factorial(numero)
print(f"El factorial de {numero} es: {resultado}")
