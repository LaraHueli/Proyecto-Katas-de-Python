# genera una funcion que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la funcion map()-


# Pedir al usuario que ingrese una frase
frase = input("Por favor, ingresa una frase: ")
print(f"Has introducido : {frase}")

palabras = frase.split() # Dividimos la frase en palabras con el metodo split()

longitud_palabras = map(len, palabras)# Usamos map() para obtener la longitud de cada palabra

print(list(longitud_palabras))# Convertimos el resultado a una lista para imprimirlo
