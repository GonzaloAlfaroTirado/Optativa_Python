# Ejercicio5: Escriba un programa que toma como dato de entrada un número que corresponde a la longitud de un radio (La longitud del radio es la mitad de la del diámetro) y nos escribe la longitud de la circunferencia (La longitud de una circunferencia es igual a pi por el diámetro), el área del
# círculo (El área de un círculo es pi multiplicado por el radio al cuadrado) y el volumen de la esfera que corresponde con dicho radio.
radio = float(input("Introduce la longitud del radio: "))
import math
longitud_circunferencia = 2 * math.pi * radio
area_circulo = math.pi * radio**2
volumen_esfera = (4/3) * math.pi * radio**3
print(f"La longitud de la circunferencia es: {longitud_circunferencia}")
print(f"El área del círculo es: {area_circulo}")
print(f"El volumen de la esfera es: {volumen_esfera}")