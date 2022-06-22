import math
cateto_op = float(input('Digite o Cateto Oposto: '))
cateto_adj = float(input('Digite o Cateto Adjacente: '))
hipotenusa = math.hypot(cateto_op,cateto_adj)
print('A hipotenusa do cateto oposto {} e do cateto adjacente {} é {:.2f}'.format(cateto_op, cateto_adj, hipotenusa))
