print("Me diga sua idade, para que eu lhe informe se você está apto a votar ou dirigir.")
idade=int(input("Sua idade; "))
if idade >= 16:
    print("você pode votar, mas não pode dirigir ainda.")
elif idade >= 18:
    print("sim você pode votar e dirigir.")
else :
    print("não, você nem pode votar nem dirigir.")