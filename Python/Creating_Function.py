def product():  # def COMEÇA A FUNÇÃO / product NOME DA FUNÇÃO
    prod = 12 * 25
    print(prod)


product()


def greet():  # def COMEÇA A FUNÇÃO / greet NOME DA FUNÇÃO
    name = input('What is Your Name: ')
    print('Welcome Young', name, 'I have been expecting you...')


greet()


# OU

def greet(name):  # def COMEÇA A FUNÇÃO / greet NOME DA FUNÇÃO
    print('Welcome Young ' + str(name) + ' I have been expecting you...')


greet('Skywalker')


def addition(a, b):
    print(a + b)


addition(45, 98)


def result(name, marks):
    print('Name: ' + str(name))
    print('Marks: ' + str(marks))


result('Anakin', 99)  # Argumento de posição
result(marks=99, name='Anakin')  # Argumento de palavra-chave


def addition2(*n):  # Quando não souber quantos argumentos irá receber, utilizar "*" que se chama Argumento Arbitrário
    sm = 0
    for num in n:
        sm += num
    print(sm)


addition2(12, 44, 56, 78, 90)
addition2(2, 3, 4)


def info(**kw):  # Utilizar "**" quando não souber quantas palavras-chaves irá receber do usuário
    for k, v in kw.items():  # Para não dar erro de pedir no máximo duas palavras-chaves, utilizar essa função items()
        print(k, ':', v)


info(Name='Anakin', Rank='NOT Jedi Master',
     Age='Too Young', Result='Order 66')

sub = lambda n, m : n - m #lamba é uma palavra especial também para criação de funções

print(sub(10, 15))
