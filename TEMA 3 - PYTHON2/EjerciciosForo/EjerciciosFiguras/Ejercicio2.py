altura = int(input("Introduce la altura del triángulo: "))

print(f"--- Triángulo Hueco de altura {altura} ---")

for i in range(1, altura + 1):
    if i == 1:
        print("4")
    elif i == altura:
        print("4" * i)
    else:
        print("4" + " " * (i - 2) + "4")