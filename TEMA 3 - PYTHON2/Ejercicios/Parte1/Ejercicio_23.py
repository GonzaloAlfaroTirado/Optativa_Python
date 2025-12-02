def calcular_compra_farmacia_interactivo():
    
    try:
        valor_compra = float(input("Introduzca el valor de compra: "))
    except ValueError:
        print("Error: Por favor, introduzca un valor numérico válido para la compra.")
        return
    
    tipo_pago = input("Introduzca el tipo de pago ('contado' o 'tarjeta'): ").lower()

    descuento_recargo = 0.0
    total_a_pagar = valor_compra

    if tipo_pago == "contado":
        descuento_recargo = valor_compra * 0.05
        total_a_pagar = valor_compra - descuento_recargo
        
    elif tipo_pago == "tarjeta":
        descuento_recargo = valor_compra * 0.03
        total_a_pagar = valor_compra + descuento_recargo
        
    else:
        print("\nTipo de pago no reconocido. No se aplica descuento ni recargo.")

    print(f"\n--- Resumen de la Compra ---")
    print(f"Valor de compra inicial: {valor_compra:.2f}")
    
    if tipo_pago == "contado":
        print(f"Descuento aplicado (5%): {descuento_recargo:.2f}")
        
    elif tipo_pago == "tarjeta":
        print(f"Recargo aplicado (3%): {descuento_recargo:.2f}")
    
    print(f"Total a pagar: {total_a_pagar:.2f}")

calcular_compra_farmacia_interactivo()