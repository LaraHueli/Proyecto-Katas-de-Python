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

def calcular_media(lista_notas, nota_aprobado = 5):
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

try:
    # Pedir los números al usuario
    numero1 = float(input("Por favor, introduce el primer número: "))  # Convertimos directamente a float
    numero2 = float(input("Por favor, introduce el segundo número: "))

    # Verificar si el divisor es diferente de 0
    if numero2 != 0:  # Si el segundo numero no es 0, se puede dividir
        division = numero1 / numero2  # Realizamos la division
        print(f"El resultado de la división es: {division}")  # Mostramos el resultado
    else:
        print("No se puede dividir por cero. Inténtalo de nuevo.")  # Mensaje de error si el divisor es 0

except ValueError:  # Capturamos el error si el usuario ingresa algo que no sea un número
    print("Por favor, introduce solo números válidos.")  # Mensaje de error en caso de entrada no numerica

    
    
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
    lista_unica = sorted(set(lista[0]), key=lista[0].index)  # Solo tomamos el primer elemento
    # map (itera cada letra) y va usando lower y upper. en cada letra y pasando a Masyuscual  y minusclua cada letra en lista unica
    resultado = list(map(lambda letra: (letra.upper(), letra.lower()), lista_unica))
    # Convertimos el resultado a lista y lo retornamos
    return resultado

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
#21  Crea una funcion que calcule el cubo de un numero dado mediante una funcion lambda

numero = int(input(f"Por favor, introduce un numero: ")) # pedimos al usuario que ingrese un numero

numero_cubo = lambda n: n ** 3 # lambda argumento: expresion

resultado = (numero_cubo(numero)) # metemos el resultado en una variable

print(f"Has introducido el numero: {numero}. Y su cubo es: {resultado}.") #printeamos


###-------------------------------------------------------------------------------------------------------------------------------------------------------------------###
# 22 Dada una lista numerica, obten el producto total de los valores de dicha lista usando la funcion reduce()
from functools import reduce #primero importaciones necesarias

numeros = [1, 3, 5, 7, 9] # lista dada
# Utilizamos reduce(función, iterable)
# - lambda x, y: x * y 
producto = reduce(lambda x, y: x * y, numeros)

print(producto) # Imprimimos el resultado


###-------------------------------------------------------------------------------------------------------------------------------------------------------------------###
# 23.-  Concatena una lista de palabras. Usa la funcion reduce()

lista_palabras = ["Concatena", " ", "una", " ",  "lista", " ", "de", " ",  "palabras"] # lista dada

# Utilizamos reduce(función, iterable)
# - lambda  
palabras_concatenadas = reduce(lambda palabra, contatenar: palabra + contatenar , lista_palabras)

print(palabras_concatenadas) # Imprimimos el resultado
# es similar al ejercicio anterior


###-------------------------------------------------------------------------------------------------------------------------------------------------------------------###
# 24 Calcula la diferencia total en los valores de una lista. Usa la funcion reduce()



lista_numeros = [51,45,10,5]

diferencia_total = reduce(lambda x,y:x-y,lista_numeros)

print(diferencia_total)
# mismo concpto que el anterior, pero la repeticion hace que se asimile bien el concepto


###-------------------------------------------------------------------------------------------------------------------------------------------------------------------###
# 25 Crea una funcion que cuente el numero de caracteres en una cadena de texto dada. no me des el resultado
texto = ["cadena de texto dada"]

def contar_caracteres(texto):
   
    numero_caracteres = 0 # contador = 0 
   
    for palabra in texto:
        
        numero_caracteres += len(palabra) # sumamos la longitud al contador (numero_caracteres = numero_caracteres + longitud_palabra)
    return numero_caracteres
resultado = contar_caracteres(texto)
print(f"El numero total de caracteres es: {resultado}")

#opcion corta

texto = "cadena de texto dada"
numero_caracteres = reduce(lambda palabra, caracter: palabra + 1, texto, 0) # texto, 0): para poner un contador
 
