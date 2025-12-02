def siguiente_segundo_interactivo():
    try:
        h = int(input("Hora (0-23): "))
        m = int(input("Minutos (0-59): "))
        s = int(input("Segundos (0-59): "))
    except ValueError:
        print("Error: Por favor, introduzca solo números enteros.")
        return

    if not (0 <= h <= 23 and 0 <= m <= 59 and 0 <= s <= 59):
        print("Error: Los valores de hora, minutos o segundos están fuera de rango.")
        return

    s += 1
    
    if s >= 60:
        s = 0
        m += 1
        
        if m >= 60:
            m = 0
            h += 1
            
            if h >= 24:
                h = 0
    
    hora_siguiente = f"{h:02d}:{m:02d}:{s:02d}"
    print(f"La hora actual es: {h:02d}:{m:02d}:{s:02d}")
    print(f"Transcurrido un segundo, la hora será: {hora_siguiente}")

siguiente_segundo_interactivo()