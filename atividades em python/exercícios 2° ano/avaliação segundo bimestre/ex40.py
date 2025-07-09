n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Agora o segundo: "))
n3 = int(input("O terceiro número: "))
n4 = int(input("O quarto : "))
n5 = int(input("É o quinto número: "))

if n1 > n2 and n3 != n4 and n3 < n5:
    print("Condições atendidas:")
    print(f"O primeiro número ({n1}) é maior que o segundo número ({n2}).")
    print(f"O terceiro número ({n3}) é diferente do quarto número ({n4}) e menor que o quinto número ({n5}).")
else:
    print("As condições não foram atendidas.")
