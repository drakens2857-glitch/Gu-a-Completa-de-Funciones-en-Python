def calcular_estadisticas(numeros):

    promedio = sum(numeros) / len(numeros)
    mayor = max(numeros)
    menor = min(numeros)
    return promedio, mayor, menor


datos = [10, 20, 30, 40, 50]
prom, may, men = calcular_estadisticas(datos)
print(f"Promedio: {prom}")
print(f"Mayor: {may}")
print(f"Menor: {men}")
