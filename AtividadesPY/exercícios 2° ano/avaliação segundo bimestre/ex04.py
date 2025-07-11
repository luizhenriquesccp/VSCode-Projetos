n =int(input("digite um numero, para eu lhe dar o seu fatorial. "))
def calcular_fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        fat = 1
        for i in range(2, n + 1):
            fat *= i
        return fat
    
r=calcular_fatorial(n)
print("o fatorial de ",n," é ",r)