print(f"El numero total de caracteres es: {numero_caracteres}")


###-------------------------------------------------------------------------------------------------------------------------------------------------------------------###
# 26  Crea una funcion lambda que calcule el resto de la duvision entre dos numeros dados.

# Pedimos al usuario dos numeros 
num1 = int(input("Por favor introduce el primer número: "))  # Dividendo
num2 = int(input("Por favor introduce el segundo número: "))  # Divisor

# Validamos  antes de realizar el calculo
if num2 == 0:
    # Si el divisor es 0 error
    print("El divisor no puede ser cero.")
elif num1 < num2:
    # Si el divisor es mayor que el dividendo, el resto es el dividendo
    print(f"El resto de la división es el número completo: {num1}")
else:
    # Usamos una funcion lambda para calcular 
    resto = lambda num1, num2: num1 % num2
    resultado = resto(num1, num2)  # Calculamos 
    print(f"El resto de la división es: {resultado}")
    
    
###-------------------------------------------------------------------------------------------------------------------------------------------------------------------###
# 27  Crea una funcion que calcule el promedio de una lista de numeros
lista_numeros =[2,7,5,3,8,12]

promedio = lambda numeros: sum(numeros)/len(numeros)

resultado = round((promedio(lista_numeros)),2)

print(f"El promedio de la lista: {lista_numeros} es :{resultado}")


###-------------------------------------------------------------------------------------------------------------------------------------------------------------------###
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


###-------------------------------------------------------------------------------------------------------------------------------------------------------------------###
# 29 Crea una funcion que convierta una variable en una cadena de texto y enmascare todos los caracteres con el caracter #, excepto los 4 ultimos.
def enmascarar(variable): # creamos la funcion
   
    texto = str(variable)  # Convertimos la variable a cadena de texto
    
    # Enmascaramos todos menos los últimos 4 caracteres
    enmascarado = "#" * (len(texto) - 4) + texto[-4:]
    
    return enmascarado     # Devolvemos el resultado
variable = "Esto es una variable"
resultado = enmascarar(variable)
print(resultado)


###-------------------------------------------------------------------------------------------------------------------------------------------------------------------###
# 30 Crea una funcion que determine si dos palabras son anagramas, es decir, si estan formadas por las mismas letras pero en diferente orden. 
# Definimos la funcion
def son_anagramas(palabra1, palabra2):
    # palabras a minusculas 
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()
        # Ordenamos las letras de cada palabra. El método `sorted` toma una secuencia y devuelve una lista    
    letras1 = sorted(palabra1)
    letras2 = sorted(palabra2)
    # Comparamos las listas 
    if letras1 == letras2:
        return True  # Las palabras son anagramas
    else:
        return False  # No son anagramas
palabra1 = "amor"
palabra2 = "roma"
resultado = son_anagramas(palabra1, palabra2)

print(f"¿Las palabras '{palabra1}' y '{palabra2}' son anagramas? {resultado}")


###-------------------------------------------------------------------------------------------------------------------------------------------------------------------###
# 31 Crea una funcion que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista. Si el nombre esta en la lista, se imprime un 
# mensaje indicando que fue encontrado, de lo contrario, se lanza una excepcion

def buscar_en_lista ():
    try:
        lista_nombres = input(f"Por favor, igresa una lsita de nombres: ").split(",") # .split(",") es un metodo que convierte un string en una lista. 
        nombre_buscado = input(f"¿Que nombre quieres buscar?: ")
        
        for nombre in lista_nombres:
            if nombre.strip() == nombre_buscado:
                return(f"El nombres buscado es: {nombre_buscado} y esta en la lista nombres ")
                break  # Salimos del bucle al encontrar el nombre
        else:
                raise ValueError# Si el bucle termina sin encontrar el nombre, lanzamos una excepcion
    except ValueError:
        return("Error: El nombre que buscas no esta en la lista.")  # Si no se puede convertir a entero, muestra este mensaje     
