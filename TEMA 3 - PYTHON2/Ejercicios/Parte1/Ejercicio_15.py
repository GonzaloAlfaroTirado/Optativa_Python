num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
num3 = float(input("Introduce el tercer número: "))

nums = [num1, num2, num3]

if len(set(nums)) == 1:
    print("Los tres números son iguales.")
else:
    mayor = max(nums)
    menor = min(nums)
    print(f"El número mayor es: {mayor}")
    print(f"El número menor es: {menor}")
