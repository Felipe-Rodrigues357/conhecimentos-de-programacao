s = 0
cont = 0
for c in range (0,6):
    n = int(input('\033[1;30mDIGITE O {}º NÚMERO INTEIRO: \033[m'.format(c+1)))
    if n % 2 == 0:
        s += n
        cont +=1
print('\033[1;34mFORAM INFORMADOS\033[m \033[1;4;31m{}\033[m \033[1;34mNÚMEROS PARES E A SOMA DE TODOS ELES É\033[m \033[1;4;31m{}\033[m'.format(cont, s))