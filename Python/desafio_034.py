salario = float(input('Digite o Salário: R$'))
if salario > 1250.00:
    aumento = salario * 0.1 # OU salário + (salário * 10/100)
    print('O Salário final é R${:.2f}'.format(salario+aumento))
else:
    aumento = salario * 0.15 # OU salário + (salário * 15/100)
    print('O Salário final é R${:.2f}'.format(salario+aumento))