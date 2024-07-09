from modelo.cardapio.item_cardapio import ItemCardapio
class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome,preco)        
        self.descricao = descricao
    
    def __str__(self):
        print(f'NOME  |  PRECO   |  DESCRICAO')
        return f'{self._nome}  |  {self._preco}  | {self._descricao}'