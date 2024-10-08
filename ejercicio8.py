def contarVocales(frase:str):
    contador=0
    for i in range(0, len(frase)):
        if frase[i] in 'aeiou':
            contador+=1
    print(f"La palabra ingresada tiene {contador} vocales")



frase = input("Ingrese una frase: ")
contarVocales(frase)
