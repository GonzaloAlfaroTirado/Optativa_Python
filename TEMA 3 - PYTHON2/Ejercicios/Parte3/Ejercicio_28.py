try:
    sueldo_base = float(input("Introduce el sueldo base del vendedor: "))
    venta1 = float(input("Introduce el importe de la Venta 1: "))
    venta2 = float(input("Introduce el importe de la Venta 2: "))
    venta3 = float(input("Introduce el importe de la Venta 3: "))
    
    total_ventas = venta1 + venta2 + venta3
    comision_porcentaje = 0.10
    
    comisiones = total_ventas * comision_porcentaje
    
    total_a_recibir = sueldo_base + comisiones
    
    print(f"\nResultados del mes:")
    print(f"* Total por comisiones (10%): {comisiones:.2f} €")
    print(f"* Sueldo total a recibir: {total_a_recibir:.2f} €")
except ValueError:
    print("Error: Por favor, introduce numeros validos.")