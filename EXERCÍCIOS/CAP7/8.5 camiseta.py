#EX 8.3 Camiseta

def make_shirt(tamanho, estampa):
    print('\nO tamanho da camisa que você escolheu é {}'.format(tamanho))
    print('É a sua estampa foi {}'.format(estampa))

make_shirt('M', 'BKA')
make_shirt(tamanho='G', estampa='BKA')

#EX 8.4 Camisetas grandes 

def make_shirt(tamanho='G', estampa='Eu amo python'):
    print('\nO tamanho da camisa que você escolheu é {}'.format(tamanho))
    print('É a sua estampa foi {}'.format(estampa))

make_shirt()
make_shirt(tamanho='M')
make_shirt(tamanho='P', estampa='BKA')

#EX 8.5 Cidades

def describe_city(cidade, pais='Brasil'):
    print('\nA cidade {} fica no pais {}'.format(cidade.title(), pais))

describe_city('barueri')
describe_city('osasco')
describe_city('nova york')