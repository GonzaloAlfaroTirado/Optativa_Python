try:
    base = float(input("Introduce la base del rectangulo: "))
    altura = float(input("Introduce la altura del rectangulo: "))
    
    perimetro = 2 * (base + altura)
    area = base * altura
    
    print(f"\nResultados:")
    print(f"* Per�metro: {perimetro}")
    print(f"* �rea: {area}")
except ValueError:
    print("Error: Por favor, introduce numeros validos.")