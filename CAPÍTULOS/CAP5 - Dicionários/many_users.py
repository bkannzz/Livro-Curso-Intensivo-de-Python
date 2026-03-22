users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
    },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
    },
}

for username, user_info in users.items():
    print('\nUsername: {}'.format(username))
    full_name = f'{user_info['first']} {user_info['last']}'

    print('\tFull name: {}'.format(full_name.title()))
    print('\tLocation: {}'.format(user_info['location']))