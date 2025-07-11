print("Diga qual opração você quer ralizar.")
print("1 para soma.")
print("2 para subtração.")
print("3 para multiplicação.")
print("4 para divisão.")

operação = int(input("Qual opereração você quer realizar. "))

n1 = float(input("digite o primeiro numero: "))
n2 = float(input("digite o segundo numero: "))
soma = n1 + n2 
sub = n1 -n2
mult = n1 * n2
div = n1 /n2
if operação == "1":
    print("a soma de ",n1,"mais ",n2,"é igual a",soma)
elif operação== "2":
    print(f"a subtração de {n1} menos {n2} é igual a",sub)
elif operação== "3":
    print(f"a multiplicação de {n1} vezes {n2} é igual a",mult)
elif operação== "4":
    print(f"a divisão de {n1} por {n2} é igual a",div)
else:
    print("erro.")