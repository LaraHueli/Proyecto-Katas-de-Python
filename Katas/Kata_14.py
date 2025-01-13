# Crea una funcion que retorne las palabras de una lista de palabras que comiencen con una letra es especifico. Usa la funcion filter().


lista_palabras = ["casa", "perro", "familia", "estudio", "Daniela", "Martina", "Miguel Angel", "Lara", "colegio", "trabajo", "manzana", "objeto", "sol"]

letra = input(f"¿Porque letras quiere que empiece?")

palabras_m = filter(lambda palabra: palabra.lower().startswith(letra), lista_palabras)

print(list(palabras_m))