def crear_perfil(nombre, edad, ciudad="No especificada", pais="Colombia"):
    perfil = f"""
=== PERFIL DE USUARIO ===
Nombre: {nombre}
Edad: {edad} años
Ciudad: {ciudad}
País: {pais}
========================
"""
    return perfil

perfil1 = crear_perfil("María", 25, "Bogotá", "Colombia")
print(perfil1)

perfil2 = crear_perfil("Juan", 30)
print(perfil2)
