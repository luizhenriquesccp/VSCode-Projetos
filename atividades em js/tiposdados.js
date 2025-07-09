// Simulação de entrada do usuário (strings)
const idadeTexto = "27";
const alturaTexto = "1.75m";
const salarioTexto = "4500.50";

// Usando parseInt (extrai apenas a parte inteira)
const idade = parseInt(idadeTexto); // 27
console.log(`Idade convertida com parseInt:`, idade);

// Usando parseFloat (extrai número decimal até onde for possível)
const altura = parseFloat(alturaTexto); // 1.75
console.log(`Altura convertida com parseFloat:`, altura);

// Usando Number (mais rígido, falha se tiver conteúdo não numérico)
const salario = Number(salarioTexto); // NaN, pois tem texto "m" no fim
console.log(`Salário convertido com Number:`, salario);

// Corrigindo para que Number funcione
const salarioCorrigido = Number("4500.50"); // 4500.50
console.log(`Salário convertido corretamente com Number:`, salarioCorrigido);

// Usando toString para transformar número em string
const salarioTextoFinal = salarioCorrigido.toString(); // "4500.5"
console.log(`Salário como texto novamente com toString:`, salarioTextoFinal);