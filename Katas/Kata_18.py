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
