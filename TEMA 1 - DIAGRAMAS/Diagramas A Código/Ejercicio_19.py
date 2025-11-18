try:
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    num3 = float(input("Introduce el tercer número: "))

    if num1 == num2 and num2 == num3:
        print("Los tres números son iguales.")
    
    elif num1 == num2:
        print(f"Hay dos números iguales ({num1}).")
        if num1 > num3:
            print(f"El mayor es {num1} y el menor es {num3}.")
        else:
            print(f"El mayor es {num3} y el menor es {num1}.")
    elif num1 == num3:
        print(f"Hay dos números iguales ({num1}).")
        if num1 > num2:
            print(f"El mayor es {num1} y el menor es {num2}.")
        else:
            print(f"El mayor es {num2} y el menor es {num1}.")
    elif num2 == num3:
        print(f"Hay dos números iguales ({num2}).")
        if num2 > num1:
            print(f"El mayor es {num2} y el menor es {num1}.")
        else:
            print(f"El mayor es {num1} y el menor es {num2}.")
    
    else:
        print("Los tres números son distintos.")
        if num1 > num2 and num1 > num3:
            mayor = num1
        elif num2 > num1 and num2 > num3:
            mayor = num2
        else:
            mayor = num3
            
        if num1 < num2 and num1 < num3:
            menor = num1
        elif num2 < num1 and num2 < num3:
            menor = num2
        else:
            menor = num3
            
        print(f"El número mayor es: {mayor}")
        print(f"El número menor es: {menor}")

except ValueError:
    print("Error: Debes introducir números válidos.")