array = []
for i in range(4):
    num = int(input(f"Digite o número para a posição {i+1}: "))
    array.append(num)

def calcular_media(array):
    if len(array) == 0:
        return 0
    
    soma = sum(array)
    media = soma / len(array)
    
    return media
media = calcular_media(array)
print("A média dos números na array é:", media)