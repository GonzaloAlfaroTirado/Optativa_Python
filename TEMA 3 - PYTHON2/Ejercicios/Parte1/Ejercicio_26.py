def evaluar_dados_interactivo():
    print("Simulación de lanzamiento de tres dados (Valores 1 a 6).")
    
    try:
        dado1 = int(input("Introduzca el resultado del Dado 1: "))
        dado2 = int(input("Introduzca el resultado del Dado 2: "))
        dado3 = int(input("Introduzca el resultado del Dado 3: "))
    except ValueError:
        print("Error: Por favor, introduzca solo números enteros.")
        return

    if not (1 <= dado1 <= 6 and 1 <= dado2 <= 6 and 1 <= dado3 <= 6):
        print("Error: Los resultados de los dados deben ser números entre 1 y 6.")
        return

    seis_count = 0
    if dado1 == 6:
        seis_count += 1
    if dado2 == 6:
        seis_count += 1
    if dado3 == 6:
        seis_count += 1
    
    if seis_count == 3:
        resultado = "Excelente"
    elif seis_count == 2:
        resultado = "Muy bien"
    elif seis_count == 1:
        resultado = "Regular"
    elif seis_count == 0:
        resultado = "Pésimo"
    else:
        resultado = "Error de conteo"

    print(f"\nResultados obtenidos: {dado1}, {dado2}, {dado3}")
    print(f"Mensaje del Casino: {resultado}")

evaluar_dados_interactivo()