class Eletro {
    constructor(ligado, voltagem, consumo) {
        this.ligado = ligado;
        this.voltagem = voltagem;
        this.consumo = consumo;
    }
    isLigado() {
        return this.ligado;
    }
    setLigado(ligado) {
        this.ligado = ligado;
    }
}

const PS2 = new Eletro(true, 60, 120);
const TV = new Eletro(false, 100, 220);

console.log("O Play 2 está ligado?", PS2.isLigado());
console.log(PS2.consumo);
console.log("A TV está ligada?", TV.isLigado());
console.log(TV.voltagem);
console.log("Ligando a TV...");
console.log(TV.setLigado(true));
console.log("A TV está ligada?", TV.isLigado());
