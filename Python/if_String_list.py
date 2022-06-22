lst = ['C', 'C++', 'RUBY', 'PHP']
print("Before List:",lst)

if 'Python' not in lst:
    lst.append('Python')
elif 'JAVA' not in lst:
    lst.append('JAVA')
else:
    lst.append('JS')

print("After List: ",lst)
