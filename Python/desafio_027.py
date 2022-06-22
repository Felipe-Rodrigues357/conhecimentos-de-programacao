nome = input('Escreva seu nome completo: ')
primeironome = nome.split()[0]
ultimonome = nome.rsplit(' ', 1)[1]
print("""Nome Completo: {}
Primeiro Nome: {}
Último Nome: {}""".format(nome, primeironome, ultimonome))
""" OU
n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é: {}'.format(nome[0]))
print('Seu último nome é: {}'.format(nome[len(nome)-1])))
"""
