# Capturar múltiples excepciones en una sola línea

try:
    n = int(input())
    print(100/n)
except (ZeroDivisionError, ValueError) as e:
    print(e)
