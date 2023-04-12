print("=-=" * 20)
print("\033[1mEMPRESTIMO\033[0m")
print("=-=" * 20)
casa = float(input("Qual o valor da casa que gostaria de comprar?"))
salario = float(input("Qual é o seu salário?"))
tempo = int(input("Em quantos anos vc gostaria de pagar?"))

parcela = (casa /tempo) / 12


if (parcela > salario * 0.3):
    print("\033[31mSEU EMPRESTIMO FOI NEGADO!!!\033[37m Seu emprestimo não pode ser aprovado porque a parcela supera o valor de 30% do seu salário. Sua parcela seria R${:.2f}".format(parcela))
else:
    print("\033[32mSEU EMPRESTIMO FOI APROVADO!!!\033[37m Sua parcela será de R${:.2f}.".format(parcela))

#OU
print("=-=" * 20)
print("\033[1mEMPRESTIMO\033[0m")
print("=-=" * 20)
casa = float(input("Qual o valor da casa que gostaria de comprar?"))
salario = float(input("Qual é o seu salário?"))
tempo = int(input("Em quantos meses vc gostaria de pagar?"))

parcela = (casa / tempo) / 12

if (parcela > salario * 0.3):
    status = "NEGADO"
else:
    status = "APROVADO"
print("\033[33mSEU EMPRESTIMO FOI {}!!!\033[37m".format(status))
