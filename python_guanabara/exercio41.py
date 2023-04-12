from datetime import date
ano_nasc = int(input("Digite o ano de nascimento do competidor:"))
ano_atual = 2017#date.today().year
idade = ano_atual - ano_nasc
if idade <= 9:
    categoria = "mirim"
elif 9 < idade <= 14:
    categoria = "infantil"
elif 14 < idade <= 19:
    categoria = "junior"
elif 19 < idade <= 25:
    categoria = "sênior"
else:
    categoria = "master"
print("O atleta de {} anos é da categoria {}.".format(idade, categoria.upper()))

#ou
ano_nasc = int(input("Digite o ano de nascimento do competidor:"))
ano_atual = date.today().year
idade = ano_atual - ano_nasc
if idade <= 9:
    categoria = "mirim"
elif idade <= 14:
    categoria = "infantil"
elif idade <= 19:
    categoria = "junior"
elif idade <= 25:
    categoria = "sênior"
else:
    categoria = "master"
print("O atleta de {} anos é da categoria {}.".format(idade, categoria.upper()))


