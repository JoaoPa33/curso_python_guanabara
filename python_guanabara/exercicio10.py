real = float(input("Quanto de dinheiro você tem na carteira? R$"))
cambio_dolar = 3.27
print(f"Com R${cambio_dolar} você pode comprar US${(real/cambio_dolar):.2f}")