# Containership

class Coder():
    def __init__(self):
        self.name = input('Name_')
        self.lang = input("Languages_")

    def sho_details(self):
        print('Name:' + str(self.name))
        print('Languages:' + str(self.lang))


class Pythoneer():
    def __init__(self):
        self.profile = Coder()

    def info(self):
        self.profile.sho_details()


jake = Pythoneer()
jake.info()

"""Inheritance

class Parent():
    def 1
    def 2
    def 3

class Child(Parent): # Modo par aque outra classe possa ter as mesmas funções """
