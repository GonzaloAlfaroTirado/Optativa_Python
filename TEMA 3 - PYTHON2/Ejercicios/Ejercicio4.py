num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
suma = num1 + num2
resta = num1 - num2
producto = num1 * num2
if num2 != 0:
    division = num1 / num2
else:
    division = None
print(f"La suma es: {suma}")
print(f"La resta es: {resta}")
print(f"El producto es: {producto}")
if division is not None:
    print(f"La división es: {division}")
else:
    print("No se puede dividir entre cero.")
