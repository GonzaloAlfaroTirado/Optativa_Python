try:
    cantidad = int(input("Introduce una cantidad (múltiplo de 5 €): "))
    
    if cantidad % 5 != 0:
        print("Error: La cantidad debe ser un múltiplo de 5.")
    else:
        print(f"Desglose para {cantidad} € en el mínimo de billetes:")
        
        restante = cantidad
        
        billetes_500 = restante // 500
        restante = restante % 500
        
        billetes_200 = restante // 200
        restante = restante % 200
 
        billetes_100 = restante // 100
        restante = restante % 100

        billetes_50 = restante // 50
        restante = restante % 50

        billetes_20 = restante // 20
        restante = restante % 20

        billetes_10 = restante // 10
        restante = restante % 10

        billetes_5 = restante // 5
        restante = restante % 5
        
        if billetes_500 > 0:
            print(f"{billetes_500} billete(s) de 500 €")
        if billetes_200 > 0:
            print(f"{billetes_200} billete(s) de 200 €")
        if billetes_100 > 0:
            print(f"{billetes_100} billete(s) de 100 €")
        if billetes_50 > 0:
            print(f"{billetes_50} billete(s) de 50 €")
        if billetes_20 > 0:
            print(f"{billetes_20} billete(s) de 20 €")
        if billetes_10 > 0:
            print(f"{billetes_10} billete(s) de 10 €")
        if billetes_5 > 0:
            print(f"{billetes_5} billete(s) de 5 €")

except ValueError:
    print("Error: Debes introducir un número entero válido.")