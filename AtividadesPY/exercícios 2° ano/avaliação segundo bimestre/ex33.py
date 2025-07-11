vetor = []

for i in range(3):
    n = int(input(f"Digite o número {i+1}: "))
    vetor.append(n)
def exibir_multiplos_de_3(vetor):
    print("Números múltiplos de 3:")
    for n in vetor:
        if n % 3 == 0:  
            print(n)

exibir_multiplos_de_3(vetor)