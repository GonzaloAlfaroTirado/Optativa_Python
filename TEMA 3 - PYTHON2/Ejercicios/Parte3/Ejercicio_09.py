positivos = 0
negativos = 0
hay_negativo = False

print("Introduce numeros no nulos. Introduce 0 para terminar.")

while True:
    try:
        num = float(input("Introduce un numero: "))
        
        if num == 0:
            break
        
        if num > 0:
            positivos += 1
        elif num < 0:
            negativos += 1
            hay_negativo = True
            
    except ValueError:
        print("Entrada no valida. Introduce un numero.")
        continue

print("\nResultados del conteo:")
print(f"* Hubo algun negativo?: {'Si' if hay_negativo else 'No'}")
print(f"* Positivos totales: {positivos}")
print(f"* Negativos totales: {negativos}")