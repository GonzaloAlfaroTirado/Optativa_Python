print("Introduce 100 números no nulos.")

se_leyo_negativo = False
numeros_leidos = 0

while numeros_leidos < 100:
    try:
        numero = float(input(f"Número {numeros_leidos + 1}/100: "))
        
        if numero == 0:
            print("El número no debe ser nulo. Inténtalo de nuevo.")
            continue
            
        if numero < 0:
            se_leyo_negativo = True
            
        numeros_leidos += 1

    except ValueError:
        print("Error: Debes introducir un número válido.")

if se_leyo_negativo:
    print("Se ha introducido al menos un número negativo.")
else:
    print("No se introdujeron números negativos.")