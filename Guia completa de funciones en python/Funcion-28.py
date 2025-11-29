def calcular_imc(peso, altura):
    
    imc = peso / (altura ** 2)
    return imc


def interpretar_imc(imc):
    
    if imc < 18.5:
        return "Bajo peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"


def reporte_imc(nombre, peso, altura):
    
    imc = calcular_imc(peso, altura)
    categoria = interpretar_imc(imc)

    print(f"=== REPORTE DE {nombre.upper()} ===")
    print(f"Peso: {peso} kg")
    print(f"Altura: {altura} m")
    print(f"IMC: {imc:.2f}")
    print(f"Categoría: {categoria}")
    print("=" * 30)
