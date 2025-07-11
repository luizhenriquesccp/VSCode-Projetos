n = int(input("Digite o numero de linhas para o triângulo retângulo: "))

def triangulo_numeros(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print() 
triangulo_numeros(n)