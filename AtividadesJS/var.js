console.log('Variáveis (var) são globais, ou seja, podem ser acessadas fora do escopo onde foram definidas (em qualquer lugar do código).');
console.log('Diferente de let que só funciona a onde ele foi declarado.'    + "' E const que não pode ser reatribuída.'");
if (true) {
    var x = 5;
}

console.log('O primeiro valor de x (variável var) é:', x);

var x = 10;
console.log('O segundo valor de x (variável var) é:', x);