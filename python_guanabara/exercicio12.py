valor = float(input("Qual é o preço do produto? R$"))
desconto = float(input("Qual é a percentagem de desconto: "))

valor_com_desconto = valor - (valor * (desconto / 100))

print("O produto que custava R${}, na promoção de {}% vai custar: R${:.2f}".format(valor, desconto, valor_com_desconto))