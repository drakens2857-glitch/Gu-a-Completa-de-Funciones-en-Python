def mostrar_info(**datos):
    
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Ana", edad=25, ciudad="Bogotá")
print()
mostrar_info(producto="Laptop", precio=1500, marca="Dell", disponible=True)
