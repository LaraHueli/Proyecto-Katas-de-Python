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
        
        
###-------------------------------------------------------------------------------------------------------------------------------------------------------------------###      
# 2.- Dada una lista de numeros, obten una nueva lista con el doble de cada valor. Usa la funcion map()
# Usando un bucle for
numeros = [1,3,5,7,9,2,4,6,8,10]
dobles =[] # lista vacía dobles
for n in numeros: #buvle for para añadir el doble
    dobles.append(n*2)
print(dobles)    

# map(función, iterable). usando lambda que es como la funcion comodin
numeros = [1,3,5,7,9,2,4,6,8,10]
dobles = map(lambda n: n * 2, numeros) # map aplica la función lambda a cada elemento de la lista
print(list (dobles) ) #  mostrar el resultado como lista, hay que convertir  map a list()

# map(función, iterable).  Definiendo una función normal
numeros = [1,3,5,7,9,2,4,6,8,10]
def valor_doble(n): # Definimos una función que multiplica un número por 2
    return n * 2
dobles = map(valor_doble, numeros) # map aplica la función "valor_doble" a cada elemento de la lista
print(list(dobles))        


###-------------------------------------------------------------------------------------------------------------------------------------------------------------------###
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


###-------------------------------------------------------------------------------------------------------------------------------------------------------------------###
# 4.-Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()."
lista1 = [7,8,9,10]
lista2 = [1,5,7,8]
diferencia = map(lambda x, y: x - y, lista1, lista2)
print (list(diferencia))                

lista1 = [7,8,9,10]
lista2 = [1,5,7,8]
def resta (x,y):
    return x-y
diferencia = map(resta, lista1, lista2)
print(list(diferencia))


###-------------------------------------------------------------------------------------------------------------------------------------------------------------------###
# 5.- Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por defecto es 5. La función debe calcular la media de los números 
# en la lista y determinar si la media es mayor o igual que nota_aprobado. Si es así, el estado será 'aprobado', de lo contrario, será 'suspenso'.
# La función debe devolver una tupla que contenga la media y el estado."
lista_notas = [4, 7, 5.5, 8, 6, 3.5, 9, 10, 4.5, 6.5]  # Lista de notas para calcular la media
nota_aprobado = 5  # Nota mínima para aprobar

def calcular_media(lista_notas, nota_aprobado):
    # Calcular la media (solo si la lista no está vacía)
    if len(lista_notas) > 0:
        media = sum(lista_notas) / len(lista_notas)  # Calcular la media
        
        # Comparar la media con nota_aprobado
        if media >= nota_aprobado:
            estado = 'Aprobado'
        else:
            estado = 'Suspenso'
    else:
        # Si la lista está vacía, media es 0 y estado es 'suspenso'
        media = 0
        estado = 'Suspenso'
    
    # Devolver la media y el estado
    return (media, estado)

# Llamada a la función para calcular el resultado
resultado = calcular_media(lista_notas, nota_aprobado)

# Imprimir el resultado (media y estado)
print(resultado)


###-------------------------------------------------------------------------------------------------------------------------------------------------------------------###
# 6.- "Escribe una función que calcule el factorial de un número de manera recursiva."
# Solicitar al usuario que introduzca un número
numero = int(input("Por favor, introduce un número: "))

# Función recursiva para calcular el factorial
def factorial(n):
    if n == 0:  # Caso base: el factorial de 0 es 1
        return 1
    else:  # Caso recursivo: n * factorial(n-1)
        return n * factorial(n - 1)

# Llamar a la función y mostrar el resultado
resultado = factorial(numero)
print(f"El factorial de {numero} es: {resultado}")


###-------------------------------------------------------------------------------------------------------------------------------------------------------------------###
# 7.- "Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()."
lista_tuplas = [(2,4,6), ("dos", "cuatro", "seis")]

lista_strings = list(map(lambda tupla: str(tupla), lista_tuplas))
print (lista_strings)
print (type(lista_strings))


###-------------------------------------------------------------------------------------------------------------------------------------------------------------------###
# 8.- "Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, 
# maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje indicando si la división fue exitosa o no."

