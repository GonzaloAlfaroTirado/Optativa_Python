try:
    n = int(input("Introduce un número entero positivo (N): "))
    
    if n < 0:
        print("El factorial no está definido para números negativos.")
    elif n == 0:
        # Caso base: 0! = 1
        print("El factorial de 0 es: 1")
    else:
        factorial = 1
        for i in range(1, n + 1):
            factorial = factorial * i
            
        print(f"El factorial de {n} (N!) es: {factorial}")

except ValueError:
    print("Error: Debes introducir un número entero válido.")