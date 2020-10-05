from Pessoa import Pessoa
import pandas as pd

# C - Create
# R - Read/ReadAll
# U - Update
# D - Delete

class PessoaDAO():


    def open(self):
        df = pd.read_csv("pessoas.csv")
        return df

    def save(self, df):
        df.to_csv("pessoas.csv", index=False)

    def create(self, pessoa):

        df = self.open()
        new_id = self.get_new_id(df)

        pessoa.id = new_id

        new_row = pd.DataFrame(data=[[
                                pessoa.id, pessoa.nome, pessoa.idade, pessoa.peso
                                ]],
                                columns=df.columns)

        df = df.append(new_row)
        self.save(df)

    def get_new_id(self, df):

        if len(df) == 0:
            id = 1
        else:
            last = df.tail(1)
            id = last.id.values[0] + 1

        return id

    def read(self,id):

        df = self.open()
        i = self.get_index(id, df)

        pessoa = Pessoa()

        pessoa.id = id
        pessoa.nome  = df.iloc[i].nome
        pessoa.idade = df.iloc[i].idade
        pessoa.peso  = df.iloc[i].peso

        return pessoa


    def read_all(self):

        df = self.open()

        pessoas = []


        for i in range(len(df)):
            pessoa = Pessoa()
            pessoa.id = df.iloc[i].id
            pessoa.nome = df.iloc[i].nome
            pessoa.idade = df.iloc[i].idade
            pessoa.peso = df.iloc[i].peso

            pessoas.append(pessoa)

        return pessoas




    def update(self, pessoa):

        df = self.open()
        id = pessoa.id

        df.loc[df.id == id, 'nome']  = pessoa.nome
        df.loc[df.id == id, 'idade'] = pessoa.idade
        df.loc[df.id == id, 'peso']  = pessoa.peso

        self.save(df)

    def delete(self, id):

        df = self.open()
        index = self.get_index(id, df)
        df = df.drop(index)

        self.save(df)


    def get_index(self, id, df):

        index = df.loc[df.id == id, :].index

        index = df.loc[df.id == id, :].index[0]

        return index










if __name__ == '__main__':


    pessoa = Pessoa()
    pessoa.nome  = 'Sandeco'
    pessoa.idade = 43
    pessoa.peso  = 80

    dao = PessoaDAO()
    dao.create(pessoa)




    pessoa.nome  = 'Sanderson Macedo'
    pessoa.idade = 44
    pessoa.peso  = 81

    dao.update(pessoa)

    #dao.delete(1)

    pessoa = dao.read(10)


    pessoas = dao.read_all()


    i =0

















