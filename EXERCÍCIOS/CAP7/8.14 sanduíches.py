#EX 8.12 Sanduíches

def montar_sanduiche(*ingredientes):
    print('\nMontando o sanduíche com os seguintes ingredientes:')
    for ingrediente in ingredientes:
        print('- {}'.format(ingrediente.title()))

montar_sanduiche('presunte', 'queijo', 'peito de peru')

#EX 8.13 Perfil de usuário

def build_profile(first, last, **user_info): 
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('rebecca', 'lobato', localização='barueri',
idade=16, país='brasil')

print(user_profile)

#EX 8.14 Carros

def inf_carros(fab, model, **descrição):
    descrição['fabricante'] = fab
    descrição['modelo'] = model
    return descrição

meu_modelo = inf_carros('BMW', 'M2 coupe', cor='azul claro')

print(meu_modelo)