# Ejercicio 10: Escriba un programa que lea dos números, calcule y muestre el valor de sus suma, resta,
# producto y división (Ten en cuenta la división por cero)
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
suma = num1 + num2
resta = num1 - num2
producto = num1 * num2
if num2 != 0:
    division = num1 / num2
else:
    division = "División por cero no permitida"
print(f"La suma es: {suma}")
print(f"La resta es: {resta}")
print(f"El producto es: {producto}")
print(f"La división es: {division}")