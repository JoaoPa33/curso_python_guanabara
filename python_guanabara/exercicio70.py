#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato. 
print("-" * 40)
print("{:^40}".format("LOJA SUPER BARATÃO"))
print("-" * 40)
c = produto_1000 = total_preco = 0
while True:
    produto = input("Nome do produto: ")
    preco = float(input("Preço do produto: R$"))
    total_preco += preco
    if preco > 1000:
        produto_1000 += 1
    if c == 0:
        preco_barato = preco
        produto_barato = produto
        preco_caro = preco
        produto_caro = produto
    else:
        if preco < preco_barato:
            preco_barato = preco
            produto_barato = produto
        elif preco > preco_caro:
            preco_caro = preco
            produto_caro = produto
    c += 1
    continuar = " "
    while continuar not in "SN":
        continuar = input("Deseja adicionar mais produtos?[S/N] ").strip().upper()[0]
    if continuar == "N":
        break
print("{:-^40}".format("FIM DAS COMPRAS"))
print(f"O total de {c} itens deu R${total_preco:.2f}")
print(f"Temos {produto_1000} produto(s) custando mais de R$1000,00")
print(f"O produto mais barato foi {produto_barato} que custava R${preco_barato:.2f}.")
print(f"O produto mais caro foi {produto_caro} que custava R${preco_caro:.2f}.")


