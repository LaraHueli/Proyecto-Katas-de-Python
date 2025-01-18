# 31 Crea una funcion que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista. Si el nombre esta en la lista, se imprime un 
# mensaje indicando que fue encontrado, de lo contrario, se lanza una excepcion

def buscar_en_lista ():
    try:
        lista_nombres = input(f"Por favor, igresa una lsita de nombres: ").split(",") # .split(",") es un método que convierte un string en una lista. 
        nombre_buscado = input(f"¿Que nombre quieres buscar?: ")
        
        for nombre in lista_nombres:
            if nombre.strip() == nombre_buscado:
                return(f"El nombres buscado es: {nombre_buscado} y esta en la lista nombres ")
                break  # Salimos del bucle al encontrar el nombre
        else:
                raise ValueError# Si el bucle termina sin encontrar el nombre, lanzamos una excepción
    except ValueError:
        return("Error: El nombre que buscas no esta en la lista.")  # Si no se puede convertir a entero, muestra este mensaje     
print(buscar_en_lista())        