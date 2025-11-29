def calcular_cuadrado(numero):
    return numero * numero

def calcular_suma_cuadrados(a, b):
    cuadrado_a = calcular_cuadrado(a)
    cuadrado_b = calcular_cuadrado(b)
    return cuadrado_a + cuadrado_b

resultado = calcular_suma_cuadrados(3, 4)
print(f"Resultado: {resultado}")
