print("Piensa un número del 1 al 100.")
print("Yo intentaré adivinarlo.")
print("Respóndeme con: 'mayor', 'menor' o 'igual'.\n")

limite_inferior = 1
limite_superior = 100
adivinado = False
intentos = 0

while not adivinado:
    intentos += 1
    
    propuesta = (limite_inferior + limite_superior) // 2
    
    pista = ""
    while pista not in ['mayor', 'menor', 'igual']:
        pista = input(f"¿Es tu número {propuesta}? (mayor / menor / igual): ").lower()

    if pista == 'igual':
        print(f"\n¡Genial! Lo adiviné en {intentos} intentos.")
        adivinado = True
    elif pista == 'mayor':
        limite_inferior = propuesta + 1
    elif pista == 'menor':
        limite_superior = propuesta - 1
        
    if limite_inferior > limite_superior:
        print("¡Oye, me has mentido! Empecemos de nuevo.")
        break