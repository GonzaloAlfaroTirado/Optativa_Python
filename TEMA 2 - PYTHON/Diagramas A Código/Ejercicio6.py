try:
    precio_original = float(input("Introduce el precio original del artículo: "))
    precio_venta = float(input("Introduce el precio de venta real: "))
    
    if precio_original <= 0:
        print("El precio original debe ser positivo.")
    elif precio_venta > precio_original:
        print("El precio de venta es mayor que el original, no hay descuento.")
    else:
        descuento_aplicado = precio_original - precio_venta
        porcentaje_descuento = (descuento_aplicado / precio_original) * 100
        print(f"El porcentaje de descuento realizado es: {porcentaje_descuento:.2f}%")

except ValueError:
    print("Error: Debes introducir números válidos.")