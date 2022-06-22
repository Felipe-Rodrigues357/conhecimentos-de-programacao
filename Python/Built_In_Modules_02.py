lst = [1, 223, 12, 34, 56, 78, 23, 454, 23, 545, 12, 234]


def EvenCheck(num):
    if num % 2 == 0:
        return True
    else:
        return False


filtered_lst = filter(EvenCheck, lst)
even_lst = []

for ele in filtered_lst:
    even_lst.append(ele)

print(even_lst)


print(
    format('age','^5')
)

print(
    format('age','<5')
)

print(
    format('age','>5')
)

print(
    format('age','*^5')
)
