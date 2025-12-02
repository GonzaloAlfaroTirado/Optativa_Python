try:
    altura = int(input("Introduce la altura de la piramide invertida: "))
    
    if altura < 1:
        print("La altura debe ser un numero entero positivo.")
    else:
        print("\nPiramide Invertida:")
        for i in range(altura, 0, -1):
            espacios = " " * (altura - i)
            
            asteriscos = "*" * (2 * i - 1)
            
            print(espacios + asteriscos)

except ValueError:
    print("Entrada no valida. Por favor, introduce un numero entero.")