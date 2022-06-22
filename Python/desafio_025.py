nome = input('Digite seu nome: ')
if (nome.lower().find('silva')) != -1:
    resposta = 'SIM'
else:
    resposta = 'NÃO'
print('O seu nome possui Silva: {}'.format(resposta))
"""OU
nome = str(input('Qual o seu nome completo: ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))
"""
