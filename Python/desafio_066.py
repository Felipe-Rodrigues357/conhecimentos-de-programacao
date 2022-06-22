n = cont = soma = 0
while n != 999:
    n = int(input('\033[1;33mESCREVA O {}º NÚMERO: \033[m'.format(cont+1)))
    if n == 999:
        break
    else:
        cont += 1
        soma += n
print('\033[1;33mFORAM DIGITADOS \033[m'
      '\033[1;34m{} \033[m'
      '\033[1;33mNÚMEROS E A SOMA ENTRE ELES É \033[m'
      '\033[1;34m{}\033[m'.format(cont, soma))
