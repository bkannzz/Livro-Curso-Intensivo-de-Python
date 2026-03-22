#EX 6.7 Pessoas 

isinhe = {
    'first': 'isabela',
    'last': 'lorrany',
    'age': 18,
    'location': 'barueri'
}

bekinhe = {
    'first': 'rebecca',
    'last': 'lobato',
    'age': 17,
    'location': 'barueri'
}

pessoa = {
    'first_name': 'roblox', 
    'last_name': 'freefire', 
    'age': 'todos', 
    'city': 'estados unidos'
}

peoples = [isinhe, bekinhe, pessoa]

for pessoa in peoples:
    print(pessoa)

#EX 6.8 Animais de estimação

kevin = {
    'animal': 'cachorro',
    'dono': 'rebecca'
}

snow = {
    'animal': 'cachorro',
    'dono': 'rebecca'
}

sofia = {
    'animal': 'cachorro',
    'dono': 'clara'
}

filinho = {
    'animal': 'gato',
    'dono': 'isabela'
}

pets = [kevin, snow, sofia, filinho]

for animais in pets:
    print(animais)

#EX 6.9 Lugares favoritos

favorite_places = {
    'isabela': ['paris','nova york', 'tokyo'],
    'rebecca': ['estados unidos', 'canadá'],
    'rayssa': ['tokyo']
}

for pessoa, lugar in favorite_places.items():
    print('Sou {} meu lugar favorito é:'.format(pessoa.title()))
    for lugares in lugar:
        print('\t{}'.format(lugares.title()))

#EX 6.10 Números favoritos

favorite_number = {
    'isabela': [17, 18, 19],
    'rebecca': [18, 19],
    'ryan': [20, 99],
    'lanny': [10],
    'vivian': [11]
}

for nome, numeros in favorite_number.items():
    print('\n{} meus números favoritos são:'.format(nome))
    for numero in numeros:
        print('{}'.format(numero))

#EX 6.11 Cidades

cidades = {
    'barueri': {
        'país': 'Brasil',
        'população': '316 mil habitantes',
        'fato': 'uma das cidades mais ricas do brasil'
    },

    'osasco': {
        'país': 'Brasil',
        'população': '756 mil habitantes',
        'fato': 'capital do cachorro-quente'
    },

    'cotia': {
        'país': 'Brasil',
        'população': '274 mil habitantes',
        'fato': 'nome cotia vem de um mamífero roedor indígena'
    }
}

for cidade, cidade_info in cidades.items():
    print('\nNome da cidade: {}'.format(cidade))
    print('país: {}'.format(cidade_info['país']))
    print('população é: {}'.format(cidade_info['população']))
    print('um fato: {}'.format(cidade_info['fato']))

#EX 6.12 Extensões

aliens = {
    'aliens_greens': [

    ],

    'aliens_reds': [

    ],

    'aliens_yellows': [

    ]
}

for alien_number in range(10):
    new_aliens = {
        'color': 'green', 
        'points': '5', 
        'speed': 'slow'}
    aliens['aliens_greens'].append(new_aliens)

for alien_number in range(10):
    new_aliens = {
        'color': 'red',
        'points': '15', 
        'speed': 'fast'}
    aliens['aliens_reds'].append(new_aliens)

for alien_number in range(10):
    new_aliens = {
        'color': 'yellow', 
        'points': '10', 
        'speed': 'medium'}
    aliens['aliens_yellows'].append(new_aliens)

print('\nALIENS VERDES:')
print(aliens['aliens_greens'])
print('\nALIENS VERMELHOS:')
print(aliens['aliens_reds'])
print('\nALIENS AMARELOS:')
print(aliens['aliens_yellows'])

print('\nTemos um total de aliens verdes: {}'.format
(len(aliens['aliens_greens'])))

print('Temos um total de aliens vermelhos: {}'.format
(len(aliens['aliens_reds'])))

print('Temos um total de aliens amarelos: {}'.format
(len(aliens['aliens_yellows'])))