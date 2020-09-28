
class Pessoa():

    def __init__(self, nome="", idade=0, peso=0):

        self.nome = nome
        self.idade = idade
        self.peso = peso

    # FUNÇÕES -> MÉTODOS
    def repirar(self):
        print(self.nome + " respirando")

    def comer(self):
        print(self.nome + " comendo")


