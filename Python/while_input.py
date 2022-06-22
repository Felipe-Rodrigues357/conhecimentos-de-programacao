lst = [1, 4, 56, 2, 4, 12, 6, 89, 11, 0]
i = 10

while i > 0:
    lst.pop(-1)
    i -= 1
print(lst)

Num = input('>')  # Sempre será STRING
print(Num)

num = 0
i = 0

while i < 4:
    num = int(input('Number_'))  # Transforma a STRING em INTEGER
    if num == 0:
        print('Square: 0')
        i += 1
        continue  # Significa que se o if for executado, ele já vai para o próximo loop, não faz o que viria depois
    if num == 1:
        print('Program Exited')
        break  # Finaliza o programa
    sq = str(num * num)
    print('Square: ' + sq)
    i += 1
else:
    print('Done')
