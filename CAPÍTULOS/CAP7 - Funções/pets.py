# ARGUMENTOS POSICIONAIS
# Atribuimos somente os valores da função

def describe_pet(animal_type, animal_name):
    """Exibe as informações sobre um animal de estimação"""
    print('Eu tenho um {}'.format(animal_type))
    print('Meu {} seu nome é {}'.format(animal_type, animal_name.title()))
    
describe_pet('cachorro', 'kevin')

# ARGUMENTOS NOMEADOS 
# Atribuimos o nome e o valor da função

def describe_pet(animal_type, animal_name):
    """Exibe as informações sobre um animal de estimação"""
    print('\nEu tenho um {}'.format(animal_type))
    print('Meu {} o nome dele é {}'.format(animal_type, animal_name.title()))
    
describe_pet(animal_type='hamster', animal_name='harry')

# DEFAULT
# Caso não atribua o valor, receberá automaticamente o valor default

def describe_pet(animal_name, animal_type='dog'):
    """Exibe as informações sobre um animal de estimação"""
    print('\nEu tenho um {}'.format(animal_type))
    print('Meu {} o nome dele é {}'.format(animal_type, animal_name.title()))
    
describe_pet('harry')