# Pedir los números al usuario
numero1 = input("Por favor, introduce el primer número: ")
numero2 = input("Por favor, introduce el segundo número: ")
# Verificar si ambos son números
if numero1.isdigit() and numero2.isdigit(): # para verificar si son numeros usamos AND porque necesitamos que los dos sean
    numero1 = int(numero1) # Convertir las entradas a enteros
    numero2 = int(numero2)# Convertir las entradas a enteros

    # Verificar si el divisor es diferente de 0
    if numero1!= 0 and numero2!= 0:
        # Realizar la división
        division = numero1 / numero2
        print(f"El resultado de la división es: {division}")
    else:
        # Manejar el caso de división por cero
        print("No se puede dividir por cero. Inténtalo de nuevo.")
else:
    # Si alguno de los dos no es un número
    print("Por favor, introduce solo números válidos.")
    
    
###-------------------------------------------------------------------------------------------------------------------------------------------------------------------###
# 9.- "Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. 
# La lista de mascotas a excluir es ['Mapache', 'Tigre', 'Serpiente Pitón', 'Cocodrilo', 'Oso']. Usa la función filter()."
lista_mascotas = ["Perro", "Gato", "Conejo", "Hamster", "Tigre", "Mapache", "Serpiente Pitón", "Cocodrilo", "Oso", "Pez", "Loro", "Tortuga", "Cobaya", "Caballo", "Huron"]
mascotas_excluidas = ['Mapache', 'Tigre', 'Serpiente Pitón', 'Cocodrilo', 'Oso']
lista_definitiva = []

def excluir_mascota(mascota):
    return mascota not in mascotas_excluidas  # Devolver True si la mascota no está en prohibidas
   
lista_definitiva = list(filter(excluir_mascota, lista_mascotas))  

print("Lista original:", lista_mascotas)
print("Mascotas excluidas:", mascotas_excluidas)
print("Lista definitiva:", lista_definitiva)


###-------------------------------------------------------------------------------------------------------------------------------------------------------------------###
# 10.- "Escribe una funcion que reciba una lista de numeros y calcule su promedio. Si la lista esta vacia, lanza una excepcion personalizada y maneja el error adecuadamente
lista_numeros = [5,7,10,11,16,20,22]

def promedio (lista):
   if len (lista) == 0:# si la longitud de la lista es 0
      print(f"La lista está vacía. No se puede calcular el promedio.")# mensaje de error
   else: #sino haz la media
     media = sum(lista) / len(lista) # media es la suma de la lista entre su longuitud
   return media  # delvuelve la media    
print(promedio(lista_numeros)) #llamamos a la funcion e imprimimos


###-------------------------------------------------------------------------------------------------------------------------------------------------------------------###
# Escribe un programa que pida al usuarioque introduzca su edad. Si el usuarioingresa un valor no numerico o un valor fuera del rango esperado (por ejemplomenos que 0 o mayor que 120).
# maneja la excepciones adecuadamente

try:
    edad = int(input(f"por favor, introduce tu edad: "))  # Intenta convertir la entrada a un entero

    if edad <= 0 or edad > 120:
     print(f"Has introducido {edad} años, eso no es un valor valido.")
    else:
     print(f"Tu edad son {edad} años.")    
except ValueError:
    print("Error: Debes ingresar un número entero.")  # Si no se puede convertir a entero, muestra este mensaje     
    
    
###-------------------------------------------------------------------------------------------------------------------------------------------------------------------###
#12. genera una funcion que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la funcion map()-
# Pedir al usuario que ingrese una frase
frase = input("Por favor, ingresa una frase: ")
print(f"Has introducido : {frase}")

palabras = frase.split() # Dividimos la frase en palabras con el metodo split()

longitud_palabras = map(len, palabras)# Usamos map() para obtener la longitud de cada palabra

print(list(longitud_palabras))# Convertimos el resultado a una lista para imprimirlo


###-------------------------------------------------------------------------------------------------------------------------------------------------------------------###
#13. Genera una funcion la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayuscula y minuscula. Las letras no puedes estar repetidas. Usa Map().
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


###-------------------------------------------------------------------------------------------------------------------------------------------------------------------###
#14 Crea una funcion que retorne las palabras de una lista de palabras que comiencen con una letra es especifico. Usa la funcion filter().

lista_palabras = ["casa", "perro", "familia", "estudio", "Daniela", "Martina", "Miguel Angel", "Lara", "colegio", "trabajo", "manzana", "objeto", "sol"]

