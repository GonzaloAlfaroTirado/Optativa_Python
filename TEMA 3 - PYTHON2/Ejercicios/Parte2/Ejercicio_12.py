try:
    altura = int(input("Introduce la altura de la escalera: "))
    
    if altura < 1:
        print("La altura debe ser un número entero positivo.")
    else:
        print("\nEscalera:")
        for i in range(1, altura + 1):
            print(str(i) * i)

except ValueError:
    print("Entrada no válida. Por favor, introduce un número entero.")