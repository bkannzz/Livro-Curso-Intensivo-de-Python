def city_pais(city, pais, population=''):
    if population:
        cidade_pais = f"{city}, {pais} {population}"
    else:
        cidade_pais = f"{city}, {pais}"
    return cidade_pais.title()