def factorial(n):

    if n == 1:
        return 1
    return n * factorial(n - 1)


resultado = factorial(5)
print(f"5! = {resultado}")

resultado2 = factorial(3)
print(f"3! = {resultado2}")
