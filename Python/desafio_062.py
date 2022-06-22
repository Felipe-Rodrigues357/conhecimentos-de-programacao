termo = int(input('\033[1;30mEscreva o Primeiro Termo: \033[m'))
razao = int(input('\033[1;30mEscreva a Razão: \033[m'))
termos = int(input('\033[1;30mQuantos termos você quer ver: \033[m'))
cont = termo
contador = 0
print('{}'.format(termo), end=' -> ')
while contador <= termos:
    contador += 1
    cont = cont + razao
    print('{}'.format(cont), end=' -> ')
print('ACABOU')
"""
OU:
termo = int(input('\033[1;30mEscreva o Primeiro Termo: \033[m'))
razao = int(input('\033[1;30mEscreva a Razão: \033[m'))
cont = termo
contador = 0
total = 0
mais = 10
print('{}'.format(termo), end=' -> ')
while mais != 0:
    total = total + mais
    while contador <= total:
        contador += 1
        cont += razao
        print('{}'.format(cont), end=' -> ')
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais: '))
print('PROGRESSÃO FINALIZADA COM {} TERMOS MOSTRADOS!'.format(total))
"""
