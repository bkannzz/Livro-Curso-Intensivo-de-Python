unconfirmed_users = ['alice', 'isabela', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop() # remove o último valor 

    print('Verifying user: {}'.format(current_user.title()))
    confirmed_users.append(current_user)

print('\nThe following users have been confirmed:')
for confirmed_user in confirmed_users:
    print(confirmed_user.title())