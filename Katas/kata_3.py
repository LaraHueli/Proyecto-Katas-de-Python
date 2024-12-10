
# 3.- Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original 
# que contengan la palabra objetivo.


palabras = [ "navidad", "villancicos", "arbolito", "luces", "estrella", "regalos", "nieve", "chimenea", "campanas", "turrón", "guirnaldas", "belén", "felicitaciones", "arbol"]

busqueda = "arbol"  # Definimos busqueda como un string
# def nombre_funcion (parametro1, parametro2). en este caso parametro1 (lista de partida) y parametro2 (que queremos buscar)
def buscar_palabras(palabras, busqueda): # Función que busca palabras que contengan la palabra clave
    nueva_lista = []
    for palabra in palabras: # Recorremos cada palabra de la lista
        if busqueda in palabra: # Verificamos si contiene la palabra clave
            nueva_lista.append(palabra) # La añadimos a la nueva lista
    return nueva_lista # Devolvemos las coincidencias

resultado = buscar_palabras(palabras, busqueda)
print(resultado)