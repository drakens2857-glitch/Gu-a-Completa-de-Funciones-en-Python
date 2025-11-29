def celsius_a_fahrenheit(celsius):

    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


temp1 = celsius_a_fahrenheit(0)
temp2 = celsius_a_fahrenheit(25)
temp3 = celsius_a_fahrenheit(100)

print(f"0°C = {temp1}°F")
print(f"25°C = {temp2}°F")
print(f"100°C = {temp3}°F")
