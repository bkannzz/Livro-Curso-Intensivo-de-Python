#EX 7.4 Ingredientes de pizza

pizza = '\nInforme algum ingrediente para sua pizza: '
pizza += '\n(Escreva PARE quando tiver terminado. )'

while True:
    ingrediente = input(pizza)
    if ingrediente == 'pare' or 'PARE':
        break
    else:
        print('{} está sendo adicionado em sua pizza!'.format(ingrediente))

#EX 7.5 Ingressos de cinema

idade = ('\nInforme sua idade: ')
idade += ('\nPara sair digite 0 ')
idade += ('\nidade: ')

while True:
    ingresso = int(input(idade))
    if ingresso == 0:
        break 
    elif ingresso < 3:
        print('O ingresso do cinema é gratuito')
    elif ingresso <= 12:
        print('Você paga U$S10')
    else:
        print('Você paga U$S15')

#EX 7.6 Três saídos 

pizza = '\nInforme algum ingrediente para sua pizza: '
pizza += '\n(Escreva PARE quando tiver terminado. )'
pizza += '\nIngrediente: '

active = True

while active:
    ingrediente = input(pizza)
    if ingrediente == 'PARE' or 'pare':
        active = False
        break
    else:
        print('{} está sendo adicionado em sua pizza!'.format(ingrediente))

#EX 7.7 Infinito

x = 1
while x <= 5:
    print(x)