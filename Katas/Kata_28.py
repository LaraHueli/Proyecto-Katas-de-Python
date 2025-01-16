# 28 Crea una función que busque y devuelva el primer elemento duplicado en una lista dada


def primer_duplicado(lista): # Definimos la función
   
    set_duplicados = set()  # conjunto vacío que no permite duplicados
  
    for numero in lista:  # Recorremos la lista con un bucle for
       
        if numero in set_duplicados:
            return numero
        set_duplicados.add(numero) # usamos add, porque los set no aceptan appdend
    return None


lista_numeros = [3, 1, 4, 2, 5, 3, 6, 7, 8, 4]


resultado = primer_duplicado(lista_numeros)# Llamamos a la función y guardamos el resultado 


print(f"El primer elemento duplicado es: {resultado}")
