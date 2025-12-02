try:
    N = int(input("Introduce un número entero positivo N: "))
    
    if N < 0:
        print("El número debe ser positivo.")
    elif N == 0:
        print(f"{N}! = 1")
    else:
        factorial = 1
        for i in range(1, N + 1):
            factorial *= i
        
        print(f"{N}! = {factorial}")

except ValueError:
    print("Entrada no válida. Por favor, introduce un número entero.")