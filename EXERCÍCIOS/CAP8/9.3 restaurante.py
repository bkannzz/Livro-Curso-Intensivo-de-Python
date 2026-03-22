#EX 9.1 Restaurante 

class Restaurant: 
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        print('As duas informações do restaurante são:')
        print('Nome do restaurante: {}'.format(self.name))
        print('Tipo de cozinha: {}'.format(self.type))

    def open_restaurant(self):
        print('\nO restaurante está aberto!')

restaurant = Restaurant('Isinhebekinhe', 'normal'.title())

restaurant.describe_restaurant()
restaurant.open_restaurant()

#EX 9.2 Três restaurantes

class Restaurant: 
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        print('\nAs duas informações do restaurante são:')
        print('Nome do restaurante: {}'.format(self.name))
        print('Tipo de cozinha: {}'.format(self.type))

    def open_restaurant(self):
        print('\nO restaurante está aberto!')

restaurant_1 = Restaurant('Isinhebekinhe', 'normal'.title())

restaurant_1.describe_restaurant()

restaurant_2 = Restaurant('Bekaray', 'diferente'.title())

restaurant_2.describe_restaurant()

restaurant_3 = Restaurant('inovazion', 'nova'.title())

restaurant_3.describe_restaurant()

#EX 9.3 Usuários

class User:
    def __init__(self, first_name, last_name, age, email):
        self.first = first_name
        self.last = last_name
        self.age = age
        self.email = email

    def describe_user(self):
        print('\nAs suas informações são:')
        print('Primeiro nome: {}'.format(self.first))
        print('Seu segundo nome: {}'.format(self.last))
        print('Sua idade: {}'.format(self.age))
        print('Seu email: {}'.format(self.email))

    def greet_user(self):
        print('Seja bem vindo ao servidor {} {}'.format(self.first, self.last))


user1 = User('Rebecca', 'Lobato', 17, 'rebeccagamer7@gmail.com')

user1.describe_user()
user1.greet_user()

user2 = User('Isabela', 'Lorrany', 18, 'isabelalorrany12@gmail.com')

user2.describe_user()
user2.greet_user()

user3 = User('Rayssa', 'Lobato', 10, 'rayssagamer1403@gmail.com')

user3.describe_user()
user3.greet_user()