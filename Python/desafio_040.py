nome = input('\033[1;30mDigite o nome do aluno: \033[m')
n1 = float(input('\033[1;30mDigite a nota da AV1: \033[m'))
n2 = float(input('\033[1;30mDigite a nota da AV2: \033[m'))
media = (n1+n2)/2
if media < 5.0:
    print('\033[1;30mO(A) Aluno(a)\033[m'
          '\033[1;32m {}\033[m'
          '\033[1;30m com média\033[m'
          '\033[1;31m {}\033[m'
          '\033[1;30m está\033[m'
          '\033[1;31m REPROVADO(A)!\033[m'.format(nome, media))
elif media >= 5.0 and media < 6.9:
    print('\033[1;30mO(A) Aluno(a)\033[m'
          '\033[1;32m {}\033[m'
          '\033[1;30m com média\033[m'
          '\033[1;33m {}\033[m'
          '\033[1;30m está em\033[m'
          '\033[1;33m RECUPERAÇÃO!\033[m'.format(nome, media))
else:
    print('\033[1;30mO(A) Aluno(a)\033[m'
          '\033[1;32m {}\033[m'
          '\033[1;30m com média\033[m'
          '\033[1;34m {}\033[m'
          '\033[1;30m está\033[m'
          '\033[1;34m APROVADO(A)!\033[m'.format(nome, media))