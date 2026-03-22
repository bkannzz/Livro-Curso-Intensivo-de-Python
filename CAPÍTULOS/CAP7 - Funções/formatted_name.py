def get_formatted_name(first_name, last_name, middle_name=''):
    """Retorna um nome completo, elegantemente formatado."""
    if middle_name:
        full_name = ('{} {} {}'.format(first_name, last_name, middle_name))
    else:
        full_name = ('{} {}'.format(first_name, last_name))
    return full_name.title()

musician = get_formatted_name('rebecca', 'lobato')
print(musician)

musician = get_formatted_name('rebecca', 'lobato', 'simeão')
print(musician)