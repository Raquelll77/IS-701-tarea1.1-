def es_primo(n):
    if n < 2:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

a = int(input("Ingrese el número a comprobar: "))
if es_primo(a):
    print(f"{a} es un número primo.")
else:
    print(f"{a} no es un número primo.")