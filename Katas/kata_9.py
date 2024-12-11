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