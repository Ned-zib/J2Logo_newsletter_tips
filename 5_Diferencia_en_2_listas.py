# Obtener la diferencia entre dos listas

# Obtiene una tercera lista con los elementos
# de la primera que no están en la segunda

lista_1 = ['a', 'b', 'c', 'd', 'e']
lista_2 = ['a', 'b', 'c']

set_1 = set(lista_1)
set_2 = set(lista_2)

lista_3 = list(set_1.symmetric_difference(set_2))

print(lista_3)
#['e', 'd']
