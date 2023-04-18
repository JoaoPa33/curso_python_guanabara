lista = []
par = []
impar = []
while True:
    while True:
        try:
            n = int(input("Digite um valor: "))
            break
        except ValueError:
            print("Valor invalido")
    #lista.append(n)
    #for c, v in enumerate(lista):
        #if v % 2 == 0:
            #par.append(v)
        #elif v % 2 == 1:
            #impar.append(v)

    if n % 2 == 0:
        if n not in lista:
            lista.append(n)
            par.append(n)
    elif n % 2 != 0:
        if n not in lista:
            lista.append(n)
            impar.append(n)
    continuar = " "
    while continuar not in "sn":
        continuar = input("Deseja continuar?[s/n]").lower().strip()[0]
    if continuar == "n":
        break
print(f"A lista completa: {lista}")
print(f"A lista de pares é: {par}")
print(f"A lista de impar é: {impar}")