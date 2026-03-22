#EX 7.1 Aluguel de carro

aluguel = input('Que tipo de carro você gostaria de alugar? ')
print('Vejamos se consigo encontrar um {} para você'.format(aluguel))

#EX 7.2 Reservas em restaurante

mesas = int(input('Quantos lugares você precisa? '))
if mesas >= 8:
    print('É necessário aguardar por uma mesa!')
else:
    print('A mesa já está disponível!')

#EX 7.3 Múltiplos de dez

numero = int(input('Informe um número: '))
if numero % 10 == 0:
    print('O número é múltiplo de DEZ')
else: 
    print('O número não é múltiplo de DEZ')