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

        else: # Si el bucle termina sin encontrar el nombre, lanzamos una excepción
            raise ValueError 

    except ValueError:
        return("Error: Esta persona no trabaja aquí.")
    # Llamada a la función
print(buscar_puesto())
 