print(buscar_en_lista()) 


###-------------------------------------------------------------------------------------------------------------------------------------------------------------------###
# 32 Crea una funcion que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y devuelve el puesto del empleado si esta en la lista,
# de lo contrario, devuelve un mensaje indicando que la persona no trabaja aqui 

def buscar_puesto(): # creamos la funcion sin parametros
    try:
        empleados = [{"nombre": "Lara Hueli", "puesto": "Analista de Datos"}, 
                     {"nombre": "Miguel Ángel Ordóñez", "puesto": "Gerente de Proyectos"},  
                     {"nombre": "Martina Ordóñez", "puesto": "Desarrolladora"}, 
                     {"nombre": "Daniela Hueli", "puesto": "Diseñadora"}]

        nombre_buscado = input("¿Qué empleado quieres buscar?: ")
       
        for empleado in empleados: # Iteramos sobre la lista de empleados
           if empleado["nombre"] == nombre_buscado: # Comparamos si el nombre del empleado coincide con el buscado
               return(f"El puesto de {nombre_buscado} es: {empleado['puesto']}")

        else: # Si el bucle termina sin encontrar el nombre, lanzamos una excepcion
            raise ValueError 

    except ValueError:
        return("Error: Esta persona no trabaja aquí.")
    # Llamada a la funcion
print(buscar_puesto())


###-------------------------------------------------------------------------------------------------------------------------------------------------------------------###
# 33 Crea una funcion lambda que sume elementos correspondientes de dos listas dadas

sumar_listas = lambda x, y: x + y # Definimos la función lambda que suma dos valores
lista1 = [3, 5, 7, 9]
lista2 = [10, 20, 30, 40]
resultado = list(map(sumar_listas, lista1, lista2))  #map para iterar sobre cada elemento y list para transformar a lista
# Mostramos el resultado
print(resultado)


###-------------------------------------------------------------------------------------------------------------------------------------------------------------------###
# Crea la clase Arbol, define un arbol generico con un tronco y ramas como atributos.
# Los metodos disponibles son crecer_tronco, nueva_rama, crecer_ramas, quitar_rama e info_arbol.
# El objetivo es implementar estos metodos para manipular la estructura del arbol.

# Código a seguir:
# 1. Inicializar un arbol con un tronco de longitud 1 y una lista vacia de ramas.
# 2. Implementar el metodo crecer_tronco para aumentar la longitud del tronco en una unidad.
# 3. Implementar el metodo nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
# 4. Implementar el metodo crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
# 5. Implementar el metodo quitar_rama para eliminar una rama en una posición especifica.
# 6. Implementar el metodo info_arbol para devolver información sobre la longitud del tronco, 
#    el numero de ramas y las longitudes de las mismas.

# Caso de uso:
# 1. Crear un arbol.
# 2. Hacer crecer el tronco del arbol una unidad.
# 3. Añadir una nueva rama al arbol.
# 4. Hacer crecer todas las ramas del arbol una unidad.
# 5. Añadir dos nuevas ramas al arbol.
# 6. Retirar la rama situada en la posicion 2.
# 7. Obtener informacion sobre el arbol.

class Arbol:
    def __init__(self):
        self.tronco = 1
        self.ramas = []
        
    def crecer_tronco (self):
        self.tronco += 1
        
    def nueva_rama (self):
        self.ramas.append(1) # append porque es una lista
      
    def crecer_ramas (self):    
        self.ramas = [rama + 1 for rama in self.ramas]
        
    def quitar_rama (self,position):
            if 0 <= position < len(self.ramas):  # Verificamos si la posicion es valida
                self.ramas.pop(position)  # Eliminamos la rama en la posicion indicada
            else:
                print("Posicion no válida. No se puede quitar la rama.")  # Mensaje si la posicion no es valida  
                
    def info_arbol(self):
        print(f"Longitud del tronco: {self.tronco}")
        print(f"Numero de ramas: {len(self.ramas)}")
        print(f"Longitudes de las ramas: {self.ramas}")            
            
