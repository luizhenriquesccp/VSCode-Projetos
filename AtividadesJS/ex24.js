const entrada = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
})

entrada.question('Digite um número para verificar se é par ou ímpar:', (nInput) => {
    const n = parseInt(nInput);
    function par_ou_impar(n) {
        if (n % 2 === 0) {
            return 'Par';
        } else {
            return 'Ímpar';
        }
    }
    const r = par_ou_impar(n);
    console.log(r);
    entrada.close();
})
