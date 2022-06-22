class Number():
    def __init__(self):
        self.num = 0

    def increase(self):
        self.num += 1

    def decrease(self):
        self.num -= 1


class NewNumber(Number):
    def __init__(self):
        super().__init__()

    def show_value(self):
        print("Value:" + str(self.num))

num = NewNumber()
num.increase()
num.increase()
num.decrease()
num.show_value()
