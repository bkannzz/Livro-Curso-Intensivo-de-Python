#EX 9.6 Sorveteria

class Restaurant: 
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        print('As duas informações do restaurante são:')
        print('Nome do restaurante: {}'.format(self.name))
        print('Tipo de cozinha: {}'.format(self.type))

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['morango', 'açaí', 'limão', 'chocolate']

    def viewflavors(self):
        print('\nLista de sabores: {}'.format(self.flavors))

sorvete = IceCreamStand('bka', 'sorveteria'.title())
sorvete.describe_restaurant()
sorvete.viewflavors()

#EX 9.7 Admin

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

class Admin(User):
    def __init__(self, first_name, last_name, age, email):
        super().__init__(first_name, last_name, age, email)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        for num, privilegios in enumerate(self.privileges, start=1):
            print('{} - {}'.format(num, privilegios))

admin = Admin('Rebecca', 'Lobato', 17, 'rebeccagamer7@gmail.com')
admin.show_privileges()

#EX 9.8 Privilégios

class Admin(User):
    def __init__(self, first_name, last_name, age, email):
        super().__init__(first_name, last_name, age, email)
        self.privilegios = Privileges()

class Privileges:
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        for num, privilegios in enumerate(self.privileges, start=1):
            print('{} - {}'.format(num, privilegios))

admin = Admin('Rebecca', 'Lobato', 17, 'rebeccagamer7@gmail.com')
admin.privilegios.show_privileges()

#EX 9.9 Trocar bateria

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()
    
    def read_odometer(self):
        print('This car hes {} miles on it.'.format(self.odometer_reading))

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You cant roll back an odometer!')

    def increment_odometer(self, miles):
        if miles > 0:
            self.odometer_reading += miles
            print('increment in odometer {} miles! '.format(miles))
        else:
            print('You cant put that value in odometer!')

class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print('This car has a {}-kWh battery'.format(self.battery_size))

    def upgrade_battery(self):
        if self.battery_size < 65:
            self.battery_size = 65

    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print('This car can go about {} miles on a full charge.'.format(range))

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year) 
        self.battery = Battery()

    def fill_gas_tank(self):
        print('This car doesnt have a gas tank!')

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()

my_leaf.battery.upgrade_battery()
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()