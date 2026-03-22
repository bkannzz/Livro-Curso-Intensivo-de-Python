players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[:4]) # corta elementos começando do 0 até o 3
print(players[2:]) # corta elementos começando do 0 até o 2
print(players[-3:])

players = ['charles', 'martina', 'michael', 'florence', 'eli']

print('Here are the first three players on my team:')
for player in players[:3]:
    print('-',player.title())