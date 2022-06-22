class Python:
    name_2 = 12
    __key = 90  # Com 2 "_" não é possível se acessar a variável fora da classe

    def __init__(self):
        name = 10  # Class Variable
        _age = 17  # Quando se coloca o " _ " informa que não deve ser utilizado essa variável fora da classe


py = Python()
print(py.name_2)
print(py.name)  # Para conseguir dar o print, precisa ter self.variavel, ou se colocar fora da função da classe
