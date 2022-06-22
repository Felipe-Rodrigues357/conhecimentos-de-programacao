variable = -10

print(
    abs(variable)  # Mostra o número absoluto
)

lst = [1, 20, 35, 0]

print(
    all(lst)  # Informa se todos os valores são verdadeiros
)

print(
    any(lst)  # Informa se qualquer um dos valores são verdadeiros
)

print(bin(111))  # Extrai o valor binário de um número

code = 'print(sum([1,2,3,4]))'
compile_code = compile(
    code,
    filename='ListSum',
    mode='eval'
)  # Serve para compilar um código direto de uma string. eval para uma linha e exec para mais de uma linha
# Pode-se pular uma linha utilizando ; ou \n
eval(compile_code)


class Number():
    def __init__(self, value, string):
        self.value = value
        self.Str = string

    def sho_val(self):
        print(self.value, self.Str)


num = Number(12, 'Twelve')
num.sho_val()
del ()  # Deleta como função
delattr(num, 'value')  # Deleta um atributo

dir()  # Funciona para ver as funções em um módulo específico

lang_lst = ['Python', 'Java', 'C', 'C++']

index_lst = enumerate(lang_lst)  # Enumerate serve para indexar elementos de uma lista

for lang in index_lst:
    print(lang)

for ind, lang in enumerate(lang_lst):
    print(ind, ':', lang)

print(
    globals() # Funciona para mostrar todos os valores dentro do arquivo do Python
)
