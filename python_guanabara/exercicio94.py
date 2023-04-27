populaçao = []
pessoa= {}
while True:
    pessoa.clear()
    pessoa["nome"] = input("Nome:")
    sexo = " "
    while sexo not in "MF":
        # while (sexo != "M" and sexo != F):
        sexo = input("Sexo: [M/F]").upper().strip()[0]
        if sexo != "M" and sexo != "F":
            print("Erro. Por favor, digite apenas M ou F")
        else:
            break
    pessoa["sexo"] = sexo
#L6:L13
    '''
    while True:
        pessoa["sexo"] = input("Sexo: [M/F]").upper().strip()[0]
        if pessoa["sexo"] in "MF":
            break
        print("Erro. Por favor, digite apenas M ou F")
    '''
    while True:
        try:
            pessoa["idade"] = int(input("Idade: "))
            break
        except ValueError:
            print("Erro. Por favor, digite um número inteiro")
    populaçao.append(pessoa.copy())
    #print(f"A ficha da pessoa {pessoa}")
#L28
   #populaçao = pessoa[:]
    continuar = " "
    while continuar not in "SN":
        continuar = input("Quer continuar:[S/N]").upper().strip()[0]
    if continuar == "N":
        break
#L30:L35
'''
    while True:
        resp = input("Quer continuar:[S/N]").upper().strip()[0]
        if resp in "SN"
            break
        print("Erro. responda apenas S ou N")
    if resp == "N":
        break
    '''
print(f"A lista de dados {populaçao}")
#A
print(f"Ao todo temos {len(populaçao)}")
#B
soma = 0
for pessoa in populaçao:
    soma += pessoa["idade"]
media = soma/len(populaçao)
print(f"A media de idade é de {media} anos")
#C
print(f"As mulheres cadastradas foram: ", end=" ")
for p in populaçao:
    if p["sexo"] == "F":
#L59 
#   if p["sexo"] in "F":
        print(p["nome"], end=" ")
print()
#D
print("A lista de pessoas que estão acima da média são:")
for p in populaçao:
    if p["idade"] >= media: 
        for k, v in p.items():
            print(f"{k} = {v}; ", end=" ")
        print()



#print(populaçao)

        
# sexo = input("Informe seu sexo:[M/F] ").upper()[0]
# if (sexo == "M" or sexo == "F"):
#     print("Sexo {} registrado com sucesso".format(sexo))
# else:
#     while (sexo != "M" and sexo != "F"):
#         sexo = input("Dados inválidos. Por favor, informe seu sexo:").upper()
#     print("Sexo {} registrado com sucesso".format(sexo))

