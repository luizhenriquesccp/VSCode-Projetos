def segundo_maior(array):
    if len(array) < 2:
        raise ValueError("O array deve ter pelo menos dois elementos.")
    
    maior = segundo_maior = float('-inf')
    
    for num in array:
        if num > maior:
            segundo_maior = maior
            maior = num
        elif maior > num > segundo_maior:
            segundo_maior = num
    
    if segundo_maior == float('-inf'):
        raise ValueError("Não há um segundo maior número no array.")
    
    return segundo_maior
array = [3, 5, 7, 2, 8, 6]
resultado = segundo_maior(array)
print(f"O segundo maior número é: {resultado}")
