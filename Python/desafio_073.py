tabela = ('Internacional', 'Flamengo', 'Atlético Mineiro', 'São Paulo',
          'Fluminense', 'Palmeiras', 'Grêmio', 'Corinthians', 'Bragantino',
          'Athelico-PR', 'Santos', 'Ceará', 'Atlético Goianiense', 'Sport',
          'Fortaleza', 'Vasco', 'Bahia', 'Goiás', 'Coritiba', 'Botafogo')
print('Os 5 Primeiros Colocados são: ', '\033[1;34m', tabela[:5], '\033[m')
print(10*'-=-=-')
print('Os 4 Últimos Colocados são: ', '\033[1;31m', tabela[16:], '\033[m')
print(10*'-=-=-')
print('Os times em ordem alfabética: ', '\033[1;33m', sorted(tabela), '\033[m')
print(10*'-=-=-')
print('O Vasco está na posição: ', '\033[1;32m', tabela.index('Vasco'), '\033[m')
