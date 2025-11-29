def contar_hasta(n):
    
    contador = 1
    while contador <= n:
        yield contador
        contador = contador + 1

for numero in contar_hasta(5):
    print(numero)
