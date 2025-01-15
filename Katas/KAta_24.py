# 24 Calcula la diferencia total en los valores de una lista. Usa la funcion reduce()

from functools import reduce # importacion necesaria

lista_numeros = [51,45,10,5]

diferencia_total = reduce(lambda x,y:x-y,lista_numeros)

print(diferencia_total)

# mismo concpto que el anterior, pero la repeticion hace que se asimile bien el concepto