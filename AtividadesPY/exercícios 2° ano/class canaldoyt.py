class canaldoyt:
    def __init__(self, inscritos):
        self._inscritos=inscritos
    @property
    def inscritos(self):
        return self._inscritos
    
    @inscritos.setter
    def inscritos(self, novos_inscritos):
        self._inscritos=novos_inscritos

n = int(input("diga o numeros de inscritos do canal. "))

canal=canaldoyt(n)

print("\nO canal tem ",canal.inscritos," inscritos. \n")

canal.inscritos=int(input("diga o novo numero de inscritos: "))

print("\nO canal agora tem ",canal.inscritos," inscritos. \n")
