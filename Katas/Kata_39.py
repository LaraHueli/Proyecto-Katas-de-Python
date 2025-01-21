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
