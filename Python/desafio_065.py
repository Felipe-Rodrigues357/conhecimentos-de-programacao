num = int(input('\033[1;32mDIGITE O NÚMERO: \033[m'))
resp = input('QUER CONTINUAR [S/N]? ').upper()
cont = 1
soma = num
maior = num
menor = num
while resp != 'N' and resp in 'S':
    num = int(input('\033[1;32mDIGITE O NÚMERO: \033[m'))
    resp = input('QUER CONTINUAR [S/N]? ').upper()
    cont += 1
    if cont > 1:
        soma = num + soma
    if num < menor:
        menor = num
    if num > maior:
        maior = num
media = float (soma/cont)
print('\033[1;33mFORAM INFORMADOS \033[m'
      '\033[1;34m{} \033[m'
      '\033[1;33mVALORES, A MÉDIA ENTRE ELES É \033[m'
      '\033[1;34m{} \033[m'
      '\n\033[1;33mO MAIOR VALOR INFORMADO FOI \033[m'
      '\033[1;34m{} \033[m'
      '\033[1;33mE O MENOR VALOR INFORMADO FOI \033[m'
      '\033[1;34m{}\033[m'.format(cont, media, maior, menor))
