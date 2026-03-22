current_number = 0
while current_number <= 10: # enquanto a variável current_numnber for menor que
# 5 ela vai ser repetida até chegar ao 5
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)