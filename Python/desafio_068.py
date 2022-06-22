import random

jogador = 0
computador = random.randint(1, 10)
escolha = input('\033[1;33mESCOLHA PAR OU ÍMPAR: \033[m').upper()
soma = 0
vitorias = 0
while True: ##WHILE INFINITO
    jogador = int(input('\033[1;33mESCOLHA UM NÚMERO DE 1 ATÉ 10: \033[m'))
    print('\033[1;30mO COMPUTADOR JOGOU: \033[m', end='')
    print(computador)
    soma = jogador + computador
    print('\033[1;33mA SOMA DOS VALORES FOI: \033[m', end='')
    print(soma)
    if escolha == 'PAR' and soma%2 == 0:
        print('\033[1;34mNÚMERO PAR! VOCÊ GANHOU ESSA RODADA!\033[m')
        vitorias += 1
    elif escolha == 'ÍMPAR' and soma%2 != 0:
        print('\033[1;34mNÚMERO ÍMPAR! VOCÊ GANHOU ESSA RODADA!\033[m')
        vitorias += 1
    if escolha == 'PAR' and soma%2 != 0:
        print('\033[1;31mNÚMERO PAR! VOCÊ PERDEU ESSA RODADA!\033[m')
        break
    elif escolha == 'ÍMPAR' and soma%2 == 0:
        print('\033[1;31mNÚMERO ÍMPAR! VOCÊ PERDEU ESSA RODADA!\033[m')
        break
    computador = random.randint(1, 10)
    escolha = input('\033[1;33mESCOLHA PAR OU ÍMPAR: \033[m').upper()
print('\033[1;33mVOCÊ GANHOU \033[m'
      '\033[1;34m{} \033[m'
      '\033[1;33mRODADAS!\033[m'.format(vitorias))
