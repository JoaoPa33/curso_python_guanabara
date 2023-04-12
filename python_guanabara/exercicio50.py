soma = 0
contador = 0
for c in range(1,7):
    valor = int(input("{} Digite um número inteiro: ".format(c)))
    if valor % 2 == 0:
        soma += valor
        contador += 1
print("Você digitou {} PARES e a soma deles deu {}.".format(contador, soma))