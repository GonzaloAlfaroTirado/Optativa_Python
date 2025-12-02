try:
    altura = int(input("Introduce la altura de la escalera: "))
    
    if altura < 1:
        print("La altura debe ser un número entero positivo.")
    else:
        print("\nEscalera:")
        for i in range(1, altura + 1):
            linea = ""
            for j in range(1, i + 1):
                linea += str(j)
            print(linea)

except ValueError:
    print("Entrada no válida. Por favor, introduce un número entero.")