class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, deposito):
        self.saldo += deposito
        print(f"Depósito de {deposito:.2f} R$ realizado com sucesso.")

    def saquar(self, saque):
        if self.saldo >= saque:
            self.saldo -= saque
            print(f"Saque de {saque:.2f} R$ realizado com sucesso.")
        else:
            print("Saldo insuficiente.")

    def dados_bancarios(self):
        print("\nTitular da conta:", self.titular)
        print(f"Saldo da conta: {self.saldo:.2f} R$")

# Entrada de dados do usuário
titular = str(input("Informe o nome do titular: "))
saldo = float(input("Informe seu saldo bancário: "))

# Criação do objeto conta bancária
conta = ContaBancaria(titular, saldo)

# Menu de operações
while True:
    conta.dados_bancarios()
    print("\nEscolha uma das opções:")
    print("1 - Consultar saldo")
    print("2 - Realizar depósito")
    print("3 - Realizar saque")
    print("4 - Sair")

    opcao = input("Opção: ")

    if opcao == "1":
        conta.dados_bancarios()
    elif opcao == "2":
        valor_deposito = float(input("Informe o valor do depósito: "))
        conta.depositar(valor_deposito)
    elif opcao == "3":
        valor_saque = float(input("Informe o valor do saque: "))
        conta.saquar(valor_saque)
    elif opcao == "4":
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")
