num = int(input('Coloque o número: '))
print('{:=^13}'.format(''))
for c in range (1, 11):
    print('{} x {:2} = {:3}'.format(num, c, num*c))
print('{:=^13}'.format(''))