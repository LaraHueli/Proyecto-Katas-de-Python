# 29 Crea una funcion que convierta una variable en una cadena de texto y enmascare todos los caracteres con el caracter #, excepto los 4 ultimos.

def enmascarar(variable): # creamos la funcion
   
    texto = str(variable)  # Convertimos la variable a cadena de texto
    
    # Enmascaramos todos menos los últimos 4 caracteres
    enmascarado = "#" * (len(texto) - 4) + texto[-4:]
    
    return enmascarado     # Devolvemos el resultado


variable = "Esto es una variable"
resultado = enmascarar(variable)
print(resultado)  
