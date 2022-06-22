valor = float(input('\033[1;30mVALOR DO PRODUTO: R$\033[m'))
print('\033[1;4;33m========OPÇÕES DE PAGAMENTO========\033[m')
opcao = int(input('\033[1;30m(1)PAGAMENTO EM DINHEIRO / CHEQUE:\033[m'
                  '\033[1;34m R${:.2f}\033[m'
                  '\n\033[1;30m(2)PAGAMENTO EM CARTÃO À VISTA:\033[m'
                  '\033[1;34m R${:.2f}\033[m'
                  '\n\033[1;30m(3)PAGAMENTO EM 2X NO CARTÃO:\033[m'
                  '\033[1;34m R${:.2f}\033[m'
                  '\n\033[1;30m(4)PAGAMENTO EM 3X OU MAIS NO CARTÃO:\033[m'
                  '\033[1;34m R${:.2f}\033[m'
                  '\n\033[1;4;30mOPÇÃO:\033[m '.format(valor-(valor*0.1),
                                                       valor-(valor*0.05),
                                                       valor,
                                                       valor+(valor*0.2))))
if opcao == 1:
    print('\033[1;30mO VALOR A SER PAGO É DE:\033[m'
          '\033[1;34m R${:.2f}\033[m'.format(valor-(valor*0.1)))
elif opcao == 2:
    print('\033[1;30mO VALOR A SER PAGO É DE:\033[m'
          '\033[1;34m R${:.2f}\033[m'.format(valor-(valor*0.05)))
elif opcao == 3:
    print('\033[1;30mO VALOR A SER PAGO É DE: 2 PARCELAS DE\033[m'
          '\033[1;31m R${:.2f}\033[m'
          '\033[1;30m NO VALOR TOTAL DE\033[m'
          '\033[1;34m R${:.2f}\033[m'.format(valor/2, valor))
elif opcao == 4:
    parcelas = int(input('\033[1;30mQUANTIDADE DE PARCELAS: \033[m'))
    print('\033[1;30mO VALOR A SER PAGO É DE:\033[m'
          '\033[1;31m {}\033[m'
          '\033[1;30m PARCELAS DE\033[m'
          '\033[1;34m R${:.2f}\033[m'
          '\033[1;30m NO VALOR TOTAL DE\033[m'
          '\033[1;34m R${:.2f}\033[m'.format(parcelas, (valor+(valor*0.2))/parcelas, valor+(valor*0.2)))
else:
    print('\033[1;4;31;40mOPÇÃO INVÁLIDA! TENTE NOVAMENTE!\033[m')