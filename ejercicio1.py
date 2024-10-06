class Rectangulo:
    def __init__(self, base:float, altura:float):
        self.base = base
        self.altura = altura
     
    def area(self) -> float:
        return self.base*self.altura
    
    def perimetro(self) -> float:
        return (self.base + self.altura)*2
    

rectangulo = Rectangulo(5,3)
area = rectangulo.area()
perimetro = rectangulo.perimetro()

print(f"El area del rectangulo es de: {area}")
print(f"El perimetro del rectangulo es de: {perimetro}")