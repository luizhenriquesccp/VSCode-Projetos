a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

def pelo_menos_um_par(a, b, c):
    if a % 2 == 0 or b % 2 == 0 or c % 2 == 0:
        return True  
    else:
        return False 
if pelo_menos_um_par(a, b, c):
    print("Pelo menos um dos números é par.")
else:
    print("Nenhum dos números é par.")
