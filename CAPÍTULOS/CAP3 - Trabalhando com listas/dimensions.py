dimensions = (200, 50) # tuplas são imutáveis = valores que não podem ser 
#alterados durante seu programa

print(dimensions[0])
print(dimensions[1])

for dimension in dimensions:
    print(dimension)

print('\nOriginal dimension:')
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print('\nModified dimension:')
for dimension in dimensions:
    print(dimension)