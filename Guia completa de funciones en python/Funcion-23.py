def aplicar_operacion(funcion, a, b):
   
    resultado = funcion(a, b)
    return resultado

def sumar(x, y):
    return x + y

def multiplicar(x, y):
    return x * y

resultado1 = aplicar_operacion(sumar, 5, 3)
resultado2 = aplicar_operacion(multiplicar, 5, 3)

print(f"Suma: {resultado1}")
print(f"Multiplicación: {resultado2}")
