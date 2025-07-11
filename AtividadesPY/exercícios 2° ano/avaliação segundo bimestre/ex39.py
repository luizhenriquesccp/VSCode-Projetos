n1 = float(input("Digite o primeiro número: "))
n2 = float(input("O segundo número: "))
n3 = float(input("Agora o terceiro : "))

vetor = [n1, n2, n3]

vetor.sort()

print("Em ordem crescente eles ficam assim:")
for n in vetor:
    print(n)
