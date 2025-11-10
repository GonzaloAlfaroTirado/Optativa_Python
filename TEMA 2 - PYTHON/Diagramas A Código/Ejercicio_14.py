try:
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

    suma = num1 + num2
    resta = num1 - num2
    producto = num1 * num2

    print(f"Suma: {num1} + {num2} = {suma}")
    print(f"Resta: {num1} - {num2} = {resta}")
    print(f"Producto: {num1} * {num2} = {producto}")

    if num2 == 0:
        print("División: No se puede dividir por cero.")
    else:
        division = num1 / num2
        print(f"División: {num1} / {num2} = {division}")

except ValueError:
    print("Error: Debes introducir números válidos.")