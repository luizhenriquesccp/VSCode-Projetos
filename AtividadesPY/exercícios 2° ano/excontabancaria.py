class contabancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, deposito):
        self.saldo += deposito
        print("Depósito de ", deposito, "R$ foi realizado.")

    def saquar(self, saque):
        if self.saldo >= saque:
            self.saldo -= saque
            print("Saque de ", saque, "R$ feito.")
        else:
            print("Saldo insuficiente.")

    def dados_bancarios(self):
        print("\nTitular da conta:", self.titular)
        print("Saldo da conta:", self.saldo, "\n")

titular = str(input("Informe o nome do titular: "))
saldo = float(input("Informe seu saldo bancário: "))

conta = contabancaria(titular, saldo)
while True:
    conta.dados_bancarios()
    print("Escolha uma opção: ")
    print("Saque aperte 1.")
    print("Depósito aperte 2")
    o = input("Sair (Qualquer outro) : ")
    if o == "2":
        valordedeposito = float(input("Informe o valor do depósito: "))
        conta.depositar(valordedeposito)
    elif o == "1":
        valordesaque = float(input("Informe o valor do saque: "))
        conta.saquar(valordesaque)
    else:
        print("Tchau.")
        break
