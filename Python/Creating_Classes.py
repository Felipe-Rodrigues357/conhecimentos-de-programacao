class Coder():
    def __init__(self, name):  # Para inicializar uma classe é obrigatório ter o __init__
        self.Name = name
    def info(self):
        print(self.Name)
    def is_pythoneer(self): # Modo de adicionar atributos dentro da classe
        if 'Python' in self.language:
            print(True)
        else:
            print(False)

cd = Coder('Jake')
cd.language = ['Python', 'C'] # Criado fora da classe, um dos meios de adicionar
cd.is_pythoneer()

print(cd.language)