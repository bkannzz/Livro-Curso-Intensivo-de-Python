answer = 17

if answer != 42:
    print('That is not the correct answer. Please try again!')

age = 19
print(age < 21) # True
print(age <= 21) # True
print(age > 21) # False
print(age >= 21) # False

age_0 = 22
age_1 = 18

print(age_0 >= 22 and age_1 >= 18) # and significa que os dois valores tem   
# que ser igual ou maior que 22 e 18 para ser True

age_1 = 22

print(age_0 >= 21 and age_1 >= 21)

age_0 = 22
age_1 = 18

print(age_0 >= 21 or age_1 >= 21) # or significa que um dos dois valores pode
# ser igual ou maior que 21 pra ser True

age_0 = 18

age_0 = 22
age_1 = 18

print(age_0 >= 21 or age_1 >= 21)

requested_toppings = ['mushroom', 'onions', 'pineapple']
print('mushroom' in requested_toppings) # in verifica se o valor está na lista
print('pepperoni' in requested_toppings)

