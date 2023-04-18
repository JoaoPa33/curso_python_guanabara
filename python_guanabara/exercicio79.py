lista = []

while True:
    while True:
        try:
            n = int(input("Digite um número inteiro: "))
            break
        except ValueError:
            print("Valor não aceito. Tente novamente.")     
    if n not in lista:
        lista.append(n)
        print("Valor adicionado com sucesso")
    else:
        print("O valor não pode ser adicionado")
    continuar = " "
    while continuar not in "SN":
        continuar = input("Quer continuar? [S/N]").strip().upper()[0]
    if continuar == "N":
    #ou if continuar in "N"
        break
lista.sort()
print(lista)
print("Fim")


