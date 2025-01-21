# # 41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, 
# después de aplicar un descuento. El programa debe hacer lo siguiente:

# 1. Solicita al usuario que ingrese el precio original de un artículo.#
# 2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no). #
# 3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
# 4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor
# a cero). Por ejemplo, descuento de 15€. 
# 5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él. 
# 6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu
# programa de Python


precio_original_articulo = float(input("Por favor, ingresa en precio original del articulo: ")) # pedir al usuario el precio original y convertir a float

# Preguntamos si tiene un cupón de descuento (booleano)
cupon_descuento = input("Tienes cupon de descuento? (responde 'si' o 'no'): ").strip().lower() # Eliminamos espacios y conviertimos a minusculas 
         

if cupon_descuento == "si": 
    cupon_descuento = True  #establecemos cupon_descuento como True
    valor_cupon = float(input("Introduce el valor de tu cupón:  ")) # en saco afirmativo pedimos el importe del cupon en float
elif cupon_descuento == "no":  
    cupon_descuento = False #establecemos cupon_descuento como False
    valor_cupon = 0 # si no tiene cupon el cupon vale 0
else:
    print("Respuesta no valida. Por favor, responde 'si' o 'no'.")
    cupon_descuento = False    
    
# Si el valor del cupón no es 0, se resta del precio. Si es 0, el precio no cambia.    
precio_total = lambda precio, valor: precio - valor if valor != 0 else precio #funcion argumento1, argumento2 : precio - valor si valor no es 0 sino solo precio
resultado = precio_total(precio_original_articulo, valor_cupon) 
print(f"El precio total es: {resultado}")









 
    