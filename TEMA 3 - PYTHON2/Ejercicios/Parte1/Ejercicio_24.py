def calcular_compra_don_pepe(monto_compra, dia_semana):
    dia_semana = dia_semana.lower()
    descuento = 0.0

    if dia_semana == "martes" or dia_semana == "jueves":
        descuento = monto_compra * 0.15
    
    total_a_pagar = monto_compra - descuento

    print(f"\nMonto de compra: {monto_compra:.2f}")
    print(f"Descuento: {descuento:.2f}")
    print(f"Total a pagar: {total_a_pagar:.2f}")

calcular_compra_don_pepe(200.00, "Jueves")