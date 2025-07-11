const n = parseInt(prompt('Digite um número para verificar se é par ou ímpar:'));
function par_ou_impar(n) {
    if (n % 2 === 0) {
        return 'Par';
    }
    else {
        return 'Ímpar';
    }
}
const r = par_ou_impar(n);
console.log(r)