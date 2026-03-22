alien_0 = {'color': 'green', 'speed': 'slow'}

point_value = alien_0.get('points', 'No point value assigned.') # get() exige
# uma chave como primeiro argumento. Como segundo argumento podemos passar um
# valor caso a chave não exista para exibir uma mensagem em vez de um erro.
print(point_value)