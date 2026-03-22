print('Me forneça dois valores para eu dividir!')
print('Insira q para sair.')

while True:

    first_number = input('\nPrimeiro número: ')
    if first_number == 'q':
        break

    second_number = input('Segundo número: ')
    if first_number == 'q':
        break

    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print('You cant divide by 0!')
    else:
        print(answer)