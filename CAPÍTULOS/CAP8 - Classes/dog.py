class Dog: # criar uma classe
    """Simples tentativa de modelar um cachorro"""
    def __init__(self, name, age):
        """Inicializa os atributos de nome e idade"""
        self.name = name
        self.age = age  

    def sit(self): # método
        """Simula um cachorro sentado em resposta a um comando"""
        print('{} is now sitting.'.format(self.name))

    def roll_over(self): # método
        """Simula um cachorro rolando em resposta a um comando"""
        print('{} rolled over!'.format(self.name))

my_dog = Dog('Kevin', 6) # criar uma instância
your_dog = Dog('Lucy', 3)

print('My dog name is {}'.format(my_dog.name))
print('My dog is {} years old.'.format(my_dog.age))
my_dog.sit()

print('\nYour dog name is {}'.format(your_dog.name))
print('Your dog is {} years old.'.format(your_dog.age))
your_dog.sit()
