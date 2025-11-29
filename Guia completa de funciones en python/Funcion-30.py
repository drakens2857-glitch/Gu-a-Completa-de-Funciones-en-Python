def validar_email(email):

    if "@" not in email:
        return False
    if "." not in email:
        return False
    if email.count("@") != 1:
        return False
    return True


def validar_telefono(telefono):

    telefono = telefono.replace(" ", "").replace("-", "")
    if len(telefono) != 10:
        return False
    if not telefono.isdigit():
        return False
    return True


print(f"Email válido: {validar_email('juan@ejemplo.com')}")
print(f"Email válido: {validar_email('juanejemplo.com')}")
print(f"Teléfono válido: {validar_telefono('300-123-4567')}")
print(f"Teléfono válido: {validar_telefono('123')}")
