number = input('Enter a number, and I tell you if it even or odd: ')
number = int(number)

if number % 2 == 0: # descubrir se um número é par ou ímpar
    print('\nThe number {} is even'.format(number))
else:
    print('\nThe number {} is odd'.format(number))