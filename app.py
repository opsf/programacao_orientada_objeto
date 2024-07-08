from modelo.restaurante import Restaurante
from modelo.cardapio.bebida import Bebida
from modelo.cardapio.prato import Prato

restarante_comedere = Restaurante('Comedere', 'Goumert')
bebida_boa = Bebida('Leite', 5.00, 'grande')
prato_dia = Prato('Pastel', 4.00, 'melhor da cidade')
restarante_comedere.acionar_bebida_no_cardapio(bebida_boa)
restarante_comedere.acionar_prato_no_cardapio(prato_dia)
restarante_comedere.listar_cardapio()



def main():        
    print(bebida_boa)
    print(prato_dia)

if __name__ == '__main__':
    main()

