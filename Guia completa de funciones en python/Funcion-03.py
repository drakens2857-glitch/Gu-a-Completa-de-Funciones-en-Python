def calcular_descuento(precio, porcentaje):
    descuento = precio * (porcentaje / 100)
    precio_final = precio - descuento
    return precio_final


precio_con_descuento = calcular_descuento(1000, 20)
print(f"Precio final: ${precio_con_descuento}")

otro_precio = calcular_descuento(500, 15)
print(f"Precio final: ${otro_precio}")
