lista = []
maior = menor = 0
for cont in range(0, 5):
    lista.append(int(input(f"Digite um valor para a posição {cont}: ")))
    print(f"Você digitou os valores: {lista}")
    if cont == 0:
        maior = menor = lista[0]
    if lista[cont] > maior:
        maior = lista[cont]
    if lista[cont] < menor:
        menor = lista[cont]

# for c, v in enumerate(lista):
#     if c == 0:
#         maior = menor = v    
#     else:
#         if maior < v:
#             maior = v
#         if menor > v:
#             menor = v
print(f"O maior valor digitado foi {maior} e aparece nas posições:", end="")
for c, v in enumerate (lista):
    if v == maior:
        print(c)#, "...", end=" ")
print(f"O menor valor digitado foi {menor} e aparece nas posições:", end="")
for c, v in enumerate (lista):
    if v == menor:
        print(c)#, "...", end=" ")