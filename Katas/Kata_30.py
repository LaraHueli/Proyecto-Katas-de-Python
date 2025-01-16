# 30 Crea una funcion que determine si dos palabras son anagramas, es decir, si estan formadas por las mismas letras pero en diferente orden. 

# 30.- Crea una función que determine si dos palabras son anagramas

# Definimos la función
def son_anagramas(palabra1, palabra2):
    # Normalizamos las palabras a minúsculas para evitar problemas con mayúsculas
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()
    
    # Ordenamos las letras de cada palabra
    # El método `sorted` toma una secuencia (como una cadena) y devuelve una lista con los elementos ordenados.
    # Por ejemplo: sorted("amor") -> ['a', 'm', 'o', 'r']
    # Esto nos ayuda a comparar si las palabras tienen las mismas letras, sin importar el orden original.
    letras1 = sorted(palabra1)
    letras2 = sorted(palabra2)
    
    # Comparamos las listas ordenadas de letras
    if letras1 == letras2:
        return True  # Las palabras son anagramas
    else:
        return False  # No son anagramas

# Ejemplo de uso
palabra1 = "amor"
palabra2 = "roma"
resultado = son_anagramas(palabra1, palabra2)

# Mostramos el resultado
print(f"¿Las palabras '{palabra1}' y '{palabra2}' son anagramas? {resultado}")
