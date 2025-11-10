MILLA_MARINA_EN_METROS = 1852

try:
    millas_marinas = float(input("Introduce la distancia en millas marinas: "))
    metros = millas_marinas * MILLA_MARINA_EN_METROS
    print(f"{millas_marinas} millas marinas equivalen a {metros} metros.")

except ValueError:
    print("Error: Debes introducir un número válido.")