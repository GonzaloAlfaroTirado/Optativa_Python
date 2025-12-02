try:
    minutos_totales = int(input("Introduce la cantidad de minutos: "))
    
    if minutos_totales < 0:
        print("Error: La cantidad de minutos debe ser positiva.")
    else:
        horas = minutos_totales // 60
        minutos_restantes = minutos_totales % 60
        
        print(f"\n{minutos_totales} minutos corresponden a:")
        print(f"* {horas} horas")
        print(f"* {minutos_restantes} minutos")
except ValueError:
    print("Error: Por favor, introduce un numero entero valido.")