letra = input(f"¿Porque letras quiere que empiece?")

palabras_m = filter(lambda palabra: palabra.lower().startswith(letra), lista_palabras)

print(list(palabras_m))


###-------------------------------------------------------------------------------------------------------------------------------------------------------------------###
# 15 Crea una función lambda que sume 3 a cada número de una lista dada.

# Lista de entrada
lista_dada = [2, 4, 3, 7, 5]  # Esta es la lista de números sobre la cual vamos a trabajar.

# Usamos map() para aplicar la función lambda a cada elemento de la lista.
# La función lambda toma cada número de la lista y le suma 3.
lista_por_3 = map(lambda x: x + 3, lista_dada)  # La función lambda toma x y devuelve x+3 para cada elemento.

# Imprimimos el resultado como una lista.
# Como map() devuelve un objeto 'map', lo convertimos en una lista para imprimir los valores.
print(list(lista_por_3))  # Convertimos el resultado de map() en una lista y lo imprimimos.


###-------------------------------------------------------------------------------------------------------------------------------------------------------------------###
#16. Escribe una función que tome una cadena de texto y un número entero n como parámetros, y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter().
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


###-------------------------------------------------------------------------------------------------------------------------------------------------------------------###
#17. Crea una funcion que tome una lista de digitos y devuelva el numero correspondiente. Por ejemplo [5,7,2] corresponde al numero quinientos setenta y dos (572):usa la funcion reduce()
from functools import reduce  # Importamos reduce desde functools

def lista_a_numero (lista_difitos): #def nombrefuncion (parametro)
    return reduce(lambda acumulado, digito: acumulado * 10 + digito, lista_digitos)   # reduce para combinar los dígitos en un único número. lambda (parametros: que hace?, con que lo hace)

lista_digitos = [6, 1, 8]  # Esto debería convertirse en 618

resultado = lista_a_numero(lista_digitos) # Llamamos a la función y mostramos el resultado
print(resultado)  # Debería imprimir: 618


###-------------------------------------------------------------------------------------------------------------------------------------------------------------------###
# 18.Escribe un programa en python que cree una lista de diccionarios que contenga informacion de estudiantes (nombre, edad, calificacion) y use la funcion filter para extraer a los 
# estudiantes con una calificacionmayor o igual a 90. Usa la funcion filter()

# Paso 1: Crear las listas individuales de datos
nombres = ["Lara", "Miguel Angel", "Daniela", "Martina", "Alejandro"]
edades = [45, 38, 27, 25, 30]
calificaciones = [95, 93, 90, 90, 65]

# Paso 2: Combinar las listas en una lista de diccionarios
lista_diccionario = [ # Combinar las listas en una lista de diccionarios usamos [] porque queremos una lista de diccioanrios
    {"nombre": nombre, "edad": edad, "calificacion": calificacion} #definimos calve:valor
    for nombre, edad, calificacion in zip(nombres, edades, calificaciones) #iteramos
]

# Paso 3: Filtrar estudiantes con calificaciones >= 90. haz una lista que filtre cada estudiante(parametro) con calificacion (clave) >90 de la lista_diccionario
estudiantes_aprobados = list(filter(lambda estudiante: estudiante["calificacion"] >= 90, lista_diccionario))

# Mostrar el resultado
print(estudiantes_aprobados)


###-------------------------------------------------------------------------------------------------------------------------------------------------------------------###
#19.  Crea una funcion lambda que filtre los numeros impares de una lista dada
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #lista dada
numeros_impares = list(filter(lambda n: n %2 != 0, numeros))
print(numeros_impares)


###-------------------------------------------------------------------------------------------------------------------------------------------------------------------###
#20. Para una lista con con elementos tipo int y str obten una nueva lista solo con los valores int. Usa la funcion filter()
lista_mezclada =["daniela", 10, "Martina", 5, "Miguel Angel", 51, "Lara", 45]
lista_int = list(filter(lambda elemento: isinstance(elemento, int), lista_mezclada))
print(lista_int)
# he tenido que buscar qué metodo podria hacer eso... isinstance(). porque he probado con type(int) is not(str) con != y con ==....


###-------------------------------------------------------------------------------------------------------------------------------------------------------------------###