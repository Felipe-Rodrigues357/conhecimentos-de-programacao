termos = int(input('\033[1;30mQUANTOS TERMOS VOCÊ QUER VER? \033[m'))
t1 = 0
t2 = 1
print('\033[1;30m{} -> {}\033[m'.format(t1, t2),end='')
contador = 3
while contador <= termos:
    t3 = t1 + t2
    print('\033[1;30m -> {}\033[m'.format(t3), end='')
    t1 = t2
    t2 = t3
    contador += 1
print('\033[1;30m -> \033[m\033[1;34mFIM\033[m')
