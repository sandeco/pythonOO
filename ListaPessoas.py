
class ListaPessoas():

    def __init__(self):
        self.pessoas = []


    def lerPessoas(self):
        pass


    def excluirPessoa(self, index):
        pass
    

    def addPessoa(self, pessoas):
        self.pessoas.append(pessoas)

    def qtdPessoas(self):
        return len(self.pessoas)



    def print_nomes(self):

        for p in self.pessoas:
            print("Nome : {}".format(p.nome))


    def refeitorio(self):

        for p in self.pessoas:
            if p.peso <= 100:
                p.comer()
            else:
                print(p.nome + " vá fazer dieta")

    def first(self):
        p = self.pessoas[0]
        print("Primeiro da lista : {}".format(p.nome))


    def last(self):
        ult = len(self.pessoas) - 1
        p = self.pessoas[ult]
        print("Último da lista : {}".format(p.nome))
