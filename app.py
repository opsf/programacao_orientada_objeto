from modelo.restaurante import Restaurante

restarante_comedere = Restaurante('Comedere', 'Goumert')
restaurante_pizza = Restaurante('Pizza', 'Italiana')
restarante_comedere.receber_avaliacao('Joao', 10)
restarante_comedere.receber_avaliacao('Bela',4)
restarante_comedere.receber_avaliacao('Clara',8)

def main():        
    Restaurante.lista_restaurantes()

if __name__ == '__main__':
    main()

