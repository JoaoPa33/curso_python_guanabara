frase = input("Digite uma frase: ").strip().upper()
lista = frase.split()
junto = "".join(lista)
invertido = ""
for c in range(len(junto)-1, -1, -1):
    invertido += junto[c]
print("O inverso de {} é {}.".format(junto, invertido))
if junto == invertido:
    print("É um PALINDROMO")
else:
    print("Não é um PALINDROMO")

#Ou
frase = input("Digite uma frase: ").strip().upper()
lista = frase.split()
junto = "".join(lista)
invertido = junto[::-1]
print("O inverso de {} é {}.".format(junto, invertido))
if junto == invertido:
    print("É um PALINDROMO")
else:
    print("Não é um PALINDROMO")

