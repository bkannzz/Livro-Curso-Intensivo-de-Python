#EX 7.8 Lanchonete 

sandwich_ordens = ['presunto e queijo', 'hambúrguer', 'calabresa'] 
finish_sandwich = []

while sandwich_ordens:
    request_sandwich = sandwich_ordens.pop()

    print('Seu lanche de {} está pronto'.format(request_sandwich))
    finish_sandwich.append(request_sandwich)

print('TODOS OS SANDWICHS PREPARADOS:')
for number, sandwich in enumerate(finish_sandwich, start=1):
    print('O número do seu pedido é {}, do sabor {}'.format(number, sandwich))

#EX 7.9 Sem pastrami

sandwich_ordens = ['pastrami', 'presunto e queijo', 'hambúrguer', 'calabresa'
'pastrami', 'pastrami'] 
finish_sandwich = []

print('ESTAMOS SEM SANDWICH DE PASTRAMI!')

while 'pastrami' in sandwich_ordens:
    sandwich_ordens.remove('pastrami')

while sandwich_ordens:
    request_sandwich = sandwich_ordens.pop()

    print('Seu lanche de {} está pronto'.format(request_sandwich))
    finish_sandwich.append(request_sandwich)

print('TODOS OS SANDWICHS PREPARADOS:')
for number, sandwich in enumerate(finish_sandwich, start=1):
    print('O número do seu pedido é {}, do sabor {}'.format(number, sandwich))

#EX 7.10 Férias tão sonhadas

pesquisa = {}

pesquisa_ativa = True

while pesquisa_ativa:
    lugar = input('Se pudesse visitar qualquer lugar do mundo, para onde' \
    ' iria? ')

    pesquisa[lugar] = lugar

    repetição = input('Outra pessoa gostaria de responder? (sim/não) ')
    if repetição == 'não':
        pesquisa_ativa = False

print('\n--- PESQUISAS ---')
for lugar in pesquisa:
    print('suas férias do sonho seria em {}'.format(lugar))