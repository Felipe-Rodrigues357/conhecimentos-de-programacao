maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('\033[1;34mEscreva o peso da {}ª pessoa: \033[m'.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('\033[1;33mO maior peso informado foi\033[m \033[1;34m{}\033[m'
      '\n\033[1;33mO menor peso informado foi\033[m \033[1;34m{}\033[m'.format(maior, menor))
