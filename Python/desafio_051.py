termo = int(input('\033[1;30mEscreva o Primeiro Termo: \033[m'))
razao = int(input('\033[1;30mEscreva a Razão: \033[m'))
decimo = termo + (10-1) * razao
for c in range(termo, decimo + razao, razao):
    print('{}'.format(c), end=' -> ')
print('ACABOU')
"""
OU PARA QUE FIQUE TUDO NA MESMA LINHA:
for c in range(0,9):
    termo+=razao
    print(termo, end=' ->')
"""