n = int(input("Digite um número inteiro:"))
print('''Escolha uma das bases para a conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
conversao = int(input("Sua opção:"))
if conversao == 1:
    conv = bin(n)[2:], "BINÁRIO"
# [:2]é pq a resposta vem com 0b+código
elif conversao == 2:
    conv = oct(n)[2:], "OCTAL"
# [:2]é pq a resposta vem com 0o+código
elif conversao == 3:
    conv = hex(n)[2:], "HEXADECIMAL"
# [:2]é pq a resposta vem com 0x+código
else:
    print("A opção escolhida é invalida")
print("O {} convertido para {} é igual a {}".format(n, conv[1], conv[0]))