N = int(input("Digiteos o valor dos primeiros N números da sequência de Fibonacci. "))

def fibonacci(N):
    fibonacci = []
    a, b = 0, 1
    for _ in range(N):
        fibonacci.append(a)
        a, b = b, a + b
    return fibonacci
sequencia = fibonacci(N)

print("Os primeiros ",N," números da sequência de Fibonacci são: ",sequencia)
