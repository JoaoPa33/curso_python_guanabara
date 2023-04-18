lista = []
pessoa = []
maior = menor = 0
while True:
    pessoa.append(input("Nome:"))
    while True:
        try:
            pessoa.append(int(input("Peso:")))
            break
        except ValueError:
            print("Peso NÃO aceito.Tente novamente")
    lista.append(pessoa[:])
    if len(lista) == 1:
        maior = menor = pessoa[1]
    else:
        if pessoa [1] > maior:
            maior = pessoa[1]
        if pessoa [1] < menor:
            menor = pessoa[1]


    pessoa.clear()
    print(f"lista{lista}")
    continuar = " "
    while continuar not in "SN":
        continuar = input("Deseja coninuar?[S/N]").upper().strip()[0]
    if continuar == "N":
        break
print(f"Ao todo, você cadastrou {len(lista)} pessoas")
print(f"O maior peso foi de {maior}KG. Que é o peso de:", end="")
for c in lista:
    if c[1] == maior:
        print(f"{c[0]}", end=" ")
print()        
print(f"O menor peso foi de {menor}Kg. Que é o peso de:", end=" ")
for c in lista:
    if c[1] == menor:
        print(f"{c[0]}", end=" ")