#  Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo", "triangulo" ) y datos  (una tupla con los datos necesarios para 
# calcular el área de la figura).

# "rectangulo", la tupla datos debe contener el ancho y el alto (en ese orden).
# "circulo", la tupla datos debe contener el radio.
# "triangulo", la tupla datos debe contener la base y la altura (en ese orden).

import math # Importamos la librería math para operaciones matematicas.

def calcular_area (figura,datos): # definimos la funcion
    if figura == "rectangulo":
        area = datos[0] * datos[1]   # Esto toma el valor del ancho (datos[0]) y lo multiplica por el alto (datos[1])
        return f"Has elegido un rectangulo y su area es {area}"
    elif figura == "circulo":
        area = math.pi * (datos[0] ** 2)  # Calcula el area del circulo
        return f"Has elegido un circulo y su area es {area}"
    elif figura == "triangulo":
        area = (datos[0] * datos[1]) / 2  # Calcula el area del triangulo
        return f"Has elegido un triangulo y su area es {area}"



figura = input("¿Que figura deseas calcular (rectangulo, circulo, triangulo)? ") # pedir al usuario

if figura == "rectangulo":
    ancho = float(input("Ingresa el ancho del rectangulo: "))  # Ancho del rectangulo
    alto = float(input("Ingresa el alto del rectangulo: "))  # Alto del rectangulo
    datos = (figura, (ancho, alto))  # Creamos la tupla con la figura y sus datos
elif figura == "circulo":
    radio = float(input("Ingresa el radio del circulo: "))  # Radio del circulo
    datos = (figura, (radio,))  # Tupla con la figura y el radio
elif figura == "triangulo":
    base = float(input("Ingresa la base del triangulo: "))  # Base del triangulo
    altura = float(input("Ingresa la altura del triangulo: "))  # Altura del triangulo
    datos = (figura, (base, altura))  # Tupla con la figura y sus datos
else:
    print("Figura no reconocida.")  # Mensaje de error si la figura no es valida
    datos = None  # No asignamos datos si la figura no es valida
    
if datos: # con este if solo llamamos a la funcion calcular_area si los datos son validos
    print(calcular_area(*datos)) # llamamos a la funcion



