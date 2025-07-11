const entrada = require('readline').createInterface({

input: process.stdin,
output: process.stdout
});

entrada.question('Digite um número: ', (xInput) => {
const X = parseFloat(xInput);
entrada.question('Digite outro número: ', (yInput) => {
    const Y = parseFloat(yInput);

    const soma = X + Y;
    const sub = X - Y;
    const div = X / Y;
    const multi = X * Y;

    console.log(`Os resultados são eles, multiplicação: ${multi}, soma: ${soma}, divisão: ${div} e subtração: ${sub}`);
    entrada.close();
});
});