pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}

print('You ordened a {}-crust pizza with the ' \
'following tippings:'.format(pizza['crust']))

for topping in pizza['toppings']:
    print('\t{}'.format(topping))
    
favorite_languages = {
    'jeh': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell']
}

for name, languages in favorite_languages.items():
    print(f'\n{name.title()}s favorite languages are:')
    for language in languages:
        print(f'\t{language.title()}')