alien_0 = {'color': 'green', 'point': 5} #dicionários = coleção de chaves-valor

print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

new_points = alien_0['point']
print('You just earned {} points!'.format(new_points))

print(alien_0['color'])
print(alien_0['point'])

alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
alien_1 = alien_0['x_position']
print('Original position: {}'.format(alien_1))

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
alien_1 = alien_0['x_position']

print('New position: {}'.format(alien_1))

alien_0 = {'color': 'green', 'points': 5}

del alien_0['points'] # remover um par de chave-valor do dicionário

print(alien_0)