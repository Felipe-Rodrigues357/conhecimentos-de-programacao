import random

aluno1 = input('Primeiro Aluno: ')
aluno2 = input('Segundo Aluno: ')
aluno3 = input('Terceiro Aluno: ')
aluno4 = input('Quarto Aluno: ')
num = random.randint(1, 4)
if num == 1:
    print('O Aluno escolhido foi {}'.format(aluno1))
elif num == 2:
    print('O Aluno escolhido foi {}'.format(aluno2))
elif num == 3:
    print('O Aluno escolhido foi {}'.format(aluno3))
elif num == 4:
    print('O Aluno escolhido foi {}'.format(aluno4))
"""OU PODERIA SER:
lista = [aluno1, aluno2, aluno3, aluno4]
num = random.choice(lista)
print('O Aluno escolhido foi {}'.format(num))"""
