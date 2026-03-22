#EX 6.4 Glossário 2

codigos = {'for': 'cria loopings', 
    'python': 'linguagem de programação.', 
    'listas': 'armazena valores e é podem ser alteradas ou melhor são mutáveis'
    '.',
    'tuplas': 'armazena valores como as listas porém são imutáveis.', 
    'hello world': 'significa primeiro passo em programação.',
    '#': '# são comentários que podemos fazer para ajudar a ler o código.',
    'strings': 'tipo primitivo que armazena variáveis que contém letras.',
    'int': 'tipo primitivo que armazena variáveis que contém números.',
    'float': 'tipo primitivo que armazena variáveis que contém números reais.',
    'boolean': 'tipo primitivo que armazena verdadeiro ou falso.'
    }
    
for codigo, significado in codigos.items():
    print('\ncódigo: {}'.format(codigo))
    print('significado: {}'.format(significado))

#EX 6.5 Rios 

rios = {'nilo': 'egito', 'amazonas': 'brasil', 'yangtzé': 'china'}

for rio, pais in rios.items():
    print('\nO rio {} atravessa o {}'.format(rio.title(), pais.title()))
for rio in rios.keys():
    print('\n',rio)
for pais in rios.values():
    print('\n',pais)

#EX 6.6 Pesquisa

favorite_languages = {
    'jeh': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

novas_pessoas = ['isabela', 'sarah', 'rebecca', 'phil', 'lyan', 'vivian']

for nome in novas_pessoas:
    if nome not in favorite_languages:
        print('Convido você a participar da pesquisa {}'.format(nome.title()))
    elif nome in favorite_languages: 
        print('Obrigada pela resposta {}'.format(nome.title()))