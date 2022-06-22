class ZeroCubeError(Exception):
    "0 (Zero) can't be passed as a Cube"


class Cube():
    def __init__(self, num):
        num = int(num)
        if num != 0:
            self.qub = num ** 3
        else:
            raise ZeroCubeError

try:
    num = Cube(input('Number_ '))
    num = Cube(input('Number_ '))
except ZeroCubeError:
    print(ZeroCubeError.__doc__)
except:
    print('UNKNOWN ERROR: Something went Wrong')
else: # Só é executado se não for encontrado erro
    print('Cube: ' + str(num.qub))
finally: # Sempre é executado!
    print('Execution Complete!')


def Cube(number):
    '''This function cubes numbers
        Code : print(number**3) '''
    print(number**3)

print(help(Cube))

