matriz_4x4 = [
    [5, 8, 3, 1],
    [7, 2, 9, 4],
    [6, 5, 2, 0],
    [4, 3, 7, 8]
]
def soma_linhas_matriz(matriz):
    for i, linha in enumerate(matriz):
        soma = sum(linha)
        print(f"Soma da linha {i+1}: {soma}")

soma_linhas_matriz(matriz_4x4)
