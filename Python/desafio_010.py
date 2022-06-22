print('{:=^10}CONTADOR DE DÓLARES{:=^10}'.format('',''))
dinheiro = float(input('Quanto você tem na carteira: R$'))
cambio = 3.27
print('Você tem R${} ou U${:.2f}'.format(dinheiro,dinheiro/cambio))
