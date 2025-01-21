# 37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras , reemplazar_palabras , eliminar_palabra . 
# Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función procesar_texto .
# Código a seguir:
# 1. Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene que devolver un diccionario.
# 2. Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra_nueva . Tiene que devolver el texto con el remplazo de palabras.
# 3. Crear una función eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra eliminada.
# 4. Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y número de argumentos variable según la opción indicada.
# Caso de uso:
# Comprueba el funcionamiento completo de la función procesar_texto

def contar_palabras (texto):
    palabras = texto.split() # .split() divide el texto en una lista de palabras separadas
    conteo = {} # Icontador diccionario a cero y vacio
    for palabra in palabras: #iteramos sobre cada palabra de la lista
        conteo[palabra]=conteo.get(palabra, 0) + 1 #.get busca la palabra, si esta edvuleve 0 y si no esta suma 1
    return conteo    


def reemplazar_palabras(texto, palabra_original, palabra_nueva): 
    return texto.replace(palabra_original, palabra_nueva) # devuelve el texto donde reemplaza la original por la nueva

def eliminar_palabra(texto, *palabra_eliminada): #ponemos* para tener un numero x de palabras
    palabras = texto.split()  # .split() divide el texto en una lista de palabras separadas
    palabras = [p for p in palabras if p != palabra_eliminada] #iteracion y cambio
    return " ".join(palabras) # .join() para unir las palabras de la lista en un único string

def procesar_texto(texto, opcion, *args): # texto de siempre, funcion a ejecutar, argumentos variables
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        return reemplazar_palabras(texto, *args)
    elif opcion == "eliminar":
        return eliminar_palabra(texto, *args)
    else:
        raise ValueError("Opción no válida")


texto = "Estoy haciendo un proyecto de Katas en python"
# Contar palabras
print(procesar_texto(texto, "contar"))

# Reemplazar una palabra
print(procesar_texto(texto, "reemplazar", "Katas", "ejercicios"))

# Eliminar una palabra
print(procesar_texto(texto, "eliminar", ("un", "proyecto", "de")))
