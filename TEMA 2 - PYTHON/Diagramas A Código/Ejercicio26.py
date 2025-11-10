try:
    nombre = input("Nombre del trabajador: ")
    horas_trabajadas = float(input("Horas trabajadas esta semana: "))
    tarifa_normal = float(input("Tarifa normal por hora (€): "))
    
    if horas_trabajadas <= 35:
        salario_bruto = horas_trabajadas * tarifa_normal
    else:
        pago_normal = 35 * tarifa_normal
        horas_extra = horas_trabajadas - 35
        pago_extra = horas_extra * (tarifa_normal * 1.5)
        salario_bruto = pago_normal + pago_extra
        
    impuestos_totales = 0
    
    if salario_bruto <= 500:
        impuestos_totales = 0
    elif salario_bruto <= 900:
        impuestos_totales = (salario_bruto - 500) * 0.25
    else:
        impuesto_tramo_2 = 400 * 0.25
        impuesto_tramo_3 = (salario_bruto - 900) * 0.45
        impuestos_totales = impuesto_tramo_2 + impuesto_tramo_3

    salario_neto = salario_bruto - impuestos_totales

    print("\n--- Recibo de Salario ---")
    print(f"Trabajador: {nombre}")
    print(f"Salario Bruto: {salario_bruto:.2f} €")
    print(f"Tasas (Impuestos): {impuestos_totales:.2f} €")
    print(f"Salario Neto Semanal: {salario_neto:.2f} €")

except ValueError:
    print("Error: Debes introducir valores numéricos válidos.")