frase = input('Digite uma frase: ')
print('Sua frase possui {} letras A...'.format(frase.lower().count('a')))
print('O primeiro A aparece na {}ª letra... '.format(frase.lower().find('a')+1))
print('O último A aparece na {}ª letra... '.format(frase.lower().rfind('a')+1))

