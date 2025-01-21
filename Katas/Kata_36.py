# 36 Crear la clase UsuarioBanco, represante a un usuario de un banco con su nombre, saldo y si tiene o no  cuenta corriente. Proporciona metodos para realizar operaciones 
# como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo:
#Codigo a Seguir:
# 1.- Inicializar un usuario con su nombre, saldo y si tiene o no cuenta coprriente mediante true o false.
# 2.- Implementar el metodo retirar_dinero para retirar dinero del saldo del usuario. Lanzara un error en casoo de nopoder hacerse
# 3.- Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actua. Lanzará un error en caso de no poder hacerse.
# 4.- 4. Implementar el método agregar_dinero para agregar dinero al saldo del usuario.

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
