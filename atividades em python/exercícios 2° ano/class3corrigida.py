class Pessoa:
    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getIdade(self):
        return self.idade

    def setIdade(self, idade):
        self.idade = idade

    def getPeso(self):
        return self.peso

    def setPeso(self, peso):
        self.peso = peso
nome = str(input("Diga o nome da pessoa: "))
idade = int(input("Digite a idade da pessoa: "))
peso = float(input("Digite o peso em kg da pessoa: "))

pessoa = Pessoa(nome, idade, peso)

print(f"A pessoa se chama {pessoa.getNome()}, ele(a) tem {pessoa.getIdade()} anos e pesa {pessoa.getPeso()} kg.")