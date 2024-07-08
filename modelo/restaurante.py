from modelo.avaliacao import Avalicao

class Restaurante:
    restaurantes=[]
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
    
    #def __str__(self):
       # return f'{self.nome} | {self.categoria}'
    
    @classmethod
    def lista_restaurantes(cls):        
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return  'ativado' if self._ativo else 'desativado'     
    
    def alterar_estado(self):
        self._ativo= not self._ativo
    
    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avalicao(cliente, nota)
        self._avaliacao.append(avaliacao)
    






