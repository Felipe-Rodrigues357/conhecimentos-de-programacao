mult = 1
n = 0
while n >= 0:
    n = int(input('\033[1;33mQUAL O VALOR PARA A TABUADA: \033[m'))
    if n <= 0:
        break
    print('-'*15)
    while mult <= 10:
        print('\033[1;34m{} x {} = {}\033[m'.format(n, mult, n*mult))
        mult += 1
    print('-' * 15)
    mult = 1
print('\033[1;31mVALOR NEGATIVO! FIM DE PROGRAMA\033[m')
