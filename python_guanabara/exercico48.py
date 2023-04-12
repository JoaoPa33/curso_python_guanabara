# otimizado
soma = 0
repeticao = 0
for contador in range (1, 501, 2):
    if contador % 3 == 0:
        soma += contador
        repeticao += 1
print("São {} números que a soma é {}.".format(repeticao, soma))

# ou
soma = 0
laco = 0
for contador in range (1, 501):
    if contador % 2 != 0 and contador % 3 == 0:
        soma += contador
        laco += 1
print("São {} números que a soma é {}.".format(laco, soma))

    