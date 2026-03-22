#EX 4.3 Contando até Vinte

numeros = []
for numero in range(1, 21):
    numeros.append(numero)
    
print(numeros)

#EX 4.4 Um milhão

milhao = []
for numero in range(1, 1000001):
    milhao.append(numero)
print(milhao)

#EX 4.5 Somando um milhão

milhao = []
for numero in range(1, 1000001):
    milhao.append(numero)
print(milhao)

print(max(milhao))
print(min(milhao))
print(sum(milhao))

#EX 4.6 Números ímpares

even_numbers = list(range(1, 21, 2))
print(even_numbers)

for impares in even_numbers:
    print(impares, end=' ')

#EX 4.7 Três

multiplos_tres = list(range (3, 31, 3))
print('\n')
print(multiplos_tres)

for tres in multiplos_tres:
    print(tres, end=' ')
print('\n')

#EX 4.8 Cubos

cubos = []

for cubo in range(1, 11):
    cubos.append(cubo**3)
    print(cubo**3, end=' ')
print('\n')

#EX 4.9 Cube Comprehension

cubo = [valor**3 for valor in range(1, 11)]
print(cubo)