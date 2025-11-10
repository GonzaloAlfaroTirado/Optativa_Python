try:
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

    if num1 < num2:
        print(f"Orden ascendente: {num1}, {num2}")
    elif num2 < num1:
        print(f"Orden ascendente: {num2}, {num1}")
    else:
        print(f"Los números son iguales: {num1}, {num2}")

except ValueError:
    print("Error: Debes introducir números válidos.")