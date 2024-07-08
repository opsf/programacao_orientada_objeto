from modelo.avaliacao import Avalicao
from modelo.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    restaurantes=[]
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)
    
    #def __str__(self):
       # return f'{self.nome} | {self.categoria}'
    
    @classmethod
    def lista_restaurantes(cls):        
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.media_avaliacao} | {restaurante.ativo}')

    @property
    def ativo(self):
        return  'ativado' if self._ativo else 'desativado'     
    
    def alterar_estado(self):
        self._ativo= not self._ativo
    
    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avalicao(cliente, nota)
        self._avaliacao.append(avaliacao)
    
    """
    @property
    def media_avaliacao(self):
        soma = 0
        quantidade = 0        
        for nota in self._avaliacao:
            soma = nota._nota + soma
            quantidade +=1
        media = round(soma/quantidade,1)
        return media
              
    @property
    def media_avaliacao(self):
        soma = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade = len(self._avaliacao)
        media = round(soma/quantidade,1)
        return media
    """
    
    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return 0
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media
    
    '''
    def acionar_bebida_no_cardapio(self,bebida):
        self._cardapio.append(bebida)
    
    def acionar_prato_no_cardapio(self,prato):
        self._cardapio.append(prato)
    '''
    
    def adicionar_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)
    
    def listar_cardapio(self):
        for cardapio in  self._cardapio:
            print(f'{cardapio._nome}')










