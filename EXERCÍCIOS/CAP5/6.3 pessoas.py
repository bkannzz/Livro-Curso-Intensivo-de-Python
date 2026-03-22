#EX 6.1 Pessoas

pessoa = {'first_name': 'rebecca', 'last_name': 'lobato', 'age': 17, 'city':
'barueri'}

for key, value in pessoa.items():
    print('\nchave: {}'.format(key))
    print('valor: {}'.format(value))

#EX 6.2 Números favoritos

favorite_number = {'isabela': 18, 'rebecca': 17, 'ryan': 17, 'lanny': 17,
'vivian': 19}

for nome, idade in favorite_number.items():
    print('\nnome: {}'.format(nome))
    print('número favorito: {}'.format(idade))

#EX 6.3 Glossário

codigos = {'for': 'cria loopings', 
    'python': 'linguagem de programação.', 
    'listas': 'armazena valores e é podem ser alteradas ou melhor são mutáveis'
    '.',
    'tuplas': 'armazena valores como as listas porém são imutáveis.', 
    'hello world': 'significa primeiro passo em programação.'}

for codigo, significado in codigos.items():
    print('\ncódigo: {}'.format(codigo))
    print('significado: {}'.format(significado))