def tamanho_maior_string(array):
    if not array:
        return 0
    
    comprimento_maximo = 0
    
    for string in array:
        if len(string) > comprimento_maximo:
            comprimento_maximo = len(string)
    
    return comprimento_maximo
array_de_strings = ["maçã", "banana", "cabelos", "cachorro"]
tamanho_maximo = tamanho_maior_string(array_de_strings)
print(f"O tamanho da maior string é: {tamanho_maximo}")