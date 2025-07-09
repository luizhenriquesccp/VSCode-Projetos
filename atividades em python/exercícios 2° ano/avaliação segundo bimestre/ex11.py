bool1 = bool(int(input("Digite 1 para True ou 0 para False (para a primeira variável): ")))
bool2 = bool(int(input("Digite 1 para True ou 0 para False (para a segunda variável): ")))
def ambas_verdadeiras(b1, b2):
    if b1 and b2:
        return True
    else:
        return False
if ambas_verdadeiras(bool1, bool2):
    print("Ambas as variáveis são verdadeiras.")
else:
    print("Pelo menos uma das variáveis é falsa.")
