USUARIO_CORRECTO = "admin"
CONTRASENA_CORRECTA = "1234"

usuario = input("Ingrese nombre de usuario: ")
contrasena = input("Ingrese contraseña: ")

if usuario == USUARIO_CORRECTO and contrasena == CONTRASENA_CORRECTA:
    print("Inicio de sesión correcto")
elif usuario != USUARIO_CORRECTO:
    print("Nombre de usuario incorrecto")
else:
    print("Contraseña incorrecta")