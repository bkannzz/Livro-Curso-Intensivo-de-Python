#EX 9.4 Convidados

from pathlib import Path

path = Path('EXERCÍCIOS/CAP9/guest.txt')
nome = input('escreva seu nome: ')

path.write_text(nome)

#EX 9.5 Livros de convidados

path = Path('EXERCÍCIOS/CAP9/guest_book.txt')

contents = ''

while True:
    nome = input('Escreva seu nome: ')
    
    if nome == 'exit':
        break
    
    contents += nome + '\n'

path.write_text(contents)