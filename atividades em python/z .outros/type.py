def verificasão(dados):
    if isinstance(dados, int):
        return "É um inteiro. "
    elif isinstance(dados, float):
        return "É um real. "
    elif isinstance(dados, str):
        return "É uma string. "
x=4.8

print(verificasão(x))