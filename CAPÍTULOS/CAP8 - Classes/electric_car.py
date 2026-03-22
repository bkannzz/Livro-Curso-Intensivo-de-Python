from car1 import Car

class Battery:
    """Simples tentativa de modelar uma bateria para um carro elétrico"""
    def __init__(self, battery_size=40):
        """Inicializa os atributos da bateria"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Exibe uma frase descrevendo o tamanho da bateria"""
        print('This car has a {}-kWh battery'.format(self.battery_size))

    def get_range(self):
        """Exibe frase sobre a distância que o carro percorre com essa bateria
        """
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print('This car can go about {} miles on a full charge.'.format(range))



class ElectricCar(Car):
    """Representa aspectos de um carro, específicos para veiculos elétricos"""

    def __init__(self, make, model, year):
        """
        Inicializa os atributos da classe-pai.
        Em seguida, inicializa os atributos específicos para um carro elétrico
        """
        super().__init__(make, model, year) # super origina chamar a classe-pai
# em superclasse e a classe-filha em subclasse
        self.battery = Battery()

    def fill_gas_tank(self):
        """Carros elétricos não tem tanques de gasolina"""
        print('This car doesnt have a gas tank!')