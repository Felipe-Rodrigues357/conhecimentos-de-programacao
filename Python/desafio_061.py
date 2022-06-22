termo = int(input('\033[1;30mEscreva o Primeiro Termo: \033[m'))
razao = int(input('\033[1;30mEscreva a Razão: \033[m'))
cont = termo
contador = 0
print('{}'.format(termo), end=' -> ')
while contador <= 8:
    contador += 1
    cont += razao
    print('{}'.format(cont), end=' -> ')
print('FIM')
