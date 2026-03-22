#EX 5.3 Cores de alienígina #1

alien_color = ['green', 'yellow', 'red']
coralien = 'green'

if coralien == 'green':
    print('Jogador acaba de ganhar 5 pontos')

alien_color = ['green', 'yellow', 'red']
coralien = 'yellow'

if coralien == 'green':
    print('Jogador acaba de ganhar 5 pontos')

#EX 5.4 Cores de alienígina #2

alien_color = ['green', 'yellow', 'red']
coralien = 'yellow'

if coralien == 'green':
    print('Jogador acaba de ganhar 5 pontos, por abrir fogo contra o alien')
else:
    print('Jogador acaba de ganhar 10 pontos.')

#EX 5.5 Cores de alienígina #3

alien_color = ['green', 'yellow', 'red']
coralien = 'red'

if coralien == 'green':
    print('Jogador acaba de ganhar 5 pontos, por abrir fogo contra o alien')
elif coralien == 'yellow':
    print('Jogador acaba de ganhar 10 pontos.')
elif coralien == 'red':
    print('Jogador acaba de ganhar 15 pontos.')
else:
    print('Essa cor de alien não existe, tente outra!')

#EX 5.6 Fases da vida

age = 4

if age < 2:
    print('Você é um neném.')
elif age < 4:
    print('Você é uma criança.')
elif age < 13:
    print('Você é um(a) garoto(a).')
elif age < 20:
    print('Você é um adolescente.')
elif age < 65:
    print('Você é um adulto.')
else:
    print('Você é um(a) idoso(a).')

#EX 5.7 Fruta favorita

favorite_fruits = ['fruta pinha', 'manga', 'morango']

if 'banana' in favorite_fruits:
    print('banana está na sua lista.')
if 'fruta pinha' in favorite_fruits:
    print('fruta pinha está na sua lista.')
if 'manga' in favorite_fruits:
    print('manga está na sua lista.')
if 'abacaxi' in favorite_fruits:
    print('abacaxi está na sua lista.')
if 'maracujá' in favorite_fruits:
    print('maracujá está na sua lista.')
