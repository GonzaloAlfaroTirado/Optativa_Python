try:
    altura = int(input("Introduce la altura de la pirámide: "))
    
    if altura < 1:
        print("La altura debe ser un número entero positivo.")
    else:
        for i in range(1, altura + 1):
            espacios = " " * (altura - i)
            
            asteriscos = "*" * (2 * i - 1)
            
            print(espacios + asteriscos)

except ValueError:
    print("Entrada no válida. Por favor, introduce un número entero.")