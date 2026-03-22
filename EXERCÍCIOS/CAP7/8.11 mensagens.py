#EX 8.9 Mensagens 

def show_messages(mensagens):
    for mensagem in mensagens:
        print(mensagem)

mensagem = ['HAHAHA', 'oii', 'te amo']
show_messages(mensagem)

#EX 8.10 Enviando mensagens

def show_messages(mensagens, enviar):
    while mensagens:
        captura_mensagem = mensagens.pop()
        print('Mensagem {} indo para nova lista...'.format(captura_mensagem))
        enviar.append(captura_mensagem)

def send_messages(enviar):
    for mensagem in enviar:
        print(mensagem)

mensagens = ['HAHAHA', 'oii', 'te amo']
enviar = []

show_messages(mensagens, enviar)
send_messages(enviar)

print(mensagens)
print(enviar)

#EX 8.11 Mensagens arquivadas

def show_messages(mensagens, enviar):
    while mensagens:
        captura_mensagem = mensagens.pop()
        print('Mensagem {} indo para nova lista...'.format(captura_mensagem))
        enviar.append(captura_mensagem)

def send_messages(enviar):
    for mensagem in enviar:
        print(mensagem)

mensagens = ['HAHAHA', 'oii', 'te amo']
enviar = []

show_messages(mensagens[:], enviar)
send_messages(enviar)

print(mensagens)
print(enviar)