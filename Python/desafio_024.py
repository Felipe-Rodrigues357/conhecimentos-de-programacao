cidade = input('Escreva qual a sua cidade: ')
if (cidade[:5].lower().find('santo')) != -1:
    resposta = 'SIM'
else:
    resposta = 'NÃO'
print('A cidade informada começa com santo: {}'.format(resposta))
"""OU:
cidade = str(input('Em que cidade você nasceu: ')).strip() -> Para retirar os espaços
print(cidade[:5].lower() == 'santo')
"""
