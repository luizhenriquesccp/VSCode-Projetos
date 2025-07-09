n1 = 6
n2 = 90
n3 = 44

def maior_dos_tres(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        maior = n1
    elif n2 >= n1 and n2 >= n3:
        maior = n2
    else:
        maior = n3
    
    return maior

r = maior_dos_tres(n1, n2, n3)
print(f"O maior número é: {r}")
