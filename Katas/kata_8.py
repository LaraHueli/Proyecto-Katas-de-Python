# 8.- "Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, 
# maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje indicando si la división fue exitosa o no."




# Pedir los números al usuario
numero1 = input("Por favor, introduce el primer número: ")
numero2 = input("Por favor, introduce el segundo número: ")

# Verificar si ambos son números
if numero1.isdigit() and numero2.isdigit(): # para verificar si son numeros usamos AND porque necesitamos que los dos sean
    numero1 = int(numero1) # Convertir las entradas a enteros
    numero2 = int(numero2)# Convertir las entradas a enteros

    # Verificar si el divisor es diferente de 0
    if numero1!= 0 and numero2!= 0:
        # Realizar la división
        division = numero1 / numero2
        print(f"El resultado de la división es: {division}")
    else:
        # Manejar el caso de división por cero
        print("No se puede dividir por cero. Inténtalo de nuevo.")
else:
    # Si alguno de los dos no es un número
    print("Por favor, introduce solo números válidos.")
