try:
    N = int(input("Introduce un numero entero positivo: "))
    
    if N < 0:
        print("El numero debe ser positivo.")
    elif N == 0:
        print(f"{N}! = 1")
    else:
        factorial = 1
        for i in range(1, N + 1):
            factorial *= i
        
        print(f"{N}! = {factorial}")

except ValueError:
    print("Entrada no valida. Por favor, introduce un numero entero.")

print("="*30)
