NUM_MAX = 100
positivos = 0
negativos = 0

print(f"Introduce {NUM_MAX} números no nulos:")
for i in range(1, NUM_MAX + 1):
    try:
        num = float(input(f"Número {i}: "))
        if num == 0:
            print("El número no puede ser nulo. Intenta de nuevo.")
            continue
        
        if num > 0:
            positivos += 1
        elif num < 0:
            negativos += 1
            
    except ValueError:
        print("Entrada no válida. Introduce un número.")
        continue

print(f"\nResultados del conteo:")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")