suma_pares = 0
suma_impares = 0

for i in range(100, 201): 
    if i % 2 == 0:
        suma_pares += i
    else:
        suma_impares += i

print(f"Suma de los numeros pares (100-200): {suma_pares}")
print(f"Suma de los numeros impares (100-200): {suma_impares}")