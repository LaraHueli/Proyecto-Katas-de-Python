# 25 Crea una funcion que cuente el numero de caracteres en una cadena de texto dada. no me des el resultado

texto = ["cadena de texto dada"]

def contar_caracteres(texto):
   
    numero_caracteres = 0 # contador = 0 
   
    for palabra in texto:
        
        numero_caracteres += len(palabra) # sumamos la longitud al contador (numero_caracteres = numero_caracteres + longitud_palabra)
    return numero_caracteres


resultado = contar_caracteres(texto)
print(f"El numero total de caracteres es: {resultado}")

#opcion corta
from functools import reduce  # Importamos 

texto = "cadena de texto dada"

numero_caracteres = reduce(lambda palabra, caracter: palabra + 1, texto, 0) # texto, 0): para poner un contador
 
print(f"El numero total de caracteres es: {numero_caracteres}")
