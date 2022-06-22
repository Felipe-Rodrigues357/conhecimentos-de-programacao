palavras = ('aprender', 'programar', 'jedi', 'anakin', 'skywalker',
            'kenobi', 'curso', 'video', 'gratis', 'dooku', 'yoda',
            'star', 'wars', 'sith', 'maul', 'ben', 'solo')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ',end = '')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
