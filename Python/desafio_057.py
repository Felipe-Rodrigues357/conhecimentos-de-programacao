nome = input('\033[1;33mNOME: \033[m').upper()
idade = input('\033[1;32mIDADE: \033[m')
sexo = 'J'
while sexo != 'M' and 'F':
    sexo = input('\033[1;30mSEXO[M/F]: \033[m').upper()
    if sexo != 'M' and 'F':
        print('\033[1;31mVALOR INVÁLIDO! TENTE NOVAMENTE!\033[m')
print('\033[1;36mINFORMAÇÕES:'
      '\nNOME:\033[m \033[1;34m{}\033[m'
      '\n\033[1;36mIDADE:\033[m \033[1;34m{}\033[m'
      '\n\033[1;36mSEXO:\033[m \033[1;34m{}\033[m'.format(nome, idade, sexo))
"""
OUTRO CÓDIGO PARA QUE ELE ACEITE ESCRITO EM QUALQUER ESPAÇO:
sexo = input('Informe seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo [M/F]: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))
"""
