print('-'*30)
print('{:^30}'.format('SKYWALKER BANK'))
print('-'*30)
saque = int(input('\033[1;33mVALOR SAQUE: R$\033[m'))
total = saque
cedula = 50
totcedula = 0
while True:
    if total >= cedula:
        total -= cedula
        totcedula += 1
    else:
        if totcedula > 0:
            print(f'TOTAL DE {totcedula} CÉDULAS DE R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totcedula = 0
        if total == 0:
            break
