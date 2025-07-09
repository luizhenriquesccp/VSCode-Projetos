class pessoa:
    def __init__(self, name, age, kg):
        self.nome=name
        self.idade=age
        self.peso=kg
    def getNome(self):
        return(self.nome)
    def setNome(self, name):
        self.nome=name
    def setIdade(self, age):
        self.idade=age
    def setPeso(self, kg):
        self.peso=kg
name=str(input("Diga o nome da pessoa; ") )
age=int(input("Digite a idade da pessoa; "))
kg=float(input("Digite o peso em kg da pessoa; "))
Pessoa=pessoa(name,age,kg)
print("a pessoa se chama; ",pessoa.setNome(),",ele(a) tem ",age," anos e tem ", kg,"kg.")
