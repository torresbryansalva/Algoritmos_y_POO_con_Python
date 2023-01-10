class Cordenadas:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def distancia(self,otraCoordenada):
        x_diff=(self.x-otraCoordenada.x)**2
        y_diff=(self.y-otraCoordenada.y)**2

        return (x_diff + y_diff)**0.5

if __name__=='__main__':
    coord1=Cordenadas(10,20)
    coord2=Cordenadas(30,60)
    
    print(coord1.distancia(coord2))
