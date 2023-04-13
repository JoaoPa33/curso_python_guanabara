# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.
mulheres_menos_20 = homens = maiores_de_18 = 0
while True:
    print("-" * 20)
    print("{:^20}".format("CADASTRE PESSOA"))
    print("-" * 20)
    idade = int(input("Idade:"))
    sexo = " "
    while sexo not in "MF":
        sexo = input("Sexo [M/F]:").strip().upper()[0]
    if idade >= 18:
        maiores_de_18 += 1
    if sexo == "M":
        homens += 1
    if sexo == "F" and idade < 20:
        mulheres_menos_20 += 1
    print("-" * 20)
    continuar = " "
    while continuar not in "SN":
        continuar = input("Quer continuar?[S/N]:").strip().upper()[0]
    if continuar == "N":
        break
print("-" * 20)
print("Total de pessoas com mais de 18 anos: {}".format(maiores_de_18))
print(f"Ao todo temos {homens} homem cadastrado")
print(f"Temos {mulheres_menos_20} mulheres com menos de 20 anos")

