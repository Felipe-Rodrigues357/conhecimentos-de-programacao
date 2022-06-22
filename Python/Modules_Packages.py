import func

func.greet_user('Johnson')
func.wish('Jacqueline')

from Func_Pack import func_package2

func_package2.bye('Kala')


'''OUTRA MANEIRA:

from func import greet_user , wish (Pode-se chamar todas as funções usando o "*")
OU
from func import *

greet_user('Johnson')
wish('Jacqueline')

É possível mudar o nome da função direto no import:
from func import greet_user as greet

greet('Johnson')

'''