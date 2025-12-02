BILLETES = [500, 200, 100, 50, 20, 10, 5]

try:
    cantidad = int(input("Introduce la cantidad de euros (multiplo de 5): "))
    
    if cantidad <= 0:
        print("La cantidad debe ser positiva.")
    elif cantidad % 5 != 0:
        print("La cantidad debe ser un multiplo de 5 €.")
    else:
        resto = cantidad
        print(f"\nDesglose minimo de {cantidad} €:")
        
        for billete in BILLETES:
            num_billetes = resto // billete
            
            if num_billetes > 0:
                print(f"* {num_billetes} billete(s) de {billete} �")
                
                resto = resto % billete

except ValueError:
    print("Entrada no valida. Por favor, introduce un numero entero.")