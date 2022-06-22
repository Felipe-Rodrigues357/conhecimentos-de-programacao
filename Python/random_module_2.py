from random import *

def die():
    return randint(1,6)

print(die())

lst = ['a','b','c','d','e','f']
shuffle(lst) # Emabaralhar uma lista

print(lst)

print(
    choice(lst) # Escolhe randomicamente um elemento da lista
)

print(
    sample(lst,3) # Escolhe randomicamente o número de elementos selecionados da lista
)
