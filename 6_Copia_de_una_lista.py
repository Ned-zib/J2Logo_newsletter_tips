# Copia de referencias
# Ambas listas tienen la misma referencia.
# Los cambios en una se ven reflejados en la otra.

from copy import deepcopy
a = [1, 2, 3, 4]
b = a
b[0] = 10

print(a)
#[10, 2, 3, 4]
print(b)
#[10, 2, 3, 4]


# Copia poco profunda (python 3)

a = [1, 2, 3, 4]
b = a.copy()
b[0] = 10

print(a)
#[1, 2, 3, 4]
print(b)
#[10, 2, 3, 4]

a = [[1, 2], [3, 4]]
b = a.copy()
b[0].append(5)

print(a)
#[[1, 2, 5], [3, 4]]
print(b)
#[[1, 2, 5], [3, 4]]


# Copia profunda (python 3)
# Crea nuevos objetos


a = [[1, 2], [3, 4]]
b = deepcopy(a)
b[0].append(5)

print(a)
#[[1, 2], [3, 4]]
print(b)
#[[1, 2, 5], [3, 4]]
