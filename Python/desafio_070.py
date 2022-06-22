print('-'*20)
print('{: ^20}'.format('SKYWALKER STORE'))
print('-'*20)
nome_produto = str
preco_produto = 0
contador = 0
mais_barato_preco = 0
mais_barato_nome = str
continuar = 'S'
total = 0
cont = 0
while continuar == 'S':
    nome_produto = input('\033[1;33mNOME DO PRODUTO: \033[m').upper()
    preco_produto = float(input('\033[1;33mPREÇO: R$\033[m'))
    continuar = input('\033[1;33mDESEJA ADICIONAR MAIS PRODUTOS [S/N]? ').upper()
    cont += 1
    if cont == 1:
        mais_barato_nome = nome_produto
        mais_barato_preco = preco_produto
    if preco_produto > 1000.00:
        contador += 1
    if preco_produto <= mais_barato_preco:
        mais_barato_nome = nome_produto
        mais_barato_preco = preco_produto
    total = preco_produto + total
    if continuar == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print('\033[1;33mO TOTAL DA COMPRA FOI R$\033[m'
      f'\033[1;34m{total:.2f}\033[m'
      '\n\033[1;33mFORAM INFORMADOS \033[m'
      f'\033[1;34m{contador} \033[m'
      '\033[1;33mPRODUTOS CUSTANDO MAIS DE R$1000.00\033[m'
      '\n\033[1;33mO PRODUTO MAIS BARATO FOI \033[m'
      f'\033[1;34m{mais_barato_nome} \033[m'
      '\033[1;33mCUSTANDO R$\033[m'
      f'\033[1;34m{mais_barato_preco:.2f}\033[m')
