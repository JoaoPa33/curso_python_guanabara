import moeda as moeda

#from moeda import moeda, metade, dobro, aumentar, diminuir

valor = float(input("Digite um valor em reais: R$"))

print(f"A metade de {moeda.moeda(valor)} é {moeda.metade(valor, True)}.")
print(f"O dobro de {moeda.moeda(valor)} é {moeda.dobro(valor, True)}.")
print(f"Aumentando 10% de {moeda.moeda(valor)} é {moeda.aumentar(valor, 10, True)}.")
print(f"Diminuindo 13% de {moeda.moeda(valor)} é {moeda.diminuir(valor, 13, True)}.")

