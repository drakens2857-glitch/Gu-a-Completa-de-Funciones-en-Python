def dividir_seguro(a, b):

    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        return "Error: No se puede dividir por cero"
    except TypeError:
        return "Error: Debes usar números"


print(dividir_seguro(10, 2))
print(dividir_seguro(10, 0))
print(dividir_seguro(10, "a"))
