print("Introduce números (un 0 para terminar).")

contador_positivos = 0
contador_negativos = 0
se_leyo_negativo = False

while True:
    try:
        numero = float(input("Introduce un número: "))
        
        if numero == 0:
            print("Se introdujo un 0. Terminando la lectura.")
            break
            
        if numero > 0:
            contador_positivos += 1
        else:
            contador_negativos += 1
            se_leyo_negativo = True
    except ValueError:
        print("Error: Debes introducir un número válido.")

print("\n--- Resultados ---")
if se_leyo_negativo:
    print("Se ha introducido al menos un número negativo.")
else:
    print("No se introdujeron números negativos.")

print(f"Total de números positivos: {contador_positivos}")
print(f"Total de números negativos: {contador_negativos}")