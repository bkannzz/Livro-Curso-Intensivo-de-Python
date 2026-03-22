#EX 3.8 Conhecendo o mundo

lugares = ['anova york', 'bhollywood', 'ctokyo', 'dparis', 'ecanadá']

print(sorted(lugares))
print(lugares)

print(sorted(lugares, reverse=True)) # ordena em ordem alfabética inversa
print(lugares)

lugares.reverse()
print(lugares)
lugares.reverse()
print(lugares)

lugares.sort()
print(lugares)

lugares.sort(reverse=True)
print(lugares)

#EX 3.9 Convidando para o jantar

jantar = ['Isinhe', 'Heath Ledger', 'Lil Peep']

print(jantar)
print('você está sendo convidada para meu jantar {}'.format(jantar[0]))
print('você está sendo convidado para meu jantar {}'.format(jantar[1]))
print('você está sendo convidado para meu jantar {}'.format(jantar[2]))

print('\nestou convidando {} convidados'.format(len(jantar)))

jantar = ['Isinhe', 'Angelina Jolie', 'Heath Ledger', 'Donnie Darko',
'Lil Peep', 'Brad Pitt']

print('\nvocê está sendo convidada para meu jantar {}'.format(jantar[0]))
print('você está sendo convidada para meu jantar {}'.format(jantar[1]))
print('você está sendo convidado para meu jantar {}'.format(jantar[2]))
print('você está sendo convidado para meu jantar {}'.format(jantar[3]))
print('você está sendo convidado para meu jantar {}'.format(jantar[4]))
print('você está sendo convidado para meu jantar {}'.format(jantar[5]))

print('\nestou convidando {} convidados'.format(len(jantar)))

#EX 3.10 Funções

lista = ['montanhas', 'rios', 'países', 'cidades', 'idiomas']

print('possuímos nesta lista {} elementos'.format(len(lista)))

lista.reverse()
print(lista)

print(sorted(lista))
print(sorted(lista, reverse=True))

lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)

lista = ['montanhas', 'rios', 'países', 'cidades', 'idiomas']

lista[1] = 'riachos'
print(lista)

lista.append('isinhe')
print(lista)

lista.insert(2, 'brawl Stars')
print(lista)

del lista[0]
print(lista)

lista.pop()
print(lista)

lista.remove('riachos')
print(lista)

