import datetime
nasc = int(input('\033[1;33mInforme seu ano de nascimento: \033[m'))
idade = datetime.date.today().year - nasc
print('\033[1;30mQuem nasceu em\033[m \033[1;33m{} \033[m'
      '\033[1;30mtem \033[1;34m{} \033[m'
      '\033[1;30manos em \033[m'
      '\033[1;31m{}...\033[m'.format(nasc, idade, datetime.date.today().year))
if idade < 18:
    print('\033[1;31mAinda faltam\033[m'
          '\033[1;34m {}\033[m'
          '\033[1;31m anos para você se alistar!'.format(18-idade))
elif idade == 18:
    print('\033[1;34mJá é hora de se alistar!\033[m')
else:
    print('\033[1;30mVocê passou da idade! Já se passaram\033[m'
          '\033[1;31m {}\033[m'
          '\033[1;30m anos que você deveria ter se alistado!'.format(idade-18))
