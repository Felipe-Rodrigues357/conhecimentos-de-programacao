casa = int(input('\033[1;33mQual o valor da casa? \033[m'))
salario = float(input('\033[1;30mQual o seu salário? \033[m'))
anos = int(input('\033[1;32mQuantos anos irá pagar? \033[m'))
meses = anos*12
prestacao = casa / meses
if prestacao >= (salario*0.3):
    print('\033[1;31mDesculpe, seu empréstimo está negado!\033[m')
else:
    print('\033[1;34mParabéns! Seu empréstimo foi aprovado! A parcela será de R${:.2f} em {} meses!'.format(prestacao, meses))
