try:
    A = int(input("Introduce la base (A): "))
    B = int(input("Introduce el exponente (B, entero positivo o 0): "))
    
    if B < 0:
        print("Por simplicidad, el exponente B debe ser positivo o cero.")
    elif B == 0:
        resultado = 1
    elif A == 0:
        resultado = 0
    else:
        resultado = 1
        for _ in range(B):
            resultado *= A
        
    print(f"\n{A}^{B} es igual a: {resultado}")

except ValueError:
    print("Entrada no valida. Por favor, introduce numeros enteros.")