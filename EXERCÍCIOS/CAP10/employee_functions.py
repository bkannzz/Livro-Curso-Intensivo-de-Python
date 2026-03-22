class Employee:
    def __init__(self, nome, sobrenome, salario):
        self.nome = nome
        self.sobrenome = sobrenome
        self.salario = salario

    def dar_aumento(self, valor=5000):
        self.salario += valor