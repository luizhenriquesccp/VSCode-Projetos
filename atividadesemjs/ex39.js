const readline = require("readline");

const entrada = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let vetor = [];

entrada.question("Digite o primeiro número: ", (n1) => {
  vetor.push(parseFloat(n1));

  entrada.question("O segundo número: ", (n2) => {
    vetor.push(parseFloat(n2));

    entrada.question("Agora o terceiro : ", (n3) => {
      vetor.push(parseFloat(n3));

      vetor.sort((a, b) => a - b);

      console.log("\nEm ordem crescente eles ficam assim:");
      vetor.forEach(n => console.log(n));

      entrada.close();
    });
  });
});