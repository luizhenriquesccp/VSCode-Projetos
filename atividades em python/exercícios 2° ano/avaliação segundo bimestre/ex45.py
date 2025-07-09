matriz = [
    [5, 8, 3, 1],
    [7, 2, 9, 4],
    [6, 5, 2, 0],
]
def somaL(matriz):
    somas = []
    
    for i in matriz:
        somas.append(sum(i))
    
    return somas
soma = somaL(matriz)

print("Soma de cada linha da matriz ",matriz,"é :")
print(soma)