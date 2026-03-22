requested_topping = 'mushrooms'

if requested_topping != 'anchovies': # != significa diferença entre os valores
    print('Hold the anchovies')

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print('Sorry, we are out of green peppers right now.')
    else:
        print('Adding {}.'.format(requested_topping))
print('\nFinished making your pizza!')

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni'
'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print('adding {}.'.format(requested_topping))
    else:
        print("sorry, we don't have {}.".format(requested_topping))

print('\nFinished making your pizza!')