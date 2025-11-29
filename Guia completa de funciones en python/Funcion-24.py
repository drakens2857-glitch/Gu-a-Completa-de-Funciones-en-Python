def operacion_compleja(x, y):
    

    def sumar():
        return x + y

    def multiplicar():
        return x * y

    def procesar():
        suma = sumar()
        producto = multiplicar()
        return suma, producto

    return procesar()


resultado = operacion_compleja(4, 5)
print(f"Suma y producto: {resultado}")
