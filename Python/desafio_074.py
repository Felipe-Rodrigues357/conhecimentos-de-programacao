import random

numeros = (random.randint(1, 10), random.randint(1, 10),
           random.randint(1, 10), random.randint(1, 10),
           random.randint(1, 10))
print(f"Os números são: ", end='')
for n in numeros:
    print(f'{n} ', end='')

print(f"\nO Maior número é: {max(numeros)}")
print(f"O Menor número é: {min(numeros)}")
