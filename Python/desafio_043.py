peso = float(input('\033[1;30mDigite o seu peso em KG: \033[m'))
altura = float(input('\033[1;30mDigite sua altura em metros: \033[m'))
imc = peso/(altura*altura) # out peso / (altura ** 2)
if imc < 18.5:
    print('\033[1;30mSeu IMC de\033[m'
          '\033[1;31m {:.1f}\033[m'
          '\033[1;30m está\033[m'
          '\033[1;31m ABAIXO DO PESO!\033[m'.format(imc))
elif imc >=18.5 and imc < 25:
    print('\033[1;30mSeu IMC de\033[m'
          '\033[1;34m {:.1f}\033[m'
          '\033[1;30m está\033[m'
          '\033[1;34m NO PESO IDEAL!\033[m'.format(imc))
elif imc >=25 and imc < 30:
    print('\033[1;30mSeu IMC de\033[m'
          '\033[1;32m {:.1f}\033[m'
          '\033[1;30m está em\033[m'
          '\033[1;32m SOBREPESO!\033[m'.format(imc))
elif imc>=30 and imc < 40:
    print('\033[1;30mSeu IMC de\033[m'
          '\033[1;33m {:.1f}\033[m'
          '\033[1;30m está em\033[m'
          '\033[1;33m OBESIDADE!\033[m'.format(imc))
else:
    print('\033[1;30mSeu IMC de\033[m'
          '\033[1;31m {:.1f}\033[m'
          '\033[1;30m está em\033[m'
          '\033[1;31m OBESIDADE MÓRBIDA!\033[m'.format(imc))