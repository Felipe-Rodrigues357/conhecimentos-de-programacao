numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis',
           'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
           'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
           'Dezenove', 'Vinte')
while True:
    n1 = int(input('Digite um número entre 0 e 20: '))
    if 0 <= n1 <= 20:
        break
    print('Tente Novamente.', end='')
print('Você digitou o número', numeros[n1])
"""OU print(f'Você digitou o número {cont[]}')"""
