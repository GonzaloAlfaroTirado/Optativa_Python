try:
    altura = int(input("Introduce la altura: "))
    if altura <= 0:
        raise ValueError
except ValueError:
    print("Error: Debes introducir un número entero válido.")
else:
    medio = altura // 2

    for i in range(altura):
        
        if i <= medio:
            x = i
        else:
            x = altura - 1 - i
        print(" " * 2 * (medio - x), end="")
        print("*", end="")
        if x > 0:
            print(" " * (2 * x - 1) + "*")
        else:
            print()