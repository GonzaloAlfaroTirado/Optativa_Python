positivos = 0
negativos = 0
hay_negativo = False

print("Introduce números no nulos. Introduce 0 para terminar.")

while True:
    try:
        num = float(input("Introduce un número: "))
        
        if num == 0:
            break
        
        if num > 0:
            positivos += 1
        elif num < 0:
            negativos += 1
            hay_negativo = True
            
    except ValueError:
        print("Entrada no válida. Introduce un número.")
        continue

print("\nResultados del conteo:")
print(f"¿Hubo algún negativo?: {'Sí' if hay_negativo else 'No'}")
print(f"¿Positivos totales: {positivos}")
print(f"¿Negativos totales: {negativos}")