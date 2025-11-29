def sumar_todos(*numeros):

    total = 0
    for numero in numeros:
        total = total + numero
    return total

print(sumar_todos(1, 2, 3))
print(sumar_todos(10, 20, 30, 40, 50))
print(sumar_todos(5))
