import math

try:
    a = float(input("Introduce la longitud del cateto a: "))
    b = float(input("Introduce la longitud del cateto b: "))
    
    hipotenusa = math.sqrt(a**2 + b**2)
    
    print(f"\nLa hipotenusa es: {hipotenusa:.2f}")
except ValueError:
    print("Error: Por favor, introduce numeros validos.")