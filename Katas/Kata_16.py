# scribe una función que tome una cadena de texto y un número entero n como parámetros, y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter().

## Primero hago la función "larga"
def mas_larga_que(cadena_texto, n): #def nombre (parametros)
    lista_palabras_largas = []  # Inicializamos una lista vacía para guardar palabras largas
    for palabra in cadena_texto.split():  # Dividimos el texto en palabras y las recorremos
        if len(palabra) > n:  # Comprobamos si la longitud de la palabra es mayor que n
            lista_palabras_largas.append(palabra)  # Si cumple la condición, la añadimos a la lista
    return lista_palabras_largas  # Devolvemos la lista de palabras largas

# Variables de entrada
numero_n = 4  # Número que indica la longitud mínima para considerar "palabras largas"
cadena_texto = "Esto es una cadena de texto"  # Cadena de texto de ejemplo

# Llamamos a la función y mostramos el resultado
resultado = mas_larga_que(cadena_texto, numero_n)
print(resultado)  # Debería imprimir: ['Esto', 'cadena', 'texto']


## Ahora con lambda y filter()
def mas_larga_que(cadena_texto, n):
    # Usamos filter() con una función lambda para filtrar palabras largas
    return list(filter(lambda palabra: len(palabra) > n, cadena_texto.split()))

# Variables de entrada (las mismas)
numero_n = 4
cadena_texto = "Esto es una cadena de texto"

# Llamamos a la función y mostramos el resultado
resultado = mas_larga_que(cadena_texto, numero_n)
print(resultado)  # Debería imprimir: ['Esto', 'cadena', 'texto']

    
    