import math

an = float(input('Digite um ângulo: '))
sen = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print('O Ângulo {} teve:\n SENO:{:.2f} \n COSSENO:{:.2f} \n TANGENTE:{:.2f}'.format(an, sen, cos, tan))
