try:
    altura = int(input("Introduce la altura de la pirámide invertida: "))
    
    if altura < 1:
        print("La altura debe ser un número entero positivo.")
    else:
        print("\nPirámide Invertida:")
        for i in range(altura, 0, -1):
            espacios = " " * (altura - i)
            
            asteriscos = "*" * (2 * i - 1)
            
            print(espacios + asteriscos)

except ValueError:
    print("Entrada no válida. Por favor, introduce un número entero.")