def obtener_datos():

    return [10, 20, 30, 40, 50]


def procesar_datos(datos):

    promedio = sum(datos) / len(datos)
    mayor = max(datos)
    menor = min(datos)
    return promedio, mayor, menor


def mostrar_resultados(promedio, mayor, menor):

    print("=== RESULTADOS ===")
    print(f"Promedio: {promedio}")
    print(f"Mayor: {mayor}")
    print(f"Menor: {menor}")
    print("==================")


def main():

    datos = obtener_datos()
    prom, may, men = procesar_datos(datos)
    mostrar_resultados(prom, may, men)


if __name__ == "__main__":
    main()
