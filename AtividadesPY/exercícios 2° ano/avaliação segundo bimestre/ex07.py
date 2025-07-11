nome = input("diga seu nome, por favor. ")
idade = input("agora sua idade. ")

if isinstance(nome, str):
    print("A variável 'nome' é do tipo str: ",nome)
else:
    print("A variável 'nome' não é do tipo str.")

if isinstance(idade, int):
    print("A variável 'idade' é do tipo int: ",idade)
else:
    print("A variável 'idade' não é do tipo int.")
