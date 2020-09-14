
class Pessoa():

    def __init__(self, nome="", idade=0, peso=0):

        ## PARA USAR PROPERTY É OBRIGATÓRIO QUE O ATRIBUTO SEJA PRIVADO
        self._nome = nome
        self._idade = idade
        self._peso = peso

    def repirar(self):
        print(self._nome + " respirando")

    def comer(self):
        print(self._nome + " comendo")

    def set_nome(self, value):
        self._nome = value

    def get_nome(self):
        return self._nome

    def set_idade(self, value):
        self._idade = value

    def get_idade(self):
        return self._idade

    nome  = property(get_nome, set_nome)
    idade = property(get_idade, set_idade, 'Propriedade idade')

