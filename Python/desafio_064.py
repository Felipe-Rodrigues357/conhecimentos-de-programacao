cont = 0
soma = 0
num = 0
num = int(input('\033[1;32mDIGITE O NÚMERO [999 PARA FINALIZAR]: \033[m'))
while num != 999:
    soma += num
    cont += 1
    num = int(input('\033[1;32mDIGITE O NÚMERO [999 PARA FINALIZAR]: \033[m'))
print('\033[1;33mFORAM DIGITADOS \033[m'
      '\033[1;34m{} \033[m'
      '\033[1;33mNÚMEROS E A SOMA ENTRE ELES É \033[m'
      '\033[34m{}\033[m'.format(cont, soma))
