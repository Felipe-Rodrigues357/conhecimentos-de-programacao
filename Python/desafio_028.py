import random
import time

print('-=-'*6)
print('JOGO DE ADVINHAÇÃO')
print('-=-'*6)
numero = random.randint(0, 5)
resposta = int(input('Tente Descobrir o Número de 0 a 5: '.upper()))
print('PROCESSANDO...')
time.sleep(3)
if resposta == numero:
    print('VOCÊ ACERTOU! O NÚMERO ESCOLHIDO FOI {}'.format(numero))
else:
    print('QUE PENA, VOCÊ ERROU! O NÚMERO ESCOLHIDO FOI {}'.format(numero))
print('-=-'*6)
print('    GAME OVER')
print('-=-'*6)
