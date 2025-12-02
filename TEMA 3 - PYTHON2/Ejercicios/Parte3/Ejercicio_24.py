try:
    num1 = float(input("Introduce el primer numero: "))
    num2 = float(input("Introduce el segundo numero: "))
    
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    
    print(f"\nResultados:")
    print(f"* Suma: {suma}")
    print(f"* Resta: {resta}")
    print(f"* Multiplicacion: {multiplicacion}")
    
    if num2 != 0:
        division = num1 / num2
        print(f"* Division: {division:.2f}")
    else:
        print("* Division: No se puede dividir por cero.")
except ValueError:
    print("Error: Por favor, introduce numeros validos.")