class IngressoCinema:
    def __init__(self, data: str, sala: int, valor: float):
        self.data = data
        self.sala = sala
        self.valor = valor

    # Métodos get e set para data
    def get_data(self):
        return self.data

    def set_data(self, data: str):
        self.data = data

    # Métodos get e set para sala
    def get_sala(self):
        return self.sala

    def set_sala(self, sala: int):
        self.sala = sala

    def get_valor(self):
        return self.valor

    def set_valor(self, valor: float):
        self.valor = valor

    def calcular_desconto(self, idade: int):
        desconto = 0
        if 12 <= idade <= 15:
            desconto = self.valor * 0.40
        elif 16 <= idade <= 20:
            desconto = self.valor * 0.30
        elif idade > 20:
            desconto = self.valor * 0.20

        print(f"O valor do seu desconto é {desconto:.2f}")

class TestarIngresso:
    def main():
        data = input("Digite a data: ")
        sala = int(input("Digite o número da sala: "))
        valor = float(input("Digite o valor do ingresso: "))

        ingresso = IngressoCinema(data, sala, valor)

        idade = int(input("Digite sua idade: "))
        ingresso.calcular_desconto(idade)

        nova_sala = int(input("Digite a nova sala: "))
        ingresso.set_sala(nova_sala)
        print("Nova sala:", ingresso.get_sala())

if __name__ == "__main__":
    TestarIngresso.main()