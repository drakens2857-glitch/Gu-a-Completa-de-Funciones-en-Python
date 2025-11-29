def formatear_precio(precio):
  
    return f"${precio:,.2f}"


def formatear_fecha(dia, mes, año):
   
    return f"{dia:02d}/{mes:02d}/{año}"


def formatear_porcentaje(valor):
    
    return f"{valor * 100:.1f}%"


print(formatear_precio(1234567.89))
print(formatear_fecha(5, 3, 2024))
print(formatear_porcentaje(0.845))
