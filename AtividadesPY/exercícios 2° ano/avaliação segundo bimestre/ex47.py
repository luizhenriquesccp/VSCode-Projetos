print("Me de um verto para, eu dizer se está em ordem crescente.")
vetor = []

for i in range(3):
    n = float(input(f"Digite o {i+1}º número : "))
    vetor.append(n)
print(vetor)
if vetor[0] < vetor[1] <vetor[2]:
    print("Sim, ele está em ordem crescente")
else:
    print("Não está em ordem crescente")