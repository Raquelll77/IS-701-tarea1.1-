import random
import string


def generadorPassword(nDigitos):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    Password = ""
    for i in range(0, nDigitos):
        Password += random.choice(caracteres)
    print(f"El password es: {Password}")

print("Generador de Password")
nDigitos = int(input("Ingrese la longitud de su password: "))
generadorPassword(nDigitos)
        

