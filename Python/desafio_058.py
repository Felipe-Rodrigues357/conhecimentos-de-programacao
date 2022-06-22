import random
import time

print('\033[1;33m-=-\033[m' * 6)
print('\033[1;34mJOGO DE ADVINHAÇÃO\033[m')
print('\033[1;33m-=-\033[m' * 6)
cont = 0
PC = random.randint(0, 10)
jogador = int(input('\033[1;32mDIGITE SEU PALPITE DE 0 A 10: \033[m'))
print('\033[1;36mPROCESSANDO...\033[m')
time.sleep(1)
while jogador != PC:
    cont += 1
    print('\033[1;31mVOCÊ ERROU! TENTE NOVAMENTE...\033[m')
    jogador = int(input('\033[1;32mDIGITE SEU PALPITE DE 0 A 10: \033[m'))
    print('\033[1;36mPROCESSANDO...\033[m')
    time.sleep(1)
print('\033[1;34mPARABÉNS VOCÊ ACERTOU EM\033[m \033[1;33m{} \033[m'
      '\033[1;34mTENTATIVAS!\033[m'
      '\n\033[1;34mO NÚMERO ESCOLHIDO FOI \033[m'
      '\033[1;33m{}\033[m'.format(cont, PC))
"""
COLOCANDO PARA INFORMAR SE O NÚMERO É MAIOR OU MENOR
while jogador != PC:
    cont += 1
    if jogador < computador:
        print('\033[1;31mVOCÊ ERROU, O NÚMERO É MAIOR! TENTE NOVAMENTE...\033[m')
    elif jogador > computador:
        print('\033[1;31mVOCÊ ERROU, O NÚMERO É MENOR! TENTE NOVAMENTE...\033[m')
    jogador = int(input('\033[1;32mDIGITE SEU PALPITE DE 0 A 10: \033[m'))
    print('\033[1;36mPROCESSANDO...\033[m')
    time.sleep(1)
"""
