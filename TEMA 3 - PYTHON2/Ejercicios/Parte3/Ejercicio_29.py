try:
    total_compra = float(input("Introduce el total de la compra: "))
    
    descuento_porcentaje = 0.15
    
    descuento = total_compra * descuento_porcentaje
    
    pago_final = total_compra - descuento
    
    print(f"\nDetalle de la compra:")
    print(f"* Descuento (15%): {descuento:.2f} €")
    print(f"* Total a pagar: {pago_final:.2f} €")
except ValueError:
    print("Error: Por favor, introduce un numero valido.")