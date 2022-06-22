for l in 'Python':  # O tamanho do loop é determinado pelo tamanho da list, string, etc
    print(l)

lst = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
new_lst = []
for ele in lst:
    new_lst.append(ele.capitalize())
print (new_lst)

lst = [10, 20, 33, 45, 67]

for num in lst:
    print(num * 2)

lst2 = ['python', 'c', 'java', 'JavaScript']
for ele in lst2:
    if ele == 'JavaScript':
        print(ele)
        continue
    print(ele.capitalize())

print(list(range(4)))
print(list(range(2, 5)))

for num in range(2, 5):
    print(num)
    print('Loop')

for n in [1, 2, 3]:
    for m in [1, 2, 3]:
        print(n, m)

lst3 = [1, 2, 5, 7, 8, 1, 3, 5, 8]
uniques_lst = []

for num in lst3:
    if num in uniques_lst:
        continue
    uniques_lst.append(num)

print(uniques_lst)
uniques_lst.sort()
print(uniques_lst)
