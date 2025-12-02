try:
    parcial1 = float(input("Nota del parcial 1 (0-10): "))
    parcial2 = float(input("Nota del parcial 2 (0-10): "))
    parcial3 = float(input("Nota del parcial 3 (0-10): "))
    
    examen_final = float(input("Nota del examen final (0-10): "))
    trabajo_final = float(input("Nota del trabajo final (0-10): "))
    
    promedio_parciales = (parcial1 + parcial2 + parcial3) / 3
    
    p_parciales = promedio_parciales * 0.55
    p_examen = examen_final * 0.30
    p_trabajo = trabajo_final * 0.15
    
    calificacion_final = p_parciales + p_examen + p_trabajo
    
    print(f"\nCalificacion Final de Algoritmos: {calificacion_final:.2f}")
except ValueError:
    print("Error: Por favor, introduce números válidos.")