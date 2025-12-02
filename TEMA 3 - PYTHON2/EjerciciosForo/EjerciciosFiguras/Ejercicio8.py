'''
Imprime un rombo sólido de altura 2n-1, centrado, usando asteriscos.

Figura para n=4:

   *
  ***
 *****
*******
 *****
  ***
   *
'''
def rombo():
    try:
        altura = int(input("Introduce la altura: "))
        if altura <= 0 or altura % 2 == 0:
            raise ValueError
    except ValueError:
        print("Error: Debes introducir un número positivo")
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
                relleno = "*" * (2 * x - 1)
                print(relleno + "*")
            else:
                print()
rombo()