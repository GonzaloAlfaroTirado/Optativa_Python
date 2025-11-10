precio_articulo = float(input("Introduce el precio del artículo: "))
precio_venta = float(input("Introduce el precio de venta: "))
descuento = ((precio_articulo - precio_venta) / precio_articulo) * 100
print(f"El porcentaje de descuento es: {descuento}%")