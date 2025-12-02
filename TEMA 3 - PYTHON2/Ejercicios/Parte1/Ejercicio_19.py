saldo = 1000

while True:
    print("\nBienvenido a su Cajero Virtual")
    print("1. Ingresar dinero en cuenta")
    print("2. Retirar dinero de la cuenta")
    print("3. Salir")
    
    opcion = input("\nElija una opción: ")
    
    if opcion == '1':
        ingreso = float(input("Cantidad a ingresar: $"))
        if ingreso > 0:
            saldo += ingreso
            print(f"Su nuevo saldo es: ${saldo:.2f}")
        else:
            print("Por favor ingrese una cantidad válida")
            
    elif opcion == '2':
        retiro = float(input("Cantidad a retirar: $"))
        if retiro > 0:
            if retiro <= saldo:
                saldo -= retiro
                print(f"Su nuevo saldo es: ${saldo:.2f}")
            else:
                print("Saldo insuficiente")
        else:
            print("Por favor ingrese una cantidad válida")
            
    elif opcion == '3':
        print("Gracias por utilizar nuestro cajero. ¡Hasta pronto!")
        break
        
    else:
        print("Opción no válida. Por favor seleccione 1, 2 o 3")