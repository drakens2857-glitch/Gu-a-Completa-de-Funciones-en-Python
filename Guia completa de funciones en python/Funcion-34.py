def crear_libro(titulo, autor, año):

    return {
        "titulo": titulo,
        "autor": autor,
        "año": año,
        "prestado": False
    }


def prestar_libro(libro):
  
    if libro["prestado"]:
        return "El libro ya está prestado"
    libro["prestado"] = True
    return f"Libro '{libro['titulo']}' prestado exitosamente"


def devolver_libro(libro):
   
    if not libro["prestado"]:
        return "El libro no estaba prestado"
    libro["prestado"] = False
    return f"Libro '{libro['titulo']}' devuelto exitosamente"


def mostrar_libro(libro):

    estado = "Prestado" if libro["prestado"] else "Disponible"
    info = f"""
Título: {libro['titulo']}
Autor: {libro['autor']}
Año: {libro['año']}
Estado: {estado}
========================
"""
    return info

libro1 = crear_libro("Cien Años de Soledad", "Gabriel García Márquez", 1967)
libro2 = crear_libro("El Principito", "Antoine de Saint-Exupéry", 1943)

print(mostrar_libro(libro1))
print(mostrar_libro(libro2))

print(prestar_libro(libro1))
print(mostrar_libro(libro1))

print(prestar_libro(libro1))
print(devolver_libro(libro1))
print(mostrar_libro(libro1))

