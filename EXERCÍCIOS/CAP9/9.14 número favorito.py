#EX 9.12 Relembrando o número favorito

from pathlib import Path
import json

def numero_existente(path):
    """se haver um número disponível ele o retornará"""
    if path.exists():
        conteudo = path.read_text()
        numero = json.loads(conteudo)
        return numero
    
def numero_novo(path):
    """Solicita um novo número"""
    numero = input('informe seu número favorito: ')
    contents = json.dumps(numero)
    path.write_text(contents)
    return numero

def relembrando_seu_numero():
    """Informa seu número favorito"""
    path = Path('EXERCÍCIOS/CAP9/numero_fav.json')
    numero = numero_existente(path)
    if numero:
        print('Seu número favorito você ja nos informou é: {}'.format(numero))
    else:
        numero = numero_novo(path)
        print('Lembrarei que seu número favorito é {}'.format(numero))

relembrando_seu_numero()

#EX 9.13 Dicionário do usuário

def get_stored_information(path):
    """Obtém as informações armazenadas, se disponível as retorna"""
    if path.exists():
        contents = path.read_text()
        informações = json.loads(contents)
        return informações
    else:
        return None

def get_new_information(path):
    """Solicita novas informações do usuário"""
    username = input('What is your name? ')
    age = input('What your age? ')
    city = input('Where your to live? ')
    informações = {'nome': username,
                    'idade': age, 
                    'cidade': city}

    contents = json.dumps(informações)
    path.write_text(contents)
    return informações

def greet_user():
    """Mostra as informações armazenadas"""
    path = Path('EXERCÍCIOS/CAP9/informações.json')
    informações = get_stored_information(path)
    if informações:
        print('suas informações são: {}'.format(informações))
    else:
        informações = get_new_information(path)
        print('Vou lembrar das suas informações, {}'.format(informações))

greet_user()

#EX 9.14 Verificando o usuário

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
    path = Path('EXERCÍCIOS/CAP9/usuário.json')
    username = get_stored_username(path)
    resposta = input('Esse é seu nome {} correto? '.format(username))
    if resposta == 's' or 'S':
        print('Bem vindo de volta, {}!'.format(username))
    else:
        username = get_new_username(path)
        print('Vou lembrar do seu nome, {}!'.format(username))

greet_user()
