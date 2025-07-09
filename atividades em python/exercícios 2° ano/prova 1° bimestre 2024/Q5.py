def fibonacci(n):
    # Inicializa a sequência de Fibonacci com os dois primeiros números
    fib_sequence = [0, 1]
    
    # Gera os próximos números da sequência até atingir N números
    for i in range(2, n):
        next_number = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_number)
    
    return fib_sequence[:n]  # Retorna apenas os primeiros N números

def main():
    # Solicita o número N ao usuário
    n = int(input("Digite a quantidade de números da sequência de Fibonacci que deseja gerar: "))
    
    if n <= 0:
        print("Por favor, insira um número positivo.")
    else:
        fib_sequence = fibonacci(n)
        print(f"Os primeiros {n} números da sequência de Fibonacci são: {fib_sequence}")

if __name__ == "__main__":
    main()
