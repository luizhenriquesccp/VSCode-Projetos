print("Conversor de Temperatura")
print("1. Celsius para Fahrenheit")
print("2. Fahrenheit para Celsius")

escolha = input("Escolha uma opção (1 ou 2): ")

if escolha == "1":
    C = float(input("digite o valor em graus Celsius, "))
    F = (C*9/5) +32
    print(f"{C}°C é igual a {F}°F")
elif escolha == "2":
    F = float(input("Digite o valor em Fahrenheit, "))
    C = (F-32)*5/9
    print(f"{F}°F é igual a {C}°C")
else:
    print("valor incoreto")