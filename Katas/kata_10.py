# 10.- "Escribe una funcion que reciba una lista de numeros y calcule su promedio. Si la lista esta vacia, lanza una excepcion personalizada y maneja el error adecuadamente

lista_numeros = [5,7,10,11,16,20,22]

def promedio (lista):
   if len (lista) == 0:# si la longitud de la lista es 0
      print(f"La lista está vacía. No se puede calcular el promedio.")# mensaje de error
   else: #sino haz la media
     media = sum(lista) / len(lista) # media es la suma de la lista entre su longuitud
   return media  # delvuelve la media    
print(promedio(lista_numeros)) #llamamos a la funcion e imprimimos