NUM_MAX = 100
hay_negativo = False

print(f"Introduce {NUM_MAX} numeros no nulos:")
for i in range(1, NUM_MAX + 1):
    try:
        num = float(input(f"Numero {i}: "))
        if num == 0:
            print("El numero no puede ser nulo. Intenta de nuevo.")
            continue
        
        if num < 0:
            hay_negativo = True
            
    except ValueError:
        print("Entrada no valida. Introduce un numero.")
        continue

if hay_negativo:
    print("\n Se ha leido al menos un numero negativo.")
else:
    print("\n No se ha leido ningun numero negativo.")