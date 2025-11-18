print("Introduce 100 números no nulos.")

contador_positivos = 0
contador_negativos = 0
numeros_leidos = 0

while numeros_leidos < 100:
    try:
        numero = float(input(f"Número {numeros_leidos + 1}/100: "))
        
        if numero == 0:
            print("El número no debe ser nulo. Inténtalo de nuevo.")
            continue
            
        if numero > 0:
            contador_positivos += 1
        else:
            contador_negativos += 1
            
        numeros_leidos += 1

    except ValueError:
        print("Error: Debes introducir un número válido.")

print("\n--- Resultados ---")
print(f"Total de números positivos: {contador_positivos}")
print(f"Total de números negativos: {contador_negativos}")