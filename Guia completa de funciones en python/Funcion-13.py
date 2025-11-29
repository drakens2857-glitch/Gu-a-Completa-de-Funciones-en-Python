def encontrar_mayor(numeros):
    
    if len(numeros) == 0:
        return None

    mayor = numeros[0]
    for numero in numeros:
        if numero > mayor:
            mayor = numero
    return mayor


lista1 = [45, 23, 67, 89, 12, 34]
lista2 = [5, 5, 5, 5]
lista3 = []

print(f"Mayor de lista1: {encontrar_mayor(lista1)}")
print(f"Mayor de lista2: {encontrar_mayor(lista2)}")
print(f"Mayor de lista3: {encontrar_mayor(lista3)}")
