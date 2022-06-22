class SumPair():
    def __init__(self, lst):
        self.List = lst
        self.List_len = len(lst)
        self.i1 = 0
        self.i2 = 1

    def __iter__(self): # Serve para transformar a classe em int para realizar funções matemáticas
        return self

    def __next__(self):
        if self.i2 == self.List_len:
            raise StopIteration  # Levanta um erro pré-definido em Python, funciona com o for
        else:
            self.sum_pair = self.List[self.i1] + self.List[self.i2]
            self.i1 += 1
            self.i2 += 1
            return self.sum_pair


l = SumPair([12, 44, 56, 78, 12, 33])
for ele in l:
    print(ele)
