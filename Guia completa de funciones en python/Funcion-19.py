def funcion_flexible(*args, **kwargs):
    
    print("Argumentos posicionales:")
    for arg in args:
        print(f" - {arg}")
    print("\nArgumentos con nombre:")
    for clave, valor in kwargs.items():
        print(f" {clave}: {valor}")

funcion_flexible(1, 2, 3, nombre="Juan", edad=30)
