vetor = []

for i in range(15):
    n = int(input(f"Digite o número {i+1}: "))
    vetor.append(n)

pares = 0
impares = 0

for n in vetor:
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
