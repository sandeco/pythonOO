from Pessoa import Pessoa
from ListaPessoas import ListaPessoas

if __name__ == '__main__':


    n_pessoas = int(input("Quantidade de pessoas : "))

    listaPessoas = ListaPessoas()
    qtd_pessoas = listaPessoas.qtdPessoas()

    print("Total de pessoas até agora : {}".format(qtd_pessoas))


    for i in range(n_pessoas):
        nome = input("Digite um nome  : ")
        peso = int(input("Digite o peso   : "))
        idade = int(input("Digite o idade : "))

        p1 = Pessoa(nome, idade, peso)

        listaPessoas.addPessoa(p1)


    print("Total de pessoas até agora : {}".format(listaPessoas.qtdPessoas()))

    listaPessoas.print_nomes()
    listaPessoas.refeitorio()
    listaPessoas.first()
    listaPessoas.last()






