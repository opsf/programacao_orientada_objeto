class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
    
    def __str__(self):
        return f'{self.nome} | {self.categoria}'
        
restarante_comedere = Restaurante('Comedere', 'Goumert')
restaurante_pizza = Restaurante('Pizza', 'Italiana')

print(restarante_comedere)
print(restaurante_pizza)
