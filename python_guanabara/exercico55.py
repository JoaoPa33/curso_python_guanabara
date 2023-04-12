menor = 0
maior = 0
for pessoa in range(1, 6):
    peso = float(input("Peso da {} pessoa: ".format(pessoa)))   
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print('''O maior peso lido foi de {}Kg
O menor peso lido foi de {}Kg'''.format(maior, menor))