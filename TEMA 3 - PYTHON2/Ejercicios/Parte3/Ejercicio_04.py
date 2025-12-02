try:
    N = int(input("Introduce un numero N: "))
    
    if N < 1:
        print("El numero debe ser mayor o igual a 1.")
    else:
        for i in range(1, N + 1):
            print(i, end=", " if i < N else "")
        print()

except ValueError:
    print("Entrada no valida. Por favor, introduce un numero entero.")