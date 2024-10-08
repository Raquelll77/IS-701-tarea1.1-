def tablaMultiplicar(n):
    print(f"La tabla del {n} es: ")
    for i in range(1, 11):
        print(f"{n} x {i} = {(n*i)}")


n = int(input("Ingrese un número entero: "))

tablaMultiplicar(n)