palavra = input("Diga um palíndromo: ")

def eh_palindromo(palavra):
    palavra = palavra.replace(" ", "").lower()

    if len(palavra) <= 1:
        return True

    if palavra[0] != palavra[-1]:
        return False

    return eh_palindromo(palavra[1:-1])

if eh_palindromo(palavra):
    print("A palavra é um palíndromo!")
else:
    print("A palavra não é um palíndromo.")
