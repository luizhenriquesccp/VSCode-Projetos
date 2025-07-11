vetor = []

for i in range(10):
    n = float(input(f"Digite o número {i+1}: "))
    vetor.append(n)
print(vetor)

def remover_negativos(vetor):
    return [n for n in vetor if n >= 0]
vetor2= remover_negativos(vetor)

print(vetor2)