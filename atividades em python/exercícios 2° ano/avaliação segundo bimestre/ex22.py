array = [5,5,5,5]

def calcular_media(array):
    if len(array) == 0:
        return 0
    
    soma = sum(array)
    media = soma / len(array)
    
    return media
media = calcular_media(array)
print("A média dos números na array é:", media)
