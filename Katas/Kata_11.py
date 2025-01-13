# Escribe un programa que pida al usuarioque introduzca su edad. Si el usuarioingresa un valor no numerico o un valor fuera del rango esperado (por ejemplomenos que 0 o mayor que 120).
# maneja la excepciones adecuadamente

try:
    edad = int(input(f"por favor, introduce tu edad: "))  # Intenta convertir la entrada a un entero

    if edad <= 0 or edad > 120 and edad is not int:
     print(f"Has introducido {edad} años, eso no es un valor valido.")
    else:
     print(f"Tu edad son {edad} años.")    
except ValueError:
    print("Error: Debes ingresar un número entero.")  # Si no se puede convertir a entero, muestra este mensaje     