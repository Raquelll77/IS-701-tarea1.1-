from random import Random

randon = Random()
randon.seed()

a = randon.randint(1,100)
nUsuario = None
contador = 0

print("¡Adivina el número entre 1 y 100!")

while(nUsuario != a):
    nUsuario = int(input("Ingresa tu intento: "))

    if(nUsuario < a):
        print("El número es mayor")

    elif(nUsuario > a):
        print("El número es menor")

    contador+=1

print(f"¡Felicitaciones! Has adivinado el número en {contador} intentos.")

