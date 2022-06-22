tot = 995
bought_sale = False # Mudar manualmente se for True ou False, isso garante o desconto
dis = 0

if tot >= 1000 or bought_sale: # Preço maior que R$1000 OU produto em Sale
    dis = 10
else: # Acontece em qualquer situação que o if não for executado
    dis = 2

total = tot - tot*dis/100
print("The Discount is R$", tot*dis/100)
print("R$", total)