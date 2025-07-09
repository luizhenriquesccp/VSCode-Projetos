print("Peço que, por favor, ao digitar sua nota, me dê um número de 1 a 10.")
n = float(input("Digite sua nota : "))
if n <= 4.9:
    print("Reprovado")
elif n <= 6.9:
    print("Recuperação")
elif n <= 10:
    print("Aprovado")
else:
    print("erro.")