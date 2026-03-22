def build_profile(first, last, **user_info): 
# 2 asterisco criam um dicionário 
# **kwargs usado para coletar argumentos nomeados
    """Retorna ao usuário o primeiro e o último nome em um dicionário"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', location='princeton',
field='physics')

print(user_profile)
