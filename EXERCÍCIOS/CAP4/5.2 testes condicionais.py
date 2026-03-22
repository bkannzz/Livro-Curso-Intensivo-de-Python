#EX 5.1 Testes condicionais

car = 'bmw'
print(car == 'bmw')

car = 'audi'
print(car == 'bmw')

car = 'mercedes'
print(car == 'mercedes')

car = 'porsche'
print(car == 'mercedes')

car = 'ferrari'
print(car == 'ferrari')

car = 'Volkswage'
print(car == 'porsche')

car = 'M2 coupe'
print(car == 'M2 coupe')

car = '911'
print(car == '910')

car = 'audi R9'
print(car == 'audi R9')

car = 'mercedes AMG'
print(car == 'mercedes amg')

#EX 5.2 Mais testes condicionais

car = 'Audi'
print(car == 'Audi')
print(car == 'audi')

car = 'M2 coupe'
print(car != 'M2 Coupe')
print(car != 'M2 coupe')
    
lista = ['JUSTIN BIEBER', 'KARATE KID']

for item in lista:
    if item == 'JUSTIN BIEBER':
        print(item.lower())
    else:
        print(item.title())

num_1 = 12
print(num_1 > 20)
print(num_1 < 20)
print(num_1 != 20)
print(num_1 <= 20)
print(num_1 >= 20)

nome_1 = 'rogerio'
nome_2 = 'sabrina'

print(nome_1 == 'rogerio' and nome_2 == 'carla')
print(nome_1 == 'rogerio' and nome_2 == 'sabrina')

print(nome_1 == 'rogerio' or nome_2 == 'carla')
print(nome_1 == 'rogeri' or nome_2 == 'sabrin')

cidades = ['barueri', 'osasco', 'carapicuiba']
print('barueri')
    
print('jandira' in cidades)

if 'aluminio' not in cidades:
    print('aluminio realmente não está na lista cidades')
print('barueri' not in cidades)