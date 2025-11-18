try:
    nota = float(input("Introduce la calificación numérica (entre 0 y 10): "))

    if nota < 0 or nota > 10:
        print("Error: La calificación debe estar entre 0 y 10.")
    elif nota < 3:
        print("Calificación: Muy Deficiente.")
    elif nota < 5:
        print("Calificación: Insuficiente.")
    elif nota < 6:
        print("Calificación: Suficiente.")
    elif nota < 7:
        print("Calificación: Bien.")
    elif nota < 9:
        print("Calificación: Notable.")
    else:
        print("Calificación: Sobresaliente.")

except ValueError:
    print("Error: Debes introducir un número válido.")