class Restaurante:
    restaurantes=[]
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)
    
    #def __str__(self):
       # return f'{self.nome} | {self.categoria}'
    
    def lista_restaurantes():        
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')
         
        
restarante_comedere = Restaurante('Comedere', 'Goumert')
restaurante_pizza = Restaurante('Pizza', 'Italiana')

Restaurante.lista_restaurantes()
