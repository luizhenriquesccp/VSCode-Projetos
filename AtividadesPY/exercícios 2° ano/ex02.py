X = float(input("digite um numero: "))

def verificar_paridade(numero):
    if numero % 2 == 0:
        print(numero, "é um número par.")
    else:
        print(numero, "é um número ímpar.")


verificar_paridade(X)  