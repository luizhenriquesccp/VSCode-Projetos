class eletro:
    def __init__(self, ligado, voltagem, consumo):
        self.ligado=ligado
        self.voltagem=voltagem 
        self.consumo=consumo
    def isligado(self):
        return (self.ligado)
    def setligado(self, ligado):
        self.ligado=ligado

PS2= eletro(True,60,120)
TV=eletro(False, 100, 220)

print("O Play 2 está ligado?", PS2.isligado())
print(PS2.consumo)
print("A TV está ligada?", TV.isligado())


# self.variavel E um atributo, variavel E um valor