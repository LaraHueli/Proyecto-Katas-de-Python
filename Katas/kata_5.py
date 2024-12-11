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
