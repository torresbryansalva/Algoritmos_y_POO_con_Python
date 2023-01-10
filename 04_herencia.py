class rectangulo:
    def __init__(self,altura,base):
        self.altura=altura
        self.base=base

    def area(self):
        return self.base*self.altura

class cuadrado(rectangulo):
    
    def __init__(self, altura):
        super().__init__(altura,altura)

rectangulo=rectangulo(4,5)
print(rectangulo.area())

cuadrado=cuadrado(4)
print(cuadrado.area())
