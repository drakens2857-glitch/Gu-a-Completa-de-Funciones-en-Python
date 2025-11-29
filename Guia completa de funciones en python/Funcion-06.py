def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: no se puede dividir por cero"
    return a / b

print(f"Suma: {sumar(10, 5)}")
print(f"Resta: {restar(10, 5)}")
print(f"Multiplicación: {multiplicar(10, 5)}")
print(f"División: {dividir(10, 5)}")
