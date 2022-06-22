numero = input('Digite um número entre 0 e 9999: ')
unidade = ''
dezena = ''
centena = ''
milhar = ''
if len(numero)==4:
    unidade = numero[3]
    dezena = numero[2]
    centena = numero[1]
    milhar = numero[0]
elif len(numero)==3:
    unidade = numero[2]
    dezena = numero[1]
    centena = numero[0]
    milhar = '0'
elif len(numero)==2:
    unidade = numero[1]
    dezena = numero[0]
    centena = '0'
    milhar = '0'
elif len(numero)==1:
    unidade = numero[0]
    dezena = '0'
    centena = '0'
    milhar = '0'
"""OU pode ser feito: 
num=int(input('Informe um número: ')
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
"""
print("""Unidade: {}
Dezena: {}
Centena: {}
Milhar: {}""".format(unidade,dezena,centena,milhar))