cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw': # == significa igualdade entre os valores
        print(car.upper())
    else:
        print(car.title())

car = 'bmw'
print(car == 'bmw') # True

car = 'audi'
print(car == 'bmw') # False

car = 'audi'
print(car == 'Audi') # False

car = 'AUDI'
print(car.lower() == 'audi') # True