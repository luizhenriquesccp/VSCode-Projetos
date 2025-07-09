import math

def calcular_raizes(a, b, c):
    delta = b**2 - 4*a*c
    
    if delta < 0:
        return "A equação não possui raízes reais."
    elif delta == 0:
        raiz = -b / (2*a)
        return f"A equação possui uma única raiz real: {raiz}"
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2*a)
        raiz2 = (-b - math.sqrt(delta)) / (2*a)
        return f"As raízes reais da equação são: {raiz1} e {raiz2}"

def main():
    print("Calculadora de raízes reais de uma equação quadrática.")
    
    a = float(input("Digite o coeficiente a: "))
    b = float(input("Digite o coeficiente b: "))
    c = float(input("Digite o coeficiente c: "))
    
    if a == 0:
        print("O coeficiente 'a' não pode ser zero em uma equação quadrática.")
    else:
        resultado = calcular_raizes(a, b, c)
        print(resultado)

if __name__ == "__main__":
    main()

