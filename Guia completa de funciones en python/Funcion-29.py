def limpiar_texto(texto):

    texto = texto.strip()
    texto = texto.lower()
    while "  " in texto:
        texto = texto.replace("  ", " ")
    return texto


def contar_palabras(texto):
  
    palabras = texto.split()
    return len(palabras)


def primera_letra_mayuscula(texto):
   
    return texto.title()


texto = " hola mundo desde PYTHON "
limpio = limpiar_texto(texto)
print(f"Original: '{texto}'")
print(f"Limpio: '{limpio}'")
print(f"Palabras: {contar_palabras(limpio)}")
print(f"Capitalizado: {primera_letra_mayuscula(limpio)}")
