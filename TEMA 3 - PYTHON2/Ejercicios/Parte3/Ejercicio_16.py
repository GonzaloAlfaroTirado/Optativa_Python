hay_diez = False
print("Introduce notas (de 0 a 10). Introduce -1 para terminar.")

while True:
    try:
        nota = float(input("Introduce nota: "))
        
        if nota == -1:
            break
            
        if 0 <= nota <= 10:
            if nota == 10:
                hay_diez = True
                
            else:
                pass
        else:
            print("Nota fuera del rango valido (0 a 10). Intenta de nuevo.")
            
    except ValueError:
        print("Entrada no valida. Introduce un numero.")
        continue

if hay_diez:
    print("\n? Hubo al menos una nota con valor 10!")
else:
    print("\n? No se registro ninguna nota con valor 10.")