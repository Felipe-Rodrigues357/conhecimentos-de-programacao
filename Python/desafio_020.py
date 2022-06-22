import random

aluno1 = str(input('Nome do primeiro aluno: '))
aluno2 = input('Nome do segundo aluno: ')
aluno3 = input('Nome do terceiro aluno: ')
aluno4 = input('Nome do quarto aluno: ')
alunos = [aluno1, aluno2, aluno3, aluno4]
ordem = random.shuffle(alunos)
print('A ordem de apresentação será: {}'.format(alunos))
