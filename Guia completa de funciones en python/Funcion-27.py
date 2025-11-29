def calcular_promedio(notas):
    
    if not notas:
        return 0
    return sum(notas) / len(notas)


def determinar_estado(promedio):
   
    if promedio >= 3.0:
        return "Aprobado"
    else:
        return "Reprobado"


def generar_reporte(nombre, notas):
    
    promedio = calcular_promedio(notas)
    estado = determinar_estado(promedio)

    reporte = f"""
=== REPORTE DE {nombre.upper()} ===
Notas: {notas}
Promedio: {promedio:.2f}
Estado: {estado}
================================
"""
    return reporte


print(generar_reporte("Ana", [4.5, 3.8, 4.0, 4.2]))
print(generar_reporte("Carlos", [2.5, 2.8, 3.0, 2.2]))
