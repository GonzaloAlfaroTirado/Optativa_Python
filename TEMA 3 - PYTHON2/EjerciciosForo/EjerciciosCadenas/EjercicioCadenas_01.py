'''
Leer una cadena desde teclado y mostrarla carácter por carácter usando un ciclo for y el índice.
'''
cadena = input("Introduce una cadena de texto: ")
longitud = len(cadena)

print("\nMostrando la cadena carácter por carácter:")
for i in range(longitud):
    print(f"Índice {i}: {cadena[i]}")