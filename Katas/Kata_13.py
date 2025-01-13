# Genera una funcion la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayuscula y minuscula. Las letras no puedes estar repetidas. Usa Map().

# Lista de ejemplo
lista = ["MaYuScUlAs"]

# Creamos la función
def tupla_mayus_minus(lista):
    # set(lista[0]) convierte la palabra en un conjunto. El conjunto de "MaYuScUlAs" sería: {'M', 'a', 'u', 'Y', 'S', 'C', 'l'}
    lista_unica = set(lista[0])  # Solo tomamos el primer elemento
    # map (itera cada letra) y va usando lower y upper. en cada letra y pasando a Masyuscual  y minusclua cada letra en lista unica
    resultado = map(lambda letra: (letra.upper(), letra.lower()), lista_unica) 
    # Convertimos el resultado a lista y lo retornamos
    return list(resultado)

# Llamamos a la función
print(tupla_mayus_minus(lista))
