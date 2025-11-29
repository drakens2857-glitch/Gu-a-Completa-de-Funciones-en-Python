def calcular_promedio(calificaciones):
    
    if not calificaciones:
        return "Error: La lista está vacía"

    if not isinstance(calificaciones, list):
        return "Error: Debes pasar una lista"

    total = sum(calificaciones)
    promedio = total / len(calificaciones)
    return promedio


print(calcular_promedio([80, 90, 85, 95]))
print(calcular_promedio([]))
print(calcular_promedio("texto"))
