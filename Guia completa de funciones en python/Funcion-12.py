def sumar_lista(numeros):
    
    total = 0
    for numero in numeros:
        total = total + numero
    return total


mi_lista = [10, 20, 30, 40, 50]
resultado = sumar_lista(mi_lista)
print(f"La suma total es: {resultado}")

otra_lista = [5, 15, 25]
otro_resultado = sumar_lista(otra_lista)
print(f"La suma total es: {otro_resultado}")
