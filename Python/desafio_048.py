s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont+1
        s = s + c
print('A SOMA DOS NÚMEROS ÍMPARES, MÚLTIPLOS DE 3 ENTRE 1 E 500 (QUE SÃO {}) É {}'.format(cont, s))
