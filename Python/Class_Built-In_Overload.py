class Numeric_Str():
    def __init__(self, Str = ''):
        self.Str = Str
    def __int__(self):
        return int(self.Str)

num = Numeric_Str('1024')
pro = int(num.Str)*2
print(pro)
print(num.Str)
