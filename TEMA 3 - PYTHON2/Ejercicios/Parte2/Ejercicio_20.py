BILLETES = [500, 200, 100, 50, 20, 10, 5]

try:
    cantidad = int(input("Introduce la cantidad de euros (múltiplo de 5): "))
    
    if cantidad <= 0:
        print("La cantidad debe ser positiva.")
    elif cantidad % 5 != 0:
        print("La cantidad debe ser un múltiplo de 5 €.")
    else:
        resto = cantidad
        print(f"\nDesglose mínimo de {cantidad} €:")
        
        for billete in BILLETES:
            num_billetes = resto // billete
            
            if num_billetes > 0:
                print(f"* {num_billetes} billete(s) de {billete} €")
                
                resto = resto % billete

except ValueError:
    print("Entrada no válida. Por favor, introduce un número entero.")