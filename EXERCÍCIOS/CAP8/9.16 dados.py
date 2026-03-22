#EX 9.13 Dados

from random import randint, choice, sample

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print('O número tirado é: {}'.format(randint(1, self.sides)))

dado = Die()
dado.roll_die()

#EX 9.14 Loteria

sorte = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'r', 'l', 'b', 'c', 'i']
bilhete1 = []

while len(bilhete1) < 4:
    bilhete1.append(choice(sorte))
        
print('Os números do seu bilhete são: {}'.format(bilhete1))

#EX 9.15 Análise de loteria

sorte = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'r', 'l', 'b', 'c', 'i']
bilhete2 = []
my_ticket = []
tentativas = 0

while len(bilhete2) < 4:
    bilhete2.append(choice(sorte))
print('O bilhete do prêmio é: {}'.format(bilhete2))

while my_ticket != bilhete2:
    my_ticket = []
    while len(my_ticket) < 4:
        my_ticket.append(choice(sorte))
    tentativas += 1

print('Os números do seu bilhete são: {}'.format(my_ticket))
print('Número de tentativas foi {} para ganhar o bilhete'.format(tentativas))