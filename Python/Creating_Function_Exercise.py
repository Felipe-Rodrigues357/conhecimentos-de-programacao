lst = [12, 12, 3, 44, 56, 99, 12, 3, 44]


def remove_dup(l):
    unique = set(l)
    u = list(unique)
    u.sort( )  # Coloca a lista em ordem crescente
    return u


print(lst)
print(remove_dup(lst))


def type_dt(data):
    dt = str(type(data))
    if 'str' in dt:
        print('String')
    elif 'int' in dt:
        print('Integer')
    elif 'float' in dt:
        print('Floating point number')
    elif 'complex' in dt:
        print('Complex Number')


print(type('Python'))
type_dt('Python')


def sum_round(*n):
    sm = 0
    d = []
    for num in n:
        sm += num
        Num = str(num).split('.')
        d.append(len(Num[1]))

    min_d = min(d)
    return round(sm, min_d)


print(sum_round(12.56, 12.88, 11.1, 90.007))


# Lista com ordem decrescente

lst = [ 5, 6, 7, 23 ,12 ,3, 3, 4 ,5, 12, 34]

def dsort(l):
    u = list(l)
    u.sort(reverse = True)
    return u

print (dsort(lst))
