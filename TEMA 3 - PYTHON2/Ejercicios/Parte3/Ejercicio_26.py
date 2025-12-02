try:
    num1 = float(input("Introduce el primer numero: "))
    num2 = float(input("Introduce el segundo numero: "))
    num3 = float(input("Introduce el tercer numero: "))
    
    media = (num1 + num2 + num3) / 3
    
    print(f"\nLa media de los tres numeros es: {media:.2f}")
except ValueError:
    print("Error: Por favor, introduce numeros validos.")