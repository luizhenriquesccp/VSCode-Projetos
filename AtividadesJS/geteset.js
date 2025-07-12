class Pessoa {
    constructor(nome, idade) {
        this.nome = nome
        this.idade= idade
    }
    getInformacoes() {
        console.log(`Nome: ${this.nome}, Idade: ${this.idade}`);
    }
    setInformacoes(nome, idade) {
        this.nome = nome;
        this.idade = idade;
    }
}
const pessoa = new Pessoa('Julia', 30);
pessoa.getInformacoes();

const entrada = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});
entrada.question('Digite o novo nome: ', (novoNome) => {
    entrada.question('digite a nova idade: ', (novaIdade) => {
        pessoa.setInformacoes(novoNome, parseInt(novaIdade));
        pessoa.getInformacoes();
        entrada.close();
    });
});