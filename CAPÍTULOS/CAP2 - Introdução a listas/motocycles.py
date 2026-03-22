motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles[0] = 'ducati' # modificar o item na lista
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.append('ducati') # adiciona um item na lista
print(motorcycles)

motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.insert(1, 'ducati') # adiciona itens em qualquer posição
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']

del motorcycles[0] # remover itens na lista
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']

popped_motorcycles = motorcycles.pop() # remove o último item da lista e 
# armazena em uma lista separada

print(motorcycles)
print(popped_motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']

first_owned = motorcycles.pop(0) # removendo um item de sua preferência
print('The first motorcycle I owned was a {}'.format(first_owned.title()))

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']

motorcycles.remove('ducati') # remover um item sem saber a posição, 
# então usamos o valor para remove-ló

print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print('\n {} is too expensive for me.'.format(too_expensive.title()))