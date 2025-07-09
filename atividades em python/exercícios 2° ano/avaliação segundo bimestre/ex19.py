soma = 0

while True:
    numero = float(input("Digite um número (ou um número negativo para sair): "))
    
    if numero < 0:
        break  
    
    soma += numero  
print(f"A soma de todos os números digitados é: {soma}")
