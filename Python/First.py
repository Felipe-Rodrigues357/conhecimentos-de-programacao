# Text
name = 'Python'  # str
print(name)

# Numeric
num = 12  # int
print(num)
num1 = 3.45  # float
num2 = 4 + 5j  # complex

# Sequence
num3 = [1, 2, 3, 4, 5, "Python"]  # list
num4 = (1, 2, 3, 4, 5)  # tuple
num5 = {1, 2, 3, 4, 5, 6}  # set (não pode ter números iguais

# Booleans
True
False

# Dictionary
dt = {'key':'val', 'k1':'val2'}
print(dt)
print(dt['key'])
# EXEMPLO:
dt = {'A':65, 'B':66}
print(dt['A'])
print(dt['B'])
print(dt.values())
print(dt.keys())

# EXEMPLO 2:
dt1 = {"C":67, "D":68}
Dt = {'1':dt, '2':dt1}
print(Dt)

dct = {"Model":"5600X", "CS":"4.6GHz", "Price":549}
print(dct["Model"])

tpl1 = ('k1','k2','k3')
val = 4
dt = dict.fromkeys(tpl1, val)
print(dt)

tpl2 = ('k1','k2','k3')
dt = dict.fromkeys(tpl2)
print(dt)

tpl3 = ('k1','k2','k3')
dt = dict.fromkeys(tpl2)
dt['k1'] = 19
dt['k2'] = 12
dt['k3'] = 11
print(dt)

tpl = ('Set', 'VRAM', 'Slots')
dt = dict.fromkeys(tpl)
dt['Set'] = 'B550'
dt['VRAM'] = '8g'
dt['Slots'] = 4
print(dt)

Str = 'Head on the hills'
print(Str[-9:].capitalize())

tpl = (1,)
tpl += (2,)
print(tpl)

Str = "Casting on the  'Beach'"
print(Str[-6:-1])
