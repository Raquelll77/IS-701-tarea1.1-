class Calculadora:
  def sumar(self, a, b):
    return a+b
  
  def restar(self, a, b):
    return a-b
  
  def multiplicar(self, a, b):
    return a*b
  
  def dividir(self, a, b):
    if b == 0:
      print("La division entre 0 no esta definida, pruebe con otro valor")
      return
    return a/b

calculo = Calculadora()

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

print(f"Suma: {calculo.sumar(a, b)}")
print(f"Resta: {calculo.restar(a, b)}")
print(f"Multiplicación: {calculo.multiplicar(a, b)}")
resultado_division = calculo.dividir(a, b)
if resultado_division is not None: 
    print(f"División: {resultado_division}")