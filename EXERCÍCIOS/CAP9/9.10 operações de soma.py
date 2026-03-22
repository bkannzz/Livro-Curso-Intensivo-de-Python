#EX 9.6 Operações de soma 

valor_1 = input('forneça um valor: ')
valor_2 = input('forneça o segundo valor: ')

try:
    soma = int(valor_1) + int(valor_2)
except ValueError:
    print('Digite um número!')
else:
    print('A soma dos valores é: {}'.format(soma))

#EX 9.7 Calculadora de soma

while True:
    valor_1 = input('forneça um valor: ')
    if valor_1 == 's':
        break

    valor_2 = input('forneça o segundo valor: ')
    if valor_2 == 's':
        break

    try:
        soma = int(valor_1) + int(valor_2)
    except ValueError:
        print('Digite um número!')
    else:
        print('A soma dos valores é: {}'.format(soma))

#EX 9.8 Gatos e cachorros

from pathlib import Path

def exibir_arq(caminho):
    try:
        conteúdo = caminho.read_text()
    except FileNotFoundError:
        print('Este arquivo: {} não foi encontrado!\n'.format(caminho))
    else:
        print('Arquivo encontrado: {}'.format(caminho))
        print('Nele tem: {}\n'.format(conteúdo))

arquivos = ['EXERCÍCIOS/CAP9/cats.txt', 'EXERCÍCIOS/CAP9/dogs.txt']

for arquivo in arquivos:
    path = Path(arquivo)
    exibir_arq(path)

#EX 9.9 Gatos e cachorros sem acusar os erros

def exibir_arq(caminho):
    try:
        conteúdo = caminho.read_text()
    except FileNotFoundError:
        pass
    else:
        print('Arquivo encontrado {}'.format(caminho))
        print('Nele tem: {}\n'.format(conteúdo))

arquivos = ['EXERCÍCIOS/CAP9/cats.txt', 'EXERCÍCIOS/CAP9/dogs.txt']

for arquivo in arquivos:
    path = Path(arquivo)
    exibir_arq(path)