#EX 9.4 Pessoas atendidas

class Restaurant: 
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print('As duas informações do restaurante são:')
        print('Nome do restaurante: {}'.format(self.name))
        print('Tipo de cozinha: {}'.format(self.type))

    def set_number_served(self, clientes):
        self.number_served = clientes

    def increment_number_served(self, pessoas):
        self.number_served += pessoas

    def open_restaurant(self):
        print('\nO restaurante está aberto!')
        print('O número de clientes atendidos são: {}'.format
(self.number_served))

restaurant = Restaurant('Isinhebekinhe', 'normal'.title())

restaurant.describe_restaurant()

restaurant.number_served = 15
restaurant.open_restaurant()

restaurant.set_number_served(20)
restaurant.open_restaurant()

restaurant.increment_number_served(130)
restaurant.open_restaurant()

#EX 9.5 Tentativas de login 

class User:
    def __init__(self, first_name, last_name, age, email):
        self.first = first_name
        self.last = last_name
        self.age = age
        self.email = email
        self.login_attempts = 0

    def increment_login_attempts(self, login):
        if login == 1:
            self.login_attempts += login
        else:
            print('não foi possível fazer isto!')

    def reset_login_attempts(self):
        self.login_attempts = 0

    def describe_user(self):
        print('\nAs suas informações são:')
        print('Primeiro nome: {}'.format(self.first))
        print('Seu segundo nome: {}'.format(self.last))
        print('Sua idade: {}'.format(self.age))
        print('Seu email: {}'.format(self.email))

    def greet_user(self):
        print('Seja bem vindo ao servidor {} {}'.format(self.first, self.last))
        print('O valor incrementado está em {}'.format(self.login_attempts))

user = User('Rebecca', 'Lobato', 17, 'rebeccagamer7@gmail.com')
user.describe_user()

user.increment_login_attempts(1)
user.increment_login_attempts(1)
user.increment_login_attempts(1)
user.increment_login_attempts(1)
user.increment_login_attempts(1)
user.greet_user()

user.reset_login_attempts()
user.greet_user()