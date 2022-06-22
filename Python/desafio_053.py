frase = input('\033[1;30mEscreva a sua frase: \033[m').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)  ## Serve para substituir os espaços por "nada"
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um Palíndromo!')
else:
    print('A frase não é um Palíndromo!')

"""
Pode ser escrito sem o for também como:
frase = input('\033[1;30mEscreva a sua frase: \033[m').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um Palíndromo!')
else:
    print('A frase não é um Palíndromo!')
"""
