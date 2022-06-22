reta1 = float(input('Qual o tamanho da primeira reta: '))
reta2 = float(input('Qual o tamanho da segunda reta: '))
reta3 = float(input('Qual o tamanho da terceira reta: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Pode-se formar um triângulo!')
else:
    print('Não se pode se formar um triângulo!')
