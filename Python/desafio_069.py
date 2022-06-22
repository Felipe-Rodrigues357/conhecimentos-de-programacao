idade = 0
sexo = 'F'
continuar = 'S'
maiores = 0
homens = 0
mulheres = 0
while continuar == 'S':
    idade = int(input('\033[1;33mDIGITE A IDADE: \033[m'))
    sexo = str(input('\033[1;33mDIGITE O SEXO [M/F]: \033[m')).upper()
    if idade > 18:
        maiores += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    continuar = input('\033[1;31mDESEJA CONTINUAR[S/N]? \033[m').upper()
    if continuar == 'N':
        break
print('\033[1;33mFORAM INFORMADOS \033[m'
      f'\033[1;34m{maiores} \033[m'
      '\033[1;33mMAIORES DE IDADE.'
      '\nFORAM INSERIDOS \033[m'
      f'\033[1;34m{homens} \033[m'
      '\033[1;33mHOMENS E \033[m'
      f'\033[1;34m{mulheres} \033[m'
      '\033[1;33mMULHERES MENORES QUE 20 ANOS!\033[m')
"""
tot18 = totH = totM20 = 0
while True:
    idade = int(input('IDADE: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input(SEXO [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        tot18 +=1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('QUER CONTINUAR [S/N]? ')).strip().upper()[0]
    if resp == 'N':
        break
"""
