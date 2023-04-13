resp = "s"
maior = menor = n = acumulador = c = 0
while resp in "Ss":
    n = int(input("Digite um número:"))
    c += 1
    acumulador += n
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    resp = input("Quer continuar [S/N]: ")
media = acumulador / c
print("Você digitou {} números e a média foi {:.2f}".format(c, media))
print("O maior valor foi {} e o menor foi {}.".format(maior, menor))
