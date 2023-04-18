lista = []
while True:
    while True:
        try:
            n = int(input("Digite um valor: "))
            break
        except ValueError:
            print("Valor invalido tente novamente.")
    lista.append(n)
    continuar = " "
    while continuar not in "SN":
        continuar = input("Deseja continuar:[S/N]").strip().upper()[0]
    if continuar == "N":
        break
print("=-=" * 20)
print(f"Voce digitou {len(lista)}")
lista.sort(reverse=True)
print(f"Os valores em ordem decrescente são {lista}")
if 5 in lista:
    print("O valor 5 faz parte da lista")
else:
    print("Valor não encontrado")
# for c, v in enumerate(lista):
#     if lista[c] == 5:
#         print("O valor 5 faz parte da lista")
#         break
        


