# está função mandará uma mensagem para cada nome que forcerem a ela

def greet_users(names):
    """Retorna uma mensagem para cada nome"""
    for name in names:
        msg = 'Hello, {}!'.format(name.title())
        print(msg)
    
usernames = ['hannah',  'ty', 'margot']
greet_users(usernames)