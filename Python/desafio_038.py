n1 = int(input('\033[1;33mDigite o Primeiro número: \033[m'))
n2 = int(input('\033[1;32mDigite o Segundo número: \033[m'))
if n1 > n2:
    print('\033[1;33mO Primeiro número é maior!\033[m')
elif n2 > n1:
    print('\033[1;32mO Segundo número é maior!\033[m')
else:
    print('\033[1;34mOs números são iguais!\033[m')
