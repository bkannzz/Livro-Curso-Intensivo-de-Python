class Car:
    """Simples tentativa de representar um carro"""
    def __init__(self, make, model, year):
        """Inicializa os atributos para descrever um carro"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """"Retorna um nome descritivo, formatado elegantemente"""
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()
    
    def update_odometer(self, mileage):
        """
        Define a leitura do hodômetro para o valor fornecido,
        Rejeita a alteração se houver tentativas de reverter o hodômetro.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You cant roll back an odometer!')

    def increment_odometer(self, miles):
        """Adiciona a quantidade fornecida á leitura do hodômetro"""
        if miles > 0:
            self.odometer_reading += miles
            print('increment in odometer {} miles! '.format(miles))
        else:
            print('You cant roll back an add in odometer')

    def read_odometer(self):
        """Exibe uma frase mostrando a quilometragem do carro, em milhas"""
        print('This car hes {} miles on it.'.format(self.odometer_reading))

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

# Alterando o valor do atributo diretamente:

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# Alterando o valor do atributo por meio de um método:

#   def update_odometer(self, mileage):
#       """"Define a leitura do hodômetro para o valor fornecido"""
#       self.odometer_reading = mileage

my_new_car.update_odometer(1)
my_new_car.read_odometer()

# Incrementando o valor de um atributo por meio de um método:

#   def increment_odometer(self, miles):
#       """Adiciona a quantidade fornecida á leitura do hodômetro"""
#       self.odometer_reading += miles

my_used_car = Car('subaru', 'outback', 2019)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()