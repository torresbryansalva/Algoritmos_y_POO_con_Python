class lavadora:

    def _init__(self):
        pass
    
    #metodo publico
    def lavar(self,temperatura='frio'):
        self._llenar_tanque_agua(temperatura)
        self._anadir_jabon()
        self._lavar()
        self._centrifugar()

    #metodos privados
    def _llenar_tanque_agua(self,temperatura):
        print(f'Llenando el tanque con agua {temperatura}')
    
    def _anadir_jabon(self):
        print('añadiendo el jabon')

    def _lavar(self):
        print('Lavando la ropa')

    def _centrifugar(self):
        print('Centrifugando la ropa')    
        
if __name__=='__main__':
    lavadora=lavadora()
    lavadora.lavar()