while True:
    try:
        numero = int(input("Introduce un número entre 0 y 99999: "))
        if 0 <= numero <= 99999:
            cifras = len(str(abs(numero)))
            print(f"El número {numero} tiene {cifras} cifras")
            break
        else:
            print("Error: El número debe estar entre 0 y 99999")
    except ValueError:
        print("Error: Debes introducir un número válido")