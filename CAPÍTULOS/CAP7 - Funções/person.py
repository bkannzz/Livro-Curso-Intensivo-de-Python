def build_person(first_name, last_name, age=None): # None e avaliado como False
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('rebecca', 'lobato', age=17)
print(musician)  