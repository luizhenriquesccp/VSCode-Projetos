def conta_ocorrencias(vetor, elemento):
    # Conta o número de ocorrências do elemento no vetor
    return vetor.count(elemento)

def main():
    vetor = [14, 85, 2, 73, 22, 14, 2, 33, 7, 6, 98, 14, 6, 33]
    elemento = 14
    
    # Conta as ocorrências do elemento
    ocorrencias = conta_ocorrencias(vetor, elemento)
    
    # Exibe o resultado
    print(f"O elemento {elemento} ocorre {ocorrencias} vezes no vetor.")

if __name__ == "__main__":
    main()