arbol = Arbol()  # Creamos un arbol
arbol.crecer_tronco()  # Hacemos crecer el tronco
arbol.nueva_rama()  # Añadimos una nueva rama
arbol.nueva_rama()  # Añadimos otra nueva rama
arbol.crecer_ramas()  # Hacemos crecer todas las ramas
print(f"Ramas despues de crecer: {arbol.ramas}")  # Mostramos las ramas despues de crecer
arbol.quitar_rama(1)  # Quitamos la rama en la posicion 1 (ajustado)
arbol.info_arbol()  # Mostramos toda la informacion del arbol


###-------------------------------------------------------------------------------------------------------------------------------------------------------------------###
# 36 Crear la clase UsuarioBanco, represante a un usuario de un banco con su nombre, saldo y si tiene o no  cuenta corriente. Proporciona metodos para realizar operaciones 
# como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo:
#Codigo a Seguir:
# 1.- Inicializar un usuario con su nombre, saldo y si tiene o no cuenta coprriente mediante true o false.
# 2.- Implementar el metodo retirar_dinero para retirar dinero del saldo del usuario. Lanzara un error en casoo de nopoder hacerse
# 3.- Implementar el metodo transferir_dinero para realizar una transferencia desde otro usuario al usuario actua. Lanzara un error en caso de no poder hacerse.
# 4.- 4. Implementar el metodo agregar_dinero para agregar dinero al saldo del usuario.

# Caso de uso:
# 1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corrient
# 2. Agregar 20 unidades de saldo de "Bob
# 3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia
# 4. Retirar 50 unidades de saldo a "Alicia


class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta):
        self.nombre = nombre
        self.saldo = saldo 
        self.cuenta = cuenta 
    def retirar_dinero(self, cantidad1):
        try:
            if self.saldo >= cantidad1:  # Verifica si el saldo es suficiente
                self.saldo -= cantidad1  # Resta la cantidad al saldo
                print(f"Has retirado {cantidad1}. Saldo restante: {self.saldo}")
            else:
                raise ValueError("Saldo insuficiente")  # Lanza el error
        except ValueError:
            print(f"Error: Saldo insuficiente")  # Captura el error lanzado
    def transferir_dinero(self, cantidad2):
        try:
            if usuario2.saldo >= cantidad2:  # Verifica si usuario2 tiene suficiente saldo
                usuario2.saldo -= cantidad2  # Resta del saldo de usuario2
                self.saldo += cantidad2  # Suma al saldo del usuario actual
                print(f"Has recibido {cantidad2} de {usuario2.nombre}. Saldo actual: {self.saldo}")
            else:
                raise ValueError("El usuario remitente no tiene suficiente saldo")
        except ValueError as mensaje:
            print(f"Error: {mensaje}")
      
usuario1 = UsuarioBanco(nombre="Alicia", saldo=100, cuenta=True)
usuario2 = UsuarioBanco(nombre="Bob", saldo=50, cuenta=True)
cantidad1 = float(input("¿Cuánto dinero deseas retirar? "))
usuario1.retirar_dinero(cantidad1) 
cantidad2 = float(input("¿Cuánto dinero deseas transferir? "))
usuario1.transferir_dinero(cantidad2)    
  
        
print("Nombre:", usuario1.nombre)
print("Saldo:", usuario1.saldo)
print("Cuenta Corriente:", usuario1.cuenta)


###-------------------------------------------------------------------------------------------------------------------------------------------------------------------###
# 37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras , reemplazar_palabras , eliminar_palabra . 
# Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función procesar_texto .
# Código a seguir:
# 1. Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene que devolver un diccionario.
# 2. Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra_nueva . Tiene que devolver el texto con el remplazo de palabras.
# 3. Crear una función eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra eliminada.
# 4. Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y número de argumentos variable según la opción indicada.
# Caso de uso:
# Comprueba el funcionamiento completo de la función procesar_texto

