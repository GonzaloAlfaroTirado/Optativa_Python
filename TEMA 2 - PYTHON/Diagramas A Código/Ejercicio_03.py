try:
    lado = float(input("Introduce la longitud del lado del cuadrado: "))
    area = lado * lado
    print(f"El área del cuadrado es: {area}")
except ValueError:
    print("Error: Debes introducir un número válido.")