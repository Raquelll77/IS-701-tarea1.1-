def fibonacci(n):
    secuenciaF = [0,1]
    for i in range(2, n):
        siguiente = secuenciaF[-1] + secuenciaF[-2]
        secuenciaF.append(siguiente)
    return secuenciaF

n = int(input("Ingrese el número de términos: "))

print(f"Secuencia de Fibonacci:\n{fibonacci(n)}")    
