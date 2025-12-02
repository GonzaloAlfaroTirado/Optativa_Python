try:
    altura = int(input("Introduce la altura de la piramide: "))
    
    if altura < 1:
        print("La altura debe ser un numero entero positivo.")
    else:
        print("\nPiramide:")
        for i in range(1, altura + 1):
            espacios = " " * (altura - i)
            
            asteriscos = "*" * (2 * i - 1)
            
            print(espacios + asteriscos)

except ValueError:
    print("Entrada no valida. Por favor, introduce un numero entero.")

print("="*30)
