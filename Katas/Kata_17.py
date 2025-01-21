#17. Crea una funcion que tome una lista de digitos y devuelva el numero correspondiente. Por ejemplo [5,7,2] corresponde al numero quinientos setenta y dos (572):usa la funcion reduce()

from functools import reduce  # Importamos reduce desde functools

def lista_a_numero (lista_difitos): #def nombrefuncion (parametro)
    return reduce(lambda acumulado, digito: acumulado * 10 + digito, lista_digitos)   # reduce para combinar los dígitos en un único número. lambda (parametros: que hace?, con que lo hace)

lista_digitos = [6, 1, 8]  # Esto debería convertirse en 618

resultado = lista_a_numero(lista_digitos) # Llamamos a la función y mostramos el resultado
print(resultado)  # Debería imprimir: 618