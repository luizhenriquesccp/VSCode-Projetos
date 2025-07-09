vetor = [10,30,15,5,68,84,12,8,60,40]
quantia = 0

for n in vetor:
    if n % 2 == 0 and n % 5 == 0:
        quantia += 1

print(f"Quantia de múltiplos de 2 e também de 5 são: {quantia}")