def contar_palabras (texto):
    palabras = texto.split() # .split() divide el texto en una lista de palabras separadas
    conteo = {} # Icontador diccionario a cero y vacio
    for palabra in palabras: #iteramos sobre cada palabra de la lista
        conteo[palabra]=conteo.get(palabra, 0) + 1 #.get busca la palabra, si esta edvuleve 0 y si no esta suma 1
    return conteo    


def reemplazar_palabras(texto, palabra_original, palabra_nueva): 
    return texto.replace(palabra_original, palabra_nueva) # devuelve el texto donde reemplaza la original por la nueva

def eliminar_palabra(texto, *palabra_eliminada): #ponemos* para tener un numero x de palabras
    palabras = texto.split()  # .split() divide el texto en una lista de palabras separadas
    palabras = [p for p in palabras if p != palabra_eliminada] #iteracion y cambio
    return " ".join(palabras) # .join() para unir las palabras de la lista en un único string

def procesar_texto(texto, opcion, *args): # texto de siempre, funcion a ejecutar, argumentos variables
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        return reemplazar_palabras(texto, *args)
    elif opcion == "eliminar":
        return eliminar_palabra(texto, *args)
    else:
        raise ValueError("Opción no válida")


texto = "Estoy haciendo un proyecto de Katas en python"
# Contar palabras
print(procesar_texto(texto, "contar"))

# Reemplazar una palabra
print(procesar_texto(texto, "reemplazar", "Katas", "ejercicios"))

# Eliminar una palabra
print(procesar_texto(texto, "eliminar", ("un", "proyecto", "de")))


###-------------------------------------------------------------------------------------------------------------------------------------------------------------------###
# 38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario

try: # try y except por si introducen una hora no valida
    hora = int(input("Por favor, dime qué hora es (en formato 24h): "))
    if 0 <= hora <= 23:
        if 6 <= hora <= 12:
            print(f"Son las {hora} horas, por lo tanto es de dia")
        elif 13 <= hora <= 18:
         print(f"Son las {hora} horas, por lo tanto es por la tarde")
    else:
        print(f"Son las {hora} horas, por lo tanto es de noche")

except ValueError:
    print("Entrada no válida. Por favor, introduce un número entero.")
    
    
###-------------------------------------------------------------------------------------------------------------------------------------------------------------------###
# 39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica 
# Las reglas de calificación son:
# - 0- 69 insuficiente 
# - 70- 79 bien 
# - 80- 89 muy bien 
# - 90- 100 excelete

try:  # try y except por si introducen un valor no válido
    calificacion = int(input("Por favor, introduce tu calificacion: "))
    if 0 <= calificacion <= 69:
        print(f"Tu calificacion es de: {calificacion}. Tu nota es: insuficiente")
    elif 70 <= calificacion <= 79:
        print(f"Tu calificacion es de: {calificacion}. Tu nota es: bien")
    elif 80 <= calificacion <= 89:
        print(f"Tu calificacion es de: {calificacion}. Tu nota es: muy bien")
    elif 90 <= calificacion <= 100:
        print(f"Tu calificacion es de: {calificacion}. Tu nota es: excelente")
    else:
        print("La calificacion debe estar entre 0 y 100.")
except ValueError:
    print("Entrada no valida. Por favor, introduce una calificcalificacionación correcta.")
  
#    Programa para determinar la calificación en texto según la calificación numérica
def determinar_calificacion(nota):
    if 0 <= nota <= 69:
        return "Insuficiente"
    elif 70 <= nota <= 79:
        return "Bien"
    elif 80 <= nota <= 89:
        return "Muy bien"
    elif 90 <= nota <= 100:
        return "Excelente"
    else:
        return "Calificación inválida"

# Solicitar calificación al usuario
calificacion = int(input("Introduce la calificación del alumno (0-100): "))

# Determinar el texto de la calificación
resultado = determinar_calificacion(calificacion)

# Mostrar el resultado
print("La calificación es:", resultado)


