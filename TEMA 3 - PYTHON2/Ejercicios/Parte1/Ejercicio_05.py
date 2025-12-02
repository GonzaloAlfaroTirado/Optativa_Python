radio = float(input("Introduce la longitud del radio: "))
import math
longitud_circunferencia = 2 * math.pi * radio
area_circulo = math.pi * radio**2
volumen_esfera = (4/3) * math.pi * radio**3
print(f"La longitud de la circunferencia es: {longitud_circunferencia}")
print(f"El área del círculo es: {area_circulo}")
print(f"El volumen de la esfera es: {volumen_esfera}")