def verificar_edad(edad):
    if edad < 0:
        return "Error: edad negativa"
    elif edad < 18:
        return "No puede votar: es menor de edad"
    else:
        return "Puede votar: es mayor de edad"


print(verificar_edad(-5))
print(verificar_edad(15))
print(verificar_edad(25))
