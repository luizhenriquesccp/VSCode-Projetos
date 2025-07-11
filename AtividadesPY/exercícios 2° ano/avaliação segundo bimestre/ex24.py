n = int(input("digite um numero; "))
def par_ou_impar(n):
    if n % 2 == 0:
        return "Par"
    else:
        return "Ímpar"
r = par_ou_impar(n)
print(r)