num = int(input('\033[1;33mEscolha um número inteiro: \033[m'))
escolha = int(input('OPÇÕES:'
                    '\n\033[1;34m"1"\033[m para Binário;'
                    '\n\033[1;34m"2"\033[m para Octal;'
                    '\n\033[1;34m"3"\033[m para Hexadecimal;'
                    '\nEscolha como você quer o número: '))
if escolha == 1:
    print('\033[1;33mO número em Binário é:\033[m \033[1;34m{}\033[m'.format(bin(num)[2:]))
elif escolha == 2:
    print('\033[1;33mO número em Octal é:\033[m \033[1;34m{}\033[m'.format(oct(num)[2:]))
elif escolha == 3:
    print('\033[1;33mO número em Hexadecimal é:\033[m \033[1;34m{}\033[m'.format(hex(num)[2:]))
else:
    print('\033[1;31mOPÇÃO INVÁLIDA!\033[m')
