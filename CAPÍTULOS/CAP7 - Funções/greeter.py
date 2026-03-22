def greet_user(username): # definindo uma função
    print('Hello, {}!'.format(username.title()))

greet_user('jesse')
greet_user('sarah')

def get_formatted_name(first_name, last_name):
    """Retorna um nome completo, elegantemente formatado."""
    full_name = ('{} {}'.format(first_name, last_name))
    return full_name.title()

while True:
    print('\nPlease tell me your name:')
    print('(enter "q" at any time to quit)')

    f_name = input('first name: ')
    if f_name == 'q':
        break

    l_name = input('last name: ')
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print('\nHello, {}!'.format(formatted_name))