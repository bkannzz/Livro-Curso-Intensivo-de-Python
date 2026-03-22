from city_functions import city_pais

def test_city_country():
    teste_city = city_pais('barueri', 'brasil')
    assert teste_city == 'Barueri, Brasil'

def test_city_country_population():
    teste_city = city_pais('barueri', 'brasil', '500 mil')
    assert teste_city == 'Barueri, Brasil 500 Mil'
