def calcular_matricula_universidad_interactivo():
    facultades_info = {
        "ing. de sistemas": {"importe": 350.00, "mensualidad": 650.00},
        "derecho": {"importe": 300.00, "mensualidad": 550.00},
        "ing. naviera": {"importe": 300.00, "mensualidad": 500.00},
        "ing. pesquera": {"importe": 310.00, "mensualidad": 460.00},
        "contabilidad": {"importe": 280.00, "mensualidad": 490.00},
        "administración": {"importe": 360.00, "mensualidad": 520.00},
    }

    nombre_postulante = input("Introduzca el nombre del postulante: ")
    facultad_input = input("Introduzca la facultad que va a estudiar (ej: Ing. de Sistemas, Derecho): ").lower()

    print(f"\n--- Costos de Matrícula para {nombre_postulante} ---")
    
    if facultad_input in facultades_info:
        data = facultades_info[facultad_input]
        importe_matricula = data["importe"]
        mensualidad = data["mensualidad"]
        
        base_imponible = importe_matricula + mensualidad
        igv_tasa = 0.18
        igv_monto = base_imponible * igv_tasa
        monto_final = base_imponible + igv_monto

        print(f"Facultad: {facultad_input.title()}")
        print(f"Importe de Matrícula: {importe_matricula:.2f}")
        print(f"Mensualidad: {mensualidad:.2f}")
        print(f"IGV 18% (sobre el total): {igv_monto:.2f}")
        print(f"Monto Final a Pagar: {monto_final:.2f}")
    else:
        print(f"Error: La facultad '{facultad_input.title()}' no se encuentra en la lista de categorías.")
        print("Facultades disponibles: " + ", ".join([f.title() for f in facultades_info.keys()]))

calcular_matricula_universidad_interactivo()