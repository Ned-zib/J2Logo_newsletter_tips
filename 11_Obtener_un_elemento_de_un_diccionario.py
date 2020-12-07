# Obtener un elemento de un diccionario

dic = {'a': 1, 'b': 2}

# Acceso a una clave que existe
print(dic['a'])
# 1

# Si se accede a una clave que no
# existe se lanza una excepción

# print(dic['c'])
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# KeyError: 'c'

# Acceso con el método get()
# En el segundo parámetro se indica un
# valor por defecto por si la clave no
# existe
print(dic.get('c', 3))
# 3
