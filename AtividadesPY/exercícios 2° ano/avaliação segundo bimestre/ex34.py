matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

def soma_diagonal_principal(matriz):
    soma = 0
    for i in range(len(matriz)):
        soma += matriz[i][i]  # Acessa o elemento da diagonal principal
    return soma

# Calcula e exibe a soma dos elementos da diagonal principal
resultado = soma_diagonal_principal(matriz)
print(f"A soma dos elementos da diagonal principal é: {resultado}")
