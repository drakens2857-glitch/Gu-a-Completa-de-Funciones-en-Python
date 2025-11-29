def mi_decorador(funcion):
    def nueva_funcion():
        print("=== Inicio ===")
        funcion()
        print("=== Fin ===")
    return nueva_funcion

@mi_decorador
def saludar():
    print("¡Hola!")

saludar()
