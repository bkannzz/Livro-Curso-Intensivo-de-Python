name = input('Please enter your name: ') # input = espera que o usuário 
#forneça algum dado para prosseguir.
print('\nHello, {}'.format(name))

prompt = ('If you share your name, we can personalize the messages ' \
'you see.')
prompt += '\nWhat is your first name? '

name = input(prompt)
print('\nHello, {}!'.format(name))

age = int(input(('How old are you? ')))
print(age)

