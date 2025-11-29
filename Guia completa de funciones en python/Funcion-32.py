def metros_a_pies(metros):
 
    return metros * 3.28084


def celsius_a_fahrenheit(celsius):
   
    return (celsius * 9/5) + 32


def kilogramos_a_libras(kg):
   
    return kg * 2.20462


def kilometros_a_millas(km):
    
    return km * 0.621371


print(f"10 metros = {metros_a_pies(10):.2f} pies")
print(f"25°C = {celsius_a_fahrenheit(25):.2f}°F")
print(f"70 kg = {kilogramos_a_libras(70):.2f} libras")
print(f"100 km = {kilometros_a_millas(100):.2f} millas")
