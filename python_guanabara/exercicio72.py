nome = ("zero", "um","dois", "tres","quatro", "cinco", "seis", 
        "sete", "oito", "nove", "dez")

while True:
    n =int(input("Digit um número ente 0 e 10: "))
    if 0 <= n <=10:
        print(f"Você digitou {nome[n]}")
        continuar = " "
        while continuar not in "SN":
            continuar = input("Deseja continuar? [S/N]").upper().strip()[0]
        if continuar == "N":
            break
    else:
        print("Tente novamente.", end=" ")

