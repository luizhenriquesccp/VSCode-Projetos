class pessoa:
    def __init__(self, name, age, kg):
        self.nome=name
        self.idade=age
        self.peso=kg
    def getNome(self):
        return(self.nome)
    def setNome(self, name):
        self.nome=name

Luiz=pessoa("Luiz",17,55)
print("A pessoa tem ",Luiz.idade, "anos.")
print("A pessoa se chama ",Luiz.nome,".")
