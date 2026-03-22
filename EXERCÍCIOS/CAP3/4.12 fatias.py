#EX 4.10 Fatias

sabores_pizzas = ['atum e queijos', 'calabresa', 'queijo', 'camarão',
'frango e queijo', 'frango catupiry e bacon', 'pepperoni']

print('Os três primeiros da lista são: {}'.format(sabores_pizzas[:3]))

print('Os três elementos que ficam no meio da lista são: {}'
.format(sabores_pizzas[2:5]))

print('Os três últimos elementos da lista são: {}'.format(sabores_pizzas[4:]))

#EX 4.11 Minhas pizzas, suas pizzas

sabores_pizzas = ['atum e queijos', 'calabresa', 'queijo']

friend_pizzas = sabores_pizzas[:]

sabores_pizzas.append('frango e queijo')
friend_pizzas.append('camarão')

print('\nMinhas pizzas favoritas são:')

for pizzas in sabores_pizzas:
    print(pizzas)

print('\nAs pizzas favoritas do meu amigo são:')
for pizzas in friend_pizzas:
    print(pizzas)

#EX 4.12 Mais loops

my_foods = ['pizza', 'falafel', 'carrot cake']
lista_animais = ['cachorro', 'gato', 'papagaio']

print('\nMinhas lista de comidas são: ')
for comidas in my_foods:
    print(comidas)

print('\nMinha lista de animais favoritos são:')
for animal in lista_animais:
    print(animal)