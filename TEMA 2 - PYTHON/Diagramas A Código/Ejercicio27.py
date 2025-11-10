print("Introduce las notas (0 a 10). Escribe -1 para terminar.")

hubo_un_diez = False

while True:
    try:
        nota = float(input("Introduce una nota: "))
        
        if nota == -1:
            print("Terminando la lectura de notas.")
            break
            
        if nota < 0 or nota > 10:
            print("Nota no válida (debe ser entre 0 y 10, o -1 para salir).")
            continue

        if nota == 10:
            hubo_un_diez = True
            
    except ValueError:
        print("Error: Introduce un número válido.")

if hubo_un_diez:
    print("Resultado: Sí, se introdujo al menos una nota con valor 10.")
else:
    print("Resultado: No se introdujo ninguna nota con valor 10.")