#EX 3.4 Lista de convidados

jantar = ['Isinhe', 'Heath Ledger', 'Lil Peep']

print(jantar)
print('você está sendo convidada para meu jantar {}'.format(jantar[0]))
print('você está sendo convidado para meu jantar {}'.format(jantar[1]))
print('você está sendo convidado para meu jantar {}'.format(jantar[2]))

#EX 3.5 Mudando a lista de convidados

jantar = ['Isinhe', 'Heath Ledger', 'Lil Peep']

print(jantar)
jantar[2] = 'Charlie Brown Jr'
print('\nvocê está sendo convidada para meu jantar {}'.format(jantar[0]))
print('você está sendo convidado para meu jantar {}'.format(jantar[1]))
print('você está sendo convidado para meu jantar {}'.format(jantar[2]))

print('\nO convidado Lil Peep não poderá comparecer.')

#EX 3.6 Mais convidados

jantar = ['Isinhe', 'Heath Ledger', 'Lil Peep']

jantar.insert(2, 'Donnie Darko')
jantar.insert(1, 'Angelina Jolie')
jantar.append('Brad Pitt')

print(jantar)

print('\nvocê está sendo convidada para meu jantar {}'.format(jantar[0]))
print('você está sendo convidada para meu jantar {}'.format(jantar[1]))
print('você está sendo convidado para meu jantar {}'.format(jantar[2]))
print('\nvocê está sendo convidado para meu jantar {}'.format(jantar[3]))
print('você está sendo convidado para meu jantar {}'.format(jantar[4]))
print('você está sendo convidado para meu jantar {}'.format(jantar[5]))

print('Encontrei uma mesa nova e consegui chamar mais pessoas')

#EX 3.7 Reduzindo a lista de convidados

jantar = ['Isinhe', 'Angelina Jolie', 'Heath Ledger', 'Donnie Darko', 
'Lil Peep', 'Brad Pitt']

print('Lamento por não poder convida-ló para o jantar {}'.format(jantar[5]))
jantar.pop()
print('Lamento por não poder convida-ló para o jantar {}'.format(jantar[4]))
jantar.pop()
print('Lamento por não poder convida-ló para o jantar {}'.format(jantar[3]))
jantar.pop()
print('Lamento por não poder convida-ló para o jantar {}'.format(jantar[2]))
jantar.pop()

print(jantar)
print('Para as pessoas que restaram, vocês ainda estão convidadas')

del jantar[1]
del jantar[0]

print(jantar)