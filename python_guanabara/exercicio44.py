# print("=-=" * 20)
# print("{:=^80}".format("\033[1;032mProdutos\033[0;037m"))
# print("=-=" * 20)
# valor = float(input("Qual o valor pago pelo produto? R$"))
# print('''Selecione a forma de pagamento:
# [1] Dinheiro ou Cheque
# [2] À vista no cartão
# [3] em até 2x no cartão
# [4] em 3X ou mais no cartão''')
# pagamento = int(input("Selecione a forma de pagamento: "))
# if pagamento == 1:
#     valor_final = (valor - (valor * 0.1)), "Dinheiro ou Cheque", "10% de desconto"
# elif pagamento == 2:
#     valor_final = (valor - (valor * 0.05)), "À vista no cartão", "5% de desconto"
# elif pagamento == 3:
#     valor_final = (valor), "2X no cartão", "0% de desconto"
# elif pagamento == 4:
#     valor_final = (valor + (valor * 0.2)), "3X ou mais no cartão", "com 20% de taxa"
# else:
#     valor_final = valor, "x", "x"
#     print("Forma de pagamento não reconhecida, tente novamente")
# print("O produto que custava R${:.2f} com a forma de pagamento:\n{}\nPassará a custar R${:.2f} com {}.".format(valor, valor_final[1], valor_final[0], valor_final[2]))

#ou
print("=-=" * 20)
print("{:=^80}".format("\033[1;032mProdutos\033[0;037m"))
print("=-=" * 20)
valor = float(input("Qual o valor pago pelo produto? R$"))
print('''Selecione a forma de pagamento:
[1] Dinheiro ou Cheque
[2] À vista no cartão
[3] em até 2x no cartão
[4] em 3X ou mais no cartão''')
pagamento = int(input("Selecione a forma de pagamento: "))
if pagamento == 1 or pagamento == 2 or pagamento == 3 or pagamento ==4:
    if pagamento == 1 :
        valor_final = (valor - (valor * 0.1)), "Dinheiro ou Cheque", "10% de desconto"
    elif pagamento == 2:
        valor_final = (valor - (valor * 0.05)), "À vista no cartão", "5% de desconto"
    elif pagamento == 3:
        valor_final = (valor), "2X no cartão", "0% de desconto"
    elif pagamento == 4:
        valor_final = (valor + (valor * 0.2)), "3X ou mais no cartão", "com 20% de taxa"
    print("O produto que custava R${:.2f} com a forma de pagamento:\n{}\nPassará a custar R${:.2f} com {}.".format(valor, valor_final[1], valor_final[0], valor_final[2]))
else:
    print("Forma de pagamento não reconhecida, tente novamente")

