user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}
for key, value in user_0.items(): # items() retorna as sequências de pares 
#chave-valor que contém no dicionário  

    print('\nKey: {}'.format(key))
    print('value: {}'.format(value))

favorite_languages = {
    'jeh': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

for name, language in favorite_languages.items():
    print('{} favorite language is {}.'.format(name.title(), language.title()))

favorite_languages = {
    'jeh': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

for name in favorite_languages.keys(): # keys() exibe somente as chaves 
    print(name.title())

favorite_languages = {
    'jeh': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

friends = ['phil', 'sarah']

for name in favorite_languages.keys():
    print('Hi {}'.format(name.title()))
    if name in friends:
        language = favorite_languages[name].title()
        print('\t{}, I see you love {}!'.format(name.title(), language))

if 'erin' not in favorite_languages.keys():
    print('Erin, please take our poll!')

for name in sorted(favorite_languages.keys()): # ordena o dicionário em ordem
# alfabética
    print('{}, thanks you for taking the poll.'.format(name))

favorite_languages = {
    'jeh': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

print('The following languages have been mentioned: ')
for language in favorite_languages.values(): # values() exibe somente valores
    print(language.title())

for language in set(favorite_languages.values()): # set() é utilizado para 
# dicionários que contém valores duplicados, esses valores vão ser exibidos 
# uma vez apenas
    print(language.title())