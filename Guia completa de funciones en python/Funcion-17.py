def crear_lista_compras(*items):

    print("=== LISTA DE COMPRAS ===")
    for i, item in enumerate(items, 1):
        print(f"{i}. {item}")
    print("========================")

crear_lista_compras("Leche", "Pan", "Huevos")
print()
crear_lista_compras("Manzanas", "Naranjas", "Plátanos", "Uvas", "Fresas")
