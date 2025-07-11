def cria_matriz():
    # Exemplo de matriz para teste
    return [
        [1, 2, 3],
        [2, 1, 4],
        [3, 4, 1]
    ]

def eh_simetrica(matriz):
    # Verifica se a matriz é quadrada
    num_linhas = len(matriz)
    num_colunas = len(matriz[0])
    
    if num_linhas != num_colunas:
        return False
    
    # Compara cada elemento com o seu elemento transposto
    for i in range(num_linhas):
        for j in range(num_colunas):
            if matriz[i][j] != matriz[j][i]:
                return False
    
    return True

def main():
    matriz = cria_matriz()
    
    # Exibe a matriz
    print("Matriz:")
    for linha in matriz:
        print(linha)
    
    # Verifica se a matriz é simétrica
    if eh_simetrica(matriz):
        print("A matriz é simétrica.")
    else:
        print("A matriz não é simétrica.")

if __name__ == "__main__":
    main()