###-------------------------------------------------------------------------------------------------------------------------------------------------------------------###
#40  Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo", "triangulo" ) y datos  (una tupla con los datos necesarios para 
# calcular el área de la figura).

# "rectangulo", la tupla datos debe contener el ancho y el alto (en ese orden).
# "circulo", la tupla datos debe contener el radio.
# "triangulo", la tupla datos debe contener la base y la altura (en ese orden).

import math # Importamos la librería math para operaciones matematicas.

def calcular_area (figura,datos): # definimos la funcion
    if figura == "rectangulo":
        area = datos[0] * datos[1]   # Esto toma el valor del ancho (datos[0]) y lo multiplica por el alto (datos[1])
        return f"Has elegido un rectangulo y su area es {area}"
    elif figura == "circulo":
        area = math.pi * (datos[0] ** 2)  # Calcula el area del circulo
        return f"Has elegido un circulo y su area es {area}"
    elif figura == "triangulo":
        area = (datos[0] * datos[1]) / 2  # Calcula el area del triangulo
        return f"Has elegido un triangulo y su area es {area}"

figura = input("¿Que figura deseas calcular (rectangulo, circulo, triangulo)? ") # pedir al usuario

if figura == "rectangulo":
    ancho = float(input("Ingresa el ancho del rectangulo: "))  # Ancho del rectangulo
    alto = float(input("Ingresa el alto del rectangulo: "))  # Alto del rectangulo
    datos = (figura, (ancho, alto))  # Creamos la tupla con la figura y sus datos
elif figura == "circulo":
    radio = float(input("Ingresa el radio del circulo: "))  # Radio del circulo
    datos = (figura, (radio,))  # Tupla con la figura y el radio
elif figura == "triangulo":
    base = float(input("Ingresa la base del triangulo: "))  # Base del triangulo
    altura = float(input("Ingresa la altura del triangulo: "))  # Altura del triangulo
    datos = (figura, (base, altura))  # Tupla con la figura y sus datos
else:
    print("Figura no reconocida.")  # Mensaje de error si la figura no es valida
    datos = None  # No asignamos datos si la figura no es valida
    
if datos: # con este if solo llamamos a la funcion calcular_area si los datos son validos
    print(calcular_area(*datos)) # llamamos a la funcion
    
    
###-------------------------------------------------------------------------------------------------------------------------------------------------------------------###
# # 41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, 
# después de aplicar un descuento. El programa debe hacer lo siguiente:

# 1. Solicita al usuario que ingrese el precio original de un artículo.#
# 2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no). #
# 3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
# 4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor
# a cero). Por ejemplo, descuento de 15€. 
# 5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él. 
# 6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu
# programa de Python


precio_original_articulo = float(input("Por favor, ingresa en precio original del articulo: ")) # pedir al usuario el precio original y convertir a float

# Preguntamos si tiene un cupón de descuento (booleano)
cupon_descuento = input("Tienes cupon de descuento? (responde 'si' o 'no'): ").strip().lower() # Eliminamos espacios y conviertimos a minusculas 
 
if cupon_descuento == "si": 
    cupon_descuento = True  #establecemos cupon_descuento como True
    valor_cupon = float(input("Introduce el valor de tu cupón:  ")) # en saco afirmativo pedimos el importe del cupon en float
elif cupon_descuento == "no":  
    cupon_descuento = False #establecemos cupon_descuento como False
    valor_cupon = 0 # si no tiene cupon el cupon vale 0
else:
    print("Respuesta no valida. Por favor, responde 'si' o 'no'.")
    cupon_descuento = False    
    
# Si el valor del cupón no es 0, se resta del precio. Si es 0, el precio no cambia.    
precio_total = lambda precio, valor: precio - valor if valor != 0 else precio #funcion argumento1, argumento2 : precio - valor si valor no es 0 sino solo precio
resultado = precio_total(precio_original_articulo, valor_cupon) 
print(f"El precio total es: {resultado}")