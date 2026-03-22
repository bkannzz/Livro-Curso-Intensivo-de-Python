prompt = '\nPlease enter the name of a city you have visited: '
prompt += '\n(Enter quit when you are finished.)'

while True:
    city = input(prompt)
    if city == 'quit':
        break # faz parar o programa imediatamente
    else:
        print('I love to go to {}!'.format(city.title()))