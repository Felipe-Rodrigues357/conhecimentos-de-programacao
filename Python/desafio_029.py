velocidade = float(input('Escreva a velocidade do carro: '))
if velocidade > 80.0:
    print('VOCÊ FOI MULTADO!')
    multa = (velocidade-80)*7
    print('O valor da multa foi: R${:.2f}'.format(multa))
else:
    print('DENTRO DO LIMITE DE VELOCIDADE!')
