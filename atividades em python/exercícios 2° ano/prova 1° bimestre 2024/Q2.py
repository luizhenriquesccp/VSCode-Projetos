def remove_duplicados(vetor):
    # Usa um conjunto para remover duplicatas e depois converte de volta para lista
    return list(set(vetor))

def main():
    vetor = [14, 85, 2, 73, 22, 14, 2, 33, 7, 6, 98, 14, 6, 33]
    
    # Remove duplicatas
    vetor_sem_duplicatas = remove_duplicados(vetor)
    
    # Exibe o vetor sem duplicatas
    print(f"Vetor original: {vetor}")
    print(f"Vetor sem duplicatas: {vetor_sem_duplicatas}")

if __name__ == "__main__":
    main()
