num = int(input('\033[1;30mEscreva um número inteiro: \033[m'))
primo = 0
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[1;34m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes!'.format(num, total))
if total == 2:
    print('E por isso, ele É PRIMO!')
else:
    print('E por isso, ele NÃO É PRIMO!')
