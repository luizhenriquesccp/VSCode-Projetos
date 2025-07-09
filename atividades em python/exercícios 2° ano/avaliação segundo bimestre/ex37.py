A = [[7,8,9],[54,2,7],[12,9,3]]
B= [[77,0,1],[5,67,34],[34,4,3]]
def soma(A, B):
    resultado = [[0,0,0],[0,0,0],[0,0,0]]
    
    for i in range(3):
        for j in range(3):
            resultado[i][j] = A[i][j] + B[i][j]
    
    return resultado
C = soma(A, B)

print("Soma das duas matrizes:")
#for i in matriz_soma:print(i)
print(C)