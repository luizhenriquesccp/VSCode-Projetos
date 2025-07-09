bool1 = bool(int(input("Digite 1 para True ou 0 para False (para a primeira variável): ")))
bool2 = bool(int(input("Digite 1 para True ou 0 para False (para a segunda variável): ")))
bool3 = bool(int(input("Digite 1 para True ou 0 para False (para a terceira variável): ")))

def pelo_menos_um_verdadeiro(b1, b2, b3):
    if b1 or b2 or b3:
        return True
    else:
        return False

if pelo_menos_um_verdadeiro(bool1, bool2, bool3):
    print("Pelo menos uma das variáveis é verdadeira.")
else:
    print("Nenhuma das variáveis é verdadeira.")
