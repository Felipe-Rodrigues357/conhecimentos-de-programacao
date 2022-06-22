class Coder():
    def code(self):
        print('Codin')

class Pythonner(Coder):
    def py_code(self):
        print('Coding in Python')

class Django (Pythonner):
    def web_dev(self):
        print('new.html @ Django')

web = Django()
web.code()
web.web_dev()
web.py_code()
