#EX 5.8 Olá, admin

usuarios = ['admin', 'bka', 'kevin', 'snow', 'isinhe']

for users in usuarios:
    if users == 'admin':
        print('Olá administrador, gostaria de ver um relatório')
    else:
        print('Boas vindas {}!'.format(users))

#EX 5.9 Sem usuários

usuarios = []

if users in usuarios:
    for users in usuarios:
        print('Remova todos usuários da lista.')
else:
    print('É necessário encontrar alguns usuários!')


#EX 5.10 Verificando nomes de usuários

current_users = ['admin', 'bka', 'kevin', 'snow', 'isinhe', 'john']
new_users = ['alex', 'bka', 'peep', 'vivian', 'isinhe', 'johN']

current_users_lower = [user.lower() for user in current_users]

for user in new_users:
    if user.lower() in current_users_lower:
        print(f'Você precisa inserir outro nome de usuário, pois já existe.')
    else:
        print(f'Nome de usuário "{user}" está disponível.')

#EX 5.11 Números ordinais

numeros = [1,2,3,4,5,6,7,8,9]

for num in numeros:
    if num == 1:
        print('1th')
    elif num == 2:
        print('2th')
    elif num == 3:
        print('3th')
    elif num == 4:
        print('4th')
    elif num == 5:
        print('5th')
    elif num == 6:
        print('6th')
    elif num == 7:
        print('7th')
    elif num == 8:
        print('8th')
    else:
        print('9th')