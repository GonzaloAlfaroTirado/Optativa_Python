"""
Imprime un diamante hueco de altura total 2n - 1, centrado con asteriscos, donde solo se imprimen los bordes y el centro.

Figura para n=5:

    *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *
 
"""
def diamante():
    try:
        altura = int(input("Introduce la altura: "))
        if altura <= 0 or altura % 2 == 0:
            raise ValueError
        
    except ValueError:
        print("Error: Debes introducir un número entero positivo.")
    else:
        medio = altura // 2

        for i in range(altura):
            if i <= medio:
                x = i
            else:
                x = altura - 1 - i

            print(" " * (medio - x), end="")

            print("*", end="")
            
            if x > 0:
                espacios_internos = " " * (2 * x - 1)
                print(espacios_internos + "*")
            else:
                print()

diamante()