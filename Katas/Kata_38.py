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
