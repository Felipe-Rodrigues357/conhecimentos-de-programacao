import datetime

print('\033[1;34mCONTADOR MAIORES DE IDADE')
atual = datetime.date.today().year
maior = 0
for c in range(1, 8):
    nasc = int(input('\033[1;30mEscreva a {}ª data de Nascimento: \033[m'.format(c)))
    idade = atual - nasc
    if idade >= 18:
        maior += 1
print('\033[1;34mForam informados\033[m \033[1;32m{}\033[m \033[1;34mmaiores de idade\033[m'.format(maior))