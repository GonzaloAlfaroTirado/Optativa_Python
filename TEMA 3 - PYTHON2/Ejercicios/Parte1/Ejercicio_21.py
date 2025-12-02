def calcular_salario_neto(nombre, horas_trabajadas, tarifa_normal):
    horas_normales = min(horas_trabajadas, 35)
    horas_extra = max(0, horas_trabajadas - 35)

    pago_normal = horas_normales * tarifa_normal
    pago_extra = horas_extra * (tarifa_normal * 1.5)

    salario_bruto = pago_normal + pago_extra

    impuesto_total = 0.0
    salario_restante = salario_bruto

    if salario_restante > 500:
        salario_restante -= 500

    impuesto_base25 = min(salario_restante, 400)
    impuesto_total += impuesto_base25 * 0.25
    salario_restante -= impuesto_base25

    impuesto_total += salario_restante * 0.45

    salario_neto = salario_bruto - impuesto_total

    print(f"\nTrabajador: {nombre}")
    print(f"Salario Bruto: {salario_bruto:.2f}")
    print(f"Tasas (Impuestos): {impuesto_total:.2f}")
    print(f"Salario Neto Semanal: {salario_neto:.2f}")

calcular_salario_neto("Jose Benítez", 40, 15)