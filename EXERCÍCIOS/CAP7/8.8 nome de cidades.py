#EX 8.6 Nome de cidades

def city_country(cidade, pais):
    print('{}, {}'.format(cidade.title(), pais.title()))

city_country('barueri', 'brasil')
city_country('são paulo', 'brasil')
city_country(cidade='nova york', pais='estados unidos')

#EX 8.7 Álbum

def make_album(artista, álbum, numero=None):
    capa = {'artista': artista, 'título do álbum': álbum}
    if numero:
        capa['número de músicas'] = numero
    return capa

print(make_album('zé ibarra', 'AFIM', numero=8))
print(make_album('TV girl', 'French exit'))

#EX 8.8 Álbuns de usuários

def make_album(artista, álbum):
    capa = {'artista': artista, 'título do álbum': álbum}
    return capa

while True:
    print('(enter "sair" at any time to quit)')

    pessoa = input('artista: ')
    if pessoa == 'sair':
        break

    titulo = input('título do álbum: ')
    if titulo == 'sair':
        break

    capa_favorita = make_album(pessoa, titulo)
    print(capa_favorita)