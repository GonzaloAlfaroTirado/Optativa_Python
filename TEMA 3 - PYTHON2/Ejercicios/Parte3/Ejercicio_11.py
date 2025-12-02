try:
    altura = int(input("Introduce la altura de la escalera: "))
    
    if altura < 1:
        print("La altura debe ser un numero entero positivo.")
    else:
        print("\nEscalera:")
        for i in range(1, altura + 1):
            print("*" * i)

except ValueError:
    print("Entrada no valida. Por favor, introduce un numero entero.")