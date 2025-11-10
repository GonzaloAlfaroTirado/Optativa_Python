def get_grade_letter(grade):
    if not (0 <= grade <= 10):
        return "Error: La calificación debe estar entre 0 y 10"
    elif grade < 3:
        return "Muy Deficiente"
    elif grade < 5:
        return "Insuficiente"
    elif grade < 6:
        return "Suficiente"
    elif grade < 7:
        return "Bien"
    elif grade < 9:
        return "Notable"
    else:
        return "Sobresaliente"

try:
    calificacion = float(input("Introduce una calificación (0-10): "))
    
    resultado = get_grade_letter(calificacion)
    print(f"La calificación {calificacion} corresponde a: {resultado}")
    
except ValueError:
    print("Error: Por favor introduce un número válido")