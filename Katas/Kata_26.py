# 26  Crea una funcion lambda que calcule el resto de la duvision entre dos numeros dados.

num1 = int(input(f"Por favor introduce el primer numero : "))
num2 = int(input(f"Por favor introduce el segundo numero : "))

resto = lambda num1, num2 : num1 % num2
resultado = resto(num1,num2)
print(f"El resto de la division es : {resultado}")