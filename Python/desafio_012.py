preco = float(input('Qual o preço do produto: R$'))
desconto = preco*5/100
novopreco = preco-desconto
print('O produto com 5% de desconto (R${}) ficou em R${}'.format(desconto, novopreco))