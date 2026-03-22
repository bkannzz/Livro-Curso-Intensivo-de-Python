from pathlib import Path
import json

def get_stored_username(path):
    """Obtém o nome de usuário armazenado, se disponível o retorna"""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def get_new_username(path):
    """Solicita um novo nome de usuário"""
    username = input('What is your name? ')
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    """Cumprimenta o usuário pelo nome."""
    path = Path('CAPÍTULOS/files_and_exceptions_cap9/username.json')
    username = get_stored_username(path)
    if username:
        print('Welcome back, {}!'.format(username))
    else:
        username = get_new_username(path)
        print('Well remember you when you come back, {}!'.format(username))

greet_user()