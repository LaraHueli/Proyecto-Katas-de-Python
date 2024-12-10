# 1.- Escribe una función que reciba una cadena e texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. 
# Los espacios no deben ser considerados.

def contar_frecuencias (cadena_texto):
   cadena = cadena_texto.replace (" ", "")  # .replace elimina espacios. sustituimos " " por "" (" ","")
   frecuencias = {} # creamos diccionario vacio
   for letra in cadena: # empezamos bucle para contar
       if letra in frecuencias:
           frecuencias[letra] += 1 # Si la letra ya está en el diccionario incrementamos su valor con += 1
       else:
           frecuencias[letra] = 1  # Si no está, lo agregamos al diccionario con un valor inicial de 1
   return frecuencias # devuelve el diccionario

cadena_texto = "esto es una cadena de texto" #definimos la variable
resultado = contar_frecuencias(cadena_texto) # llamamos a la funcion
print(resultado) #imprimimos el resultado
        