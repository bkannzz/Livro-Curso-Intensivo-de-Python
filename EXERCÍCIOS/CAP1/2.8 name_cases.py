#EX 2.3 Mensagem pessoal

nome = 'isinhe'
print('Olá {}, gostaria de aprender um pouco de Python hoje?'.format(nome))

#EX 2.4 Maiúsculas e minúsculas

print(nome.lower())
print(nome.upper())
print(nome.title())

#EX 2.5 Citação famosa

print('Albert Einstein disse uma vez: "Uma pessoa que nunca cometeu um erro ' \
'nunca tentou nada de novo".')

#EX 2.6 Citação famosa 2

famous_person = 'Albert Einstein'
message = 'Uma pessoa que nunca cometeu um erro nunca tentou nada de novo'
print('{}: {}'.format(famous_person, message))

#EX 2.7 Removendo nomes

nome = '\trebecca\t'
print(nome)
print(nome.lstrip())
print(nome.rstrip())
print(nome.strip())

#EX 2.8 Extensões de arquivo

filename = 'python_notes.txt'
filename1 = filename.removesuffix('.txt')

print(filename1)