# La sentencia else en un bucle for

# Lo que hay dentro del else se ejecuta
# si no se ejecuta el break

vocales = ['a', 'e', 'i', 'o', 'u']
for c in vocales:
    if c == 'b':
        break
    else:
        print('No se ha encontrado el carácter b')

# No se ha encontrado el carácter b
