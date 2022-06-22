n1 = int(input('\033[1;33mDIGITE O PRIMEIRO NÚMERO: \033[m'))
n2 = int(input('\033[1;33mDIGITE O SEGUNDO NÚMERO: \033[m'))
print('\033[1;30m-=-\033[m' * 6)
print('\033[1;34mMENU DE ESCOLHA\033[m')
print('\033[1;30m-=-\033[m' * 6)
print('\033[1;31m[1]\033[m'
      '\033[1;33m SOMAR\033[m'
      '\n\033[1;31m[2]\033[m'
      '\033[1;33m MULTIPLICAR\033[m'
      '\n\033[1;31m[3]\033[m'
      '\033[1;33m MAIOR\033[m'
      '\n\033[1;31m[4]\033[m'
      '\033[1;33m NOVOS NÚMEROS\033[m'
      '\n\033[1;31m[5]\033[m'
      '\033[1;33m SAIR\033[m')
escolha = int(input('\n\033[1;33mDIGITE SUA ESCOLHA: \033[m'))
maior = 0
while escolha != 5:
    print('\033[1;30m-=-\033[m' * 6)
    print('\033[1;34mRESULTADO\033[m')
    print('\033[1;30m-=-\033[m' * 6)
    if escolha == 1:
        print('\033[1;33mA SOMA ENTRE \033[m'
              '\033[1;31m{}\033[m'
              '\033[1;33m E \033[m'
              '\033[1;31m{}\033[m'
              '\033[1;33m É \033[m'
              '\033[1;34m{}\033[m'.format(n1, n2, n1 + n2))
        print('\033[1;30m-=-\033[m' * 6)
        print('\033[1;34mMENU DE ESCOLHA\033[m')
        print('\033[1;30m-=-\033[m' * 6)
        print('\033[1;31m[1]\033[m'
              '\033[1;33m SOMAR\033[m'
              '\n\033[1;31m[2]\033[m'
              '\033[1;33m MULTIPLICAR\033[m'
              '\n\033[1;31m[3]\033[m'
              '\033[1;33m MAIOR\033[m'
              '\n\033[1;31m[4]\033[m'
              '\033[1;33m NOVOS NÚMEROS\033[m'
              '\n\033[1;31m[5]\033[m'
              '\033[1;33m SAIR\033[m')
        escolha = int(input('\n\033[1;33mDIGITE SUA ESCOLHA: \033[m'))
    elif escolha == 2:
        print('\033[1;33mA MULTIPLICAÇÃO ENTRE \033[m'
              '\033[1;31m{}\033[m'
              '\033[1;33m E \033[m'
              '\033[1;31m{}\033[m'
              '\033[1;33m É \033[m'
              '\033[1;34m{}\033[m'.format(n1, n2, n1 * n2))
        print('\033[1;30m-=-\033[m' * 6)
        print('\033[1;34mMENU DE ESCOLHA\033[m')
        print('\033[1;30m-=-\033[m' * 6)
        print('\033[1;31m[1]\033[m'
              '\033[1;33m SOMAR\033[m'
              '\n\033[1;31m[2]\033[m'
              '\033[1;33m MULTIPLICAR\033[m'
              '\n\033[1;31m[3]\033[m'
              '\033[1;33m MAIOR\033[m'
              '\n\033[1;31m[4]\033[m'
              '\033[1;33m NOVOS NÚMEROS\033[m'
              '\n\033[1;31m[5]\033[m'
              '\033[1;33m SAIR\033[m')
        escolha = int(input('\n\033[1;33mDIGITE SUA ESCOLHA: \033[m'))
    elif escolha == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('\033[1;33mO MAIOR NÚMERO ENTRE \033[m'
              '\033[1;31m{}\033[m'
              '\033[1;33m E \033[m'
              '\033[1;31m{}\033[m'
              '\033[1;33m É \033[m'
              '\033[1;34m{}\033[m'.format(n1, n2, maior))
        print('\033[1;30m-=-\033[m' * 6)
        print('\033[1;34mMENU DE ESCOLHA\033[m')
        print('\033[1;30m-=-\033[m' * 6)
        print('\033[1;31m[1]\033[m'
              '\033[1;33m SOMAR\033[m'
              '\n\033[1;31m[2]\033[m'
              '\033[1;33m MULTIPLICAR\033[m'
              '\n\033[1;31m[3]\033[m'
              '\033[1;33m MAIOR\033[m'
              '\n\033[1;31m[4]\033[m'
              '\033[1;33m NOVOS NÚMEROS\033[m'
              '\n\033[1;31m[5]\033[m'
              '\033[1;33m SAIR\033[m')
        escolha = int(input('\n\033[1;33mDIGITE SUA ESCOLHA: \033[m'))
    elif escolha == 4:
        n1 = int(input('\033[1;33mDIGITE O NOVO PRIMEIRO NÚMERO: \033[m'))
        n2 = int(input('\033[1;33mDIGITE O NOVO SEGUNDO NÚMERO: \033[m'))
        print('\033[1;30m-=-\033[m' * 6)
        print('\033[1;34mMENU DE ESCOLHA\033[m')
        print('\033[1;30m-=-\033[m' * 6)
        print('\033[1;31m[1]\033[m'
              '\033[1;33m SOMAR\033[m'
              '\n\033[1;31m[2]\033[m'
              '\033[1;33m MULTIPLICAR\033[m'
              '\n\033[1;31m[3]\033[m'
              '\033[1;33m MAIOR\033[m'
              '\n\033[1;31m[4]\033[m'
              '\033[1;33m NOVOS NÚMEROS\033[m'
              '\n\033[1;31m[5]\033[m'
              '\033[1;33m SAIR\033[m')
        escolha = int(input('\n\033[1;33mDIGITE SUA ESCOLHA: \033[m'))
    else:
        print('\033[1;31mOPÇÃO INVÁLIDA! TENTE NOVAMENTE!\033[m')
        print('\033[1;30m-=-\033[m' * 6)
        print('\033[1;34mMENU DE ESCOLHA\033[m')
        print('\033[1;30m-=-\033[m' * 6)
        print('\033[1;31m[1]\033[m'
              '\033[1;33m SOMAR\033[m'
              '\n\033[1;31m[2]\033[m'
              '\033[1;33m MULTIPLICAR\033[m'
              '\n\033[1;31m[3]\033[m'
              '\033[1;33m MAIOR\033[m'
              '\n\033[1;31m[4]\033[m'
              '\033[1;33m NOVOS NÚMEROS\033[m'
              '\n\033[1;31m[5]\033[m'
              '\033[1;33m SAIR\033[m')
        escolha = int(input('\n\033[1;33mDIGITE SUA ESCOLHA: \033[m'))
print('\033[1;30m-=-\033[m' * 6)
print('\033[1;31mFIM DO PROGRAMA\033[m')
print('\033[1;30m-=-\033[m' * 6)
