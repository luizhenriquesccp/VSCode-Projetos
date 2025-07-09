matriz = [[2,5],[5,2]]
print("Para a matriz; ")
for i in matriz:
    print(i)
soma1 = matriz[0][0] + matriz[1][1]
soma2 = matriz[0][1] + matriz[1][0]
print("A soma dos elementos da diagonal principal é:",soma1)
print("A soma dos elementos da diagonal segundaria é:", soma2)