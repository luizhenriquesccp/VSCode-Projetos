const array = [1, 2, 3, 4, 5];

console.log('Primeiro exemplo, uma lista:', array);

const matriz = [
    [1, 2],
    [3, 4],
    [5, 6]
];

console.log('Segundo exemplo, uma lista de listas:');
for (let linha of matriz) {
    console.log( linha);
}