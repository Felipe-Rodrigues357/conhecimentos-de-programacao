num = int(input('\033[1;33mDIGITE O NÚMERO PARA FATORIAL: \033[m'))
contador = num
fatorial = 1
print('\033[1;34m{}\033[m'.format(num), end='')
while contador != 1:
    print('\033[1;30m X \033[m'
          '\033[1;34m{}\033[m'.format(contador - 1),end='')
    fatorial = fatorial * contador
    contador -= 1
print('\033[1;30m = \033[m'
      '\033[1;34m{}\033[m'.format(fatorial))
"""
NA BIBLIOTECA math TEM UMA FUNÇÃO FACTORIAL:
f = factorial(n)
"""
