dias = int(input('Quantos dias foi alugado: '))
km = float(input('Quantos KM rodados: '))
total = (dias*60)+(km*0.15)
print('O carro foi alugado por {} dias e teve {}KM rodados.\nO valor total desse aluguel foi de R${:.2f}'.format(dias, km, total))