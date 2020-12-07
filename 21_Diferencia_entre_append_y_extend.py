# Diferencia entre los métodos append() y extend() de la clase list

# append() añade un elemento/objeto al final de la lista
elems = [1, 'a', 7]
elems.append(2)

print(elems)
#[1, 'a', 7, 2]

elems.append([8, 9])

print(elems)
#[1, 'a', 7, 2, [8, 9]]

# extend() añade los elementos de un iterable al final de la lista
elems = [1, 'a', 7]
elems.extend([8, 9])

print(elems)
#[1, 'a', 7, 8, 9]
