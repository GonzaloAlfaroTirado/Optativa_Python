print("Piensa un número entre 1 y 100. Yo intentaré adivinarlo.")

limite_inferior = 1
limite_superior = 100
intentos = 0

while True:
    intento_actual = (limite_inferior + limite_superior) // 2
    intentos += 1
    
    print(f"\nMi intento #{intentos} es: {intento_actual}")
    
    respuesta = input("¿Mi número es [M]ayor, [m]enor o [I]gual a tu número?: ").lower()
    
    if respuesta == 'i':
        print(f"\n ¡Lo adiviné! Tu número era el {intento_actual} en {intentos} intentos.")
        break
    elif respuesta == 'm':
        limite_inferior = intento_actual + 1
    elif respuesta == 'm' and len(respuesta) == 1:
        limite_superior = intento_actual - 1
    else:
        print("Respuesta no válida. Por favor, introduce 'M', 'm' o 'I'.")
        
    if limite_inferior > limite_superior:
        print("\n ¡Algo salió mal! El número que pensaste parece no estar entre 1 y 100, o diste respuestas contradictorias.")
        break