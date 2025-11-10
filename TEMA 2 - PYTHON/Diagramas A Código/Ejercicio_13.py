try:
    n = int(input("Introduce un número entero positivo (N): "))
    
    if n <= 0:
        print("El número debe ser positivo.")
    else:
        print(f"Números del 1 al {n}:")
        for i in range(1, n + 1):
            print(i)

except ValueError:
    print("Error: Debes introducir un número entero válido.")