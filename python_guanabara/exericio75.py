a = int(input("Digite um numero:"))
b = int(input("Digite um numero:"))
c = int(input("Digite um numero:"))
d = int(input("Digite um numero:"))
tupas_int = (a, b, c, d)
print(tupas_int)
#tupas = str(tupas_int)
#print(tupas)


print(f"Você digitou os valores {tupas_int}")

print(f"O valor 9 apareceu {tupas_int.count(9)} vezes.")
if 3 in tupas_int:
    print(f"O valor 3 apareceu pela primeira vez na {tupas_int.index(3) + 1} posicão.")
else:
    print("O valor 3 não apareceu.")
pares = 0
impares = 0
for p in tupas_int:
    if p % 2 == 0:
        pares+=1
    if p % 2 != 0:
        impares+=1
print(f"Foram digitados {pares} valores pares.")
print(f"Foram digitados {impares} valores impares.")
