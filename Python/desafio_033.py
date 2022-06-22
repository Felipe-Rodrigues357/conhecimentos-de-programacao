n1 = float(input('1º Número: '))
n2 = float(input('2º Número: '))
n3 = float(input('3º Número: '))
if n1>n2 and n1>n3:
    maior = n1
    print('O Maior número é: {}'.format(maior))
    if n2<n3:
        menor = n2
        print('O Menor número é: {}'.format(menor))
    else:
        menor = n3
        print(print('O Menor número é: {}'.format(menor)))
if n2>n1 and n2>n3:
    maior = n2
    print('O Maior número é: {}'.format(maior))
    if n1<n3:
        menor = n1
        print('O Menor número é: {}'.format(menor))
    else:
        menor = n3
        print(print('O Menor número é: {}'.format(menor)))
if n3>n2 and n3>n1:
    maior = n3
    print('O Maior número é: {}'.format(maior))
    if n2<n1:
        menor = n2
        print('O Menor número é: {}'.format(menor))
    else:
        menor = n1
        print(print('O Menor número é: {}'.format(menor)))