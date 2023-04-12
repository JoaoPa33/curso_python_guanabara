dias = int(input("Por quantos dias o carro foi alugado? "))
km = float(input("Quantos Km rodado? "))

diaria = dias * 60
kilometragem = km * 0.15

print("O total a pagar é de R${:.2f}.".format(diaria + kilometragem))