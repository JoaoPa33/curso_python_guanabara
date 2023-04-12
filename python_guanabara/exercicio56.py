total_idade = 0
nome_velho = ""
idade_velho = 0
for pessoa in range(1, 5):
    print("-----{} PESSOA ------".format(pessoa))
    nome = input("Nome:").strip()
    idade = int(input("Idade:"))
    sexo = input("Sexo [M/F]").strip()
    total_idade += idade
    if sexo in "Mm": 
        if idade > idade_velho:
            nome_velho = nome
            idade_velho = idade
    else:
        idade_mulher = 0
        if idade < 20:
            idade_mulher += 1

print("A média de idade do grupo é de {:.2f} anos".format(total_idade / 4))
print("O homem mais velho se chama {} e tem {} anos.".format(nome_velho, idade_velho))
print("E {} mulheres tem menos de 20 anos".format(idade_mulher))