import math

try:
    radio = float(input("Introduce la longitud del radio: "))
    
    if radio < 0:
        print("El radio no puede ser negativo.")
    else:
        diametro = 2 * radio
        longitud_circunferencia = math.pi * diametro
        
        area_circulo = math.pi * (radio ** 2)
        
        volumen_esfera = (4/3) * math.pi * (radio ** 3)
        
        print(f"Radio introducido: {radio}")
        print(f"Longitud de la circunferencia: {longitud_circunferencia:.2f}")
        print(f"Área del círculo: {area_circulo:.2f}")
        print(f"Volumen de la esfera: {volumen_esfera:.2f}")

except ValueError:
    print("Error: Debes introducir un número válido.")