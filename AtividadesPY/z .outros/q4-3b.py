class eletro:
    def __init__(self, ligado, voltagem, consumo):
        self.ligado=ligado
        self.voltagem=voltagem 
        self.consumo=consumo
    def isligado(self):
        return (self.ligado)
    def setligado(self, ligado):
        self.ligado=ligado

class TV(eletro):
    def __init__(self, ligado, voltagem, consumo, volume,tamanho):
        super().__init__(ligado, voltagem, consumo)
        self.volume=volume
        self.tamanho=tamanho
    def getsom(self):
        return(self.volume)
    def _setsom(self, volume):
        self.volume=volume
    def gettamanho(self):
        return(self.tamanho)
    def _settamanho(self, tamanho):
        self.tamanho=tamanho

LGTV=TV(True,220,15,volume=0,tamanho=00)

s=int(input("\n""Altere o volume: "))
t=int(input("\n""O tamanho: "))

LGTV._setsom(s)
LGTV._settamanho(t)

if LGTV.ligado == True:
    print("\n""A TV esta ligada numa voltagem de: ")
    print(LGTV.voltagem)
    print("\n""No volume:")
    print(LGTV.volume)
    print("Tamanho da 'legenda' :")
    print(LGTV.tamanho)
else:
    print("A TV esta desligada.")