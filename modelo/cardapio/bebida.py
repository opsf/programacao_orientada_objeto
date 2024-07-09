from modelo.cardapio.item_cardapio import ItemCardapio
class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self.tamanho = tamanho
        
    def __str__(self):
        print(f'NOME  |  PRECO  | TAMANHO'   )
        return f'{self._nome}  |  {self._preco}  | {self._tamanho}'