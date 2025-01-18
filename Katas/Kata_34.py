# Crea la clase Arbol, define un árbol genérico con un tronco y ramas como atributos.
# Los métodos disponibles son crecer_tronco, nueva_rama, crecer_ramas, quitar_rama e info_arbol.
# El objetivo es implementar estos métodos para manipular la estructura del árbol.

# Código a seguir:
# 1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
# 2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
# 3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
# 4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
# 5. Implementar el método quitar_rama para eliminar una rama en una posición específica.
# 6. Implementar el método info_arbol para devolver información sobre la longitud del tronco, 
#    el número de ramas y las longitudes de las mismas.

# Caso de uso:
# 1. Crear un árbol.
# 2. Hacer crecer el tronco del árbol una unidad.
# 3. Añadir una nueva rama al árbol.
# 4. Hacer crecer todas las ramas del árbol una unidad.
# 5. Añadir dos nuevas ramas al árbol.
# 6. Retirar la rama situada en la posición 2.
# 7. Obtener información sobre el árbol.



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
            if 0 <= position < len(self.ramas):  # Verificamos si la posición es válida
                self.ramas.pop(position)  # Eliminamos la rama en la posición indicada
            else:
                print("Posicion no válida. No se puede quitar la rama.")  # Mensaje si la posición no es válida  
                
    def info_arbol(self):
        print(f"Longitud del tronco: {self.tronco}")
        print(f"Numero de ramas: {len(self.ramas)}")
        print(f"Longitudes de las ramas: {self.ramas}")            

             
             
arbol = Arbol()  # Creamos un árbol
arbol.crecer_tronco()  # Hacemos crecer el tronco
arbol.nueva_rama()  # Añadimos una nueva rama
arbol.nueva_rama()  # Añadimos otra nueva rama
arbol.crecer_ramas()  # Hacemos crecer todas las ramas
print(f"Ramas despues de crecer: {arbol.ramas}")  # Mostramos las ramas después de crecer
arbol.quitar_rama(1)  # Quitamos la rama en la posición 1 (ajustado)
arbol.info_arbol()  # Mostramos toda la información del árbol

