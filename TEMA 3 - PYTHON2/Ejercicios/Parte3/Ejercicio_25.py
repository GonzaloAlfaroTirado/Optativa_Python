try:
    grados_fahrenheit = float(input("Introduce la temperatura en grados Fahrenheit: "))
    
    grados_celsius = (grados_fahrenheit - 32) * 5/9
    
    print(f"\n{grados_fahrenheit}ºF equivalen a {grados_celsius:.2f}ºC.")
except ValueError:
    print("Error: Por favor, introduce un numero valido.")