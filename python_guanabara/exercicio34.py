salario = float(input("Qual o salário do funcionario? R$"))
if salario > 1250:
    print("O salário de \033[1mR${:.2f}\033[0m receberá um reajuste de \033[1m10%\033[0m passando a ser de \033[1mR${:.2f}\033[0m".format(salario, (salario * 0.1) + salario))
else:
    print("O salário de \033[1mR${:.2f}\033[0m receberá um reajuste de \033[1m15%\033[0m passando a ser de \033[1mR${:.2f}\033[0m".format(salario, (salario * 0.15) + salario))
#Ou
salario = float(input("Qual o salário do funcionario? R$"))
if salario > 1250:
    novo = salario + (salario * 10 / 100)
    ajuste = 10
else:
    novo = salario + (salario * 15 / 100)
    ajuste = 15
print("O salário de \033[1mR${:.2f}\033[0m receberá um reajuste de \033[1m{}%\033[0m passando a ser de \033[1mR${:.2f}\033[0m".format(salario, ajuste, novo))
