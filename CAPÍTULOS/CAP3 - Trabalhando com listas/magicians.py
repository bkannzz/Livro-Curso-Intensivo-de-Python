magicians = ['alice', 'david', 'carolina']

for magician in magicians: # para cada mágico na lista de mágicos, exiba o nome
# do mágico
    print('{}, that was a great trick!'.format(magician.title()))
    print("i can't wait to see your next trick, {}.\n"
.format(magician.title()))
    print('Thank you, everyone. That was a great magic show!')
