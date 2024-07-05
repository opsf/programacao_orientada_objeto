class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

restarante_comedere = Restaurante('Comedere', 'Goumert')
restaurante_pizza = Restaurante('Pizza', 'Italiana')

print(restarante_comedere,restaurante_pizza)