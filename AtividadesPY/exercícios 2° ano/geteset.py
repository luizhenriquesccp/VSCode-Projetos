class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_informacoes(self):
        print(f'Nome: {self.nome}, Idade: {self.idade}')

    def set_informacoes(self, nome, idade):
        self.nome = nome
        self.idade = idade

pessoa = Pessoa('Julia', 30)
pessoa.get_informacoes()

novo_nome = input('Digite o novo nome: ')
nova_idade = int(input('Digite a nova idade: '))

pessoa.set_informacoes(novo_nome, nova_idade)
pessoa.get_informacoes()