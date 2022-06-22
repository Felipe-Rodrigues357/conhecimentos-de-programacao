import datetime
ano_nascimento = int(input('\033[1;30mEscreva seu ano de nascimento: \033[m'))
idade = datetime.date.today().year - ano_nascimento
if idade < 9:
    print('\033[1;30mVocê tem {} anos e sua categoria é:\033[m'
          '\033[1;34m MIRIM!\033[m'.format(idade))
elif idade >= 9 and idade < 14:
    print('\033[1;30mVocê tem {} anos e sua categoria é:\033[m'
          '\033[1;34m INFANTIL!\033[m'.format(idade))
elif idade >= 14 and idade < 19:
    print('\033[1;30mVocê tem {} anos e sua categoria é:\033[m'
          '\033[1;34m JUNIOR!\033[m'.format(idade))
elif idade >= 19 and idade < 25:
    print('\033[1;30mVocê tem {} anos e sua categoria é:\033[m'
          '\033[1;34m SÊNIOR!\033[m'.format(idade))
else:
    print('\033[1;30mVocê tem {} anos e sua categoria é:\033[m'
          '\033[1;34m MASTER!\033[m'.format(idade))