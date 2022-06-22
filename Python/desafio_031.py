print('------------SKYWALKER TRAVELS------------')
distancia = float(input('Distância até o Destino: '))
if distancia <= 200:
    preco = distancia*0.5
    print('VALOR PASSAGEM: {:.2f} REPUBLIC CREDITS'.format(preco))
else:
    preco = distancia*0.45
    print('VALOR PASSAGEM: {:.2f} REPUBLIC CREDITS'.format(preco))
print('------------SKYWALKER TRAVELS------------')
