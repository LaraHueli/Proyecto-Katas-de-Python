# Para una lista con con elementos tipo int y str obten una nueva lista solo con los valores int. Usa la funcion filter()

lista_mezclada =["daniela", 10, "Martina", 5, "Miguel Angel", 51, "Lara", 45]

lista_int = list(filter(lambda elemento: isinstance(elemento, int), lista_mezclada))


print(lista_int)

# he tenido que buscar qué metodo podria hacer eso... isinstance(). porque he probado con type(int) is not(str) con != y con ==....