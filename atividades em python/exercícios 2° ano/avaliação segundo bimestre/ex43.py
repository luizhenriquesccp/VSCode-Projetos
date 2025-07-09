matriz = [[12, 7, 3, 9, 5],[4, 19, 2, 8, 15],[9, 22, 11, 6, 7],[8, 6, 25, 3, 10],[14, 17, 2, 23, 9]]

def maior_valor_matriz(matriz):
    maior_valor = 0

    for i in matriz:
        for elemento in i:
            if elemento > maior_valor:
                maior_valor = elemento

    return maior_valor

print("O maior valor da matriz é:", maior_valor_matriz(matriz))
