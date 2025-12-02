NUM_MAX = 100
hay_negativo = False

print(f"Introduce {NUM_MAX} números no nulos:")
for i in range(1, NUM_MAX + 1):
    try:
        num = float(input(f"Número {i}: "))
        if num == 0:
            print("El número no puede ser nulo. Intenta de nuevo.")
            continue
        
        if num < 0:
            hay_negativo = True
            
    except ValueError:
        print("Entrada no válida. Introduce un número.")
        continue

if hay_negativo:
    print("\n Se ha leído al menos un número negativo.")
else:
    print("\n No se ha leído ningún número negativo.")