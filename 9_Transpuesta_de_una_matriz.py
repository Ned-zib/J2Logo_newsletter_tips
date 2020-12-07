# Calcular la transpuesta de una matriz

x = [(1, 2, 4), ('u', 'v', 'w')]
y = zip(*x)
z = list(y)

print(z)
#[(1, 'u'), (2, 'v'), (4, 'w')]
