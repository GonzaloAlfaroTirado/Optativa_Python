suma_pares = 0
suma_impares = 0

for numero in range(100, 201):
    if numero % 2 == 0:
        # Es par
        suma_pares += numero
    else:
        # Es impar
        suma_impares += numero

print(f"Suma de los números pares (100-200): {suma_pares}")
print(f"Suma de los números impares (100-200): {suma_impares}")