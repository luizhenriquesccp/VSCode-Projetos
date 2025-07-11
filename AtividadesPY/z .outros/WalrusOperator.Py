if (vendas:=int(input("vendas do funcionario."))) > 1000:
    bonus = 0.05 * vendas
else:
    bonus = 0
print("bonus: ",bonus)