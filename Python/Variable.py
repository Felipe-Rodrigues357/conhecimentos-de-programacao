age = 21
print(age)
# Starts with letter, case sensitive

Str = '''Master has failed more,
than the beginner has tried'''
print(Str[0:6])
print(Str[0:6] + Str[41:51])
print(Str[33:45] + Str[10:17])
print(Str[11:17])
print(Str[18:22])
print(len(Str))

Str = 'Life is not a race or game, it is lie'
print(Str[14:18].capitalize())
print(Str[22:26].upper())
print(Str[0].lower() + Str[1:4].upper())
print(Str[28:37].capitalize())

num1 = 112
num2 = 20.45
num3 = 7 + 3j
print(num1 + num2 + num3)
print(num2 * num3)
num4 = num2 * num3
print(round(num1 % num2, 2))
print(round(num1 / num2, 2))
print(round(num4.imag, 2))

lst = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
lst.remove("cherry")
lst.remove("melon")
lst.remove("kiwi")
lst.append("guava")
lst.append("peach")
lst.reverse()
print(lst)
print(len(lst))

tpl = "('python',)"
print(tpl)
tpl = tuple('Python')
print(type(tpl))

tpl = (3, 6, 9)
lst = [12, 15, 18]
tpl1 = tuple(lst)
tpl2 = tpl + tpl1
print(tpl2)

lst = [0, 12, 3, 4, 12, 4, 12, 34, 12, 33, 7, 8, 2, 90, 23, 45, 12, 33]
LIST = set(lst)
print(list(LIST))

set1, set2 = {'ProductA', 'ProductC', 'ProductY', 'ProductX', 'ProductL'}, {'ProductY', 'ProductM', 'ProductR',
                                                                            'ProductC', 'ProductR'}
print(set1 & set2)
