"""

Imprime una estrella de ocho puntas combinando líneas verticales, horizontales y diagonales con asteriscos en una matriz de tamaño impar n x n (ej. 9x9).

Figura para n=9:

*   *   *
 *  *  *
  * * *
*********
  * * *
 *  *  *
*   *   *

"""
def estrella_ocho_puntas():
    try:
        altura = int(input("Introduce un tamaño impar para la estrella (n x n): "))
        if altura <= 0 or altura % 2 == 0:
            raise ValueError
    except ValueError:
        print("Error: Debes introducir un número entero positivo impar.")
    else:
        medio = altura // 2

    for i in range(altura):
        for j in range(altura):
            if i == medio or j == medio or i == j or i + j == altura - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
estrella_ocho_puntas()