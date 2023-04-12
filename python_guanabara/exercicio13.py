atual = float(input("Qual é o salário do Funcionário? R$"))
aumento = float(input("Qual é o % de aumento? "))

novo_salario = atual + (atual * (aumento/100))

print("Um funcionário que ganhava R${}, com {}% de aumento, passa a receber R${:.2f}.".format(atual, aumento, novo_salario))