array = []
arrayI=[]
for i in range(5):
    num = int(input(f"Digite o número para a posição {i+1}: "))
    array.append(num)
for j in range(4, -1, -1):  # Percorre os índices de 4 até 0
    arrayI.append(array[j])  # Adiciona o valor correspondente da array original em ordem inversa

print("Array em ordem inversa:")
print(arrayI)
print("Array original:")
print(array)