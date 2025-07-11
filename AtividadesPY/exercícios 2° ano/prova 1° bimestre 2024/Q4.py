def main():
    print("Escolha uma operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    # Solicita a operação desejada
    operacao = input("Digite o número da operação desejada (1/2/3/4): ")

    # Solicita os dois números
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))

    # Realiza a operação escolhida
    if operacao == '1':
        resultado = numero1 + numero2
        print(f"{numero1} + {numero2} = {resultado}")
    elif operacao == '2':
        resultado = numero1 - numero2
        print(f"{numero1} - {numero2} = {resultado}")
    elif operacao == '3':
        resultado = numero1 * numero2
        print(f"{numero1} * {numero2} = {resultado}")
    elif operacao == '4':
        if numero2 != 0:
            resultado = numero1 / numero2
            print(f"{numero1} / {numero2} = {resultado}")
        else:
            print("Erro: Divisão por zero não é permitida.")
    else:
        print("Operação inválida. Por favor, escolha uma operação válida (1/2/3/4).")

if __name__ == "__main__":
    main()
