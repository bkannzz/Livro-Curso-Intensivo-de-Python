def make_pizza(*toppings): 
# 1 asterisco coloca todos os valores em um tupla
# *args coleta argumentos posicionais arbitrários
    """Retorna os ingredientes da pizza"""
    print('\nMaking a pizza with the following toppings:')
    for topping in toppings:
        print('- {}'.format(topping))

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

def make_pizza(size, *toppings): 
    """Retorna o tamanho e os ingredientes da pizza"""
    print('\nMaking a {}-inch pizza with the following toppings:'.format(size))
    for topping in toppings:
        print('- {}'.format(topping))

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')