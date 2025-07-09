def busca_na_matriz(matriz, numero):
    linhas = len(matriz)
    colunas = len(matriz[0])
    
    linha = 0
    coluna = colunas - 1
    
    while linha < linhas and coluna >= 0:
        if matriz[linha][coluna] == numero:
            return True 
        elif matriz[linha][coluna] > numero:
            coluna -= 1  
        else:
            linha += 1  
    
    return False 

if __name__ == "__main__":
    matriz = [
        [1, 4, 7, 11],
        [2, 5, 8, 12],
        [3, 6, 9, 16]
    ]
    
    numero = int(input("Digite o número que deseja buscar na matriz: "))
    
    if busca_na_matriz(matriz, numero):
        print(f"O número {numero} está presente na matriz.")
    else:
        print(f"O número {numero} NÃO está presente na matriz.")
